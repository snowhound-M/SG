import sqlite3

# Define IDs as a dictionary
ids_dict = {
    "ids": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50
    ]
}

# Extract IDs from the dictionary
def extract_ids_from_dict(dictionary):
    return dictionary['ids']

# Insert IDs into the database
def insert_ids_into_db(ids, db_path):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ids_table (
        id INTEGER PRIMARY KEY
    )
    ''')

    # Insert IDs into the table
    cursor.executemany('INSERT INTO ids_table (id) VALUES (?)', [(id,) for id in ids])

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def main():
    db_path = 'database.db'  # Path to your SQLite database file

    ids = extract_ids_from_dict(ids_dict)
    insert_ids_into_db(ids, db_path)

if __name__ == '__main__':
    main()

import sqlite3

# Define the data as a dictionary
data = {
    "users": [
        {"user_id": 7475936622, "name": "Good", "username": "-", "timestamp": "29/07/24 15:00:00"},
        {"user_id": 6781896926, "name": "Asmita", "username": "-", "timestamp": "29/07/24 15:01:00"},
        {"user_id": 1508089158, "name": "Ishika", "username": "-", "timestamp": "29/07/24 15:02:00"},
        {"user_id": 7324549725, "name": "Anmol Mishra", "username": "-", "timestamp": "29/07/24 15:03:00"},
        {"user_id": 689899354, "name": "Krishna", "username": "-", "timestamp": "29/07/24 15:04:00"},
        {"user_id": 7417984306, "name": "Rahul", "username": "-", "timestamp": "29/07/24 15:05:00"},
        {"user_id": 7413395357, "name": "Thor", "username": "-", "timestamp": "29/07/24 15:06:00"},
        {"user_id": 1851649652, "name": "A M", "username": "-", "timestamp": "29/07/24 15:07:00"},
        {"user_id": 7112621900, "name": "Kiran", "username": "-", "timestamp": "29/07/24 15:08:00"},
        {"user_id": 6943386045, "name": "Ayush", "username": "-", "timestamp": "29/07/24 15:09:00"},
        {"user_id": 7267167440, "name": "Sonia Sharma", "username": "-", "timestamp": "29/07/24 15:10:00"},
        {"user_id": 6991377519, "name": "Gaurav", "username": "-", "timestamp": "29/07/24 15:11:00"},
        {"user_id": 7315680624, "name": "The Stubborn:)✨♥", "username": "-", "timestamp": "29/07/24 15:12:00"},
        {"user_id": 5657826426, "name": "Surya Jaiswal", "username": "-", "timestamp": "29/07/24 15:13:00"},
        {"user_id": 7017662272, "name": "Mradul Sharma", "username": "-", "timestamp": "29/07/24 15:14:00"},
        {"user_id": 6894259695, "name": "RK", "username": "-", "timestamp": "29/07/24 15:15:00"},
        {"user_id": 6969674897, "name": "Arun", "username": "-", "timestamp": "29/07/24 15:16:00"},
        {"user_id": 6847297037, "name": ".", "username": "-", "timestamp": "29/07/24 15:17:00"},
        {"user_id": 1380756212, "name": "SHAIKH", "username": "-", "timestamp": "29/07/24 15:18:00"},
        {"user_id": 7370743009, "name": "Lav", "username": "-", "timestamp": "29/07/24 15:19:00"},
        {"user_id": 6080259290, "name": "Unknown", "username": "-", "timestamp": "29/07/24 15:20:00"},
        {"user_id": 1295626938, "name": "colty", "username": "@Colty420", "timestamp": "29/07/24 15:21:00"},
        {"user_id": 2113725376, "name": "Pramod", "username": "-", "timestamp": "29/07/24 15:22:00"},
        {"user_id": 7393093143, "name": "Parth", "username": "-", "timestamp": "29/07/24 15:23:00"},
        {"user_id": 5208683829, "name": "ceratine✌️❤️❣️", "username": "@ceratine267", "timestamp": "29/07/24 15:24:00"},
        {"user_id": 5902985175, "name": "SRS", "username": "-", "timestamp": "29/07/24 15:25:00"},
        {"user_id": 6148709539, "name": "Pppp", "username": "-", "timestamp": "29/07/24 15:26:00"},
        {"user_id": 7078680440, "name": "Mil 02", "username": "@Kl_Mil_02", "timestamp": "29/07/24 15:27:00"},
        {"user_id": 1578419305, "name": "Mukesh", "username": "-", "timestamp": "29/07/24 15:28:00"},
        {"user_id": 6730510893, "name": "Nikki", "username": "-", "timestamp": "29/07/24 15:29:00"}
    ]
}

# Function to insert data into the database
def insert_users_into_db(users, db_path):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        username TEXT,
        timestamp TEXT
    )
    ''')

    # Insert users into the table
    cursor.executemany('''
    INSERT OR IGNORE INTO users (user_id, name, username, timestamp)
    VALUES (?, ?, ?, ?)
    ''', [(user['user_id'], user['name'], user['username'], user['timestamp']) for user in users])

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def main():
    db_path = 'database.db'  # Path to your SQLite database file

    # Extract users list from the data dictionary
    users = data['users']
    insert_users_into_db(users, db_path)

