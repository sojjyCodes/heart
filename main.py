import turtle

pen = turtle.Turtle()
pen.pensize(4)
pen.speed(1)
pen.color('black')
pen.begin_fill()
pen.fillcolor("red")
pen.lt(150)
pen.fd(180)
pen.circle(-90, 180)
pen.seth(60)
pen.circle(-90, 180)
pen.fd(180)
pen.end_fill()
pen.write("     I love coding")
pen.hideturtle()


turtle.mainloop()