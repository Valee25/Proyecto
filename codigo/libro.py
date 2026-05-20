import re                           # importa lo que permite buscar patrones en texto (regex)
import requests

class Libro:                        # es el molde para crear objetos

    def __init__(self, enlace):             # esto se ejecuta automáticamente cada vez que se llama Libro()

        self.enlace = enlace           # guarda el link de internet de donde vino el libro, empieza vacío
        self.crear_libro()



    # Crear método libro

    def crear_libro(self):

        req = requests.get(self.enlace)   # Accede al link y descarga el libro

        '''print(req.status_code)
        print(req.text[:300])''' 

        texto = req.text                  # Req se refiere al libro, entonces extrae el texto del libro


        # Patrones de regex para metadatos básicos

        match_titulo = re.search(r'Title:\s+(.+\n.+)', texto)  
        str_titulo = match_titulo.group(1)

        if match_titulo:  # :)
            print("Título:", str_titulo)    

        match_autor = re.search(r'Author:\s+(.+)', texto)        
        str_autor = match_autor.group(1)                        

        if match_autor:
            print("Autor:", str_autor) 

        match_idioma = re.search(r'Language:\s+(.+)', texto)
        str_idioma = match_idioma.group(1)

        if match_idioma:
            print("Idioma:", str_idioma)

        match_fecha = re.search(r'Release date:\s+(.+)', texto)  
        str_fecha = match_fecha.group(1)     

        if match_fecha:
            print("Publicación:", str_fecha)

        match_enlace = re.search(r'Other information and formats:\s+(.+)', texto)
        str_enlace = match_enlace.group(1)

        if match_enlace:
            print("Enlace:", str_enlace)


        # Verifica si el link es de un libro o no, si sí entonces aparece disponible 

        if match_titulo == None and match_autor == None and match_idioma == None and match_fecha == None and match_enlace == None:
            print("El libro no está disponible.")

        else:
            print("El libro está disponible!")
        

        # Preguntar si el usuario quiere descargar el libro

        while True: 
            print("¿Quieres descargar el libro? Escribe 1 continuar, 0 para salir.")           
            respuesta = int(input())
            if respuesta == 1:
                print("La descarga iniciará inmediatamente!")
                # Guarda el req
                with open("salida.txt", "w", encoding="utf-8") as f:
                    f.write(req.text)
                    break

            elif respuesta == 0:
                print("De acuerdo!")
                break

            else: 
                print("Opción inválida, intenta de nuevo.")
                break
    

        self.titulo = ""            # guarda el nombre del libro, empieza vacío porque aún no sabemos cuál es
        self.autor = ""             # guarda quién escribió el libro, empieza vacío
        self.idioma = ""            # guarda en qué idioma está el libro, empieza vacío
        self.fecha = ""             # guarda cuándo se publicó en Gutenberg, empieza vacío
        self.ruta = ""              # guarda en qué carpeta del pc está guardado el .txt, empieza vacío
        self.estado = "Disponible" 



L1 = Libro('https://www.gutenberg.org/cache/epub/78625/pg78625.txt') 
print(L1)
