import sqlite3
import os

db_path = os.path.join(os.environ.get("DB_PATH"), os.environ.get("DB_NAME"))

def get_conn() -> sqlite3.connect:
    conn = sqlite3.connect(db_path)
    return conn

def init_db():
    os.mkdir(os.environ.get("DB_PATH"))
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE user(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   uid INTEGER NOT NULL UNIQUE,
                   user_name TEXT NOT NULL
                   )
            """)
    cursor.execute("""
            CREATE TABLE task(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_gave_id INTEGER NOT NULL,
                   user_took_id INTEGER NOT NULL,
                   task_def TEXT NOT NULL,
                   completed INTEGER DEFAULT 0,
                   appointment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
            """)
    conn.commit()
    conn.close()

def check_db() -> bool: # checks if there is a db created (so we can create one)
    if not os.path.exists(os.environ.get("DB_PATH")):
        return False
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name = 'user'") 
    result = cursor.fetchone()
    conn.close()
    return result
    
def check_user(user_id:int) -> bool: # checks if a user added in db so they can assign task
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM user WHERE uid=?) ", (user_id, )) 
    result = cursor.fetchone()
    conn.close()
    return result


def execute_query(query, params:tuple = ()):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    result = cursor.fetchall()
    return result