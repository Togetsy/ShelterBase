import services.owner_service as owner_service

def show_owners():
    owners = owner_service.get_all_owners()

    if not owners:
        print("Владельцев пока нет.")
        return

    for owner in owners:
        print(
            f"\nID: {owner.id} | "
            f"ФИО: {owner.name} | "
            f"Адрес: {owner.address} | "
            f"Телефон: {owner.phone} | "
            f"Email: {owner.email or 'Не указан'}"
        )


def add_owner():
    try:
        name = input("ФИО владельца: ")
        address = input("Адрес: ")
        phone = input("Номер телефона: ")
        email = input("Электронная почта: ")

        owner_service.create_owner(name, address, phone, email)

        print("Владелец успешно добавлен!")

    except Exception as error:
        print(f"Ошибка: {error}")


def edit_owner():
    try:
        owner_id = int(input("Введите ID владельца: "))

        name = input("Новое ФИО: ")
        address = input("Новый адрес: ")
        phone = input("Новый номер телефона: ")
        email = input("Новая электронная почта: ")

        owner_service.update_owner(
            owner_id, name, address, phone, email
        )

        print("Данные владельца обновлены!")

    except ValueError:
        print("ID должен быть числом.")
    except Exception as error:
        print(f"Ошибка: {error}")


def delete_owner():
    try:
        owner_id = int(input("Введите ID владельца для удаления: "))

        owner_service.delete_owner(owner_id)

        print("Владелец удалён!")

    except ValueError:
        print("ID должен быть числом.")
    except Exception as error:
        print(f"Ошибка: {error}")