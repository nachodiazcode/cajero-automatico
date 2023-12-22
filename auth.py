class AuthManager:
    def __init__(self):
        self.usuarios = {}  # Almacena los usuarios registrados: {username: password}
        
    def mostrar_usuarios_registrados(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print("-", usuario)

    def registrarse(self):
        print("Registrarse")
        nuevo_usuario = input("Ingrese un nombre de usuario: ")
        nueva_contraseña = input("Ingrese una contraseña: ")

        if nuevo_usuario in self.usuarios:
            print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        else:
            self.usuarios[nuevo_usuario] = nueva_contraseña
            print("Usuario registrado correctamente.")

    def iniciarSesion(self):
        print("Iniciar Sesión")
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        if username in self.usuarios and self.usuarios[username] == password:
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return False