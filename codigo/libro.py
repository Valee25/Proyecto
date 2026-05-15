import re                           # importa lo que permite buscar patrones en texto (regex)
import requests

class Libro:                        # es el molde para crear objetos

    def __init__(self):             # esto se ejecuta automáticamente cada vez que se llama Libro()
        self.titulo = ""            # guarda el nombre del libro, empieza vacío porque aún no sabemos cuál es
        self.autor = ""             # guarda quién escribió el libro, empieza vacío
        self.idioma = ""            # guarda en qué idioma está el libro, empieza vacío
        self.fecha = ""             # guarda cuándo se publicó en Gutenberg, empieza vacío
        self.enlace = ""            # guarda el link de internet de donde vino el libro, empieza vacío
        self.ruta = ""              # guarda en qué carpeta del pc está guardado el .txt, empieza vacío
        self.estado = "Disponible"  # todos los libros nuevos llegan disponibles





from datetime import datetime, timedelta

class Prestamo:

    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre                        # nombre de quien hace el prestamo
        self.correo = correo                        # correo de quien hace el prestamo
        self.telefono = telefono                    # telefono de quien hace el prestamo
        self.fecha_prestamo = datetime.now()                     # fecha de hoy automatica
        self.fecha_devolucion = datetime.now() + timedelta(days=15)  # 15 dias despues



class Usuario:

    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre        # nombre de quien pide el libro
        self.correo = correo        # correo de contacto
        self.telefono = telefono    # numero de telefono



