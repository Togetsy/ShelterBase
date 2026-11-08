
from services import auth_service


def login():
    print("\n----- АВТОРИЗАЦИЯ -----")

    username = input("Логин: ")
    password = input("Пароль: ")

    user = auth_service.login_user(username, password)

    if user is None:
        print("Неверный логин или пароль.")
        return None

    print(f"\nДобро пожаловать, {user.username}!")

    if user.role == "admin":
        print("Роль: Администратор")
    else:
        print("Роль: Сотрудник")

    return user

def setup_admin():
    print("\n----- СОЗДАНИЕ АДМИНИСТРАТОРА -----")

    username = input("Придумайте логин: ")
    password = input("Придумайте пароль: ")

    if auth_service.create_first_admin(username, password):
        print("Администратор успешно создан!")
        return True

    print("Не удалось создать администратора.")
    return False

def add_employee(current_user):
    print("\n----- СОЗДАНИЕ СОТРУДНИКА -----")

    username = input("Придумайте логин сотрудника: ")
    password = input("Придумайте пароль: ")
    password_repeat = input("Повторите пароль: ")

    if password != password_repeat:
        print("Пароли не совпадают.")
        return

    if auth_service.create_employee(current_user, username, password):
        print("Сотрудник успешно создан!")
    else:
        print("Не удалось создать сотрудника.")
        print("Проверьте логин и права доступа.")

def delete_employee(current_user):
    print("\n----- УДАЛЕНИЕ СОТРУДНИКА -----")

    username = input("Введите логин сотрудника: ")

    if auth_service.delete_employee(current_user, username):
        print("Сотрудник успешно удалён!")
    else:
        print("Не удалось удалить сотрудника.")
        print("Проверьте логин и права доступа.")
