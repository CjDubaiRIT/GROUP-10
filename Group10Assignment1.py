import turtle


#Three separate functions for hexagons
#Go to the required coordinates for each function
#Ask the user to enter the color for the border and the shape for each function


def hexagon(hex_border,hex_color):
    turta=turtle
    turta.penup()
    turta.goto(-200,125)
    turta.pendown()
    turta.speed(10)
    turta.pencolor(hex_border)
    turta.fillcolor(hex_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.end_fill()




def hexagon1(hex_border, hex_color):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(-150 , 0)
    turta.pendown()
    #needs to be another coordinate above the first hex
    turta.pencolor(hex_border)
    turta.fillcolor(hex_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.end_fill()




def hexagon2(hex_border, hex_color):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(-100, -125)
    #needs to be another coordinate above the second hex
    turta.pendown()
    turta.pencolor(hex_border)
    turta.fillcolor(hex_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.end_fill()


#Three separate functions for squares
#Go to the required coordinates for each function
#Ask the user to enter the color for the border and the shape for each function




def square(square_border,square_colour):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(50 , 125)
    turta.pendown()
    turta.pencolor(square_border)
    turta.fillcolor(square_colour)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()




def square1(square_border, square_colour):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(100 , 0)
    turta.pendown()
    turta.pencolor(square_border)
    turta.fillcolor(square_colour)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()




def square2(square_border, square_colour):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(150,-125)
    turta.pendown()
    turta.pencolor(square_border)
    turta.fillcolor(square_colour)
    turta.begin_fill()
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.end_fill()








#Three separate functions for circles
#Go to the required coordinates for each function
#Ask the user to enter the color for the border and the shape for each function
def circle(circle_color,circle_border):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(-30 , 125)
    turta.pendown()
    turta.fillcolor(circle_color)
    turta.pencolor(circle_border)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()




def circle1(circle_color, circle_border):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(20, 0)
    turta.pendown()
    turta.fillcolor(circle_color)
    turta.pencolor(circle_border)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()




def circle2(circle_color, circle_border):
    turta=turtle
    turta.speed(10)
    turta.penup()
    turta.goto(70 , -125)
    turta.pendown()
    turta.fillcolor(circle_color)
    turta.pencolor(circle_border)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()

def pattern(hex_border, hex_color, circle_color, circle_border,square_border, square_colour):
    #print the shape
   hexagon(hex_border, hex_color)
   circle(circle_color, circle_border)
   square(square_border, square_colour)
   hexagon1(hex_border, hex_color)
   circle1(circle_color, circle_border)
   square1(square_border, square_colour)
   hexagon2(hex_border, hex_color)
   circle2(circle_color, circle_border)
   square2(square_border, square_colour)





def main():
   turta=turtle
   #the color of the pen can be set by the user using the variables
   hex_border=str(input("name shape's color for the hexagon:"))
   hex_color=str(input("name border color for the hexagon:"))
   #print the shape




   #the color of the pen can be set by the user using the variables
   square_border=str(input("name border color for the square:"))
   square_colour=str(input("name shape's color for the square:"))
   #print the shape




   #the color of the pen can be set by the user using the variables
   circle_border=str(input("name border color for the circle:"))
   circle_color=str(input("name shape's color for the circle:"))
   
   pattern(hex_border, hex_color, circle_color, circle_border,square_border, square_colour)

   done=input("press enter to close")
   
 
 
 
 
 
 
 
main()



















