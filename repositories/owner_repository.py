from database.database import get_connection
from models.owner import Owner

def _map(row):
    return Owner(*row)

def create(name, address, phone, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO owners (name, address, phone, email)
        VALUES (?, ?, ?, ?)
    """, (name, address, phone, email))

    conn.commit()
    owner_id = cursor.lastrowid
    conn.close()

    return owner_id

def get_by_id(owner_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, address, phone, email
        FROM owners
        WHERE id = ?
    """, (owner_id,))

    row = cursor.fetchone()
    conn.close()

    return _map(row) if row else None

def get_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, address, phone, email
        FROM owners
    """)

    rows = cursor.fetchall()
    conn.close()

    return [_map(row) for row in rows]

def update(owner_id, name, address, phone, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE owners
        SET name = ?, address = ?, phone = ?, email = ?
        WHERE id = ?
    """, (name, address, phone, email, owner_id))

    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result

def delete(owner_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM owners
        WHERE id = ?
    """, (owner_id,))

    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result