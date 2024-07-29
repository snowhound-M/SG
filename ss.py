from telethon import TelegramClient, events
import sqlite3, asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pandas as pd

api_id = 27598177
api_hash = "2a17655facad0790ca4ceb626ef23feb"
bot_token = "7268485439:AAEJGIflr-VRhYfXl0Suz5sWFoW7UYwqHdg"

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

         batch_size=50
         for i in range(0, len(user_ids), batch_size):
              batch = user_ids[i:i + batch_size]
              tasks = [process_user(user_id) for (user_id,) in batch]
              asyncio.gather(*tasks)

async def process_user(user_id):
    try:
         user = await client.get_entity(user_id)
         new_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
         new_username = f"@{user.username}" if user.username else "-"
         timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')

         cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp DESC', (user_id,))
         rows = cursor.fetchall()

         if rows:
              old_name, old_username, _ = rows[0]
              name_changed = old_name != new_name
              username_changed = old_username != new_username
              if name_changed and not username_changed:
                   cursor.execute('INSERT INTO users (user_id, name, username, timestamp) VALUES (?, ?, ?, ?)', (user_id, new_name, old_username, timestamp))
                   conn.commit()
                   print(f'Updated record for user_id {user_id} with name "{new_name}", username "{old_username}" and timestamp {timestamp}.')
              elif not name_changed and username_changed:
                   cursor.execute('INSERT INTO users (user_id, name, username, timestamp) VALUES (?, ?, ?, ?)', (user_id, old_name, new_username, timestamp))
                   conn.commit()
                   print(f'Updated record for user_id {user_id} with name "{old_name}", username "{new_username}" and timestamp {timestamp}.')
         else:
              return
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

    cursor.execute('SELECT DISTINCT user_id FROM users')
    user_ids = cursor.fetchall()

    if not any(users_id == user_id for (users_id,) in user_ids):
         # Store user information in the database
         cursor.execute('INSERT INTO users (user_id, name, username, timestamp) VALUES (?, ?, ?, ?)', (user_id, name, username, timestamp))
         conn.commit()

    await event.respond(f"Welcome {name}!")

# Function to retrieve user history by user ID
def get_user_history_by_id(user_id):
    cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp', (user_id,))
    all_entries = cursor.fetchall()
    print(all_entries)
    
    if not all_entries:
         return None

    unique_names = []
    last_name = None

    for name, username, timestamp in all_entries:
         if name != last_name:
              unique_names.append((name, timestamp))
              last_name = name

    unique_usernames = []
    last_username = None

    for name, username, timestamp in all_entries:
         if username != last_username:
              unique_usernames.append((username, timestamp))
              last_username = username
    return {'names': unique_names, 'usernames': unique_usernames}

# Handler for messages containing just a user ID
@client.on(events.NewMessage)
async def id_handler(event):
    try:
         user_id = int(event.message.text.strip())
         history = get_user_history_by_id(user_id)
         if history:
              name_entries = [f'`{i+1}. [{timestamp}]` {name}' for i, (name, timestamp) in enumerate(history['names'])]
              username_entries = [f'`{i+1}. [{timestamp}]` {username if username != "-" else "(empty)"}' for i, (username, timestamp) in enumerate(history['usernames'])]
              response = f'**History for** **[{user_id}](tg://user?id={user_id})**\n\n**Names**\n'  + '\n'.join(name_entries) + '\n\n**Usernames**\n' + '\n'.join(username_entries)
         else:
              response = f'No data available (**{user_id}**)'
    except ValueError:
         # Ignore if the message is not a user ID
         print("Failed due to ValueError.")
         return
    except Exception as e:
         print(f"Failed for user {user_id}: {e}")
         return
    await event.respond(response)

if __name__ == "__main__":
    client.run_until_disconnected()