if __name__ == '__main__':
    main()

from telethon import TelegramClient, events
import sqlite3, asyncio, time
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
    user_id INTEGER,
    name TEXT,
    username TEXT,
    timestamp TEXT
)
''')
conn.commit()

scheduler = AsyncIOScheduler()

async def update_user_info():
    function_start = time.time()
    start = time.time()
    cursor.execute('SELECT DISTINCT user_id FROM users')
    end = time.time()
    user_ids = cursor.fetchall()
    print(user_ids)
    print(f"Database fetching started : {start} Database fetching ended : {end} Database fetching completed in : {end - start}")
    if user_ids:

         batch_size=50
         batch_start = time.time()
         for i in range(0, len(user_ids), batch_size):
              batch = user_ids[i:i + batch_size]
              print(batch)
              tasks = [process_user(user_id) for (user_id,) in batch]
              try:
                   task_start = time.time()
                   asyncio.gather(*tasks)
                   task_end = time.time()
                   print(f"Task started : {task_start} Task ended : {task_end} Task completed in : {task_end - task_start}")
              except Exception as e:
                   print(f"Error occurred while gathering tasks: {e}")
         batch_end = time.time()
         print(f"Batch started : {batch_start} Batch ended : {batch_end} Batch completed in : {batch_end - batch_start}")
    function_end = time.time()
    print(f"Function started : {function_start} Function ended : {function_end} Function completed in : {function_end - function_start}")

async def process_user(user_id):
    process_start = time.time()
    try:
         print(user_id)
         user = await client.get_entity(user_id)
         new_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
         new_username = f"@{user.username}" if user.username else "-"
         timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')

         cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp DESC', (user_id,))
         rows = cursor.fetchall()

         if rows:
              old_name, old_username, _ = rows[0]
              name_changed = old_name != new_name
              print(name_changed)
              username_changed = old_username != new_username
              print(username_changed)
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
    process_end = time.time()
    print(f"Process started : {process_start} Process ended : {process_end} Process completed in : {process_end - process_start}")

try:
    scheduler.add_job(update_user_info, 'interval', seconds=2)  # Adjust the interval as needed
    scheduler.start()
except Exception as e:
    print(f"Error occurred while scheduling tasks: {e}") 

# Function to retrieve user history by user ID
def get_user_history_by_id(user_id):
    cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp', (user_id,))
    first_entries = cursor.fetchone()
    print(first_entries)
    cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp', (user_id,))
    all_entries = cursor.fetchall()
    print(all_entries)
    
    if not all_entries:
         return None

    unique_names = []
    last_name, last_username, _ = first_entries

    for name, username, timestamp in all_entries:
         if name != last_name:
              unique_names.append((name, timestamp))
              last_name = name

    print(unique_names)
    unique_usernames = []

    for name, username, timestamp in all_entries:
         if username != last_username:
              unique_usernames.append((username, timestamp))
              last_username = username

    print(unique_usernames)
    return {'names': unique_names, 'usernames': unique_usernames}

# Handler for messages containing just a user ID
@client.on(events.NewMessage)
async def id_handler(event):
    try:
         user_id = int(event.message.text.strip())
         history = get_user_history_by_id(user_id)
         print(history)
         if history:
              name_entries = [f'`{i+1}. [{timestamp}]` {name}' for i, (name, timestamp) in enumerate(history['names'])]
              username_entries = [f'`{i+1}. [{timestamp}]` {username if username != "-" else "(empty)"}' for i, (username, timestamp) in enumerate(history['usernames'])] 
              response = f'`The following info is updated since {min(history["names"], key=lambda x: x[1])[1].split(" ")[0] if history["names"] else min(history["usernames"], key=lambda x: x[1])[1].split(" ")[0]}`\n\n**🎭 History for** **[{user_id}](tg://user?id={user_id})**\n\n**Names**\n'  + '\n'.join(name_entries) + '\n\n**Usernames**\n' + '\n'.join(username_entries)
         else:
              response = f'No data available (**{user_id}**)'
    except ValueError:
         if event.message.text.strip() == "/start":
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
              response = f"Hi **{name}** ! 🎉\n\nWelcome to `SANGMATA BOT`, where exploring user info is both easy and exciting!\n\n`What can I do for you?`\n\n- **Uncover the history** of any user ID.\n- **Monitor your own profile changes.**\n\n\nTo begin, simply provide a user ID.\n\nAlways `Restart` the bot with /start."
         else:
              response = 'Use either ID or /start command.'
    except Exception as e:
         print(f"Failed for user {user_id}: {e}")
         return
    await event.respond(response)

# Handler for messages to retrieve user history table from database 
@client.on(events.NewMessage(pattern=r'/db'))
async def database_retriever(event):
    try:
       db_table = pd.read_sql_query('SELECT * FROM users', conn)
       print(db_table)
    except:
       return

if __name__ == "__main__":
    client.run_until_disconnected()

import asyncio
import sqlite3
import time
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pandas as pd
from pyrogram import Client, filters

api_id = 27598177
api_hash = "2a17655facad0790ca4ceb626ef23feb"
bot_token = "7268485439:AAEJGIflr-VRhYfXl0Suz5sWFoW7UYwqHdg"

app = Client("HistoryTracker", api_id, api_hash, bot_token=bot_token)

# Set up SQLite Database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table to store the history of names and usernames with timestamps
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    name TEXT,
    username TEXT,
    timestamp TEXT
)
''')
conn.commit()

