from datetime import date, datetime
class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        extrato = f"{self.data_hora} | {self.tipo} | {self.valor} |"
        return extrato
    

