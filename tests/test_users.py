import json
import pytest
from dotenv import load_dotenv
from app.models.user import User
from app.crud import create_tables, drop_tables, insert_user, get_users

load_dotenv(dotenv_path=".env.test")

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Create and drop tables around tests"""
    create_tables()
    yield
    drop_tables()

# ---------------- Tests ----------------
def test_insert_and_get_users():
    insert_user(User(email="bob@example.com", username="bobby", user_password="test123"))
    insert_user(User(email="bobby@example.com", username="alice", user_password="test123"))

    users = get_users()
    assert len(users) == 2
    assert users[0]["username"] == "bobby"
    assert users[1]["email"] == "bobby@example.com"
