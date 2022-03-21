from tkinter import *
import Board.Table as BT
import Balls.Pool_Balls as BB
import Balls.CueBall as BC
import CueStick.MouseHandler as mouse
import Board.Potholes as BP
import CueStick.Meter as meter
import CueStick.CueStickS as cs
import CueStick.AxisLine as CX
import threading as thread
import CanvasUpdate as cu
import Balls.Move_Balls as BM

# Main root window
root = Tk()
root.geometry('900x450+150-0')

# canvas
canvas = Canvas(root)
canvas.config(bg='black', width='900', height='450')
canvas.place(x=0, y=0)

# init_Table
BT.draw_table(canvas)
BP.draw_holes(canvas)
mouse.get_canvas(canvas)
meter.meter(canvas)

''' init_Balls '''
# for PoolBalls
BB.ball_pos()
BB.create_balls(canvas)
# for CueBalls
BC.cue_ball(canvas)

count = 1


def move(event):
    global count
    count += 1
    mouse.isMoving = False
    meter.isPulled = True
    print('hitt')
    if count == 3:
        meter.isPulled = False
        print('run')
        # programme to move Ball when stick is hitted
        BC.BallMoving = True
        cu.destroy(canvas, CX.Axis, CX.cue_circle, CX.Ctr_line, CX.Dir_line)
        RunCue = thread.Thread(BM.move_balls(canvas, root))
        RunCue.start()
    meter.create_ned(canvas, root)
    count = 1
    return

# for CueStick
cs.create_stick(canvas)
CX.create_axis(canvas)
canvas.bind('<Motion>', mouse.mouse)
root.bind('<space>', move)

root.mainloop()
