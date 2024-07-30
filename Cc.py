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
