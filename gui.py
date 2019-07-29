from tkinter import *
from os import system

def get_values():
    print('get_values activated')
    global a,b,c,d,du,dv, graph_type
    a = w4.get()
    b = w3.get()
    c = w2.get()
    d = w1.get()

    du = w6.get()
    dv = w5.get()

    graph_type = variable.get()

    print(a, b, c, d, du, dv, graph_type)
    return a, b, c, d, du, dv, graph_type

### New Image ###
def load_image(a,b,c,d,du,dv, graph_type):
    global img, i, label
    print('load_image called')

    system('rm image.png')
    system('python eigens.py --a '+ str(a) + ' --b ' + str(b)
                  + ' --c ' + str(c) + ' --d ' + str(d)
                  + ' --du ' + str(du) + ' --dv ' + str(dv) + ' --graph_type ' + graph_type)

    img = PhotoImage(file="image.png")
    i = canvas.create_image(20,20, anchor=NW, image=img)
    print('python eigens.py --a '+ str(a) + ' --b ' + str(b)
                  + ' --c ' + str(c) + ' --d ' + str(d)
                  + ' --du ' + str(du) + ' --dv ' + str(dv) + ' --graph_type ' + graph_type)
    label = Label(image=img)
    label.image = img # keep a reference!
    label.pack()
    canvas.update_idletasks()
    label.update()
    canvas.update()


### Canvas & Image ###
root = Tk()
canvas = Canvas(root, width = 750, height = 600)

t=0
def callback():
    global t
    if t > 0:
        label.pack_forget()

    t +=1
    get_values()
    load_image(a,b,c,d,du,dv, graph_type)


butt = Button(root, text="OK", command=callback, width = 16, height = 4)
butt.pack(side = BOTTOM)

### Jacobian ###
w1 = Scale(root, from_=2, to=-2, resolution = 0.1, label = 'd')
w1.pack(side = RIGHT)
w2 = Scale(root, from_=2, to=-2, resolution = 0.1, label = 'c')
w2.pack(side = RIGHT)
w3 = Scale(root, from_=2, to=-2, resolution = 0.1, label = 'b')
w3.pack(side = RIGHT)
w4 = Scale(root, from_=2, to=-2, resolution = 0.1, label = 'a')
w4.pack(side = RIGHT)

### Diffusivities ###
w5 = Scale(root, from_=1, to=0, resolution = 0.1, label = 'dv')
w5.pack(side = LEFT)

w6 = Scale(root, from_=1, to=0, resolution = 0.1, label = 'du')
w6.pack(side = LEFT)

### Graph ###
variable = StringVar(root)
variable.set("ring") # default value

w7 = OptionMenu(root, variable, "ring", "random")
w7.pack(side = BOTTOM)

T1 = Text(root, height=2, width=13)
T1.pack(side = LEFT)
T1.insert(1.0, "DIFFUSIVITIES")

T2 = Text(root, height=2, width=10)
T2.pack(side = RIGHT)
T2.insert(1.0, "JACOBIAN \nENTRIES")

mainloop()
