from tkinter import *
from math import *
from numpy import array

screen_shape = (1000, 1000)
translate = (500, 500)

def create_circle(point, radius, canvas, fill = 'black'):
    canvas.create_oval(point.val[0] - radius + translate[0], 
                       point.val[1] - radius + translate[1], 
                       point.val[0] + radius + translate[0], 
                       point.val[1] + radius + translate[1], 
                       fill=fill)

def connect(point_one, point_two, canvas):
    canvas.create_line(point_one.val[0] + translate[0], 
                       point_one.val[1] + translate[1], 
                       point_two.val[0] + translate[0], 
                       point_two.val[1] + translate[1])

root = Tk('Sim')
root.geometry(f'{screen_shape[0]}x{screen_shape[1]}')

canvas = Canvas(root, bg='white', height=screen_shape[0], width=screen_shape[1])
canvas.place(x=-2, y=-2)


#############
##
## 2D
##
#############

rotation = array(
    [[cos(pi/100), -sin(pi/100)],
     [sin(pi/100),  cos(pi/100)]
    ]
)


#############
##
## 3D
##
#############

rotationZ = array(
    [[cos(pi/200), -sin(pi/200), 0],
     [sin(pi/200),  cos(pi/200), 0],
     [         0,           0, 1]
    ]
)

rotationX = array(
    [[1,            0,            0],
     [0,  cos(pi/200), -sin(pi/200)],
     [0,  sin(pi/200),  cos(pi/200)]
    ]
)

rotationY = array(
    [[cos(pi/200), 0, -sin(pi/200)],
     [          0, 1,            0],
     [sin(pi/200), 0,  cos(pi/200)]
    ]
)

# Projection matrix from 3D to 2D
projection = array(
    [[1, 0, 0],
     [0, 1, 0]]
)

class Vector2D:

    def __init__(self, array):
        self.val = array

    def draw(self, canvas):
        create_circle(self, 2, canvas)
        pass

    def rotate(self, rotation):
        self.val = self.val @ rotation

class Vector3D:

    def __init__(self, array):
        self.val = array

    def draw(self, canvas):
        Vector2D(projection.dot(self.val)).draw(canvas)

    def rotate(self, rotation):
        self.val = self.val @ rotation

to_draw = [

    # Front
    Vector3D(array([  0,-100, 25])), # 0
    Vector3D(array([ 25, -70, 25])),
    Vector3D(array([-25, -70, 25])),
    Vector3D(array([ 40, -20, 25])),
    Vector3D(array([-40, -20, 25])),
    Vector3D(array([ 32,   0, 25])),
    Vector3D(array([-32,   0, 25])),
    Vector3D(array([  0,  16, 25])),

    # Back
    Vector3D(array([  0,-100, -25])), # 8
    Vector3D(array([ 25, -70, -25])),
    Vector3D(array([-25, -70, -25])),
    Vector3D(array([ 40, -20, -25])),
    Vector3D(array([-40, -20, -25])),
    Vector3D(array([ 32,   0, -25])),
    Vector3D(array([-32,   0, -25])),
    Vector3D(array([  0,  16, -25])),

    # 0 on the z-axis
    Vector3D(array([  0,-140, 0])),   # 16

    Vector3D(array([ 18,-130, 0])),
    Vector3D(array([-18,-130, 0])),

    Vector3D(array([ 40,-100, 0])),
    Vector3D(array([-40,-100, 0])),

    Vector3D(array([ 54, -60, 0])),
    Vector3D(array([-54, -60, 0])),

    Vector3D(array([ 60, -25, 0])),
    Vector3D(array([-60, -25, 0])),

    Vector3D(array([ 60, -15, 0])),
    Vector3D(array([-60, -15, 0])),

    Vector3D(array([ 55, -0, 0])),
    Vector3D(array([-55, -0, 0])),

    Vector3D(array([ 32, 20, 0])),
    Vector3D(array([-32, 20, 0])),

    Vector3D(array([-0, 30, 0])),

    # 32

    # 12 on the z-axis
    Vector3D(array([10,-115, 12.5])),
    Vector3D(array([-10,-115, 12.5])),

    Vector3D(array([ 45, -50, 12.5])),
    Vector3D(array([-45, -50, 12.5])),

    Vector3D(array([ 50, -16, 12.5])),
    Vector3D(array([-50, -16, 12.5])),

    Vector3D(array([ 28,  10, 12.5])),
    Vector3D(array([-28,  10, 12.5])),

    # -12 on the z-axis
    Vector3D(array([10,-115, -12.5])),
    Vector3D(array([-10,-115, -12.5])),

    Vector3D(array([ 45, -50, -12.5])),
    Vector3D(array([-45, -50, -12.5])),

    Vector3D(array([ 50, -16, -12.5])),
    Vector3D(array([-50, -16, -12.5])),

    Vector3D(array([ 28,  10, -12.5])),
    Vector3D(array([-28,  10, -12.5])),
]

