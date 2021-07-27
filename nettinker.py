# import turtle
# colors=['red','purple','blue','green','orange','yellow','skyblue','pink','white','black']
# t=turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%8])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)

import turtle
loadwindow=turtle.Screen()
turtle .speed(2)

for i in range(100):
    turtle .circle(5*i)
    turtle .circle (-5*i)
    turtle.left(i)
turtle .exitonclick()

