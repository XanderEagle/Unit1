# by Xander Eagle
# September 17, 2019
# this draws 4 octagons in different colors without touching
import turtle


# this loop makes the octagon and adds the color
def makeaoctagon(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(70)
        turtle.left(45)
    turtle.end_fill()


# this tells the turtle where to make the next octagon
def goto(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


# this says the specific color along with activating the octagon creation loop
makeaoctagon("maroon")

# this says the specific coordinates for the next octagon
goto(200, 0)

makeaoctagon("teal")
goto(200, 200)
makeaoctagon("yellow")
goto(0, 200)
makeaoctagon("purple")
turtle.exitonclick()