from tkinter import *

root = Tk()
root.title('Node Mapper')
canvas = Canvas(root, bg='white', width = 1600,height = 900)

scale = 1.0

class Circle:
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		
circles = []

def update_canvas():
	canvas.delete("all")
	for circle in circles:
		coord = (circle.x-circle.radius)*scale, (circle.y-circle.radius)*scale, (circle.x+circle.radius)*scale, (circle.y+circle.radius)*scale
		canvas.create_oval(coord, outline="black", fill="white",width=2)
		canvas.pack(expand = True, fill = BOTH)

def place_circle(x,y, radius):
	circles.append(Circle(x,y, radius))
	update_canvas()
	
def click_event(event):
	place_circle(event.x, event.y, 100)

def scroll_event(event):
	global scale
	if event.delta > 0:
		scale += 0.01
	elif event.delta < 0:
		scale -= 0.01
	update_canvas()

canvas.pack(expand = True, fill = BOTH)
root.bind("<Button>", click_event)
root.bind("<MouseWheel>", scroll_event)
root.mainloop()

