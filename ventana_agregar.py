import customtkinter as ctk
from tkinter import messagebox # para mostrar alertas de erro o éxito
import requests   # para descargar el texto del libro desde internet 
import re  # para extraer los metadatos (título,autor,etc.)lo que esta haciendo mariana
import os  #os segun lo que entiendo lo vamos a utilizar para manejo de archivos

from libro import libro # pues aqui importamos en otro codigo de la clase libro que ya tenemos

class VentanaAgregar:
    """"
    Ventana emergente para agregar un libro nuevo pegando su enlace de Project Gutenberg.
    """
    def __init__(self, ventana_padre, biblioteca, callback_actualizar):
        """
        ventana_padre        : la ventana principal (para que esta se abra encima)
        biblioteca           : el objeto Biblioteca para agregar el libro al catálogo
        callback_actualizar  : función de la ventana principal que refresca la tabla
        """
        # Guardamos las referencias que necesitamos
        self.biblioteca = biblioteca
        self.callback_actualizar = callback_actualizar

        # Creamos la ventana secundaria con customtkinter
        self.ventana = ctk.CTkToplevel(ventana_padre)
        self.ventana.title("Agregar libro")
        self.ventana.geometry("520x280")
        self.ventana.resizable(False, False)

        #Bloqueo la ventan principal mientras esta esté abierta
        self.ventana.grab_set()
        self.contruir_interfaz()

        def contruir_interfaz(self):

            # Frame general con padding interno
            frame = ctk.CTkFrame(self.ventana,fg_color="blue") # Aqui ponemos el color de nuestra venta la cual puede ser de 3 maneras
            frame.pack(fill="both", expand=True, padx=20, pady=15) # segun lo que lei esto crea una margen

            ctk.CTkLabel(
                frame,
                text="Pega el enlace del libro de Project Gutenberg (.txt)",
                anchor="w"
            ).pack(fill="x", pady=(0,4))
