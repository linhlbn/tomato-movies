import turtle

def draw_triangle(step):
    move.shape("turtle")
    move.speed(0)
    move.color("orange", "yellow")
    count = 0	
    while (count<3) :
        move.forward(step) 
        move.left(120)                
        count = count + 1
        
        
def draw_fractals():
#new algorithm
    number = 20
    times = 7
    while (times != 0) :
        for i in range(0,times):
            draw_triangle(number)
            move.forward(number)
        move.backward(number*times)
        move.left(60)
        move.forward(number)
        move.right(60)
        times = times - 1

window = turtle.Screen()
window.bgcolor("white")
move = turtle.Turtle()
draw_fractals()
window.exitonclick()
