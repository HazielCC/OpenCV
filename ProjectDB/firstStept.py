import sqlite3

from ProjectDB.utilities.files_utilities import set_db_root


class DataBase:
    def __init__(self):
        self.db_name = "ProjectDB.db"
        self.connection = sqlite3.connect(set_db_root(self.db_name))
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS general(
            alumno TEXT PRIMARY KEY,
            materia TEXT,
            calificacion INTEGER
            )
            """
        )
        self.connection.commit()

    def add_student(self, name_student):
        self.cursor.execute(
            "INSERT INTO general (alumno) VALUES(?)",
            (name_student,),
        )
        self.connection.commit()

    def delete_student(self, name_student):
        self.cursor.execute(
            "DELETE FROM general WHERE alumno = (?)",
            (name_student,),
        )
        self.connection.commit()

    def update_materia(self, name_materia, name_student):
        try:
            self.cursor.execute(
                "UPDATE general SET materia = ? WHERE alumno = ?",
                (
                    name_materia,
                    name_student,
                ),
            )
            if self.cursor.rowcount == 0:
                print(f"No rows updated. Student '{name_student}' not found.")
            else:
                print(f"rows affected: {self.cursor.rowcount} ")
                self.connection.commit()
                self.cursor.execute(
                    "SELECT * FROM general WHERE alumno = ?", (name_student,)
                )
                lista = self.cursor.fetchall()
                print(lista)
                return lista
        except sqlite3.Error as e:
            print(e)

    def update_calificacion(self, calificacion, name_student):
        self.cursor.execute(
            "UPDATE general SET calificacion = ? WHERE alumno = ?",
            (
                calificacion,
                name_student,
            ),
        )
        self.connection.commit()

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM general")
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = DataBase()
    db.create_table()
    # db.add_student("pepe")
    # db.delete_student("pepe")
    db.update_materia("ciencia", "pepe")
