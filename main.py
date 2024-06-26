import os
import random
from core.input_helper import gen_input_to_list
from structures.guia import guia_questions
from structures.package import package_questions
from structures.user import user_questions
from structures.electronic_bill import electronic_bill_questions
from core.file_manager import load_file, save_data

# Contantes
USERS_FILE_PATH = './data/users.json'
PACKAGES_FILE_PATH = './data/packages.json'
BILLS_FILE_PATH = './data/bills.json'
GUIAS_FILE_PATH = './data/guias.json'
USERS_FILE_PATH = './data/users.json'

def clear_console():
    command = 'clear'
    if os.name == 'nt':
        command = 'cls'
    os.system(command)

def user_creation():
    users = load_file(USERS_FILE_PATH)
    encontrado = False
    exit = False
    while not encontrado:
        print('Seleccione una opcion antes de comenzar \n1.Iniciar sesión en su cuenta \n2.Registrar una nueva cuenta \n3.Salir')
        option = int(input())
        if option == 1:
            target_email = input('Porfavor Ingrese el correo electrónico asociado a su cuenta: ')
            for user in users:
                if target_email == user[0]:
                    print(f'Usuario seleccionado: {user[0]}')
                    password = input('Ingrese la contraseña de la cuenta: ')
                    print(user[5])
                    if password == user[5]:
                        print('Inicio de sesión exitoso')
                        app(user[6])
                        exit = True
            if exit == False:
                print('Usuario no encontrado o contraseña incorrecta')


        elif option == 2:
            clear_console()
            print('[CREACION DE USUARIO]')
            new_user = gen_input_to_list(user_questions)
            id = random.randint(100000, 999999)

            new_user.append(id)
            users.append(new_user)
            save_data(USERS_FILE_PATH, users)

            clear_console()
            print('[USUARIO CREADO]')

        elif option == 3:
            print('Saliendo...')
            encontrado = True
        else:
            clear_console()
            print("Usted ha ingresado un número incorrecto")
            
           

def app(user_id):
    packages = load_file(PACKAGES_FILE_PATH)
    bills = load_file(BILLS_FILE_PATH)
    guias = load_file(GUIAS_FILE_PATH)
    num_autoincremental = 0

    for guia in guias:
        if guia[5] > num_autoincremental:
            num_autoincremental = guia[5]

    clear_console()
    while True:
        print(packages)
        print(bills)
        print(guias)
    
        print("Bienvenido a la Mensajería Fidélitas\n")
        print("1. Ingresar un nuevo paquete")
        print("2. Cambiar estado de un paquete")
        print("3. Rastrear un paquete")
        print("4. Ingresar una nueva factura")
        print("5. Ver estadisticas de la cuenta")
        print("6. Salir\n")
    
        option = input()

        if option == "1":
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

            new_package.append(user_id)
            new_guia.append(user_id)

            packages.append(new_package)
            guias.append(new_guia)

            save_data(PACKAGES_FILE_PATH, packages)
            save_data(GUIAS_FILE_PATH, guias)
            clear_console()
            print('[PAQUETE CREADO]')
            print("El paquete se ha creado con el numero de guia: ", num_autoincremental)

        elif option == "2":
            packages = load_file(PACKAGES_FILE_PATH)
            
            if len(packages) == 0:
                print("No hay paquetes")
                continue
            try:
                numero_guia = int(input("Ingrese el numero de guía: "))
            except ValueError as error:
                clear_console()
                print("Ha ingresado un numero invalido")
                continue

            reference_package = None
            for package in packages:
                if numero_guia == package[6]:
                    reference_package = package
    
            if reference_package == None:
                print("No se ha encontrado el paquete indicado")
            else:
                package_status = input('Elija un estado entre (Creado-Recolectado-Entrega Fallida-Entregado): ').upper().replace(' ','')
                if package_status not in ['CREADO','RECOLECTADO','ENTREGAFALLIDA','ENTREGADO']:
                    print('Ha escrito una opción incorrecta')
                    continue
                reference_package[5] = package_status

                save_data(PACKAGES_FILE_PATH, packages)
                print('Estado cambiado con exito')

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

            if reference_package == None:
                print("No se ha encontrado el paquete indicado")
            else:
                print('El Estado de su paquete es', reference_package[5])    

        elif option == "4": 
            bills = load_file(BILLS_FILE_PATH)
            clear_console()
            print('[CREACION DE FACTURA ELECTRONICA]')
            new_electronic_bill = gen_input_to_list(electronic_bill_questions)
            new_electronic_bill.append(user_id)
            bills.append(new_electronic_bill)
            save_data(BILLS_FILE_PATH, bills)
            clear_console()
            print('[FACTURA ELECTRONICA CREADA]')
        
        elif option == "5":
            clear_console()
            print('[MODULO DE ESTADISTICAS]')
            salir = False
            while not salir:
                bills = load_file(BILLS_FILE_PATH)
                guias = load_file(GUIAS_FILE_PATH)
                packages = load_file(PACKAGES_FILE_PATH)
                print('Elija una de las siguientes opciones \n1.Mostrar total de envios realizados \n2.Lista de paquetes enviados \n3.Monto de cobro \n4.Cantidad de paquetes enviados por número de telefono \n5.Cantidad de envios por numero de cédula \n6. Salir del modulo de estadisticas')
                elegir = int(input())
                if elegir == 1:
                    paquete_suma = 0
                    for package in packages:
                        if package[7] == user_id:
                            paquete_suma+=1
                    clear_console()
                    print(f'El total de paquetes enviados es {paquete_suma}')

                elif elegir == 2:
                    user_packages = []
                    for package in packages:
                        if package[7] == user_id:
                            user_packages.append(package)
                    clear_console()
                    if len(user_packages) == 0:
                        print('No se encontraron paquetes enviados')
                        continue

                    print('Lista de paquetes enviados')
                    for package in user_packages:
                        print(package)

                elif elegir == 3:
                    numero_guia = int(input('Ingrese el numero de guia a consultar:'))
                    for guia in guias:
                        if numero_guia == guia[5]:
                            clear_console()
                            print(f'El monto de cobro de la guia {numero_guia} es: {guia[4]}')

                elif elegir == 4:
                    numero_telefono = input('Ingrese el numero telefonico, para consultar la cantidad de paquetes encontrados bajo ese numero bajo su cuenta: ')
                    suma_telefono = 0
                    for paquete in packages:
                        if paquete[7] == user_id and paquete[1] == numero_telefono:
                            suma_telefono+=1
                    clear_console()
                    print(f'El total de paquetes enviados con el numero de telefono {numero_telefono} es {suma_telefono}')

                elif elegir == 5:
                    numero_cedula = input('Ingrese el numero de cedula, para consultar la cantidad de paquetes encontrados bajo esa cedula bajo su cuenta: ')
                    suma_cedula = 0
                    for paquete in packages:
                        if paquete[7] == user_id and paquete[2] == numero_cedula:
                            suma_cedula+=1
                    clear_console()
                    print(f'El total de paquetes enviados con el numero de telefono {numero_cedula} es {suma_cedula}')  
            
                elif elegir == 6:
                    print('Saliendo del modulo de estadísticas')
                    salir = True 
                else: 
                    print('Porfavor seleccione una opción valida')
        elif option == '6':
            print('Saliendo...')
            break
        else:
            clear_console()
            print("Usted ha ingresado un número incorrecto")
try:
    user_creation()
except KeyboardInterrupt:
    print('Saliendo...')
except ValueError as error:
    print('Ha digitado un valor incorrecto, por favor intente de nuevo...')