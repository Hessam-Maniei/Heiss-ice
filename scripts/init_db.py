import sqlite3
from pathlib import Path

# Path handling (robust & portable)
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "planner.db"

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# User table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")
.......

# AVAILABILITY
cursor.execute("""
CREATE TABLE IF NOT EXISTS availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT,
    is_free INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
""")

# LOCATIONS
cursor.execute("""
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    latitude REAL,
    longitude REAL
);
""")

#  WEATHER 
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER,
    date TEXT,
    temperature REAL,
    precipitation REAL,
    description TEXT,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);
""")

# EVENTS (final matched output)
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    location_id INTEGER,
    score REAL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);
""")

conn.commit()
conn.close()

print("planner.db created successfully at:", DB_PATH)
