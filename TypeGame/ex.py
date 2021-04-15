GlowScript 3.0 VPython

#Creating Ball
myBall = sphere(color=color.red, radius=2)

#Creating Box
myBox = box(pos = vec(5,0,0),color = color.blue, size = vec(0.5,4,1))

myBall.color = color.green
myBox.pos.x =10

#Vectors
r = vector(3,4,5)
r_arrow = arrow(pos = vector(0,0,0),axis = r, shaftwidth = 0.2)