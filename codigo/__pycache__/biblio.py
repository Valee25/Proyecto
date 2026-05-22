import json   # Guarda y carga datos en formato JSON (texto tipo diccionario)
import os     # Para trabajar con carpetas y archivos del sistema 
from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        # Agregar un libro nuevo a la lista
        self.libros.append(libro)

    def buscar_por_titulo(self, titulo):
        # Buscar por titulo sin importar mayusculas o minusculas
        resultados = []
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)
        return resultados
    
    def buscar_por_autor(self, autor):
        # Buscar por autor sin importar mayusculas o minusculas
        resultados = []
        for libro in self.libros:
            if autor.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados
    

    #### REVISIÓN

    def guardar(self, ruta="datos/libros.json"):
        # Crea la carpeta "datos" si no existe en el proyecto
        os.makedirs("datos", exist_ok=True)
        # Abre el archivo libros.json para escribir en él
        with open(ruta, "w", encoding="utf-8") as f:
            # Recorre cada libro, lo convierte a diccionario con to_dict() y los guarda todos juntos en el archivo
            json.dump([libro.to_dict() for libro in self.libros], f, ensure_ascii=False, indent=4)

    def cargar(self, ruta="datos/libros.json"):
        # Si el archivo no existe todavía, no hace nada
        if not os.path.exists(ruta):
            return
        # Abre el archivo y lee todos los libros guardados
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
        # Recorre cada diccionario y lo convierte de vuelta a objeto Libro con from_dict()
        self.libros = [Libro.from_dict(d) for d in datos]

    