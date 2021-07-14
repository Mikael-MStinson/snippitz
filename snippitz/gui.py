from tkinter import *

root = Tk()
root.title('Node Mapper')
canvas = Canvas(root, bg='white', width = 1600,height = 900)

def place_circle(x,y, radius):
	coord = x-radius, y-radius, x+radius, y+radius
	canvas.create_oval(coord, outline="black", fill="white",width=2)
	canvas.pack(expand = True, fill = BOTH)
	
def click_event(event):
	place_circle(event.x, event.y, 100)

canvas.pack(expand = True, fill = BOTH)
root.bind("<Button>", click_event)
root.mainloop()

