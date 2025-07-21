name = input("Coloque su nombre: ")
y_o_b = int(input("Coloque su edad: "))
department = input("Coloque su departamento: ")
dpi = input("Coloque su número de DPI: ")

def name_check(name):
    name_x = name.list()
    counter = 0
    for letter in name_x:
        counter += 1
        if counter <= 5:
            return False
    return True

def age_check(yob):
    age_x = 2025 - yob
    if age_x <= 0 or age_x < 18:
        print("Usted no es apto para votar")
        return False
    else:
        print("Usted puede votar")