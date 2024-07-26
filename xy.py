from datetime import datetime
from telethon import TelegramClient, events
from telethon.tl.types import UpdateUserName
import sqlite3
import asyncio

# Replace with your own values
api_id = 27598177
api_hash = "2a17655facad0790ca4ceb626ef23feb"
bot_token = "7268485439:AAEJGIflr-VRhYfXl0Suz5sWFoW7UYwqHdg"

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
@client.on(events.Raw)
async def user_update_handler(event):
    timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    print(event)
    if isinstance(event, UpdateUserName):
         print("Passed.")
         pass
    else:
         print("Failed.")
         return
    if event.user_id:
        user_id = event.user_id
        new_name = f"{event.first_name} {event.last_name}" if event.last_name else event.first_name
        new_username = f"@{event.username}" if event.username else "-"

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
    cursor.execute('SELECT name, timestamp FROM user_history WHERE user_id=? ORDER BY timestamp', (user_id,))
    names = cursor.fetchall()
    cursor.execute('SELECT username, timestamp FROM user_history WHERE user_id=? ORDER BY timestamp', (user_id,))
    usernames = cursor.fetchall()
    return {'names': names, 'usernames': usernames}

# Function to retrieve user history by username
def get_user_history_by_username(username):
    try:
        entity = client.get_entity(username)
        user_id = entity.id
    except:
        return
    cursor.execute('SELECT name, timestamp FROM user_history WHERE user_id=? ORDER BY timestamp', (user_id,))
    names = cursor.fetchall()
    cursor.execute('SELECT username, timestamp FROM user_history WHERE user_id=? ORDER BY timestamp', (user_id,))
    usernames = cursor.fetchall()
    return {'names': names, 'usernames': usernames}

# Handler for messages containing just a user ID
@client.on(events.NewMessage)
async def id_handler(event):
    try:
        user_id = int(event.message.text.strip())
        history = get_user_history_by_id(user_id)
        if history:
            name_entries = [f'`{i+1}. [{timestamp}]` {name}' for i, (name, timestamp) in enumerate(history['names'])]
            username_entries = [f'`{i+1}. [{timestamp}]` {username if username != "-" else "(empty)"}' for i, (username, timestamp) in enumerate(history['usernames'])]
            response = f'**History for** {user_id}\n\n**Names**\n'  + '\n'.join(name_entries) + '\n\n**Usernames**\n' + '\n'.join(username_entries)
        else:
            response = f'No history found for {user_id}.'
    except ValueError:
        # Ignore if the message is not a user ID
        return

    await event.respond(response)

# Handler for messages to retrieve user history by username
@client.on(events.NewMessage(pattern=r'/allhistory\s+@(\w+)'))
async def username_handler(event):
    try:
        username = event.pattern_match.group(1)
        history = get_user_history_by_username(username)
        if history:
            name_entries = [f'`{i+1}. [{timestamp}]` {name}' for i, (name, timestamp) in enumerate(history['names'])]
            username_entries = [f'`{i+1}. [{timestamp}]` {username if username != "-" else "(empty)"}' for i, (username, timestamp) in enumerate(history['usernames'])]
            response = f'**History for** {username}\n\n**Names**\n'  + '\n'.join(name_entries) + '\n\n**Usernames**\n' + '\n'.join(username_entries)
        else:
            response = f'No history found for {username}.'
    except ValueError:
        # Ignore if the message is not a user ID
        return

    await event.respond(response)


if __name__ == '__main__':
    client.run_until_disconnected()
