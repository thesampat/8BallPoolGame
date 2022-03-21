import time as t

import Balls.CueBall as BC
import Balls.Pool_Balls as BB
import Board.Table as BT
import CanvasUpdate as CU
import CueStick

BallMoving = False
is_initialMoving = True
CueBallX = BC.CueBallX
CueBallY = BC.CueBallY
CueBall_Size = BB.Size_of_Ball
CueCtrX = CueBallX + (CueBall_Size / 2)
CueCtrY = CueBallY + (CueBall_Size / 2)
Thread = ''
Overlap = False


def move_balls(canvas, root):
    global CueBallY, CueBallX, BallMoving, CueCtrX, CueCtrY
    # initializers
    Power = CueStick.Meter.power
    ReqHB = 0.015 * Power
    Adj = CueStick.MouseHandler.Adj
    Opp = CueStick.MouseHandler.Opp
    CActHB = CueStick.MouseHandler.Hyp
    PActHB = ''
    Control = ''
    time = 0.0000000001

    # Booleans to control the Scopes
    MoveBalls = False
    moveCue = True
    Double_Collide = False
    self = ''
    Px, Py = [int(0) for x in range(BB.No_of_Balls)], [int(0) for x in range(BB.No_of_Balls)]
    SOpp, SAdj, OOpp, OAdj = [int(x) for x in range(BB.No_of_Balls)], [int(x) for x in range(BB.No_of_Balls)], '', ''
    lastBoundX = ''
    lastBoundY = ''
    lastBoundPX = ''
    lastBoundPY = ''
    MovingBalls = []
    Collided = False
    Cx = ''
    Cy = ''

    # Framework for Handling Balls
    while ReqHB > 0.000:
        BallMoving = True

        # initializing the direction of cueBall
        if MoveBalls is not True:
            # Cx = abs(ReqHB / CActHB) * Opp
            # Cy = abs(ReqHB / CActHB) * Adj
            Cx = 1
            Cy = 1

            # Bound for CueBall
            pos = canvas.coords(BC.CueBall)
            if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
                Cx = -Cx
                Opp = -Opp
                # Ax.Touchball = False
                # Capture last Boundary
                lastBoundX = CueBallX
                lastBoundY = CueBallY
            if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
                Cy = -Cy
                Adj = -Adj
                # Ax.Touchball = False
                # Capture last Boundary
                lastBoundX = CueBallX
                lastBoundY = CueBallY

        if moveCue is True:
            canvas.move(BC.CueBall, Cx, Cy)

        # Update positions of CueBalls
        pos = canvas.coords(BC.CueBall)
        CueBallX = pos[0]
        CueBallY = pos[1]
        CueCtrX = CueBallX + (CueBall_Size / 2)
        CueCtrY = CueBallY + (CueBall_Size / 2)
        Ax = CueStick.AxisLine

        if collide_detection(CueBallX, CueBallY):
            print('test2')
            self = collide_detection(CueBallX, CueBallY)[1]
            print(self, 'test2')
            L = collide_detection(CueBallX, CueBallY)[2]
            if lastBoundX is '':
                lastBoundX = Ax.AxisEndX
                lastBoundY = Ax.AxisEndY
            over_lap(CueBallX, CueBallY, BB.ballX[self], BB.ballY[self], L)
            Collided = True

        # check if ball collided with any
        if Collided:
            MovingBalls.append(self)
            # coordinated calculation for primary ball
            CueStick.MouseHandler.gen_attributes(BB.ballX[self], BB.ballY[self], CueBallX, CueBallY)
            if Double_Collide is False:
                SAdj[self] = CueStick.MouseHandler.Adj
                SOpp[self] = CueStick.MouseHandler.Opp
                PActHB = CueStick.MouseHandler.Hyp

            # Handling secondary ball which are coming indirect form corners
            if Ax.Touchball is False:
                if lastBoundX is '':
                    lastBoundX = Ax.AxisFaceX
                    lastBoundY = Ax.AxisFaceY
                Ax.create_lines(lastBoundX, lastBoundY, BB.ballX[self], BB.ballY[self], CueBallX, CueBallY, False)
                Ax.Touchball = True


            # Coordinate calculation for secondary ball
            CueStick.MouseHandler.gen_attributes(Ax.dir_lineX, Ax.dir_lineY, CueBallX, CueBallY)
            OAdj = CueStick.MouseHandler.Adj
            CActHB = CueStick.MouseHandler.Hyp
            OOpp = CueStick.MouseHandler.Opp
            MoveBalls = True
            # MoveCue = False
            Collided = True

        if MoveBalls:
            for ball in range(BB.No_of_Balls):
                if Double_Collide is False:
                    # for primary ball
                    Px[self] = abs(ReqHB / PActHB) * SOpp[self]
                    Py[self] = abs(ReqHB / PActHB) * SAdj[self]

            # For secondary ball
            Cx = abs(ReqHB / CActHB) * OOpp
            Cy = abs(ReqHB / CActHB) * OAdj

            # move secondary ball after collision
            for i in range(BB.No_of_Balls):
                canvas.move(BB.Pool_[i], Px[i], Py[i])

                ball = canvas.coords(BB.Pool_[i])
                # update primary ball position on arry
                BB.ballX[i] = ball[0]
                BB.ballY[i] = ball[1]

            # Border for PotBalls
            for ball in range(BB.No_of_Balls):
                pos = canvas.coords(BB.Pool_[ball])
                if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
                    Px[ball] = -Px[ball]
                    SOpp[ball] = -SOpp[ball]
                    lastBoundPX = BB.ballX[ball]
                    lastBoundPY = BB.ballY[ball]
                if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
                    Py[ball] = -Py[ball]
                    SAdj[ball] = -SAdj[ball]
                    lastBoundPX = BB.ballX[ball]
                    lastBoundPY = BB.ballY[ball]

            # Border for CueBall
            pos = canvas.coords(BC.CueBall)
            if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
                Cx = -Cx
                OOpp = -OOpp
            if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
                Cy = -Cy
                OAdj = -OAdj

        # ReqHB -= 0.00005
        time = 0.0076  # time += 0.0000001
        t.sleep(time)
        canvas.update()
        CU.reprint(canvas, root, 0, CueStick.CueStickS.Stick)
        Collided = False

    # Redraw components after shot
    CueStick.CueStickS.create_stick(canvas)
    CueStick.MouseHandler.isMoving = True
    CueStick.Meter.meter(canvas)
    CueStick.AxisLine.create_axis(canvas)


