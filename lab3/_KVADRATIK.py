from graph import *
brushColor("blue")
rectangle(0,0,400,400)
penColor("yellow")
brushColor("yellow")
x=180; y=180
obj=rectangle(x,y,x+20,y+20)
dx=0;dy=0
def keyPressed(event):
    global dx, dy
    if event.keycode == VK_LEFT:
        dx=-1; dy=0
    elif event.keycode == VK_RIGHT:
        dx=1; dy=0
    elif event.keycode == VK_UP:
        dx=0; dy=-1
    elif event.keycode == VK_DOWN:
        dx=0; dy=1
    elif event.keycode == VK_ESCAPE:
        close()
    elif event.keycode == VK_SPACE:
        dx=0; dy=0
    elif event.keycode == 188:
        dx=-1; dy=1
    elif event.keycode == 190:
        dx=1; dy=-1
    elif event.keycode == 75:
        dx=-1; dy=-1
    elif event.keycode == 76:
        dx=1; dy=1
def update():
    global dx, dy

    if xCoord(obj)<=0 or xCoord(obj)>=379:
        dx=0
    if yCoord(obj)<=0 or yCoord(obj)>=379:
        dy=0
    else: moveObjectBy(obj,dx,dy)
onKey(keyPressed)
onTimer(update,50)
run()
