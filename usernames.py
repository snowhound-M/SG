from datetime import datetime
from telethon import TelegramClient, events
import sqlite3
import asyncio

# Replace with your own values
api_id = 25271591
api_hash = "f34e58a37b8f88fbbe19f85ffaa36f4f"
bot_token = "6864922631:AAHHeX2_3V27SwEW98-mh1EXycce3cdOouk"

# Initialize the Telegram client
client = TelegramClient('UsernameBot', api_id, api_hash).start(bot_token=bot_token)

# Set up SQLite database
conn = sqlite3.connect('usernames.db')
cursor = conn.cursor()

# Create a table to store the history of names and usernames with timestamps
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_history (
    user_id INTEGER,
    name TEXT,
    username TEXT,
    timestamp TEXT,
    PRIMARY KEY (user_id, timestamp)
)
''')
conn.commit()

# Event handler for user updates
@client.on(events.UserUpdate)
async def user_update_handler(event):
    timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    if event.user_id:
        user_id = event.user_id
        new_name = f"{event.first_name} {event.last_name}" if event.last_name else event.first_name
        new_username = event.username

        cursor.execute('SELECT username, name, timestamp FROM user_history WHERE user_id=? ORDER BY timestamp DESC', (user_id,))
        rows = cursor.fetchall()

        if rows:
            old_username, old_name, _ = rows[0]
            if old_username != new_username or old_name != new_name:
                cursor.execute('INSERT INTO user_history (user_id, name, username, timestamp) VALUES (?, ?, ?, ?)', (user_id, new_name, new_username, timestamp))
                conn.commit()
                print(f'Updated record for user_id {user_id} with name "{new_name}", username "{new_username}" and timestamp {timestamp}.')
        else:
            cursor.execute('INSERT INTO user_history (user_id, name, username, timestamp) VALUES (?, ?, ?, ?)', (user_id, new_name, new_username, timestamp))
            conn.commit()
            print(f'Inserted new record for user_id {user_id} with name "{new_name}", username "{new_username}" and timestamp {timestamp}.')

# Function to retrieve user history by user ID
def get_user_history_by_id(user_id):
    cursor.execute('SELECT name, username, timestamp FROM user_history WHERE user_id=? ORDER BY timestamp DESC', (user_id,))
    rows = cursor.fetchall()
    return rows

# Function to retrieve user history by username
def get_user_history_by_username(username):
    cursor.execute('SELECT user_id, name, username, timestamp FROM user_history WHERE username=? ORDER BY timestamp DESC', (username,))
    rows = cursor.fetchall()
    return rows

# Handler for messages containing just a user ID
@client.on(events.NewMessage)
async def id_handler(event):
    try:
        user_id = int(event.message.text.strip())
        history = get_user_history_by_id(user_id)
        if history:
            response = f'History for user_id {user_id}:\n'
            for record in history:
                name, username, timestamp = record
                response += f'Name: {name}, Username: {username}, Timestamp: {timestamp}\n'
        else:
            response = f'No history found for user_id {user_id}.'
    except ValueError:
        # Ignore if the message is not a user ID
        return

    await event.respond(response)

# Handler for messages to retrieve user history by username
@client.on(events.NewMessage(pattern=r'/allhistory'))
async def username_handler(event):
    args = event.message.text.split()
    if len(args) == 2:
        query = args[1]
        if query.startswith('@'):
            username = query[1:]
        else:
            username = query

        history = get_user_history_by_username(username)
        if history:
            response = f'History for username @{username}:\n'
            for record in history:
                user_id, name, username, timestamp = record
                response += f'User ID: {user_id}, Name: {name}, Username: {username}, Timestamp: {timestamp}\n'
        else:
            response = f'No history found for username @{username}.'

        await event.respond(response)
    else:
        await event.respond('Usage: /allhistory @username')

async def main():
    async with client:
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
