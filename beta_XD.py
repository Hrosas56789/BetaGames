import turtle

scr=turtle.Screen()
trt=turtle.Turtle()
scr.tracer(1,0)


for everth in range (-248,210):
    trt.forward(everth)
    trt.right(132)
    trt.circle(14)
    trt.left(321)
    trt.forward(everth)


scr.mainloop()