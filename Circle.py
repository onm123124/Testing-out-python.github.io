
# import turtle
import turtle
from processing_py import*
# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
 
# setup turtle pen
t= turtle.Pen()
 
# changes the speed of the turtle
t.speed(1000)
 
# changes the background color
turtle.bgcolor("black")
 
# make spiral_web
for x in range(200):
    t.pencolor(colors[x%6]) # setting color
    t.width(x/100 + 1) # setting width
    t.forward(x) # moving forward
    t.left(59) # moving left
 
turtle.done()
t.speed(100)
 
turtle.bgcolor("black") # changes the background color

Hi=False
bool(Hi=False) 
if(Hi==True):
    print("hi")
else:
    print("bye")
