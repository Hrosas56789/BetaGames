import turtle

scr=turtle.Screen()
trt=turtle.Turtle()
scr.tracer(1,0)

trt.color("black")

for everth in range (-295,285):
    trt.forward(everth)
    trt.right(231)
    trt.forward(everth)
    trt.right(682)
    trt.forward(everth)
    trt.left(321)


scr.mainloop()