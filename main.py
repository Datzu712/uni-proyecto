# from core.input_helper import gen_inputs_to_dict
# from structures.user import User
# from structures.electronic_bill import ElectronicBill
# from structures.package import Package

# print("Bienvenido a la Mensajería Fidélitas\n")

# users = []
# packages = []
# bills = []

# while True:
#     print(users)
#     print(packages)
#     print(bills)
#     print("Si desea registrar una cuenta de usuario, ingrese - 1 -\n\nSi desea registrar los datos para una factura electrónica, ingrese - 2 -\n\nSi desea agregar los datos para crear su paquete, ingrese - 3 -\n")

#     option = int(input("Ingrese una opción: "))
#     if option == 1:
#         new_user = gen_inputs_to_dict(User)
#         users.append(new_user)
#     if option == 2:
#         new_bill = gen_inputs_to_dict(ElectronicBill)
#         bills.append(new_bill)
#     if option == 3:
#         new_package = gen_inputs_to_dict(Package)
#         packages.append(new_package)
#     else:
#         print("Usted ha ingresado un número incorrecto")
