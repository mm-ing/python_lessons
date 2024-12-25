import tkinter as tk
import math

# Function to rotate a point around a given center
def rotate_point(x, y, cx, cy, angle):
    radians = math.radians(angle)
    cos_val = math.cos(radians)
    sin_val = math.sin(radians)
    x -= cx
    y -= cy
    x_new = x * cos_val - y * sin_val
    y_new = x * sin_val + y * cos_val
    return x_new + cx, y_new + cy

# Function to rotate a rectangle
def rotate_rectangle(canvas, rect, angle):
    coords = canvas.coords(rect)
    cx = (coords[0] + coords[2]) / 2
    cy = (coords[1] + coords[3]) / 2
    new_coords = []
    for i in range(0, len(coords), 2):
        x, y = coords[i], coords[i+1]
        new_x, new_y = rotate_point(x, y, cx, cy, angle)
        new_coords.extend([new_x, new_y])
    canvas.coords(rect, *new_coords)

# Create the main window
root = tk.Tk()
root.title("Rotate Object Example")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create a rectangle
rect = canvas.create_rectangle(100, 100, 200, 200, fill="blue")

# Button to rotate the rectangle
rotate_button = tk.Button(root, text="Rotate", command=lambda: rotate_rectangle(canvas, rect, 45))
rotate_button.pack()

# Run the Tkinter event loop
root.mainloop()
