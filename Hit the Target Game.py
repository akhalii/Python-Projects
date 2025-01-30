#Hit the turtle game
import turtle

#Constants
SCREEN_WIDTH = 600
SCREEN_LENGTH = 600
TARGET_LLEFT_X = 50
TARGET_LLEFT_Y = 300
TARGET_LENGTH = 25
FORCE_FACTOR = 20
PROJECTILE_SPEED = 1
NORTH = 90
EAST = 0
SOUTH = 270
WEST = 180

#Canvas
def canvas():
    length = SCREEN_LENGTH
    width = SCREEN_WIDTH
    turtle.setup(length,width)

#Target
def target():
    target_length = TARGET_LENGTH
    turtle.penup()
    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    for i in range(4):
        turtle.forward(target_length)
        turtle.right(90)
    turtle.penup()

#Center Turtle
def center_turtle():
    turtle.goto(0,0)
    turtle.setheading(EAST)
    turtle.speed(PROJECTILE_SPEED)

#Get Angle and Force From User
def get_user_input():
    angle = float(input("Enter projectile angle: "))
    force = float(input("Enter projectile force: "))
    return angle, force

#Calculate distance
def calculate_distance(force):
    distance = force * FORCE_FACTOR
    return distance

#Set Angle
def set_angle():
    turtle.setheading(angle)

#Launch Projectile
def launch_projectile():
    distance = calculate_distance()
    turtle.pendown()
    turtle.forward(distance)

#Did It Hit the Target?
def hit_target():
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_LENGTH) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_LENGTH)):
            print("You hit the target!")
        
    else:
        print("You missed the target!")

#Main Function
def main():
    canvas()
    target()
    center_turtle()
    get_user_input()
    calculate_distance(get_user_input())
    set_angle(get_user_input())
    launch_projectile()
    hit_target()

main()
