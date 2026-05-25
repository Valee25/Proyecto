from datetime import datetime, timedelta
from biblio import Biblioteca
from usuario import Usuario

class Usuario:

    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre        
        self.correo = correo        
        self.telefono = telefono  
          
class Prestamo:

    def __init__(self, usuario, libro): #agregar biblio (mover de dispo a prestado y vicev)

        self.usuario = usuario
        self.libro = libro
        self.libro.estado = "Prestado"
        self.fecha_prestamo = datetime.now()                         # Fecha de hoy automática
        self.fecha_devolucion = datetime.now() + timedelta(days=15)  # 15 días después

    def devolucion(self, clave):
        if clave == "123p":
            print("Funcionó")
            self.libro.estado = "Disponible"
        else:
            print("No funcionó")


from libro import Libro

L1 = Libro('https://www.gutenberg.org/cache/epub/78625/pg78625.txt')
Us = Usuario("Alejandro", "alejandro@gmail.com", "123")
Pr1 = Prestamo(Us, L1)
print(L1.estado)  # Prestado
Pr1.devolucion("123p")
print(L1.estado)  # Disponible
