import turtle

life = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("blue")
life.color("green")
life.shape("turtle")

size = 20
life.penup()
z = int(input("ingrese la cantidad de pasos que dará su tortuga ", ))

for _ in range (z):
    life.stamp()
    life.forward(size)
    life.right(45)
    size = size + 3

life.pendown()

for _ in range (z):
    life.color("yellow")
    life.left(45)
    life.backward(size)
    size = size - 3

life.left(90)
life.forward(10)
life.right(90)

for _ in range (z):
    life.color("red")
    life.forward(size)
    life.right(45)
    size = size + 3

window.mainloop()

