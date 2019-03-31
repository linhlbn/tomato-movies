import turtle

def draw_circle(radius):
    move.shape("arrow")
    move.color("#1DE9B6", "#a0c8f0")
    move.circle(radius)		
    
def draw_triple_circle(radius):
    for j in range(0,3):
        draw_circle(radius)
        move.left(120)    
    
def draw_triangle(step):
    move.shape("turtle")
    move.speed(0.5)
    move.color("#F50057", "yellow")
    count = 0	
    while (count<3) :
        move.forward(step) 
        move.left(120)                
        count = count + 1
        
def draw_fractals():
#new algorithm
    number = 15
    rad = 50
    times = 0
    final = times
    while (times != 0) :
        draw_triple_circle(rad)
        for i in range(0,times):
            draw_triangle(number)
            move.forward(number)
            draw_triple_circle(rad)
        rad = rad + 2    
        move.backward(number*times)
        move.left(60)
        move.forward(number)
        move.right(60)
        times = times - 1
    draw_circle(rad+5)
    move.right(60)
    move.forward(number*final)
    #move.left(60)
    #move.forward(number)

window = turtle.Screen()
window.bgcolor("#EEEEEE")
move = turtle.Turtle()
draw_fractals()
window.exitonclick()
