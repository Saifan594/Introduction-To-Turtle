import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Spiral Pattern")

mypen = turtle.Turtle()
size = 0

while True:
    
    for i in range(4):
        mypen.fd(size + 1)
        mypen.left(90)
        size -= 5
    
    size += 1