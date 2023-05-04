import tkinter as tk
from tkinter import filedialog
# from tkmacosx import Button
from PIL import Image, ImageTk
from funciones_programa import *

def ventana_informacion():
    ventana_info = tk.Toplevel()
    ventana_info.title('Informacion sobre datos oscuros') 
    ventana_info.geometry('900x600+300+100')
    ventana_info.config(bg='#253874')
    #Frame
    info_frame= tk.Frame(ventana_info, width=400, height=600, bg='#253874')
    info_frame.place(x= 500, y=0)
    info_frame.grid_propagate(0)
    #Titulo
    titulo2 = tk.Label(ventana_info, text='NO A LA HUELLA DE \nCARBONO DIGITAL', bg= '#253874', fg= 'white', font=('Arial', 30))
    titulo2.place(x= 40, y= 50)
    # #Informacion
    titulo2_1 = tk.Label(info_frame, text='Impacto medioambiental', bg= '#253874', fg= 'white', font=('Arial', 18))
    titulo2_1.grid(row=0, column=0, sticky='w', padx=0, pady=20)

    parrafo1= tk.Label(info_frame, text='Cada año son responsables de la emisión de millones \nde CO₂ a la atmósfera, pues estos datos que no son \nutilizados solo consumen energía.', bg= '#253874', fg= 'white', font=('Arial', 11))
    parrafo1.grid(row=1, column=0, sticky='w', padx=0, pady=10)

    titulo2_2 = tk.Label(info_frame, text='Consumo de energia', bg= '#253874', fg= 'white', font=('Arial', 18))
    titulo2_2.grid(row=2, column=0, sticky='w', padx=0, pady=20)

    parrafo2= tk.Label(info_frame, text='Estos ocupan espacio en servidores gigantescos, \npor lo que consumen mucha electricidad; por lo que,\naparte de tener costos de mantenimiento de \nalmacenes, también existe un costo para el medio \nambiente.', bg= '#253874', fg= 'white', font=('Arial', 11))
    parrafo2.grid(row=3, column=0, sticky='w', padx=0, pady=10)

    titulo2_3 = tk.Label(info_frame, text='Toma de decisiones', bg= '#253874', fg= 'white', font=('Arial', 18))
    titulo2_3.grid(row=4, column=0, sticky='w', padx=0, pady=20)

    parrafo3= tk.Label(info_frame, text='Reducir los datos oscuros puede ayudar a los \nconsumidores y los reguladores a tomar decisiones \nmás informadas sobre sus elecciones de consumo y \nsobre la regulación de las prácticas empresariales.', bg= '#253874', fg= 'white', font=('Arial', 11))
    parrafo3.grid(row=5, column=0, sticky='w', padx=0, pady=10)
    #Imagen
    imagen_mundo = Image.open('mundito.png')
    imagen_mundo = imagen_mundo.resize((490,490), Image.ANTIALIAS)
    foto_mundo = ImageTk.PhotoImage(imagen_mundo)
    label_imagen = tk.Label(ventana_info, image=foto_mundo, borderwidth=0)
    label_imagen.Image = foto_mundo
    #Posicion
    label_imagen.place(x=0, y=200)
    #Boton regreso
    boton_regreso = tk.Button(ventana_info, text="Regresar", command= lambda: ventana_info.destroy() ,bg= 'gray')
    boton_regreso.place(x=800, y=550)

def ventana_inicio_ruta():
    global entrada_ruta, ventana_ruta
    ventana_ruta = tk.Toplevel()
    ventana_ruta.title('Eliminacion y comprension de archivos') 
    ventana_ruta.geometry('850x500+300+100')
    ventana_ruta.config(bg='#143E76')
    label_instruccion= tk.Label(ventana_ruta, text="*Coloca la ruta de las carpetas a examinar\nPor ejemplo la ruta de Documentos: C:/Usuarios/[Nombre de usuario]/Documentos",  bg= '#143E76', fg= 'white', font=('Arial', 15))
    label_instruccion.place(x=20, y=20)
    label_ruta= tk.Label(ventana_ruta, text="Ingrese la ruta:",  bg= '#143E76', fg= 'white', font=('Arial', 32, 'bold'))
    label_ruta.place(x=50, y=150)
    #Textbox para ingresar la ruta
    entrada_ruta= tk.Entry(ventana_ruta, width=50)
    entrada_ruta.place(x=370, y=170)
    # Boton ingresar la ruta
    boton_ingreso= tk.Button(ventana_ruta, text="Ingresar",  bg= 'gray', command = funcion_ingreso_ruta)
    boton_ingreso.place(x=690, y=170)
    #Boton de regreso
    boton_regreso= tk.Button(ventana_ruta, text="Regresar", command=lambda: ventana_ruta.destroy(), bg= 'gray')
    boton_regreso.place(x=30, y=420)

