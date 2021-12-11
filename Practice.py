import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

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
    draw_sky(canvas, 0, 0,)
    
   


def draw_sky(canvas, x, y):
    # canvas.create_oval(x, y, x + 100, y + 100, fill="#FFC53A", width=False)
    canvas.create_rectangle(x, y, x+800, y+500, fill="#3E7CB1", width=0)


    #  canvas.create_image(x, y,fill="#02182B")




# Draw Horizontal lines
    # for i in range(top, bottom, fill):
    #     canvas.create_line(left, i, right, i)

# Draw Vertical lines
    # for i in range(left, right, grid_spacing):
    #     canvas.create_line(left, i, right, i)
 

main()