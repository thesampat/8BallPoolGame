from math import *
from tkinter import Canvas as C

import CueStick.AxisLine as CX
from CueStick import AxisLine
from CueStick import CueStickS as CC

Opp = None
Adj = None
Hyp = None
X = 555
Y = 286
# Stick Attributes
CCanvas = C
isMoving = True


def mouse(event):
    if isMoving is not False:
        global X, Y
        X = event.x
        Y = event.y
        # X = 10
        # Y = 160
        move_stick()
        # print(X, Y)


def get_canvas(GCanvas):
    global CCanvas
    CCanvas = GCanvas


def gen_attributes(x, y, x1, y1):
    global Opp, Adj, Hyp
    Opp = x - x1
    Adj = y - y1
    Hyp = sqrt((Opp * Opp) + (Adj * Adj))
    return Hyp


def move_stick():
    CCanvas.delete(CC.Stick)
    CCanvas.delete(AxisLine.Axis)
    CCanvas.delete(AxisLine.cue_circle)
    CCanvas.delete(AxisLine.Ctr_line, AxisLine.Dir_line)
    CC.intStick = False
    CX.intAxis = False
    CC.create_stick(CCanvas)
    AxisLine.create_axis(CCanvas)