scheduler = AsyncIOScheduler()

async def update_user_info():
    function_start = time.time()
    start = time.time()
    cursor.execute('SELECT DISTINCT user_id FROM users')
    end = time.time()
    user_ids = cursor.fetchall()
    print(user_ids)
    print(f"Database fetching started : {start} Database fetching ended : {end} Database fetching completed in : {end - start}")
    if user_ids:

        batch_size = 50
        batch_start = time.time()
        for i in range(0, len(user_ids), batch_size):
            batch = user_ids[i:i + batch_size]
            print(batch)
            tasks = [process_user(user_id) for (user_id,) in batch]
            try:
                task_start = time.time()
                await asyncio.gather(*tasks)
                task_end = time.time()
                print(f"Task started : {task_start} Task ended : {task_end} Task completed in : {task_end - task_start}")
            except Exception as e:
                print(f"Error occurred while gathering tasks: {e}")
        batch_end = time.time()
        print(f"Batch started : {batch_start} Batch ended : {batch_end} Batch completed in : {batch_end - batch_start}")
    function_end = time.time()
    print(f"Function started : {function_start} Function ended : {function_end} Function completed in : {function_end - function_start}")

async def process_user(user_id):
    process_start = time.time()
    try:
        print(user_id)
        user = await app.get_users(user_id)
        new_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        new_username = f"@{user.username}" if user.username else "-"
        timestamp = datetime.now().strftime('%d/%m/%y %H:%M:%S')

        cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp DESC', (user_id,))
        rows = cursor.fetchall()

        if rows:
            old_name, old_username, _ = rows[0]
            name_changed = old_name != new_name
            print(name_changed)
            username_changed = old_username != new_username
            print(username_changed)
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
    process_end = time.time()
    print(f"Process started : {process_start} Process ended : {process_end} Process completed in : {process_end - process_start}")

