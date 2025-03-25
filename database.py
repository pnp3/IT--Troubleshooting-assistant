import sqlite3
from datetime import datetime

DATABASE_NAME = 'troubleshoot.db'

def get_db_connection():
    """Create a connection to the SQLite database"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create issues table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS issues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        resolution TEXT,
        created_at TIMESTAMP NOT NULL,
        resolved_at TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def save_issue(description, diagnosis):
    """Save a new issue to the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO issues (description, diagnosis, created_at) VALUES (?, ?, ?)',
        (description, diagnosis, datetime.now())
    )
    
    issue_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return issue_id

def update_resolution(issue_id, resolution):
    """Update an issue with its resolution"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'UPDATE issues SET resolution = ?, resolved_at = ? WHERE id = ?',
        (resolution, datetime.now(), issue_id)
    )
    
    conn.commit()
    conn.close()

def get_all_issues():
    """Get all issues from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM issues ORDER BY created_at DESC')
    issues = cursor.fetchall()
    
    conn.close()
    
    return issues

def get_issue(issue_id):
    """Get a specific issue by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM issues WHERE id = ?', (issue_id,))
    issue = cursor.fetchone()
    
    conn.close()
    
    return issue 