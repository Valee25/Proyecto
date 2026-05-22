import re                           # importa lo que permite buscar patrones en texto (regex)
import requests
import os
from Libro_Boceto import Libro as LibroFinal

class Libro:                        # es el molde para crear objetos

    def __init__(self, enlace):             # esto se ejecuta automáticamente cada vez que se llama Libro()

        self.enlace = enlace           # guarda el link de internet de donde vino el libro, empieza vacío
        self.estado = "Disponible"
        self.crear_libro()


    # Crear método libro

    def crear_libro(self):

        req = requests.get(self.enlace)   # Accede al link y descarga el libro

        '''print(req.status_code)
        print(req.text[:300])''' 

        texto = req.text                  # Req se refiere al libro, entonces extrae el texto del libro


        # Patrones de regex para metadatos básicos

        match_titulo = re.search(r'Title:\s+(.+\n.+)', texto)  

        if match_titulo:  
            str_titulo = match_titulo.group(1)     # normalizarlo sin el salto de linea o tabs:c
            self.titulo = " ".join(str_titulo.split())
            print("Título:", self.titulo)

        match_autor = re.search(r'Author:\s+(.+)', texto)                            

        if match_autor:
            str_autor = match_autor.group(1)    
            print("Autor:", str_autor) 
            self.autor = str_autor

        match_idioma = re.search(r'Language:\s+(.+)', texto)

        if match_idioma:
            str_idioma = match_idioma.group(1)
            print("Idioma:", str_idioma)
            self.idioma = str_idioma

        match_fecha = re.search(r'Release date:\s+(.+)', texto)      

        if match_fecha:
            str_fecha = match_fecha.group(1) 
            print("Publicación:", str_fecha)
            self.fecha = str_fecha

        match_enlace = re.search(r'Other information and formats:\s+(.+)', texto)

        if match_enlace:
            str_enlace = match_enlace.group(1)
            print("Enlace:", str_enlace)
            self.enlace = str_enlace


        # Verifica si el link es de un libro o no, si sí entonces aparece disponible 

        if match_titulo == None and match_autor == None and match_idioma == None and match_fecha == None and match_enlace == None:
            print("El libro no está disponible.")

        else:
            print("El libro está disponible!")
        
        nombre_libro = None  # Si el usuario no descarga, la ruta queda vacía

        # Preguntar si el usuario quiere descargar el libro
        while True: 
            print("¿Quieres descargar el libro? Escribe 1 continuar, 0 para salir.")           
            respuesta = int(input())
            
            if respuesta == 1:
                os.makedirs("libros", exist_ok=True)
                nombre_libro = "libros/" + self.titulo.replace(" ", "_") + ".txt"
                print(f"Descargando: {nombre_libro}")
                with open(nombre_libro, "w", encoding="utf-8") as f:
                    f.write(req.text)
                break

            elif respuesta == 0:
                print("De acuerdo!")
                break

            else: 
                print("Opción inválida, intenta de nuevo.")
                break

        
        libro_final = LibroFinal(
            titulo=self.titulo,
            autor=self.autor,
            idioma=self.idioma,
            release_date=self.fecha,
            enlace=self.enlace,
            ruta_local=nombre_libro
        )
        return libro_final
    
    
L1 = Libro('https://www.gutenberg.org/cache/epub/78625/pg78625.txt')
libro = L1.crear_libro()  # ← esto retorna el LibroFinal
print(libro.titulo)
print(libro.estado)