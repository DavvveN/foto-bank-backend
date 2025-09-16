from datetime import datetime
import json
import uuid
from app.database.connection import get_connection
from app.models.user import User

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id CHAR(36) PRIMARY KEY,
        email VARCHAR(100) NOT NULL UNIQUE,
        username VARCHAR(100) NOT NULL, 
        user_password VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20), 
        profile_pic_url VARCHAR (255),
        metadata JSON, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        last_login_at TIMESTAMP NULL
    )
    """)
    cursor.close()
    conn.close()

def insert_user(user : User):
    conn = get_connection() 
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO users (
            user_id, email, username, user_password, phone_number, profile_pic_url, metadata, created_at, updated_at
        ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)
    """
    now = datetime.now()
    if not user.user_id:
        user.user_id = str(uuid.uuid4())
    
    cursor.execute(sql, (
        user.user_id,
        user.email,
        user.username,
        user.user_password,
        user.phone_number,
        user.profile_pic_url,
        json.dumps(user.metadata) if user.metadata else None,
        now,
        now
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return user.user_id

def drop_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.close()
    conn.close()

def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result