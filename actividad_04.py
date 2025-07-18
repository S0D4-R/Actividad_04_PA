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
                      "\n4. Salir")
    match menu_inpt:
        case "1":
            temp_student_name = input("Coloque el nombre del estudiante: ")
            temp_student_avg_score = input("Coloque su promedio: ")
            students_compendium.update({temp_student_name:temp_student_avg_score})
        case "2":
            print(students_compendium)
        case "3":
            pass
        case "4":
            print("Gracias por usar el programa")
            key = False