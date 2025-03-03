# Archivos de Proyecto
import os

CURRENT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DB_FILE = os.path.join(CURRENT_DIRECTORY, "db")


def set_db_root(db_name):
    return os.path.join(CURRENT_DIRECTORY, "db", db_name)


if __name__ == "__main__":
    print(CURRENT_DIRECTORY)
    print(DB_FILE)
