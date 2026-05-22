from customtkinter import *
class agregarLibro(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("AGREGAR LIBRO")
        self.configure(fg_color= "#d9dbff")

        
        self.geometry("1000x700")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=1)
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=30)
        self.grid_rowconfigure(2, weight=1)


        self.ventna_anterior()
        self.tabla1()
       
    def ventna_anterior(self):

        self.linea1 = CTkFrame(self,
                               height= 2,
                               fg_color= "#696dc2")
        self.linea1.grid(row=0, columnspan= 3, column=0, padx=0, pady=(50,0), sticky= "we")
        
        self.devolver = CTkButton(self,
                                    text="Atrás",
                                    fg_color= "#1a1c43",
                                    height= 40,
                                    corner_radius= 5,
                                    command=self.button_callbck)
        self.devolver.grid(row=0, column=0, padx=30, pady=0, sticky= "w")

    def tabla1(self):
        self.cuadro1 = CTkFrame(self,
                                   fg_color= "#bec1f6",
                                   border_color= "#696dc2",
                                   border_width= 1,
                                   corner_radius= 5)
        self.cuadro1.grid(row=1, column=0, columnspan= 2, padx=(100,0), pady=0, sticky= "nsew")

        self.cuadro1.grid_columnconfigure(0, weight=4)
        self.cuadro1.grid_columnconfigure(1, weight=3)
        self.cuadro1.grid_columnconfigure(2, weight=2)        
        self.cuadro1.grid_columnconfigure(3, weight=2)  

        self.cuadro1.grid_rowconfigure(0, weight=1)
        self.cuadro1.grid_rowconfigure(1, weight=6)
        self.cuadro1.grid_rowconfigure(2, weight=2)

        titulo_cuadro1 = "AGREGAR LIBRO"
        self.titulo = CTkLabel(self.cuadro1,
                                        text= titulo_cuadro1,
                                        text_color="black",
                                        font=("Calibri Light", 30, "bold"),
                                        fg_color="transparent")
        self.titulo.grid(row=0, column=0, padx=30, pady=0, sticky="w")

        self.label_subtitulo = CTkLabel(self.cuadro1,
                                        text="Ingresa el enlace del libro",
                                        text_color="#454ccd",
                                        font=("Calibri Light", 15, "bold"),
                                        fg_color="transparent")
        self.label_subtitulo.grid(row=0, column=0, padx=30, pady=(80, 0), sticky="w")





    def button_callbck(self):
        print("button clicked")