def funcion_ingreso_ruta():
    global entrada_ruta, ventana_ruta, label_archivo, label_pregunta, boton_comprimir, boton_eliminar
    ruta = entrada_ruta.get()
    # ruta = filedialog.askdirectory()
    lista_ordenada, neww_path, flag = cosa(ruta)
    label_pregunta = tk.Label(ventana_ruta); label_pregunta.place(x=600, y=250)
    if flag:
        label_pregunta["text"] = "¿Desea comprimir o eliminar?"
        label_archivo = tk.Label(ventana_ruta); label_archivo.place(x = 50, y=300)
        label_nombre_archivo= tk.Label(ventana_ruta, text="Nombre del archivo:", bg= '#143E76', fg= 'white', font=('Arial', 18, 'bold'))
        label_nombre_archivo.place(x=50, y=250)
        boton_comprimir = tk.Button(ventana_ruta)
        boton_eliminar = tk.Button(ventana_ruta)
        i = 0
        funcion_botones_poner(i, lista_ordenada, neww_path)
    else:
        label_pregunta["text"] = "Carpeta vacia, o sin archvos viejos"


def funcion_botones_poner(i, lista_ordenada, neww_path):
    global label_archivo, label_pregunta,  boton_comprimir, boton_eliminar
    if i <= len(lista_ordenada)-1:
        archivo = list(lista_ordenada[i].keys())[0]
        fecha = list(lista_ordenada[i].values())[0]
        label_archivo['text'] = f"{i+1}. {archivo} ({fecha})"
        boton_comprimir.configure(text= "Comprimir" , command=lambda: comprimir_archivo(i, lista_ordenada, neww_path))
        boton_comprimir.place(x = 650, y = 300)
        boton_eliminar.configure(text= "Eliminar", command=lambda: eliminar_archivo(i, lista_ordenada, neww_path))
        boton_eliminar.place(x = 730, y = 300)
    else:
        label_archivo['text'] = ""
        label_pregunta['text'] = "Optimizacion finalizada"
        boton_comprimir.place_forget()
        boton_eliminar.place_forget()
        

def cosa2(i, lista_ordenada, neww_path):
    global ventana_comprimir
    comprimir(lista_ordenada, neww_path, i)
    funcion_botones_poner(i+1, lista_ordenada, neww_path)
    ventana_comprimir.destroy()

def cosa1(i, lista_ordenada, neww_path):
    global ventana_borrar
    eliminar(lista_ordenada, neww_path, i)
    funcion_botones_poner(i+1, lista_ordenada, neww_path)
    ventana_borrar.destroy()

def comprimir_archivo(i, lista_ordenada, neww_path):
    global ventana_comprimir
    ventana_comprimir= tk.Toplevel()
    ventana_comprimir.title('Comprimir de archivos') 
    ventana_comprimir.geometry('400x200+500+300')
    ventana_comprimir.config(bg='#A6A6A6')
    #Nombre del archivo
    nombre_archivo= tk.Label(ventana_comprimir, text='Nombre archivo', bg= '#A6A6A6', fg= 'black', font=('Arial', 20))
    nombre_archivo.grid(row=0, column=1, pady=20)
    #Imagen icono advertencia
    imagen_advertencia = Image.open('adver.png')
    imagen_advertencia = imagen_advertencia.resize((100,100), Image.ANTIALIAS)
    icono= ImageTk.PhotoImage(imagen_advertencia)
    label_icono=tk.Label(ventana_comprimir, image=icono, borderwidth=0)
    label_icono.Image = icono
    label_icono.grid(row=2, column=0)
    #Preguntar si desea borrar y crear botones
    pregunta= tk.Label(ventana_comprimir, text='¿Desea Comprimir el archivo?', bg= '#A6A6A6', fg= 'black', font=('Arial', 15))
    pregunta.grid(row=1, column=1)
    boton_si= tk.Button(ventana_comprimir, text='Si', command=lambda: cosa2(i, lista_ordenada, neww_path), bg="#0097B2", fg="black", font=("Arial", 16), ) 
    boton_si.grid(row=2, column=1, pady=10)
    boton_no= tk.Button(ventana_comprimir, text='No', command=lambda: ventana_comprimir.destroy(), bg="#0097B2", fg="black", font=("Arial", 16), ) 
    boton_no.grid(row=2, column=2, pady=10)