# Collision Detection
def collide_detection(CueBallx, CueBallY):
    for i in range(BB.No_of_Balls):
        CueStick.MouseHandler.gen_attributes(CueBallX, CueBallY, BB.ballX[i], BB.ballY[i])
        if CueStick.MouseHandler.Hyp <= 20:
            return True, i, CueStick.MouseHandler.Hyp
    return False


def second_collide(Ballx, BallY, MovingBalls):
    for items in MovingBalls:
        for j in range(BB.No_of_Balls):
            if Ballx[items] is Ballx[j] or BallY[items] is BallY[j]:
                continue
            CueStick.MouseHandler.gen_attributes(Ballx[items], BallY[items], Ballx[j], BallY[j])
            if CueStick.MouseHandler.Hyp <= 20:
                return True, items, j, CueStick.MouseHandler.Hyp
    return False


def over_lap(bx, by, b1x, b1y, length):
    # check Overlap side
    CueStick.MouseHandler.gen_attributes(bx, by, b1x, b1y)
    Adj = CueStick.MouseHandler.Adj
    Opp = CueStick.MouseHandler.Opp
    Hyp = CueStick.MouseHandler.Hyp
    length = 20 - abs(length)
    b1x = b1x - abs(length / Hyp) * Opp
    b1y = b1y - abs(length / Hyp) * Adj
    return b1x, b1y
