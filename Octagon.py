import turtle

def makeaoctagon():
    for x in range(8):
        turtle.forward(70)
        turtle.left(45)

turtle.fillcolor("maroon")
turtle.begin_fill()
makeaoctagon()
turtle.end_fill()

turtle.up()
turtle.goto(200,0)


turtle.fillcolor("teal")
turtle.begin_fill()
makeaoctagon()
turtle.end_fill()


turtle.up()
turtle.goto(400,0)


turtle.fillcolor("yellow")
turtle.begin_fill()
makeaoctagon()
turtle.end_fill()


turtle.up()
turtle.goto(600,0)


turtle.fillcolor("purple")
turtle.begin_fill()
makeaoctagon()
turtle.end_fill()


turtle.exitonclick()
