import turtle
import math

t = turtle.Turtle()
s = turtle.Screen()
m = math
finestra_max = 800
s.setup(finestra_max, finestra_max)
punt_inicial = -300

def tp(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def trobar_costat_tri_rect(b, c, h=0):
    if h == 0:
        a = (b ** 2 + c ** 2) ** (1/2)
    else:
        a = (b ** 2 - c ** 2) ** (1/2)
    return(a)

def dibuixar_tri_rect(b, c, tamany=12):

    # ajusta la mida dels costats    
    if b > c:
        escala = 0.9 * (finestra_max / 2 / b ) + 300 / b
    else:
        escala = 0.9 * (finestra_max / 2 / c) + 300 / c
    a = trobar_costat_tri_rect(b, c, 0)    
    a = round(a, 2)
    b = round(float(b), 2)
    c = round(float(c), 2)

    # declaracio de variables
    t.speed(0)
    catet_1 = float(escala * b)
    hipotenusa = float(escala * a)
    catet_2 = float(escala * c)
    angle_x = m.degrees(m.atan(c/b))   
    angle_y = m.degrees(m.atan(b/c))
    angle_gir_x = 180 - angle_x
    angle_gir_y = 180 - angle_y

    # dibuixa el triangle
    tp(punt_inicial, punt_inicial)    
    t.forward(catet_1)
    t.left(angle_gir_x)
    t.forward(hipotenusa)
    t.left(angle_gir_y)
    t.forward(catet_2)
    t.setheading(0)

    # escriu nombres
    tp(catet_1 / 2 + punt_inicial, - tamany - 12 + punt_inicial)
    t.write(b, align="center", font=("Arial", tamany, "bold"))
    tp(catet_1 / 2 + 6 + punt_inicial, catet_2 / 2 + punt_inicial)
    t.write(a, align="center", font=("Arial", tamany, "bold"))
    tp(punt_inicial - 12, catet_2 / 2 + punt_inicial)
    t.write(c, align="center", font=("Arial", tamany, "bold"))
    
    # dibuixa els angles
    tp(catet_1 - 20 + punt_inicial, punt_inicial)
    t.setheading(-90)
    t.circle(20, -angle_x)
    tp(punt_inicial, catet_2 - 20 + punt_inicial)
    t.setheading(0)
    t.circle(20, angle_y)
    tp(20 + punt_inicial, punt_inicial)
    t.setheading(90)
    t.forward(20)
    t.setheading(180)
    t.forward(20)

    tp(0, 0)
    t.setheading(0)
    t.speed(1)

dibuixar_tri_rect(15, 8)

turtle.exitonclick()
