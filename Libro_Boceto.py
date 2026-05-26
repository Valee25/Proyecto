import math
import re

class Libro:
    def __init__(self, titulo, autor, idioma, release_date, enlace, ruta_local, estado="Disponible"):
        
        self.titulo = titulo     # self. Sí mismo
        self.autor = autor
        self.idioma = idioma
        self.release_date = release_date
        self.enlace = enlace
        self.ruta_local = ruta_local
        self.estado = estado     # Disponible o en Prestamo
        self._texto_cache = None     # Opcional
        
    def obtener_texto (self):     #Leer el contenido del libro en txt
        if self._texto_cache is not None:     # En caso de ser leido, retorna el archivo original
            return self._texto_cache
        if not self.ruta_local:     # Sí no, se retorna un string vacío
            return
        
        try:     # Manejo de excepciones
            with open (self.ruta_local, "r", encoding="uft-8") as f:
                self._texto_cache = f.read ()
        except FileNotFoundError:     # Sí el arechivo no existe se retorna vacío
            self._texto_cache = ""
        except UnicodeDecodeError:
            try:
                with open(self.ruta_local, "r", encoding="uft-8") as f:
                    self._texto_cache = f.read ()
            except Exception:
                self._texto_cache = ""
        return self._texto_cache
    
    def obtener_plbs (self):     # Función que nos ayudará con listas con palabras del texto
        texto = self.obtener_texto()
        if not texto:
            return []
        plbs = re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚüÜÑñ]+', texto)     # Buscamos todas las palabras que cumplan con esta secuencia
        return [p.lower() for p in plbs]     # Conversión del texto a minúsculas
    
    def contar_plbs (self):     # Total de palabras del Libro
        return len(self.obtener_plbs())
    
    def estimar_pags (self):     # Contador de páginas en base a /300
        total = self.contar_plbs()
        if total == 0:
            return 0
        return math.ceil(total/300)     # El math.ceil es para redondear la división hacia arriba
    
    def obtener_preview(self):     # Función para retornar las primeras  600 palabras del libro
        plbs = self.obtener_plbs()
        primeras_600 = plbs[:600]
        return " ".join(primeras_600)     # Unir todas en un string legible
    
    def plbs_mas_repetidas(self, cantidad=10):
        stopwords = {
    'a', 'al', 'algo', 'algunas', 'algunos', 'ante', 'antes', 'como', 'con', 'contra', 'cual', 'cuando', 'de', 'del', 'desde', 'donde', 'durante', 
    'el', 'ella', 'ellos', 'en', 'entre', 'es', 'esa', 'ese', 'eso', 'esta', 'estaba', 'estado', 'estoy', 'fue', 'ha', 'había', 'han', 
    'has', 'hasta', 'hay', 'la', 'las', 'le', 'les', 'lo', 'los', 'me', 'mi', 'mis', 'mucho', 'muy', 'más', 'nada', 'ni', 'no', 'nos', 
    'nuestro', 'o', 'para', 'pero', 'por', 'que', 'se', 'ser', 'si', 'sin', 'sobre', 'su', 'sus', 'también', 'te', 'tener', 'tengo', 
    'tu', 'un', 'una', 'y', 'ya', 'yo', 'él', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 
    'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 
    'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 
    'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 
    'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 
    'own', 's', 'same', 'she', 'should', 'so', 'some', 'such', 't', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 
    'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 
    'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves'
    }
        plbs = self.obtener_plbs()     # Llamamos a la función de obtener palabras
        if not plbs:
            return []
        
        frecuencia = {}     # Contador con las palabra más repetida
        for plb in plbs:
            if plb in stopwords:     # Sí esta en la lista de palabras más comunes, la salta
                continue
            if plb in frecuencia:     # Sí esta en el diccionario, se le suma 1 al contador
                frecuencia[plb] += 1
            else:     # Sí no existe, empieza el contador
                frecuencia[plb] = 1
                
        orden = sorted(frecuencia.items(), key=lambda par: par[1], reverse=True)     # lambda nos da el top
        return orden[:cantidad]
    
    def buscar_plb(self, plb_buscar):     # Cuántas veces apareece una palabra en el libro
        if not plb_buscar:
            return 0
        
        plbs = self.obtener_plbs()
        busqueda = plb_buscar.lower().strip()     # Conversión a minúsculas
        contador = 0
        for plb in plbs:     # Aplicamos un for para contar palabras
            if plb == busqueda:
                contador += 1
        return contador
    
    def cambiar_est(self, nuevo_estado):     # Función para cambiar el estado del libro
        if nuevo_estado not in ("Disponible", "Prestado"):     # Validar que el libro está en la biblioteca
            raise ValueError(f"ERROR: {nuevo_estado}")     # Raise para lanzar excepciones
        self.estado = nuevo_estado     # En caso de estarlo, se le atrivuye su estado
        
    def conver_dicc(self):     # Convierte el libro a un diccionario de Python
        return {
            "Título": self.titulo,
            "Autor": self.autor,
            "Idioma": self.idioma,
            "release_date": self.release_date,
            "Ruta_local": self.ruta_local,
            "Estado": self.estado,
            }
