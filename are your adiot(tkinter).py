from tkinter import *
from random import random
def move(event):
	x = xsize * random()
	y = ysize * random()

	master.geometry("%dx%d+%d+%d" % (w,h,x,y))


master = Tk()
xsize = master.winfo_screenwidth()
ysize = master.winfo_screenheight()
w = 200
h = 50

master.minsize(w,h)
master.title('let me check')

Label(master,text="Are you and idoit?").pack()

b = Button(master,text='No')
b.pack()
b.bind('<Enter>',move)

master.mainloop()