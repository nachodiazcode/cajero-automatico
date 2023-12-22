from auth import AuthManager
from model import CajeroAutomatico
from view import CajeroView

class CajeroController:
    def __init__(self):
        self.cajero = CajeroAutomatico()
        self.view = CajeroView()
        self.auth = AuthManager()

    def run(self):
        while True:
            self.view.show_menu()
            option = int(input("Ingrese una opción: "))
            if option == 0:
                self.auth.registrarse()
            elif option == 1:
                self.auth.iniciarSesion()
            elif option == 3:
                self.cajero.girarSaldo()
            elif option == 4:
                self.cajero.verSaldo()
            elif option == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no reconocida!")