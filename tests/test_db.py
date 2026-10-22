
import sqlite3

base = sqlite3.connect("shelter.db")
cursor = base.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS species (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )""")
cursor.execute("INSERT OR IGNORE INTO species (name) VALUES (?)", ('Кошка',))
cursor.execute("INSERT OR IGNORE INTO species (name) VALUES (?)", ('Собака',))

cursor.execute("""CREATE TABLE IF NOT EXISTS animals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    species_id INTEGER NOT NULL,
                    sex TEXT NOT NULL,
                    age INTEGER,
                    status TEXT NOT NULL DEFAULT 'В приюте',
                    FOREIGN KEY (species_id) REFERENCES species (id)
                )""")

def add_animal():
    name = input("Кличка животного: ")
    species_id = int(input("Вид (1 — кошка, 2 — собака): "))
    sex = input("Пол (М/Ж): ")
    age = int(input("Возраст: "))
    status = input("Статус: ")
    cursor.execute("""
        INSERT INTO animals (name, species_id, sex, age, status)
        VALUES (?, ?, ?, ?, ?)
    """, (name, species_id, sex, age, status))

    base.commit()
    print("Животное добавлено!")

def show_animals():
    cursor.execute("""
        SELECT animals.id, animals.name, species.name,
               animals.sex, animals.age, animals.status
        FROM animals
        JOIN species ON animals.species_id = species.id
    """)

    animals = cursor.fetchall()

    if not animals:
        print("В приюте пока нет животных.")
        return

    for animal in animals:
        print(
            f"ID: {animal[0]} | "
            f"Кличка: {animal[1]} | "
            f"Вид: {animal[2]} | "
            f"Пол: {animal[3]} | "
            f"Возраст: {animal[4]} | "
            f"Статус: {animal[5]}"
        )
def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить животное")
        print("2. Показать всех животных")
        print("3. Выйти")
        print("4. Поиск животного")
        print("5. Изменить статус животного")
        print("6. Удалить животное")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            add_animal()
        elif choice == '2':
            show_animals()
        elif choice == '3':
            break
        elif choice == '4':
            search_animal()
        elif choice == '5':
            change_status()
        elif choice == '6':
            delete_animal()
        else:
            print("Неверный выбор. Попробуйте снова.")

def search_animal():
    search_name = input("Введите кличку животного для поиска: ")
    cursor.execute("""
        SELECT animals.id, animals.name, species.name,
               animals.sex, animals.age, animals.status
        FROM animals
        JOIN species ON animals.species_id = species.id
        WHERE animals.name LIKE ?
    """, ('%' + search_name + '%',))

    results = cursor.fetchall()

    if not results:
        print("Животное с такой кличкой не найдено.")
        return

    for animal in results:
        print(
            f"ID: {animal[0]} | "
            f"Кличка: {animal[1]} | "
            f"Вид: {animal[2]} | "
            f"Пол: {animal[3]} | "
            f"Возраст: {animal[4]} | "
            f"Статус: {animal[5]}"
        )
def change_status():
    animal_id = int(input("Введите ID животного для изменения статуса: "))
    new_status = input("Введите новый статус: ")

    cursor.execute("""
        UPDATE animals
        SET status = ?
        WHERE id = ?
    """, (new_status, animal_id))

    if cursor.rowcount == 0:
        print("Животное с таким ID не найдено.")
    else:
        print("Статус животного обновлен.")
    base.commit()

def delete_animal():
    animal_id = int(input("Введите ID животного для удаления: "))

    cursor.execute("""
        DELETE FROM animals
        WHERE id = ?
    """, (animal_id,))

    if cursor.rowcount == 0:
        print("Животное с таким ID не найдено.")
    else:
        print("Животное удалено.")
    base.commit()

base.commit()

menu()
base.close()
