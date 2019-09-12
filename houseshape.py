import turtle
turtle.fillcolor("purple")
turtle.begin_fill()
for x in range(4):
    turtle.forward(200)
    turtle.right(90)
turtle.left(90)
turtle.end_fill()

turtle.fillcolor("aqua")
turtle.begin_fill()
turtle.right(45)
turtle.forward(140)
turtle.right(90)
turtle.forward(140)
turtle.end_fill()

turtle.exitonclick()




