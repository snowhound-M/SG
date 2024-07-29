from telethon import TelegramClient, events
import sqlite3
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pandas as pd

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

client = TelegramClient('HistoryTracker', api_id, api_hash).start(bot_token=bot_token)

# Set up SQLite Database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store the history of names and usernames with timestamps
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY,
name TEXT,
username TEXT,
timestamp TEXT
)
''')
conn.commit()

scheduler = AsyncIOScheduler()

async def update_user_info():
cursor.execute('SELECT DISTINCT user_id FROM users')
user_ids = cursor.fetchall()
if user_ids:
for user_id, in user_ids:
try:
user = await client.get_entity(user_id)
name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
username = f"@{user.username}" if user.username else "-"
timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')

cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp DESC', (user_id,))
rows = cursor.fetchall()

cursor.execute('''
INSERT INTO users (user_id, name, username, timestamp)
VALUES (?, ?, ?, ?)
''', (user_id, name, username, timestamp))
conn.commit()
except Exception as e:
print(f"Failed to update info for user {user_id}: {e}")

scheduler.add_job(update_user_info, 'interval', minutes=1)  # Adjust the interval as needed
scheduler.start()

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
user = await event.get_sender()
user_id = user.id
name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
username = f"@{user.username}" if user.username else "-"
timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')

    # Store user information in the database
    cursor.execute('''
        INSERT INTO users (user_id, name, username, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (user_id, name, username, timestamp))
    conn.commit()

    await event.respond(f"Welcome {name}!")


if __name__ == "__main__":
    client.run_until_disconnected()
