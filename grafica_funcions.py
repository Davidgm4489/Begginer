import turtle


t = turtle.Turtle()
s = turtle.Screen()

finestra_mida = 800
tick_mida = 5
eix_mida = int(0.95 * finestra_mida / 2)
tick_sep = int(eix_mida / 10)
eix_mida = int(tick_sep * 10)
s.setup(finestra_mida, finestra_mida)


def tp(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def dibuixar_eix(max_x, max_y):
    """
    Funció per a dibuixar els eixos X,Y
    """
    turtle.tracer(0)
    t.pensize(3)
    eix_x = int(0.95 * max_x / 2)
    eix_y = int(0.95 * max_y / 2)
    tick_x = int(eix_x / 10)
    tick_y = int(eix_y / 10)
    eix_x = tick_x * 10
    eix_y = tick_y * 10

    # dibuixa el eix de les x
    t.teleport(-eix_x, 0)
    t.setheading(0)
    t.forward(2 * eix_x)

    # dibuixa el eix de les y
    t.teleport(0, -eix_y)
    t.setheading(90)
    t.forward(2 * eix_y)

    # dibuixa els ticks del eix x    
    t.setheading(-90)
    for x in range(-eix_x, eix_x+tick_x, tick_x):
        t.teleport(x, tick_mida)
        t.forward(2 * tick_mida)

    # dibuixa els ticks del eix y    
    t.setheading(0)
    for y in range(-eix_y, eix_y+tick_y, tick_y):
        t.teleport(-tick_mida, y)
        t.forward(2 * tick_mida)
    t.teleport(0, 0)
    t.setheading(0)
    turtle.update()
    t.pensize(1)

def quadricula(separacio):

    # dibuixa linies de les x
    t.setheading(0)
    for y in range(-eix_mida, eix_mida + 1, separacio):
        tp(-eix_mida, y)
        t.forward(2 * eix_mida)

    # dibuixa linies de les y
    t.setheading(-90)
    for x in range(-eix_mida, eix_mida + 1, separacio):
        tp(x, -eix_mida)
        t.forward(-2 * eix_mida)

def fun_lin(m=1, n=0):
    turtle.tracer(0)
    t.pensize(2)

    # ajustant a l'escala
    n = n * int(0.95 * finestra_mida / 20)
    t.teleport(-finestra_mida / 2, (m * (-finestra_mida) + n) / 2)

    # bucle que fara la recta
    for x in range(int(-finestra_mida / 2), int(finestra_mida / 2)):
        y = m * x + n
        t.goto(x, y)
    t.teleport(0, 0)
    t.pensize(1)
    turtle.update()

def fun_para(a=1, b=0, c=0):
    turtle.tracer(0)
    t.pensize(2)   
    # ajustant a l'escala
    a = a / int(0.95 * finestra_mida / 20)
    c = c * int(0.95 * finestra_mida / 20)

    t.teleport(-finestra_mida / 2, (a * (-finestra_mida) ** 2 + b * (-finestra_mida) + c) / 2)
    
    # bucle que dibuixara la paràbola
    for x in range(int(-finestra_mida / 2), int(finestra_mida / 2)):
        y = a * x ** 2 + b * x + c
        if y < finestra_mida:
            t.goto(x, y)
    t.teleport(0, 0)
    t.pensize(1)
    turtle.update()


dibuixar_eix(finestra_mida, finestra_mida)
quadricula(tick_sep)
fun_para()
fun_lin()

turtle.exitonclick()
