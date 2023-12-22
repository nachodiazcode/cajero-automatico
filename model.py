class CajeroAutomatico:
    def __init__(self):
        self.saldo = 0
            

    def depositarSaldo(self):
        print("Ingresar Saldo")
        monto = float(input("Ingrese monto a depositar: "))
        self.saldo += monto
        print(f"Se depositaron {monto} unidades. Saldo total: {self.saldo}")

    def girarSaldo(self):
        print("Girando saldo")
        monto = float(input("Ingrese monto a girar: "))
        self.saldo -= monto
        print(f"Se giraron {monto} unidades. Saldo total: {self.saldo}")

    def verSaldo(self):
        print(f"Saldo total: {self.saldo}")