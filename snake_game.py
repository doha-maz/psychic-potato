#part 1 : screen
#part 2 : head
#part 3 : food
#part 4 : body
#part 5 : border Collisions
#part 6 : body Collisions
#part 7 : scoring

import turtle
import time
import random

delay=0.1

#Score
score=0
highScore=0

# set up the screen
wn = turtle.Screen()#creating a window for the game
wn.title("Snake Game")#changing the title of the game
wn.bgcolor("purple")#making the background of the window purple
wn.setup(width=600, height=600)
wn.tracer(0)#it turns of the animation on the screen(and the screen updates)

#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()#so it does not draw anything
head.goto(0,0)#when the games starts we want the head to be in the center of the screen
head.direction="stop"

#snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier",24,"normal"))

#functions

#directions
def go_up():
    if head.direction != "down":
       head.direction="up"

def go_down():
    if head.direction != "up":
       head.direction="down"

def go_right():
    if head.direction != "left":
       head.direction="right"

def go_left():
    if head.direction != "right":
       head.direction="left"

#movements
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"x")
wn.onkeypress(go_left,"l")
wn.onkeypress(go_right,"m")



#Main game loop
while True:
    wn.update()

    #Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments list
        segments.clear()

        #reset the score
        score=0

        #Reset the delay
        delay =0.1

        pen.clear()
        pen.write("score:{} High Score: {}".format(score, highScore), align="center", font=("Courier",24,"normal") )


    #check for a collision with the food
    if head.distance(food)<20:
        #Move the food to a random spot
        x= random.randint(-200,200)
        y= random.randint(-200,200)
        food.goto(x,y)
        
        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten  the delay
        delay-=0.001

        #Increase the score
        score +=10

        if score > highScore:
            highScore = score
        
        pen.clear()
        pen.write("score:{} High Score: {}".format(score, highScore), align="center", font=("Courier",24,"normal") )

    #Move the end segments first in reverse order
    for i in range(len(segments)-1, 0, -1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)



    move()

    #check for the head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #Hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segments list
            segments.clear()

            #reset the score
            score=0

            #Reset the delay
            delay =0.1

            #Update the score display
            pen.clear()
            pen.write("score:{} High Score: {}".format(score, highScore), align="center", font=("Courier",24,"normal") )

    time.sleep(delay)
   

wn.mainloop() 