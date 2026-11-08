import services.animal_service as animal_service
import services.species_service as species_service
def show_animals():
    animals = animal_service.get_all_animals()

    if not animals:
        print("Животных пока нет.")
        return

    for animal in animals:
        print(
            f"\nID: {animal.id} | "
            f"Кличка: {animal.name} | "
            f"Вид: {animal.species_name} | "
            f"Пол: {animal.sex} | "
            f"Возраст: {animal.age} | "
            f"Статус: {animal.status} | "
            f"Владелец: {animal.owner_name or 'Нет'} | "
            f"Телефон: {animal.owner_phone or 'Нет'}"
        )


def add_animal():
    try:
        name = input("Кличка животного: ")

        print("\nДоступные виды:")
        for species in species_service.get_all_species():
            print(f"{species.id}. {species.name}")

        species_id = int(input("Введите ID вида: "))
        sex = input("Пол (М/Ж): ")
        age = int(input("Возраст: "))
        status = input("Статус: ")

        animal_service.create_animal(
            name, species_id, sex, age, status
        )

        print("Животное успешно добавлено!")

    except ValueError:
        print("Ошибка: ID и возраст должны быть числами.")
    except Exception as error:
        print(f"Ошибка: {error}")

def search_animal():
    try:
        name = input("Введите кличку для поиска: ")
        animals = animal_service.search_animals(name)

        if not animals:
            print("Животные не найдены.")
            return

        for animal in animals:
            print(
                f"ID: {animal.id} | "
                f"Кличка: {animal.name} | "
                f"Вид: {animal.species_name} | "
                f"Пол: {animal.sex} | "
                f"Возраст: {animal.age} | "
                f"Статус: {animal.status}"
            )

    except Exception as error:
        print(f"Ошибка: {error}")

def change_animal_status():
    try:
        animal_id = int(input("Введите ID животного: "))
        new_status = input("Введите новый статус: ")

        animal_service.change_status(animal_id, new_status)

        print("Статус успешно изменён!")

    except ValueError:
        print("ID должен быть числом.")
    except Exception as error:
        print(f"Ошибка: {error}")

def delete_animal():
    try:
        animal_id = int(input("Введите ID животного для удаления: "))

        animal_service.delete_animal(animal_id)

        print("Животное удалено!")

    except ValueError:
        print("ID должен быть числом.")
    except Exception as error:
        print(f"Ошибка: {error}")

def assign_animal_owner():
    try:
        animal_id = int(input("Введите ID животного: "))
        owner_id = int(input("Введите ID владельца: "))

        animal_service.assign_owner(animal_id, owner_id)

        print("Владелец успешно назначен!")

    except ValueError:
        print("ID должны быть числами.")
    except Exception as error:
        print(f"Ошибка: {error}")