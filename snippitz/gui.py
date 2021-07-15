from tkinter import *

root = Tk()
root.title('Node Mapper')
canvas = Canvas(root, bg='white', width = 1600,height = 900)

last_mouse_x = 0
last_mouse_y = 0

class Circle:
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
		
circles = []


class PanZoomHandler:
	def __init__(self):
		self.zoom_amount = 1.0 	# higher zoom scales everything up, moves the camera in
								# lower zoom scales everything down, moves the camera out
		self.pan_x = 0 			# positive pans the camera to the right, moves the canvas to the left
								# negative pans the camera to the left, moves the canvas to the right
		self.pan_y = 0 			# positive pans the camera down, moves the canvas up
								# negative pans the camera up, moves the canvas down
	
	def pan(self, delta_x, delta_y):
		self.pan_x += delta_x*(1/self.zoom_amount)
		self.pan_y += delta_y*(1/self.zoom_amount)
		
	def zoom(self, amount, focus_x = 0, focus_y = 0):
		'''
			the view needs to pan as the camera zooms in and out to ensure the same point remains in focus during the pan
			in order to do this, we need to get the projected mouse coordinates before the zoom, and then after.
			Then pan the delta
		'''
		old_screen_x, old_screen_y = self.canvas_to_screen_coordinates(focus_x,focus_y)
		self.zoom_amount += amount
		if self.zoom_amount < 0.001:
			self.zoom_amount = 0.001
		new_screen_x, new_screen_y = self.canvas_to_screen_coordinates(focus_x,focus_y)
		self.pan(new_screen_x-old_screen_x,new_screen_y-old_screen_y)
	
	def canvas_to_screen_coordinates(self, x, y):
		''' 
			This translates the canvas coordinates to screen coordinates.
			When panning, if an object is at 0,0 and the camera is panned to 20,-10 then the object should be rendered at -20,10 in order to appear in the correct location on the screen. This can be done by subtracting pan_x, pan_y from x, y.
			When zooming, if an object is at 20,-10 and the zoom is at 0.5, then the object should be rendered at 10,-5 to appear in the correct location on the screen. This can be done by multiplying x, y with zoom
		'''
		return self.zoom_amount*(x-self.pan_x), self.zoom_amount*(y-self.pan_y)
		
	def screen_to_canvas_coordinates(self, x, y):
		'''
			This translates the screen coordinates to canvas coordinates.
			When panning, if the mouse is at 0,0 and the camera is panned to 20,-10, then the mouse should be considered to be at 20,-10 in order to interact with the correct part of the canvas. This can be done by adding pan_x, pan_y to x, y.
			When zooming, if the mouse is at 20,-10 and the zoom is at 0.5, then the mouse should be considered to be at 40,-20 in order to interact with the correct part of the canvas. This can be done by multiplying x, y with 1/zoom
		'''
		return (x/self.zoom_amount)+self.pan_x, (y/self.zoom_amount)+self.pan_y

panzoom = PanZoomHandler()
	
def update_canvas():
	canvas.delete("all")
	for circle in circles:
		x,y = panzoom.canvas_to_screen_coordinates(circle.x, circle.y)
		radius = panzoom.zoom_amount*circle.radius
		coord = x-radius,y-radius,x+radius,y+radius
		canvas.create_oval(coord, outline="black", fill="white",width=2)
		canvas.pack(expand = True, fill = BOTH)

	
def click_event(event):
	global last_mouse_x
	global last_mouse_y
	last_mouse_x = event.x
	last_mouse_y = event.y
	circles.append(Circle(*panzoom.screen_to_canvas_coordinates(event.x,event.y), 100))
	update_canvas()

def scroll_event(event):
	if event.delta > 0:
		panzoom.zoom(0.05, *panzoom.screen_to_canvas_coordinates(event.x,event.y))
	elif event.delta < 0:
		panzoom.zoom(-0.05, *panzoom.screen_to_canvas_coordinates(event.x,event.y))
	update_canvas()
	
def drag_event(event):
	global last_mouse_x
	global last_mouse_y
	panzoom.pan(last_mouse_x - event.x, last_mouse_y - event.y)
	last_mouse_x = event.x
	last_mouse_y = event.y
	update_canvas()

canvas.pack(expand = True, fill = BOTH)
root.bind("<Button-1>", click_event)
root.bind("<MouseWheel>", scroll_event)
root.bind("<B1-Motion>", drag_event) 
root.mainloop()

