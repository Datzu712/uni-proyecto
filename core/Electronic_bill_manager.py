from ..structures.Electronic_bill import Electronic_bill
from .Input_helper import pedir_datos

class electronic_bill_manager:
    def __init__(self) -> None:
        self.bill = []
    def add_bill(self,bill):
        self.bill.append(bill)    
    def registrar_bill(self):
        new_bill = pedir_datos(Electronic_bill)
        self.add_bill(new_bill)
