class Libro:
  try
    def __init__(self, titulo, autor, idioma, fecha_publicacion, link, ruta_archivo):
        self.titulo             = titulo
        self.autor              = autor
        self.idioma             = idioma
        self.fecha_publicacion  = fecha_publicacion
        self.link               = link
        self.ruta_archivo       = ruta_archivo
        self.estado             = "Disponible"  

     def str(self):
        return f"{self.titulo} — {self.autor} [{self.estado}]"

    except
