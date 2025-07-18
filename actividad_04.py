key = True
class CollegeStudent:
    def __init__(self, name, age, course, avg_score):
        self.name = name
        self.age = age
        self.course = course
        self.avg_score = avg_score

students_compendium = {}
while key:
    menu_inpt = input("----------Bienvenido----------\n"
                      "\n1. Agregar estudiante"
                      "\n2.Mostrar lista de estudiantes"
                      "\n3. Calcular promedio general"
                      "\n4. Salir\n\nSeleccione una opción: ")
    match menu_inpt:
        case "1":
            try:
                temp_student_name = input("Coloque el nombre del estudiante: ")
                temp_student_avg_score = int(input("Coloque su promedio: "))
                students_compendium.update({temp_student_name:temp_student_avg_score})
            except ValueError:
                print("Eso no es un número.")
        case "2":
            print(students_compendium)
        case "3":
            cumulator = 0
            temp_score = 0
            for name, score in students_compendium:
                cumulator += 1
                temp_score += score
            print("")
        case "4":
            print("Gracias por usar el programa")
            key = False