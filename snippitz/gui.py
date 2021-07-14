'''
when zooming in and out, the mouse is not used as an origin to zoom into

likewise, when placing a circle at a different scale, the mouse coordinates are not scaled
'''

from tkinter import *

root = Tk()
root.title('Node Mapper')
canvas = Canvas(root, bg='white', width = 1600,height = 900)

scale = 1.0
pan_x = 0
pan_y = 0
last_mouse_x = 0
last_mouse_y = 0

class Circle:
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		
circles = []

def update_canvas():
	canvas.delete("all")
	for circle in circles:
		coord = (circle.x-circle.radius)*scale+pan_x, (circle.y-circle.radius)*scale+pan_y, (circle.x+circle.radius)*scale+pan_x, (circle.y+circle.radius)*scale+pan_y
		canvas.create_oval(coord, outline="black", fill="white",width=2)
		canvas.pack(expand = True, fill = BOTH)

	
def click_event(event):
	global last_mouse_x
	global last_mouse_y
	last_mouse_x = event.x
	last_mouse_y = event.y
	circles.append(Circle(event.x*(1/scale)-pan_x*(1/scale), event.y*(1/scale)-pan_y*(1/scale), 100))
	update_canvas()

def scroll_event(event):
	global scale
	if event.delta > 0:
		scale += 0.01
	elif event.delta < 0:
		scale -= 0.01
	update_canvas()
	
def drag_event(event):
	global pan_x
	global pan_y
	global last_mouse_x
	global last_mouse_y
	pan_x += event.x - last_mouse_x
	pan_y += event.y - last_mouse_y
	last_mouse_x = event.x
	last_mouse_y = event.y
	update_canvas()

canvas.pack(expand = True, fill = BOTH)
root.bind("<Button>", click_event)
root.bind("<MouseWheel>", scroll_event)
canvas.bind("<B1-Motion>", drag_event) 
root.mainloop()

