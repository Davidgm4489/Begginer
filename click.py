import turtle
import random

contador = 0

r = random.Random()

wn = turtle.Screen()
wn.setup(600, 600)

c = turtle.Turtle()
c.pencolor("white")
c.speed(0)
c.ht()

msg = turtle.Turtle()
msg.ht()
msg.color("white")
msg.penup()

def click(x, y):
    if -150 < x < 150 and -150 < y < 150:
        contador += 1

def actualitzar_punts():
    msg.clear()
    msg.write(f"Punts: {contador}", align="center", font=("Arial", 18, "bold"))

wn.onscreenclick(click)

c.goto(-200, 200)
c.pendown()
for _ in range(4):
    c.forward(400)
    c.right(90)
c.penup()

c.fillcolor("yellow")
c.begin_fill()
c.circle(10)
c.end_fill()

while True:

