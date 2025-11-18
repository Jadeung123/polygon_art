import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def first_function():
    for _ in range(30):
        num_sides = 3
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def second_function():
    for _ in range(30):
        num_sides = 4
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def third_function():
    for _ in range(30):
        num_sides = 5
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def fourth_function():
    for _ in range(30):
        num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def fifth_function():
    for _ in range(30):
        num_sides = 3
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def sixth_function():
    for _ in range(30):
        num_sides = 4
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def seventh_function():
    for _ in range(30):
        num_sides = 5
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def eighth_function():
    for _ in range(30):
        num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio
        draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def ninth_function():
    for _ in range(30):
        num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)
        first_chance = random.randint(0, 1)
        if first_chance:
            reduction_ratio = 0.618
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            second_chance = random.randint(0, 1)
            if second_chance:
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size *= reduction_ratio
                draw_polygon(num_sides, size, orientation, location, color, border_size)
    turtle.done()

def choices(choice):
    if choice == '1':
        first_function()
    elif choice == '2':
        second_function()
    elif choice == '3':
        third_function()
    elif choice == '4':
        fourth_function()
    elif choice == '5':
        fifth_function()
    elif choice == '6':
        sixth_function()
    elif choice == '7':
        seventh_function()
    elif choice == '8':
        eighth_function()
    elif choice == '9':
        ninth_function()


choice = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ")
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
choices(choice)

# draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618

# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]

# # adjust the size according to the reduction ratio
# size *= reduction_ratio

# # draw the second polygon embedded inside the original 
# draw_polygon(num_sides, size, orientation, location, color, border_size)

# # hold the window; close it by clicking the window close 'x' mark
# turtle.done()