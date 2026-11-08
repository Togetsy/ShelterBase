from database.database import initialize_database
from repositories import user_repository
from ui import auth_ui
from ui.menu import menu

def main():
    initialize_database()

    if user_repository.count_users() == 0:
        print("В системе ещё нет пользователей.")
        print("Необходимо создать администратора.")

        if not auth_ui.setup_admin():
            return

    user = auth_ui.login()

    if user is not None:
        menu(user)

if __name__ == "__main__":
    main()
