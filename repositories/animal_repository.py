from database.database import get_connection
from models.animal import Animal

def _map(row):
    return Animal(*row)

def create(name, species_id, sex, age, status, owner_id=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO animals
        (name, species_id, sex, age, status, owner_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, species_id, sex, age, status, owner_id))

    conn.commit()
    animal_id = cursor.lastrowid
    conn.close()

    return animal_id

def get_by_id(animal_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT animals.id, animals.name, animals.species_id,
               animals.sex, animals.age, animals.status,
               animals.owner_id,
               species.name, owners.name, owners.phone
        FROM animals
        JOIN species ON animals.species_id = species.id
        LEFT JOIN owners ON animals.owner_id = owners.id
        WHERE animals.id = ?
    """, (animal_id,))

    row = cursor.fetchone()
    conn.close()

    return _map(row) if row else None

def get_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT animals.id, animals.name, animals.species_id,
               animals.sex, animals.age, animals.status,
               animals.owner_id,
               species.name, owners.name, owners.phone
        FROM animals
        JOIN species ON animals.species_id = species.id
        LEFT JOIN owners ON animals.owner_id = owners.id
    """)

    rows = cursor.fetchall()
    conn.close()

    return [_map(row) for row in rows]

def search_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT animals.id, animals.name, animals.species_id,
               animals.sex, animals.age, animals.status,
               animals.owner_id,
               species.name, owners.name, owners.phone
        FROM animals
        JOIN species ON animals.species_id = species.id
        LEFT JOIN owners ON animals.owner_id = owners.id
        WHERE animals.name LIKE ?
    """, ('%' + name + '%',))

    rows = cursor.fetchall()
    conn.close()

    return [_map(row) for row in rows]

def update(animal_id, name, species_id, sex, age, status, owner_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE animals
        SET name = ?,
            species_id = ?,
            sex = ?,
            age = ?,
            status = ?,
            owner_id = ?
        WHERE id = ?
    """, (name, species_id, sex, age, status, owner_id, animal_id))

    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result

def update_status(animal_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE animals
        SET status = ?
        WHERE id = ?
    """, (status, animal_id))

    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result

def assign_owner(animal_id, owner_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE animals
        SET owner_id = ?
        WHERE id = ?
    """, (owner_id, animal_id))

    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result

def delete(animal_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM animals
        WHERE id = ?
    """, (animal_id,))

    conn.commit()
    result = cursor.rowcount
    conn.close()

    return result