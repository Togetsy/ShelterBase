from ui import auth_ui
from ui import animal_ui
from ui import owner_ui


def menu(user):
    while True:
        print("\n----- УЧЁТ ЖИВОТНЫХ ПРИЮТА -----")
        print(f"Пользователь: {user.username}")

        if user.role == "admin":
            print("Роль: Администратор")
            print("1. Добавить животное")
            print("2. Показать всех животных")
            print("3. Найти животное")
            print("4. Изменить статус животного")
            print("5. Удалить животное")
            print("6. Назначить владельца животному")
            print("7. Добавить владельца")
            print("8. Показать всех владельцев")
            print("9. Изменить данные владельца")
            print("10. Удалить владельца")
            print("11. Создать сотрудника")
            print("12. Удалить сотрудника")

        else:
            print("Роль: Сотрудник")
            print("2. Показать всех животных")
            print("3. Найти животное")
            print("8. Показать всех владельцев")
            
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1" and user.role == "admin":
            animal_ui.add_animal()

        elif choice == "2":
            animal_ui.show_animals()

        elif choice == "3":
            animal_ui.search_animal()

        elif choice == "4" and user.role == "admin":
            animal_ui.change_animal_status()

        elif choice == "5" and user.role == "admin":
            animal_ui.delete_animal()

        elif choice == "6" and user.role == "admin":
            animal_ui.assign_animal_owner()

        elif choice == "7" and user.role == "admin":
            owner_ui.add_owner()

        elif choice == "8":
            owner_ui.show_owners()

        elif choice == "9" and user.role == "admin":
            owner_ui.edit_owner()

        elif choice == "10" and user.role == "admin":
            owner_ui.delete_owner()

        elif choice == "11" and user.role == "admin":
            auth_ui.add_employee(user)
            
        elif choice == "12" and user.role == "admin":
            auth_ui.delete_employee(user)

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Недоступное действие или неверный выбор.")
