import turtle

turtle.Screen().bgcolor("cyan")

square = turtle.Turtle()
side_num = 4
side_len = 100
angle = 360 / side_num

square.fd(side_len)
square.rt(angle)

square.fd(side_len)
square.rt(angle)

square.fd(side_len)
square.rt(angle)

square.fd(side_len)
square.rt(angle)

turtle.done()