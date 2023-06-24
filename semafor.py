import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(width=500,height=500,bg="white")
root.title("Semafór")
canvas.pack()

s = 5
timer = 57


def setup():
    canvas.create_rectangle(200,100,300,400,fill="black")
    canvas.create_rectangle(239,70,260,500,fill="black")
    canvas.create_polygon(180,100,250,80,320,100,fill="black")
    canvas.create_polygon(180,400,250,420,320,400,fill="black")


def light_setup():
    for i in range(0,200,85):
        print(i)
        canvas.create_oval(220,130+i,280,190+i,fill="dark grey")
        canvas.create_oval(220+s,130+i+s,280-s,190+i-s,fill="grey")


def time():
    global timer
    if timer != 0:
        timer -= 1
        canvas.delete('cas')
        #canvas.create_text(400,400,text=timer,tag="cas")
        canvas.after(1000,time)
        
    if timer <= 38 and timer > 0:
        changer_red()
        canvas.delete('yellow_colour')
        
    if timer > 40 and timer <= 57:
        changer_green()
        canvas.delete('yellow_colour')
        canvas.delete('red_colour')
        
    if timer <= 40 and timer > 38:
        changer_yellow()
        canvas.delete('red_colour')
        canvas.delete('green_colour')
        
    if timer < 60 and timer > 57:
        changer_yellow()
        canvas.delete('red_colour')
        
    elif timer == 0:
        timer = 60
        time()


def changer_red():
        canvas.create_oval(220,130,280,190,fill="dark red", tag="red_colour")
        canvas.create_oval(220+s,130+s,280-s,190-s,fill="red", tag="red_colour")


def changer_yellow():
        canvas.create_oval(220,215,280,275,fill="orange", tag="yellow_colour")
        canvas.create_oval(220+s,215+s,280-s,275-s,fill="yellow", tag="yellow_colour")


def changer_green():
        canvas.create_oval(220,300,280,360,fill="dark green", tag="green_colour")
        canvas.create_oval(220+s,300+s,280-s,360-s,fill="spring green", tag="green_colour")

setup()
light_setup()
time()
root.mainloop()
