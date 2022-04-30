"""slowly draws a rectangle"""

# import modules
import turtle

def draw_rectangle(t, x, y, width, height):
    """draws a rectangle"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_circle_on_vertices_of_rectangle(t, x, y, width, height):
    """draws a circle on the vertices of a rectangle"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(x + width, y)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(x + width, y + height)
    t.pendown()
    t.circle(10)
    t.penup()
    t.goto(x, y + height)
    t.pendown()
    t.circle(10)

if __name__ == "__main__":
    # create turtle
    t = turtle.Turtle()
    # set screen
    wn = turtle.Screen()
    # set background color
    wn.bgcolor("lightgreen")
    # set speed
    t.speed(0)
    # draw rectangle
    draw_rectangle(t, -100, -50, 200, 100)
    # draw circle on vertices of rectangle
    draw_circle_on_vertices_of_rectangle(t, -100, -50, 200, 100)
    # wait for user to close window
    wn.exitonclick()
