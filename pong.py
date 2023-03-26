import turtle
import os
#from playsound import playsound (not using at the moment)

#Create the game window
wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech - freecodecamp tutorial")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   #set animation speed (not paddle movement speed)
paddle_a.shape("square")   #default 20px by 20px
paddle_a.shapesize(stretch_len=1, stretch_wid=5)   #default length x 1, default width x 5, so width is 20x5 (100px)
paddle_a.color("white")
paddle_a.penup()   #no drawing when moving
paddle_a.goto(-350, 0)   #location on axis, 0 is middle, negative left, positive right


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#Add dx/dx, every time the ball move, it will move the indicated amount of pixels
#you can adjust the dx/dy numbers to make the game work as you wish
ball.dx = 2   #moves 2 px positive on x axis (right)
ball.dy = -2   #moves 2 pixels positive on y axis (up)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor()   #ycor is turtle function to return location of y coordinate
    y += 20   #adds 20px every time it goes up
    paddle_a.sety(y)   #set y coordinate to the new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard Binding
wn.listen()   #listens to keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")   #up arrow
wn.onkeypress(paddle_b_down, "Down")   #down arrow

#Main Game Loop
while True:
    #anytime the loop runs we will update the screen
    wn.update()

    #Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   #reverses direction
        os.system("afplay arcadebling.wav&")
        #playsound('arcadebling.wav')
            #playsound has delay and the & symbol causes errors if used

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        #add scoring
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay bounce.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        #add scoring
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay bounce.wav&")

    #Paddle & Ball Collisions
    #check if ball is colliding with the paddle and if it is in the center of the paddle to reverse direction
    if (ball.xcor() > 340 and ball.xcor() < 350) and(ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and(ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
