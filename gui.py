from tkinter import *
from os import system

def get_values():
    print('get_values activated')
    global a,b,c,d,du,dv
    a = w4.get()
    b = w3.get()
    c = w2.get()
    d = w1.get()

    du = w6.get()
    dv = w5.get()

    print(a, b, c, d, du, dv)
    return a, b, c, d, du, dv

### New Image ###
def load_image(a,b,c,d,du,dv):
    global img, i, label
    print('load_image called')

    system('rm image.png')
    system('python eigens.py --a '+ str(a) + ' --b ' + str(b)
                  + ' --c ' + str(c) + ' --d ' + str(d)
                  + ' --du ' + str(du) + ' --dv ' + str(dv))

    img = PhotoImage(file="image.png")
    i = canvas.create_image(20,20, anchor=NW, image=img)
    print('python eigens.py --a '+ str(a) + ' --b ' + str(b)
                  + ' --c ' + str(c) + ' --d ' + str(d)
                  + ' --du ' + str(du) + ' --dv ' + str(dv))
    label = Label(image=img)
    label.image = img # keep a reference!
    label.pack()
    canvas.update_idletasks()
    label.update()
    canvas.update()


### Canvas & Image ###
root = Tk()
canvas = Canvas(root, width = 700, height = 550)

t=0
def callback():
    global t
    if t > 0:
        label.pack_forget()

    t +=1
    get_values()
    load_image(a,b,c,d,du,dv)


butt = Button(root, text="OK", command=callback, width = 16, height = 4)
butt.pack(side = BOTTOM)

### Jacobian ###
w1 = Scale(root, from_=1, to=-1, resolution = 0.1, label = 'd')
w1.pack(side = RIGHT)
w2 = Scale(root, from_=1, to=-1, resolution = 0.1, label = 'c')
w2.pack(side = RIGHT)
w3 = Scale(root, from_=1, to=-1, resolution = 0.1, label = 'b')
w3.pack(side = RIGHT)
w4 = Scale(root, from_=1, to=-1, resolution = 0.1, label = 'a')
w4.pack(side = RIGHT)

### Diffusivities ###
w5 = Scale(root, from_=0.5, to=0, resolution = 0.1, label = 'dv')
w5.pack(side = LEFT)

w6 = Scale(root, from_=0.05, to=0, resolution = 0.01, label = 'du')
w6.pack(side = LEFT)

mainloop()
