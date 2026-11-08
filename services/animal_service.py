from repositories import animal_repository
from repositories import species_repository
from repositories import owner_repository

def create_animal(name, species_id, sex, age, status, owner_id=None):

    if not name.strip():
        raise Exception("Кличка не может быть пустой")

    if sex not in ("М", "Ж"):
        raise Exception("Пол должен быть М или Ж")

    if age is not None and age < 0:
        raise Exception("Возраст не может быть отрицательным")

    if not status.strip():
        raise Exception("Статус не может быть пустым")

    if not species_repository.get_by_id(species_id):
        raise Exception("Указанный вид животного не существует")

    if owner_id is not None:
        if not owner_repository.get_by_id(owner_id):
            raise Exception("Указанный владелец не существует")

    return animal_repository.create(
        name, species_id, sex, age, status, owner_id
    )

def get_all_animals():
    return animal_repository.get_all()

def get_animal(animal_id):
    animal = animal_repository.get_by_id(animal_id)

    if not animal:
        raise Exception("Животное не найдено")

    return animal

def search_animals(name):
    if not name.strip():
        raise Exception("Введите кличку для поиска")

    return animal_repository.search_by_name(name)

def change_status(animal_id, new_status):
    if not new_status.strip():
        raise Exception("Статус не может быть пустым")

    if not animal_repository.get_by_id(animal_id):
        raise Exception("Животное не найдено")

    animal_repository.update_status(animal_id, new_status)

def assign_owner(animal_id, owner_id):

    if not animal_repository.get_by_id(animal_id):
        raise Exception("Животное не найдено")

    if not owner_repository.get_by_id(owner_id):
        raise Exception("Владелец не найден")

    animal_repository.assign_owner(animal_id, owner_id)

def delete_animal(animal_id):
    if not animal_repository.get_by_id(animal_id):
        raise Exception("Животное не найдено")

    animal_repository.delete(animal_id)

def update_animal(animal_id, name, species_id, sex, age, status, owner_id):

    if not animal_repository.get_by_id(animal_id):
        raise Exception("Животное не найдено")

    if not name.strip():
        raise Exception("Кличка не может быть пустой")

    if sex not in ("М", "Ж"):
        raise Exception("Пол должен быть М или Ж")

    if age is not None and age < 0:
        raise Exception("Возраст не может быть отрицательным")

    if not status.strip():
        raise Exception("Статус не может быть пустым")

    if not species_repository.get_by_id(species_id):
        raise Exception("Вид животного не найден")

    if owner_id is not None:
        if not owner_repository.get_by_id(owner_id):
            raise Exception("Владелец не найден")

    animal_repository.update(
        animal_id, name, species_id, sex, age, status, owner_id
    )