import os

from core.input_helper import gen_input_to_list
from structures.guia import guia_questions
from structures.package import package_questions
from structures.user import user_questions
from structures.electronic_bill import electronic_bill_questions


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

users = []
packages = []
bills = []
guias = []

num_autoincremental = 0

while True:
    print(packages)
    print(guias)
    print("Bienvenido a la Mensajería Fidélitas\n")
    print("1. Ingresar un nuevo usuario")
    print("2. Ingresar un nuevo paquete")
    print("3. Ingresar una nueva factura")
    print("4. Salir\n")
   
    option = input()
   
    if option == "1":     
        clear_console()
        print('[CREACION DE USUARIO]')
        new_user = gen_input_to_list(user_questions)
        users.append(new_user)
        clear_console()
        print('[USUARIO CREADO]')

    elif option == "2":
        clear_console()
        print('[CREACION PAQUETE]')
        new_package = gen_input_to_list(package_questions)
        clear_console()
        print('[CREACION DE LA GUIA]')
        new_guia = gen_input_to_list(guia_questions)
        num_autoincremental += 1

        # Se le agrega la ID a la guia
        new_guia.append(num_autoincremental)

        # Se le agrega el estado al paquete
        new_package.append('CREADO')
        # Se le agrega la ID de la guia
        new_package.append(num_autoincremental)

        packages.append(new_package)
        guias.append(new_guia)
        clear_console()
        print('[PAQUETE CREADO]')

    elif option == "3":     
        clear_console()
        print('[CREACION DE FACTURA ELECTRONICA]')
        new_electronic_bill = gen_input_to_list(electronic_bill_questions)
        bills.append(new_electronic_bill)
        clear_console()
        print('[FACTURA ELECTRONICA CREADA]')
        
    elif option == '4':
        print('Saliendo...')
        break
    else:
        clear_console()
        print("Usted ha ingresado un número incorrecto")
    
    
    




   
