import turtle
myScreen = turtle.Screen()
trt002 = turtle.Turtle()

def mover() :
    trt002.forward(20)
    myScreen.listen()

def move() :
    trt002.back(20)
    myScreen.listen()

def movew() :
    trt002.left(20)
    myScreen.listen()

def moves() :
    trt002.right(20)
    myScreen.listen()

myScreen.listen()
myScreen.onkeypress(mover, "w")
myScreen.onkeypress(move, "s")
myScreen.onkeypress(movew, "a")
myScreen.onkeypress(moves, "d")


myScreen.mainloop()