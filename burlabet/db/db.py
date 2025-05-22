from typing import List
import sqlite3
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from burlabet.entities.user import User

load_dotenv()

DB_PATH: str = os.getenv("DB_PATH")

def init_db() -> None:
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY,
      expires_at TEXT NOT NULL
    )
  ''')
  conn.commit()
  conn.close()

def add_user(id: int, days: int = 30) -> None:
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  expires_at = (datetime.now() + timedelta(days=days)).isoformat()
  c.execute("INSERT OR REPLACE INTO users (id, expires_at) VALUES (?, ?)", (id, expires_at))
  conn.commit()
  conn.close()

def is_user_valid(id: str) -> bool:
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute("SELECT expires_at FROM users WHERE id = ?", (id,))
  row = c.fetchone()
  conn.close()
  if row:
    return datetime.fromisoformat(row[0]) > datetime.now()
  return False

def get_users() -> List[User]:
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute("SELECT id, expires_at FROM users")
  users = c.fetchall()
  conn.close()
  if not users:
    return []
  return [User(id, expires_at) for id, expires_at in users]

def get_user(id: int) -> User | None:
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute("SELECT id, expires_at FROM users WHERE id = ?", (id,))
  row = c.fetchone()
  conn.close()
  if not row:
    return None
  return User(row[0], row[1])
