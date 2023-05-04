import turtle

#Boton para ir al programa
def boton(x, y, width, height, text, cuadro):
    cuadro.goto(x, y)
    cuadro.pendown()
    cuadro.fillcolor("#253874")
    cuadro.begin_fill()
    for i in range(2):
        cuadro.forward(width)
        cuadro.left(90)
        cuadro.forward(height)
        cuadro.left(90)
    cuadro.end_fill()
    cuadro.penup(), cuadro.color('white')
    cuadro.goto(-20, -115)
    cuadro.write(text, align="center", font=("Arial", 20, "bold"))

def boton_click(x, y):
    # función que se ejecuta cuando se hace clic en el botón
    print("Botón clickeado!")

#Boton para mas informacion 'flecha'
def boton_flecha_info(cuadro):
    cuadro.forward(100), cuadro.right(90), cuadro.forward(0), cuadro.right(180)
    cuadro.pendown()
    cuadro.begin_fill()
    cuadro.color('#253874')
    cuadro.circle(25)
    cuadro.end_fill()
    #Flecha
    cuadro.left(90), cuadro.penup(), cuadro.color('white'), cuadro.forward(40), cuadro.right(180),cuadro.pendown(), cuadro.forward(25)
