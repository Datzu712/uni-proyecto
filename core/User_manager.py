from .Input_helper import pedir_datos
from ..structures.User import User

class User_manager:
    
    def __init__(self):
        self.users = []
        
    def add_user(self, user):
        self.users.append(user)

    def registrar_usuario(self):
        new_user = pedir_datos(User)
        self.add_user(new_user)
        





