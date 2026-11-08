from repositories import owner_repository

def create_owner(name, address, phone, email):

    if not name.strip():
        raise Exception("ФИО не может быть пустым")

    if not address.strip():
        raise Exception("Адрес не может быть пустым")

    if not phone.strip():
        raise Exception("Номер телефона не может быть пустым")

    return owner_repository.create(
        name, address, phone, email
    )

def get_all_owners():
    return owner_repository.get_all()

def get_owner(owner_id):
    owner = owner_repository.get_by_id(owner_id)

    if not owner:
        raise Exception("Владелец не найден")

    return owner

def update_owner(owner_id, name, address, phone, email):

    if not owner_repository.get_by_id(owner_id):
        raise Exception("Владелец не найден")

    if not name.strip():
        raise Exception("ФИО не может быть пустым")

    if not address.strip():
        raise Exception("Адрес не может быть пустым")

    if not phone.strip():
        raise Exception("Телефон не может быть пустым")

    owner_repository.update(
        owner_id, name, address, phone, email
    )

def delete_owner(owner_id):

    if not owner_repository.get_by_id(owner_id):
        raise Exception("Владелец не найден")

    owner_repository.delete(owner_id)