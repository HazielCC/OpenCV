from rich import print

from ProjectDB.firstStept import DataBase


def get_options():
    print("Por favor, seleccione una opción:")

    options = input(
        """
        1. Crear tabla en Base de Datos
        2. Insertar Alumnos
        3. Mostrar Alumnos
        4. Actualizar Calificación
        5. Actualizar Materia
        6. Salir
        """.replace(
            "  ", ""
        )
    ).strip()

    option = int(options) if options.isdigit() else options

    if option not in [1, 2, 3, 4, 5, 6]:
        print("Por favor, seleccione una opción válida.")
        return get_options()

    return option


db = DataBase()
while True:
    user_option = get_options()

    if user_option == 1:
        print("Creando tabla en Base de Datos...")
        db.create_table()
    elif user_option == 2:
        print("Insertando Alumnos...")
        name_student = input("Por favor, ingrese el nombre del alumno: ")
        name_student = name_student.strip() if name_student.isalpha() else None
        if name_student is None:
            print("[red]El nombre del alumno no es válido.")
            continue
        db.add_student(name_student)
    elif user_option == 3:
        print("Mostrando Alumnos...")
        students = db.get_all_students()
        print(students)
    elif user_option == 4:
        print("Actualizando Calificación...")
        name_student = input("Por favor, ingrese el nombre del alumno: ")
        name_student = name_student.strip() if name_student.isalpha() else None
        if name_student is None:
            print("[red]El nombre del alumno no es válido.")
            continue

        calificacion = input("Por favor, ingrese la calificación del alumno: ")
        calificacion = calificacion.strip() if calificacion.isdigit() else None
        if calificacion is None:
            print("[red]La calificación no es válida.")
            continue
        db.update_calificacion(calificacion, name_student)

    elif user_option == 5:
        print("Actualizando Materia...")
        print("Actualizando Calificación...")
        name_student = input("Por favor, ingrese el nombre del alumno: ")
        name_student = name_student.strip() if name_student.isalpha() else None
        if name_student is None:
            print("[red]El nombre del alumno no es válido.")
            continue

        name_materia = input("Por favor, ingrese la calificación del alumno: ")
        name_materia = name_materia.strip() if name_materia.isdigit() else None
        if name_materia is None:
            print("[red]La calificación no es válida.")
            continue

        db.update_materia(name_materia, name_student)
    else:
        print("Saliendo del programa...")
        break
