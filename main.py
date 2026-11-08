from ui.menu import menu
from database.database import initialize_database


def main():
    initialize_database()
    menu()


if __name__ == "__main__":
    main()