import sqlite3

from proyectFace.utilities.files_utilities import set_db_root


class DataBase:
    def __init__(self):
        self.db_name = "facesDB.db"
        self.connection = sqlite3.connect(set_db_root(self.db_name))
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS recognizers(
            person TEXT,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.connection.commit()

    def add_guy(self, student):
        self.cursor.execute(
            """
            INSERT INTO recognizers(person) VALUES (?)
            """,
            (student,),
        )
        self.connection.commit()


if __name__ == "__main__":
    db = DataBase()
    db.create_table()
    db.add_guy("pepe")
