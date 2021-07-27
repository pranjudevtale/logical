import turtle
pen=turtle.Turtle()
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(133)
    curve()
    pen .left(120)
    curve() 
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color("black")
    pen.write("Love You",font=("z003",30,"bold"))             
heart()
# # pen.resizable("false","false","false","false","false","false","false")
txt()
pen.ht()

# import turtle
# loadwindow=turtle.Screen()
# turtle .speed(2)

# for i in range(100):
#     turtle .circle(5*i)
#     turtle .circle (-5*i)
#     turtle.left(i)
# turtle .exitonclick()



import turtle
pen=turtle.Turtle()
def curve():
    for i in range  (200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(133)
    curve()
    pen .left(120)
    curve()
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color("black")
    pen.write("pranju",font=("z003",30,"bold"))
heart()
pen.resizable("false","false","false","false" ,"false")
txt()
pen.ht()
