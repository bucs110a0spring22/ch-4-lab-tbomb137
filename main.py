import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help


def setupWindow(wn):
  wn.setworldcoordinates(-360,-1,360,1)

def setupWindow2(wn):
  wn.setworldcoordinates(-250,-15,250,15)

def setupAxis(dart):
  turtle.setworldcoordinates(-360,-1,360,1)
  dart.color('black')
  dart.up()
  dart.goto(0,-1)
  dart.down()
  dart.goto(0,1)
  dart.up()
  dart.goto(-360,0)
  dart.down()
  dart.goto(360,0)
  dart.up()

def drawSineCurve(dart):
  for i in range(-360,360,1):
    x = i
    z = math.radians(i)
    y = math.sin(z)
    dart.down()
    dart.shape("turtle")
    dart.color('red')
    dart.goto(x,y)
  dart.up()

def drawCosineCurve(dart):
  for i in range(-360,360,1):
    x = i
    z = math.radians(i)
    y = math.cos(z)
    dart.color('blue')
    dart.goto(x,y)
    dart.down()
  dart.up()

def drawTangentCurve(dart):
  for i in range(-360,360,1):
    x = i
    z = math.radians(i)
    y = math.tan(z)
    dart.color('green')
    dart.goto(x,y)
    dart.down()

def drawaSineCurve(dart):
  for i in range(-360,360,1):
    x = i
    z = math.radians(i)
    y = math.sinh(z)
    dart.down()
    dart.color('cyan')
    dart.goto(x,y)
  dart.up()

def drawaCosineCurve(dart):
  for i in range(-360,360,1):
    x = i
    z = math.radians(i)
    y = math.cosh(z)
    dart.color('pink')
    dart.goto(x,y)
    dart.down()
  dart.up()

def drawaTangentCurve(dart):
  for i in range(-360,360,1):
    x = i
    z = math.radians(i)
    y = math.tanh(z)
    dart.color('yellow')
    dart.goto(x,y)
    dart.down()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
  
    setupWindow2(wn)
    setupAxis(dart)
    drawaSineCurve(dart)
    drawaCosineCurve(dart)
    drawaTangentCurve(dart)
    wn.exitonclick()
main()
