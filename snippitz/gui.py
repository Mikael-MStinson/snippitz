from tkinter import *

root = Tk()
root.title('Node Mapper')
canvas = Canvas(root, bg='white', width = 1600,height = 900)

def place_circle(x,y, radius):
	coord = x-radius, y-radius, x+radius, y+radius
	canvas.create_oval(coord, outline="black", fill="white",width=2)
place_circle(300,500,100)

canvas.pack(expand = True, fill = BOTH)
root.mainloop()

