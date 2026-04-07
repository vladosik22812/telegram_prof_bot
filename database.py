import sqlite3
import json

def create_tables():
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            username TEXT,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            result_data TEXT,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    """)
    
    connection.commit()
    connection.close()
    print("База данных готова")

def add_user(user_id, first_name, username):
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, first_name, username) VALUES (?, ?, ?)",
        (user_id, first_name, username)
    )
    
    connection.commit()
    connection.close()

def get_user(user_id):
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    
    connection.close()
    return user

def save_test_result(user_id, results):
    connection = sqlite3.connect("bot_database.db")
    cursor = connection.cursor()
    
    results_json = json.dumps(results)
    
    cursor.execute(
        "INSERT INTO test_results (user_id, result_data) VALUES (?, ?)",
        (user_id, results_json)
    )
    
    connection.commit()
    connection.close()
    print(f"✅ Результат сохранён для {user_id}")

if __name__ == "__main__":
    create_tables()