import tkinter as tk
import math


def main():
    # The width and height of the scene window.
    width = 1380
    height = 800

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)


    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    draw_sky(canvas, 0, 0)
    # draw_sun(canvas, 20, 20, ray_count=10)
    draw_sun(canvas, 1000, 60, scale=2, ray_count= 10)
    draw_ground(canvas, 0, 500)
    draw_cloud(canvas, 100, 150)
    draw_cloud(canvas, 200, 100)
    draw_cloud(canvas, 100, 100)
    draw_cloud_2(canvas, 300, 50)
    draw_cloud_3(canvas, 200, 200)
    draw_cloud_3(canvas, 490, 100)
    draw_cloud_4(canvas, 590, 150)
    draw_cloud_2(canvas, 490, 180)
    draw_cloud_2(canvas, 450, 100)
    draw_cloud(canvas, 780, 150)
    draw_cloud_2(canvas, 900, 100)
    draw_cloud(canvas, 700, 200)
    draw_cloud_5(canvas, 1000, 200)
    draw_cloud(canvas, 600, 70)
    draw_cloud_2(canvas, 700, 250)
    draw_cloud_2(canvas, 700, 150)
    draw_cloud_2(canvas, 1070, 100)
    draw_house(canvas,200, 50)
   
    
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

   
    
   


def draw_sky(canvas, x, y):
    canvas.create_rectangle(x, y, x+1380, y+800, fill="#02182B", width=0)


def draw_sun(canvas, sun_left, sun_top, scale=1, ray_count=0):
    # (NOTe: Adding the parameter called {scale}
    # enable me have different sizes of sun each
    # time i add the scale to where I am calling
    # the draw_sun function at the def main().

    # When creating a define function like this,
    # what we want to do is to put all the metrics at the
    # top and then all of our drawing codes afterwards.


    # If i want to make the drawing of the sun 
    # have some light rays, then i need to include
    # the folling in my code. 

    # Metrics: Constants
    sun_width = 70 * scale
    sun_height =70 * scale
    ray_length = 60 * scale
    ray_width = 2 * scale
    # ray_count = 10

    # Calculations
    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    # Figure out the center of the sun
    sun_center_x = sun_left +  (sun_width /2)
    sun_center_y = sun_top +  (sun_height/ 2)


    # Drawing codes based on the calculations
    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="red", width=False)

    for i in range(ray_count):
        # How do i figure out where to draw the line for the rays?
        angle = (2 * math.pi / ray_count) * i
        #This help's me know the ray e nds
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, fill="red", width=ray_width)

def draw_ground(canvas, x, y,):
    canvas.create_rectangle(x, y, x+1380, y+800, fill="#96F550", width=0)


def draw_cloud(canvas, x, y, scale=1):
    canvas.create_oval(x, y, x + 300, y + 100, fill="white",  width=False)

def draw_cloud_2(canvas, x, y):
    canvas.create_oval(x, y, x+200, y+100, fill="white", width=False)

def draw_cloud_3(canvas, x, y):
    canvas.create_oval(x, y, x+150, y+80, fill="white", width=False)

def draw_cloud_4(canvas, x, y):
    canvas.create_oval(x, y, x+200, y+90, fill="white", width=False)

def draw_cloud_5(canvas, x, y):
    canvas.create_oval(x, y, x+150, y+100, fill="white", width=False)

def draw_house(canvas, x, y):
    canvas.create_rectangle(x, y, x + 10, y + 10, fill="white")

   

# def draw_twelvth_cloud(canvas, x, y):
#     canvas.create_oval(x, y, x+200, y+100, fill="white", width=False)

# def draw_thirteen_cloud(canvas, x, y):
#     canvas.create_oval(x, y, x+200, y+100, fill="white", width=False)



def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    #metrics: Things that affect the drawing code
    text_horizontal_margin = 20
    text_vertical_margin = 10

    # Drawing code
    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    #Draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

main()