while True:

    connect(to_draw[0], to_draw[1], canvas)
    connect(to_draw[0], to_draw[2], canvas)
    connect(to_draw[1], to_draw[3], canvas)
    connect(to_draw[2], to_draw[4], canvas)
    connect(to_draw[3], to_draw[5], canvas)
    connect(to_draw[4], to_draw[6], canvas)
    connect(to_draw[5], to_draw[7], canvas)
    connect(to_draw[6], to_draw[7], canvas)

    connect(to_draw[0+8], to_draw[1+8], canvas)
    connect(to_draw[0+8], to_draw[2+8], canvas)
    connect(to_draw[1+8], to_draw[3+8], canvas)
    connect(to_draw[2+8], to_draw[4+8], canvas)
    connect(to_draw[3+8], to_draw[5+8], canvas)
    connect(to_draw[4+8], to_draw[6+8], canvas)
    connect(to_draw[5+8], to_draw[7+8], canvas)
    connect(to_draw[6+8], to_draw[7+8], canvas)

    connect(to_draw[0+16], to_draw[1+16], canvas)
    connect(to_draw[0+16], to_draw[2+16], canvas)
    connect(to_draw[1+16], to_draw[3+16], canvas)
    connect(to_draw[2+16], to_draw[4+16], canvas)
    connect(to_draw[3+16], to_draw[5+16], canvas)
    connect(to_draw[4+16], to_draw[6+16], canvas)
    connect(to_draw[5+16], to_draw[7+16], canvas)
    connect(to_draw[6+16], to_draw[8+16], canvas)
    connect(to_draw[7+16], to_draw[9+16], canvas)
    connect(to_draw[8+16], to_draw[10+16], canvas)
    connect(to_draw[9+16], to_draw[11+16], canvas)
    connect(to_draw[10+16], to_draw[12+16], canvas)
    connect(to_draw[11+16], to_draw[13+16], canvas)
    connect(to_draw[12+16], to_draw[14+16], canvas)
    connect(to_draw[13+16], to_draw[15+16], canvas)
    connect(to_draw[15+16], to_draw[14+16], canvas)

    connect(to_draw[0+32], to_draw[0], canvas)
    connect(to_draw[1+32], to_draw[0], canvas)

    connect(to_draw[0+32], to_draw[16], canvas)
    connect(to_draw[1+32], to_draw[16], canvas)

    connect(to_draw[0+32], to_draw[3 + 16], canvas)
    connect(to_draw[1+32], to_draw[4 + 16], canvas)

    connect(to_draw[0+32], to_draw[1 + 0], canvas)
    connect(to_draw[1+32], to_draw[2 + 0], canvas)

    connect(to_draw[3+16], to_draw[1 + 0], canvas)
    connect(to_draw[4+16], to_draw[2 + 0], canvas)

    connect(to_draw[2+32], to_draw[1 + 0], canvas)
    connect(to_draw[3+32], to_draw[2 + 0], canvas)

    connect(to_draw[2+32], to_draw[3 + 16], canvas)
    connect(to_draw[3+32], to_draw[4 + 16], canvas)

    connect(to_draw[2+32], to_draw[5 + 16], canvas)
    connect(to_draw[3+32], to_draw[6 + 16], canvas)

    connect(to_draw[2+32], to_draw[7 + 16], canvas)
    connect(to_draw[3+32], to_draw[8 + 16], canvas)

    connect(to_draw[2+32], to_draw[3], canvas)
    connect(to_draw[3+32], to_draw[4], canvas)

    connect(to_draw[4+32], to_draw[3], canvas)
    connect(to_draw[5+32], to_draw[4], canvas)

    connect(to_draw[4+32], to_draw[7+16], canvas)
    connect(to_draw[5+32], to_draw[8+16], canvas)

    connect(to_draw[4+32], to_draw[9+16], canvas)
    connect(to_draw[5+32], to_draw[10+16], canvas)

    connect(to_draw[4+32], to_draw[5], canvas)
    connect(to_draw[5+32], to_draw[6], canvas)

    connect(to_draw[9+16], to_draw[5], canvas)
    connect(to_draw[10+16], to_draw[6], canvas)

    connect(to_draw[6+32], to_draw[5], canvas)
    connect(to_draw[7+32], to_draw[6], canvas)

    connect(to_draw[6+32], to_draw[7], canvas)
    connect(to_draw[7+32], to_draw[7], canvas)

    connect(to_draw[15+16], to_draw[7], canvas)

    connect(to_draw[6+32], to_draw[11+16], canvas)
    connect(to_draw[7+32], to_draw[12+16], canvas)

    connect(to_draw[6+32], to_draw[13+16], canvas)
    connect(to_draw[7+32], to_draw[14+16], canvas)


    # Oteh side
    connect(to_draw[0+32 + 8], to_draw[0 + 8], canvas)
    connect(to_draw[1+32 + 8], to_draw[0 + 8], canvas)

    connect(to_draw[0+32 + 8], to_draw[16], canvas)
    connect(to_draw[1+32 + 8], to_draw[16], canvas)

    connect(to_draw[0+32 + 8], to_draw[3 + 16], canvas)
    connect(to_draw[1+32 + 8], to_draw[4 + 16], canvas)

    connect(to_draw[0+32 + 8], to_draw[1 + 0 + 8], canvas)
    connect(to_draw[1+32 + 8], to_draw[2 + 0 + 8], canvas)

    connect(to_draw[2+32 + 8], to_draw[1 + 0 + 8], canvas)
    connect(to_draw[3+32 + 8], to_draw[2 + 0 + 8], canvas)

    connect(to_draw[2+32 + 8], to_draw[3 + 16], canvas)
    connect(to_draw[3+32 + 8], to_draw[4 + 16], canvas)

    connect(to_draw[2+32 + 8], to_draw[5 + 16], canvas)
    connect(to_draw[3+32 + 8], to_draw[6 + 16], canvas)

    connect(to_draw[2+32 + 8], to_draw[7 + 16], canvas)
    connect(to_draw[3+32 + 8], to_draw[8 + 16], canvas)

    connect(to_draw[2+32 + 8], to_draw[3 + 8], canvas)
    connect(to_draw[3+32 + 8], to_draw[4 + 8], canvas)

    connect(to_draw[4+32 + 8], to_draw[3 + 8], canvas)
    connect(to_draw[5+32 + 8], to_draw[4 + 8], canvas)

    connect(to_draw[4+32 + 8], to_draw[7+16], canvas)
    connect(to_draw[5+32 + 8], to_draw[8+16], canvas)

    connect(to_draw[4+32 + 8], to_draw[9+16], canvas)
    connect(to_draw[5+32 + 8], to_draw[10+16], canvas)

    connect(to_draw[4+32 + 8], to_draw[5 + 8], canvas)
    connect(to_draw[5+32 + 8], to_draw[6 + 8], canvas)

    connect(to_draw[6+32 + 8], to_draw[5 + 8], canvas)
    connect(to_draw[7+32 + 8], to_draw[6 + 8], canvas)

    connect(to_draw[6+32 + 8], to_draw[7 + 8], canvas)
    connect(to_draw[7+32 + 8], to_draw[7 + 8], canvas)

    connect(to_draw[6+32 + 8], to_draw[11+16], canvas)
    connect(to_draw[7+32 + 8], to_draw[12+16], canvas)

    connect(to_draw[6+32 + 8], to_draw[13+16], canvas)
    connect(to_draw[7+32 + 8], to_draw[14+16], canvas)

    for point in to_draw:
        #point.draw(canvas)
        point.rotate(rotationX @ rotationY)

    root.update()
    canvas.delete('all')
    sleep(0.01)
