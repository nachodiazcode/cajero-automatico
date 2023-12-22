from model import CajeroAutomatico
from view import CajeroView

class CajeroController:
    def __init__(self):
        self.cajero = CajeroAutomatico()
        self.view = CajeroView()

    def run(self):
        while True:
            self.view.show_menu()
            option = int(input("Ingrese una opción: "))
            if option == 1:
                self.cajero.depositarSaldo()
            elif option == 2:
                self.cajero.girarSaldo()
            elif option == 3:
                self.cajero.verSaldo()
            elif option == 4:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no reconocida!")