from ..structures.Paquetes import Paquetes
from .Input_helper import pedir_datos

class paquetes_manager:
    def __init__(self) -> None:
        self.paquetes = []
    def add_paquete(self,paquete):
        self.paquetes.append(paquete)    
    def registrar_paquete(self):
        new_paquete = pedir_datos(Paquetes)
        self.add_paquete(new_paquete)