from ui import animal_ui
from ui import owner_ui


def menu():
    while True:
        print("\n----- УЧЁТ ЖИВОТНЫХ ПРИЮТА -----")
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
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            animal_ui.add_animal()

        elif choice == "2":
            animal_ui.show_animals()

        elif choice == "3":
            animal_ui.search_animal()

        elif choice == "4":
            animal_ui.change_animal_status()

        elif choice == "5":
            animal_ui.delete_animal()

        elif choice == "6":
            animal_ui.assign_animal_owner()

        elif choice == "7":
            owner_ui.add_owner()

        elif choice == "8":
            owner_ui.show_owners()

        elif choice == "9":
            owner_ui.edit_owner()

        elif choice == "10":
            owner_ui.delete_owner()

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")