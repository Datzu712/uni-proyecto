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

    print(users)
    print(packages)
    print(bills)
    print(guias)
    
    print("Bienvenido a la Mensajería Fidélitas\n")
    print("1. Ingresar un nuevo usuario")
    print("2. Ingresar un nuevo paquete")
    print("3. Cambiar estado de un paquete")
    print("4. Ingresar una nueva factura")
    print("5. Salir\n")
   
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
        print("El paquete se ha creado con el numero de guia: ", num_autoincremental)

    elif option == "3":
        
        if len(packages) == 0:
            print("No hay paquetes")
            continue
        try:
            numero_guia = int(input("Ingrese el numero de guía: "))
        except ValueError as error:
            print("Ingreso un numero invalido")
            continue  
        reference_package = None
        for package in packages:
            if numero_guia == package[6]:
                reference_package = package
        if package == None:
            print("No se ha encontrado el paquete indicado")
        else:
            package_status = input('Eliga un estado entre (Creado-Recolectado-Entrega Fallida-Entregado): ').upper().replace(' ','')
            print(package_status)
            if package_status not in ['CREADO','RECOLECTADO','ENTREGAFALLIDA','ENTREGADO']:
                print('Ha escrito una opción incorrecta')
                continue
            package[5] = package_status
            print('Estado cambiado con exito')
        

    elif option == "4":     
        clear_console()
        print('[CREACION DE FACTURA ELECTRONICA]')
        new_electronic_bill = gen_input_to_list(electronic_bill_questions)
        bills.append(new_electronic_bill)
        clear_console()
        print('[FACTURA ELECTRONICA CREADA]')
        
    elif option == '5':
        print('Saliendo...')
        break
    else:
        clear_console()
        print("Usted ha ingresado un número incorrecto")
    
    
    




   
