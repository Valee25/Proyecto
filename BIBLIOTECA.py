from customtkinter import *
from agregarLibro import *
import info_libro
from libro_boceto import Libro

class App(CTk):
    def __init__(self):
        super().__init__()

        self.libros = []
        self.toplevel_window = None

        self.title("BIBLIOTECA")
        self.configure(fg_color= "#d9dbff")

        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.geometry(f"{self.screenwidth}x{self.screenheight}+0+0")

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=9)
        self.grid_columnconfigure(2, weight=2)
        

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=6)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=10)
        self.grid_rowconfigure(4, weight=4)

        #cositas
        Titulo= "BIBLIOTECA"
        subtitulo = "Explora el inventario de la biblioteca"
        self.label = CTkLabel(self, 
                              text= Titulo,
                              text_color= "black",
                              font= ("Calibri Light", 30, "bold"),
                              #anchor= nada
                              fg_color="transparent",)
        self.label.grid(row=0, column=0, padx=100, pady=0, sticky= "w")

        self.subtitulo = CTkLabel(self, 
                              text= subtitulo,
                              text_color= "#454ccd",
                              font= ("Calibri Light", 15, "bold"),
                              #anchor= nada
                              fg_color="transparent",)
        self.subtitulo.grid(row=0, column=0, padx=100, pady=(50,0), sticky= "w")


        self.button2 = CTkButton(self,
                                text="agregar libro",
                                fg_color= "#1a1c43",
                                height= 40,
                                corner_radius= 5,
                                command=self.button2_callbck)
        self.button2.grid(row=0, column=2, padx=(10,50), pady=(10,5), sticky= "w")

        self.entry = CTkEntry(self,
                            placeholder_text="Buscar libro",
                            width=700,
                            fg_color= "#ffffff",
                            border_color= "#1a1c43",
                            height= 30,
                            )
        self.entry.grid(row=0, column=0, padx=100, pady=(120,0), sticky= "w")

        self.button_buscar = CTkButton(self,
                                       text="Buscar",
                                       fg_color= "#1a1c43",
                                       height= 40,
                                       corner_radius= 5,
                                       command=self.button_callbck)
        self.button_buscar.grid(row=0, column=1, padx=20, pady=(120,0), sticky= "w")


        self.linea1 = CTkFrame(self,
                               height= 2,
                               fg_color= "#696dc2")
        self.linea1.grid(row=0, columnspan= 2, column=0, padx=(100,0), pady=(210,0), sticky= "we")
        self.tabla()

    
    def tabla(self):
        if hasattr(self, 'book_table'):
            self.book_table.destroy()

        self.book_table = CTkFrame(self,
                                   fg_color= "#bec1f6",
                                   border_color= "#696dc2",
                                   border_width= 1,
                                   corner_radius= 5)
        self.book_table.grid(row=1, column=0, columnspan= 2, padx=(100,0), pady=(0,0), sticky= "nswe")

        self.book_table.grid_columnconfigure(0, weight=4)
        self.book_table.grid_columnconfigure(1, weight=3)
        self.book_table.grid_columnconfigure(2, weight=2)        
        self.book_table.grid_columnconfigure(3, weight=2)  

        cabecera=["Título", "Autor", "Estado", "Más"]
        for x in range(4):
            self.descripcion = CTkLabel(self.book_table, 
                                text= cabecera[x],
                                text_color= "black",
                                font= ("Calibri Light", 20, "bold"),
                                #anchor= nada
                                fg_color="transparent",)
            self.descripcion.grid(row=0, column=x, padx=10, pady=5, sticky= "w")

        # supongamos que va a ser una lista
        def poblar_tabla(self, libros):
        
            for i, libro in enumerate(libros):
                fila = i + 1 

            self.titulo_libro = CTkLabel(self.book_table,
                                text=libro.titulo,
                                text_color="black",
                                font=("Calibri Light", 15),
                                #anchor= nada
                                fg_color="transparent")
            self.titulo_libro.grid(row=fila, column=0, padx=10, pady=5, sticky="w")
            
            self.autor_libro = CTkLabel(self.book_table,
                                text=libro.autor,
                                text_color="black",
                                font=("Calibri Light", 15),
                                #anchor= nada
                                fg_color="transparent")
            self.autor_libro.grid(row=fila, column=1, padx=10, pady=5, sticky="w")
            
            self.estado_libro = CTkLabel(self.book_table,
                                text=libro.estado,
                                text_color="black",
                                font=("Calibri Light", 15),
                                #anchor= nada
                                fg_color="transparent" if libro.estado == "Disponible" else "#00028a")
            self.estado_libro.grid(row=fila, column=2, padx=10, pady=5, sticky="w")

            texto_boton = "Más información"
            self.mas_info = CTkButton(self.book_table,
                                text= texto_boton,
                                text_color="black",
                                font=("Calibri Light", 15),
                                #anchor= nada
                                fg_color="transparent",
                                command= self.mas_info_callback)
            self.mas_info.grid(row=fila, column=3, padx=10, pady=5, sticky="w")



        
    

    def button_callbck(self):
        print("button clicked")
        
    def mas_info_callback(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = info_libro(self)
                
            self.toplevel_window.grab_set() 
            
        else:
            self.toplevel_window.lift()
            self.toplevel_window.focus_force()

    def button2_callbck(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = agregarLibro(self)   
               
            self.toplevel_window.grab_set() 
            
        else:
            self.toplevel_window.lift()
            self.toplevel_window.focus_force()
app = App()
app.mainloop()
