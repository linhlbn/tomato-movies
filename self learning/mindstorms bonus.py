import turtle

def draw_square():    
    move.shape("arrow")
    move.color("#285078", "#a0c8f0")
    move.speed(1)
    count = 0	
    while (count<4) : 			
        move.forward(200)
        move.right(90)
        count = count + 1
		
def draw_circle():
    move.shape("circle")
    move.color("green", "red")
    move.circle(118)		

def draw_triangle():
    move.shape("turtle")
    move.color("orange", "yellow")
    count = 0	
    while (count<3) :
        move.right(120)    
        move.forward(132)        
        count = count + 1
			 
window = turtle.Screen()
window.bgcolor("white")
move = turtle.Turtle()
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()
