"""Stripper snowman performing her heart out in front of an audience -- Turtle project."""
__author__ = "730467698"


from turtle import Turtle, colormode, done 
import random 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    ertle.screen.bgcolor("cadetblue4")
    stage(ertle)
    audience_members(ertle)
    upper_body(ertle)
    mid_body(ertle)
    lower_body(ertle)
    stripper_pole(ertle)


def pen_tasks(t: Turtle, x: float, y: float, c: str) -> None:
    """Various functions to control the drawing pen tool."""
    t.penup()
    t.goto(x, y)
    t.setheading(0.0)
    t.down()
    t.speed(100)
    t.hideturtle()
    t.color(c)


def upper_body(ertle: Turtle) -> None:
    """This upper_body function draws the two hair pieces, snowman head, both eyes, the carrot nose, and the lips."""
    draw_circle(ertle, 0, 210, 110, "darkgoldenrod1")
    draw_circle(ertle, 0, 245, 75)
    draw_rectangle(ertle, -75, 400, 150, 40, "darkgoldenrod1")
    draw_square(ertle, -45, 350, 20, "cornflowerblue")
    draw_square(ertle, 25, 350, 20, "cornflowerblue")
    draw_nose(ertle, 45, 305)
    draw_circle(ertle, 0, 262, 17, "red")
    draw_rectangle(ertle, -17, 279, 34, 3)


def mid_body(ertle: Turtle) -> None:
    """This mid_body function draws the snowman chest, bikini top and strings, and both arms."""
    draw_circle(ertle, 0, 83, 87)
    bikini(ertle, -80, 180)
    bikini(ertle, 0, 180)
    draw_rectangle(ertle, -87, 205, 174, 7)
    left_arm(ertle, 88, 175, 130, 7)
    draw_rectangle(ertle, -217, 175, 130, 7, "chocolate4")


def lower_body(ertle: Turtle) -> None:
    """This lower_body function draws the snowman bottom, bikini bottom, bikini waistband, and bikini middle."""
    draw_circle(ertle, 0, -25, 99)
    bikini(ertle, -82, 132, 163, "right")
    draw_circle(ertle, 0, 73, 12, "black")
    draw_rectangle(ertle, -83, 135, 165, 7)


def stripper_pole(ertle: Turtle) -> None:
    """This stripper_pole function draws the long pole and pole base."""
    draw_rectangle(ertle, -230, 675, 15, 750, "gray")
    flat_oval(ertle, -258, -95, 50)


def stage(ertle: Turtle) -> None:
    """This stage function creates both parts of the stage the snowman stands on, and the blue background behind the stage."""
    draw_rectangle(ertle, -750, -50, 13000, 4000, "gray")
    flat_oval(ertle, -785, 0, 1100, "lightgray")
    draw_rectangle(ertle, -700, 500, 1600, 250, "cadetblue4")


def audience_members(ertle: Turtle) -> None:
    """This audience_members function creates the various parts of the audience members: their upper and mid body, hats, hat brims, and red seats."""
    i: int = 0
    x_offset: float = 205
    """I decided to import the random function and use it to randomly change the heights of each audience member in this loop."""
    while i < 7:
        y_offset: int = random.randint(0, 7)
        draw_circle(ertle, -625 + i * x_offset, -310 - i * y_offset, 65)
        draw_circle(ertle, -625 + i * x_offset, -430 - i * y_offset, 77)
        draw_square(ertle, -668 + i * x_offset, -130 - i * y_offset, 90)
        draw_rectangle(ertle, -700 + i * x_offset, -190 - i * y_offset, 150, 30)
        draw_square(ertle, -707 + i * x_offset, -325 - i * y_offset, 170, "dark red")
        i = i + 1


def draw_square(a_turtle: Turtle, x: float, y: float, width: float, c: str = "black") -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    pen_tasks(a_turtle, x, y, c) 
    a_turtle.fillcolor(c)
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1 
    a_turtle.end_fill()


def draw_nose(b_turtle: Turtle, x: float, y: float) -> None:
    """Draw snowman nose whose top-left corner is located at x, y."""
    pen_tasks(b_turtle, x, y, "orange")
    b_turtle.begin_fill()
    i: int = 15
    while i > 0:
        b_turtle.down()
        b_turtle.goto(x - 3 * i, y)
        b_turtle.circle(i)
        b_turtle.penup()
        i = i - 1
    b_turtle.end_fill()


def draw_circle(c_turtle: Turtle, x: float, y: float, width: float, c: str = "white") -> None:
    """Draw a circle of the given width and color whose top-left corner is located at x, y."""
    pen_tasks(c_turtle, x, y, c)
    c_turtle.fillcolor(c)
    c_turtle.begin_fill()
    "I decided to try out the turtle.circle() method to create the snowman body sections and eyes."
    c_turtle.circle(width)
    c_turtle.end_fill()


def draw_rectangle(d_turtle: Turtle, x: float, y: float, width: float, length: float, c: str = "black") -> None:
    """Draw a rectangle of the given width, length, and color whose top-left corner is located at x, y."""
    pen_tasks(d_turtle, x, y, c)
    d_turtle.fillcolor(c)
    d_turtle.begin_fill()
    i: int = 0
    while i < 2:
        d_turtle.forward(width)
        d_turtle.right(90)
        d_turtle.forward(length)
        d_turtle.right(90)
        i = i + 1
    d_turtle.end_fill()


def bikini(e_turtle: Turtle, x: float, y: float, side_length: float = 75, orient: str = "left") -> None:
    """Draw snowman bikini of a given side_length and orientation whose top-left corner is located at x, y."""
    pen_tasks(e_turtle, x, y, "black")
    e_turtle.color("black")
    e_turtle.goto(x, y)
    s: int = 0
    while (s < 100):
        e_turtle.forward(side_length)
        if orient == "left":
            e_turtle.left(120.5)
        else:
            e_turtle.right(120.5)
        side_length = side_length * 0.98
        s = s + 1


def left_arm(f_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw left arm of snowman of the given width and length whose top-left corner is located at x, y."""
    pen_tasks(f_turtle, x, y, "chocolate4")
    f_turtle.color("chocolate4")
    f_turtle.begin_fill()
    f_turtle.right(10)
    for i in range(2):
        f_turtle.forward(width)
        f_turtle.right(90)
        f_turtle.forward(length)
        f_turtle.right(90)
    f_turtle.end_fill()


def flat_oval(g_turtle: Turtle, x: float, y: float, r: float, c: str = "gray") -> None:   
    """Draw flat_oval base of stripper pole of a given radius and whose top-left corner is located at x, y."""   
    pen_tasks(g_turtle, x, y, c)  
    g_turtle.fillcolor(c)  
    g_turtle.begin_fill() 
    g_turtle.right(45)
    for loop in range(2):
        g_turtle.circle(r, 90)
        g_turtle.circle(r / 12, 90)
    g_turtle.end_fill() 


if __name__ == "__main__":
    main()
    done()