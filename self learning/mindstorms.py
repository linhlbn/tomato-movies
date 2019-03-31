import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()

    brad.speed(1)
    brad.shape("classic")
    brad.color("red")
    brad.forward(200)
    brad.right(90)

    brad.speed(1)
    brad.shape("circle")
    brad.color("blue")
    brad.forward(200)
    brad.right(90)
    
    brad.speed(1)
    brad.shape("triangle")
    brad.color("green", "red")
    brad.forward(200)
    brad.right(90)
    
    brad.speed(1)
    brad.shape("arrow")
    brad.color("#285078", "#a0c8f0")
    brad.forward(200)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()
draw_square()
