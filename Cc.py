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