def eliminar_archivo(i, lista_ordenada, neww_path):
    global ventana_borrar
    ventana_borrar= tk.Toplevel()
    ventana_borrar.title('Eliminacion de archivos') 
    ventana_borrar.geometry('400x200+500+300')
    ventana_borrar.config(bg='#A6A6A6')
    #Nombre del archivo
    nombre_archivo= tk.Label(ventana_borrar, text='Nombre archivo', bg= '#A6A6A6', fg= 'black', font=('Arial', 20))
    nombre_archivo.grid(row=0, column=1, pady=20)
    #Imagen icono advertencia
    imagen_advertencia = Image.open('adver.png')
    imagen_advertencia = imagen_advertencia.resize((100,100), Image.ANTIALIAS)
    icono= ImageTk.PhotoImage(imagen_advertencia)
    label_icono=tk.Label(ventana_borrar, image=icono, borderwidth=0)
    label_icono.Image = icono
    label_icono.grid(row=2, column=0)
    #Preguntar si desea borrar y crear botones
    pregunta= tk.Label(ventana_borrar, text='¿Desea borrar el archivo?', bg= '#A6A6A6', fg= 'black', font=('Arial', 15))
    pregunta.grid(row=1, column=1)
    boton_si= tk.Button(ventana_borrar, text='Si', command=lambda: cosa1(i, lista_ordenada, neww_path), bg="#0097B2", fg="black", font=("Arial", 16), ) 
    boton_si.grid(row=2, column=1, pady=10)
    boton_no= tk.Button(ventana_borrar, text='No', command=lambda: ventana_borrar.destroy(), bg="#0097B2", fg="black", font=("Arial", 16), ) 
    boton_no.grid(row=2, column=2, pady=10)

#Ventana de inicio
ventana_inicio = tk.Tk()
ventana_inicio.title('Proyecto Datos Oscuros') 
ventana_inicio.geometry('850x600+300+100')
ventana_inicio.resizable(0,0)
imagen_fondo = tk.PhotoImage(file='fondo.png')
fondo = tk.Label(ventana_inicio, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)
fondo.lift()

# Creamos un canvas en la ventana
canvas = tk.Canvas(ventana_inicio, width=400, height=400)
canvas.place(relx=0.5, rely=0.5, anchor='center')

# Dibujar cuadro
canvas.create_rectangle(0, 0, 400,400, fill="white")

# Agregamos informacion en el canvas
titulo1= tk.Label(ventana_inicio, text='Practica eliminar\nlos datos oscuros', bg= 'white', fg= '#253874', font=('Arial', 28))
titulo1.place(x= 280, y = 120)
parrafo_1= tk.Label(ventana_inicio, text='Reducir los datos oscuros y \nasegurarse de que solo se \nalmacenen los datos necesarios \npuede contribuir a reducir el \nimpacto ambiental y las emisiones \nde gases de efecto invernadero .', bg= 'white', fg= '#253874', font=('Arial', 16))
parrafo_1.place(x= 270, y = 230)

#Boton para ir al programa
boton_programa= tk.Button(ventana_inicio, text='Ir al programa', command=ventana_inicio_ruta, bg="#253874", fg="white", font=("Arial", 16)) 
boton_programa.place(x= 350, y = 405) 
canvas.create_rectangle(100, 300, 300, 350, fill="#253874")

#Boton para mas informacion
boton_info=tk.Button(ventana_inicio, text='Mas info', command=ventana_informacion, bg="#253874", fg="white", font=("Arial", 16), ) 
boton_info.place(x= 370, y = 460)


# Ejecutamos el bucle principal de la aplicación
ventana_inicio.mainloop()

#D:\Descargas