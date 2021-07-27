import tkinter as tkr
import time

tk=tkr.Tk()
canvas=tkr.canvas(tk,width=300,height=400)
canvas.grid()

ball=canvas.creat.oval(5,5,60,60, fill="red")
x=1
y=9
while True:
    canvas.move(ball,x,y)
    pos=canvas.coords(ball)
    if pos[3]>=400 or pos[1]<=0:
        y=-y
    if pos[2]>=300 or pos[0]<=0:
        x=-x
    tk.update()
    time.sieep(0.025)
    pass
tk.mainloop()