from database.database import get_connection
from models.species import Species

def _map(row):
    return Species(*row)

def create(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO species(name)
    VALUES(?)
    """, (name,))
    conn.commit()
    species_id = cursor.lastrowid
    conn.close()

    return species_id

def get_by_id(species_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name
        FROM species
        WHERE id = ?
    """, (species_id,))
    row = cursor.fetchone()
    conn.close()

    return _map(row) if row else None

def get_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name
        FROM species
    """)

    rows = cursor.fetchall()
    conn.close
    return [_map(row) for row in rows]

def update(species_id, name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE species
        SET name = ?
        WHERE id = ?
    """, (name, species_id))
    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result

def delete(species_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM species
        WHERE id = ?
    """, (species_id,))
    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result


    