try:
    scheduler.add_job(update_user_info, 'interval', seconds=2)  # Adjust the interval as needed
    scheduler.start()
except Exception as e:
    print(f"Error occurred while scheduling tasks: {e}")

# Function to retrieve user history by user ID
def get_user_history_by_id(user_id):
    cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp', (user_id,))
    first_entries = cursor.fetchone()
    print(first_entries)
    cursor.execute('SELECT name, username, timestamp FROM users WHERE user_id=? ORDER BY timestamp', (user_id,))
    all_entries = cursor.fetchall()
    print(all_entries)
    
    if not all_entries:
        return None

    unique_names = []
    last_name = first_entries[0] if first_entries else None

    for name, username, timestamp in all_entries:
        if name != last_name:
            unique_names.append((name, timestamp))
            last_name = name

    print(unique_names)
    unique_usernames = []
    last_username = first_entries[1] if first_entries else None

    for name, username, timestamp in all_entries:
        if username != last_username:
            unique_usernames.append((username, timestamp))
            last_username = username

    print(unique_usernames)
    return {'names': unique_names, 'usernames': unique_usernames}

# Handler for messages containing just a user ID
@app.on_message(filters.text & ~filters.command('start'))
async def id_handler(client, message):
    try:
        user_id = int(message.text.strip())
        history = get_user_history_by_id(user_id)
        print(history)
        if history:
            name_entries = [f'`{i+1}. [{timestamp}]` {name}' for i, (name, timestamp) in enumerate(history['names'])]
            username_entries = [f'`{i+1}. [{timestamp}]` {username if username != "-" else "(empty)"}' for i, (username, timestamp) in enumerate(history['usernames'])] 
            response = f'`The following info is updated since {min(history["names"], key=lambda x: x[1])[1].split(" ")[0] if history["names"] else min(history["usernames"], key=lambda x: x[1])[1].split(" ")[0]}`\n\n**🎭 History for** **[{user_id}](tg://user?id={user_id})**\n\n**Names**\n'  + '\n'.join(name_entries) + '\n\n**Usernames**\n' + '\n'.join(username_entries)
        else:
            response = f'No data available (**{user_id}**)'
    except ValueError:
        if message.text.strip() == "/start":
            user = message.from_user
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
            response = f"Hi **{name}** ! 🎉\n\nWelcome to `SANGMATA BOT`, where exploring user info is both easy and exciting!\n\n`What can I do for you?`\n\n- **Uncover the history** of any user ID.\n- **Monitor your own profile changes.**\n\n\nTo begin, simply provide a user ID.\n\nAlways `Restart` the bot with /start."
        else:
            response = 'Use either ID or /start command.'
    except Exception as e:
        print(f"Failed for user {user_id}: {e}")
        return
    await message.reply(response)

# Handler for messages to retrieve user history table from database 
@app.on_message(filters.command('db'))
async def database_retriever(client, message):
    try:
        db_table = pd.read_sql_query('SELECT * FROM users', conn)
        print(db_table)
    except Exception as e:
        print(f"Failed to retrieve database table: {e}")

if __name__ == "__main__":
    app.run()
