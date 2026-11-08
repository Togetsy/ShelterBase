
from database.database import get_connection
from models.user import User

def add_user(username, password_hash, salt, role):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, password_hash, salt, role)
        VALUES (?, ?, ?, ?)
    """, (username, password_hash, salt, role))

    conn.commit()
    user_id = cursor.lastrowid
    conn.close()

    return user_id


def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, password_hash, salt, role
        FROM users
        WHERE username = ?
    """, (username,))

    result = cursor.fetchone()
    conn.close()

    if result is None:
        return None

    return User(*result)

def count_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    conn.close()
    return count

def delete_employee(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM users
        WHERE username = ? AND role = 'employee'
    """, (username,))

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted > 0
