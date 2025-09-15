import json
import pytest
from dotenv import load_dotenv
import os
from app.database import get_connection

load_dotenv(dotenv_path=".env.test")

# ---------------- Helpers ----------------
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20),
        profile_pic_url VARCHAR(255),
        metadata JSON,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        last_login_at TIMESTAMP NULL
    )
    """)
    cursor.close()
    conn.close()

def drop_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.close()
    conn.close()

def insert_user(name, email, password, phone_number=None, profile_pic_url=None, metadata=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, email, password, phone_number, profile_pic_url, metadata)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (name, email, password, phone_number, profile_pic_url, json.dumps(metadata) if metadata else None))
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

# ---------------- Fixtures ----------------
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Create and drop tables around tests"""
    create_tables()
    yield
    drop_tables()

# ---------------- Tests ----------------
def test_insert_and_get_users():
    insert_user("Alice", "alice@example.com", "hashedpass", metadata={"theme": "dark"})
    insert_user("Bob", "bob@example.com", "hashedpass", phone_number="1234567890")

    users = get_users()
    assert len(users) == 2
    assert users[0]["name"] == "Alice"
    assert users[1]["email"] == "bob@example.com"
