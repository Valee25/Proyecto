from datetime import datetime, timedelta

class Usuario:

    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre        
        self.correo = correo        
        self.telefono = telefono  
          
class Prestamo:

    def __init__(self, usuario):

        self.usuario = usuario
        self.fecha_prestamo = datetime.now()                     # fecha de hoy automatica
        self.fecha_devolucion = datetime.now() + timedelta(days=15)  # 15 dias despues
