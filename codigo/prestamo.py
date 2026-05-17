from datetime import datetime, timedelta

class Prestamo:

    def __init__(self, usuario):

        self.usuario = usuario
        self.fecha_prestamo = datetime.now()                     # fecha de hoy automatica
        self.fecha_devolucion = datetime.now() + timedelta(days=15)  # 15 dias despues