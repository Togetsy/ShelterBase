from repositories import species_repository

def create_species(name):

    if not name.strip():
        raise Exception("Название вида не может быть пустым")

    return species_repository.create(name)

def get_all_species():
    return species_repository.get_all()

def get_species(species_id):
    species = species_repository.get_by_id(species_id)

    if not species:
        raise Exception("Вид животного не найден")

    return species

def update_species(species_id, name):

    if not species_repository.get_by_id(species_id):
        raise Exception("Вид животного не найден")

    if not name.strip():
        raise Exception("Название вида не может быть пустым")

    species_repository.update(species_id, name)

def delete_species(species_id):

    if not species_repository.get_by_id(species_id):
        raise Exception("Вид животного не найден")

    species_repository.delete(species_id)