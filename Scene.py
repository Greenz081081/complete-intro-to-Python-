import tkinter as tk
import math

def main():
    # The width and height of the scene window.
    width = 1400
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
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

    draw_sky(canvas, 0, 0)
    draw_sun(canvas, 680, 100, ray_count= 10)
    draw_grass(canvas, 0, 500)
    draw_road(canvas, 0, 510)
    draw_road_mark(canvas, 0, 522)
    draw_road_mark(canvas, 250, 522)
    draw_road_mark(canvas, 550, 522)
    draw_road_mark(canvas, 850, 522)
    draw_road_mark(canvas, 1070, 522)
    draw_road_mark(canvas, 1350, 522)
    draw_green_grass(canvas, 0, 630)
    draw_cloud(canvas, 100, 150,)
    draw_cloud(canvas, 200, 100,)
    draw_cloud(canvas, 100, 100,)
    draw_cloud_2(canvas, 300, 50)
    draw_cloud_3(canvas, 200, 200)
    draw_cloud_3(canvas, 490, 100)
    draw_cloud_4(canvas, 590, 150)
    draw_cloud_2(canvas, 490, 200)
    draw_cloud_2(canvas, 450, 100)
    draw_cloud_2(canvas, 1100, 70)
    draw_cloud_2(canvas, 1150, 100)
    draw_cloud_5(canvas, 790, 0)
    draw_pole(canvas, 95, 200) 
    draw_pole_2(canvas, 100, 210)
    draw_light(canvas, 130, 225)
    draw_tree_trunk(canvas, 910, 200)
    draw_leaf(canvas, 880, 100)
    draw_leaf(canvas, 850, 200)
    draw_leaf(canvas, 950, 180)
    draw_leaf(canvas, 800, 120)
    draw_fruit_2(canvas, 890, 250)
    draw_fruit_2(canvas, 990, 230)
    draw_fruit_2(canvas, 950, 150)
    draw_fruit_2(canvas, 850, 170)
    draw_fruit(canvas, 890, 250)
    draw_fruit(canvas, 990, 230)
    draw_fruit(canvas, 950, 150)
    draw_fruit(canvas, 850, 170) 
    draw_fence(canvas, 20, 350)
    draw_fence(canvas, 110, 350)
    draw_fence(canvas, 200, 350)
    draw_fence(canvas, 290, 350)
    draw_fence(canvas, 390, 350)
    draw_fence(canvas, 490, 350)
    draw_fence(canvas, 590, 350)
    draw_fence(canvas, 690, 350)
    draw_fence(canvas, 790, 350)
    draw_fence(canvas, 1090, 350)
    draw_fence(canvas, 1190, 350)
    draw_fence(canvas, 1290, 350)
    draw_fence_2(canvas, 0, 450)
    draw_fence_2(canvas, 0, 550)
    draw_fence_2(canvas, 0, 650)
    draw_fence_3(canvas, 1082, 450)
    draw_fence_3(canvas, 1082, 550)
    draw_fence_3(canvas, 1082, 650)
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

def draw_sky(canvas, x, y):
    """
    Draw the sky in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_rectangle(x, y, x+1400, y+500, fill="#A7CCED", width=0)

def draw_sun(canvas, sun_left, sun_top, scale=1, ray_count=0):
    """
    Draw the sun in the canvas. sun_left, and sun_top contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        sun_left: left side of the region
        sun_top: top side of the region
        scale: An adjustable size of the sun
        raycount: An adjustable ray of the sun
    Return: nothing 
    """

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
    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="yellow", width=False)

    for i in range(ray_count):
        # How do i figure out where to draw the line for the rays?
        angle = (2 * math.pi / ray_count) * i
        #This help's me know the ray e nds
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, fill="yellow", width=ray_width)


def draw_grass(canvas, x, y,):
    """
    Draw a lighter grass in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_rectangle(x, y, x+1400, y+500, fill="#5CF64A", width=0)

def draw_cloud(canvas, x, y):
    """
    Draw a cloud in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x+300, y+100, fill="white", width=False)

def draw_cloud_2(canvas, x, y):
    """ 
    Draw a different shape of cloud in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x+200, y+100, fill="white", width=False)

def draw_cloud_3(canvas, x, y):
    """
    Draw a different shape of cloud in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x+150, y+80, fill="white", width=False)

def draw_cloud_4(canvas, x, y):
    """
    Draw a different shape of cloud in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x+200, y+90, fill="white", width=False)

def draw_cloud_5(canvas, x, y):
    """
    Draw grass in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x+200, y+30, fill="white", width=False)

def draw_fence(canvas, top, bottom):
    """
    Draw a horizontal fence in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    fence_width =  50
    fence_height = 500
    canvas.create_rectangle(top, bottom, top + fence_width, bottom + fence_height, fill="#F3DFA2")

def draw_fence_2(canvas, left, right):
    """
    Draw a vertical fence in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    fence_width = 850
    fence_height = 30
    canvas.create_rectangle(left, right, left + fence_width, right + fence_height, fill="#F3DFA2")


def draw_fence_3(canvas, left, right):
    """
    Draw different length of fence in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    fence_width = 400
    fence_height = 30
    canvas.create_rectangle(left, right, left + fence_width, right + fence_height, fill="#F3DFA2")


def draw_tree_trunk(canvas, top, bottom):
    """
    Draw a tree in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    tree_width =  50
    tree_height = 400
    canvas.create_rectangle(top, bottom, top + tree_width, bottom + tree_height, fill="#5E3023")

def draw_leaf(canvas, x, y):
    """
    Draw leaves in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x + 120, y + 120, fill="green", width=False)

def draw_fruit(canvas, x, y):
    """
    Draw fruits in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x + 10 , y + 10, fill="yellow", width=False)

def draw_fruit_2(canvas, x, y):
    """
    Draw different shape of fruits in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x + 30, y + 30, fill="red")

def draw_green_grass(canvas, x, y,):
    """
    Draw a darker green grass in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    grass_width = 1400
    grass_height = 500
    canvas.create_rectangle(x, y, x + grass_width, y + grass_height, fill="green", width=0)

def draw_pole(canvas, x, y):
    """
    Draw a horizontal light pole in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    light_width = 15
    light_height = 400
    canvas.create_rectangle(x, y, x + light_width, y + light_height, fill="#666B6A")


def draw_pole_2(canvas, x, y):
    """
    Draw a vertical light pole in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    light_width = 80
    light_height = 15
    canvas.create_rectangle(x, y, x + light_width, y + light_height, fill="#666B6A")

def draw_light(canvas, x, y):
    """
    Draw light in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    canvas.create_oval(x, y, x + 30, y + 30, fill="#4EFFEF")


def draw_road(canvas, x, y):
    """
    Draw road in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    road_width = 1400
    road_height = 55
    canvas.create_rectangle(x, y, x + road_width, y + road_height, fill="black" )

def draw_road_mark(canvas, x, y):
    """
    Draw road marks in the canvas. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    road_mark_width = 170
    road_mark_height = 15
    canvas.create_rectangle(x, y,x + road_mark_width, y + road_mark_height, fill="white")


def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    """
    Draw grid of lines in the canvas to give appropriate
    cordinates. x, and y contain the extent in
    pixels of the region where the scene should be drawn.

    Parameters:
        y: left side of the region
        x: right side of the region
    Return: nothing 
    """
    # metrics: Things that affect the drawing code
    text_horizontal_margin = 20
    text_vertical_margin = 10

    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    #Draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")


# Call the main function so that
# this program will start executing.
main()