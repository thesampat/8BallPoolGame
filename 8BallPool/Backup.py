import time as t

import Balls.CueBall as BC
import Balls.Pool_Balls as BB
import Board.Potholes as Hole
import Board.Table as BT
import CanvasUpdate as CU
import CueStick as mouse


BallMoving = False
is_initialMoving = True
CueBallX = BC.CueBallX
CueBallY = BC.CueBallY
CueBall_Size = BB.Size_of_Ball
CueCtrX = CueBallX + (CueBall_Size / 2)
CueCtrY = CueBallY + (CueBall_Size / 2)
Thread = ''


def move_balls(canvas, root):
    global CueBallY, CueBallX, BallMoving, CueCtrX, CueCtrY
    # initializers
    Power = mouse.Meter.power
    ReqHB = 0.015 * Power
    Adj = mouse.MouseHandler.Adj
    Opp = mouse.MouseHandler.Opp
    CActHB = mouse.MouseHandler.Hyp
    PActHB = ''
    time = 0.0000000001

    # Booleans to control the Scopes
    MoveBalls = False
    moveCue = True
    Double_Collide = False
    self = ''
    Px, Py = [int(0) for x in range(BB.No_of_Balls)], [int(0) for x in range(BB.No_of_Balls)]
    SOpp, SAdj, OOpp, OAdj = [int(0) for x in range(BB.No_of_Balls)], [int(0) for x in range(BB.No_of_Balls)], '', ''
    lastBoundX = ''
    lastBoundY = ''
    lastBoundPX = ''
    lastBoundPY = ''

    # Framework for Handling Balls
    while ReqHB > 0.000:
        BallMoving = True

        # initializing the direction of cueBall
        if MoveBalls is not True:
            Cx = abs(ReqHB / CActHB) * Opp
            Cy = abs(ReqHB / CActHB) * Adj

            # Bound for CueBall
            pos = canvas.coords(BC.CueBall)
            if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
                Cx = -Cx
                Opp = -Opp
                # Capture last Boundary
                lastBoundX = CueBallX
                lastBoundY = CueBallY
            if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
                Cy = -Cy
                Adj = -Adj
                # Touchball = False
                # Capture last Boundary
                lastBoundX = CueBallX
                lastBoundY = CueBallY

        if moveCue is True:
            canvas.move(BC.CueBall, Cx, Cy)

        # Update positions of CueBalls
        pos = canvas.coords(BC.CueBall)
        CueBallX = pos[0]
        CueBallY = pos[1]
        # Hole.fall(CueBallX, CueBallY)
        CueCtrX = CueBallX + (CueBall_Size / 2)
        CueCtrY = CueBallY + (CueBall_Size / 2)

        # check if ball collided with any
        if collide_detection(CueBallX, CueBallY, BB.ballX, BB.ballY):
            self = collide_detection(CueBallX, CueBallY, BB.ballX, BB.ballY)[1]
            mouse.MouseHandler.gen_attributes(BB.ballX[self], BB.ballY[self], CueBallX, CueBallY)
            if Double_Collide is False:
                SAdj[self] = mouse.MouseHandler.Adj
                SOpp[self] = mouse.MouseHandler.Opp
                Ax = mouse.AxisLine
                Ctr = mouse.MouseHandler.Adj
                PActHB = mouse.MouseHandler.Hyp
            print(Ax.Touchball)
            if Ax.Touchball is False:
                print('redirect')
                if lastBoundY is '':
                    lastBoundX = Ax.AxisEndX
                    lastBoundY = Ax.AxisEndY
                mouse.MouseHandler.gen_attributes(lastBoundX, lastBoundY, BB.ballX[self], BB.ballY[self])
                Control = mouse.MouseHandler.Opp
                if int(lastBoundY) <= BT.Tb_Board_Y or int(lastBoundY) >= BT.Tb_Board_Y2:
                    Control = -mouse.MouseHandler.Adj
                mouse.AxisLine.create_lines(lastBoundX, lastBoundY, BB.ballX[self], BB.ballY[self], CueBallX, CueBallY, Control, False)
                Ax.Touchball = False
                # return

            mouse.MouseHandler.gen_attributes(Ax.dir_lineX, Ax.dir_lineY, CueBallX, CueBallY)
            OAdj = mouse.MouseHandler.Adj
            CActHB = mouse.MouseHandler.Hyp
            OOpp = mouse.MouseHandler.Opp
            MoveBalls = True
            MoveCue = False

        if MoveBalls:
            if Double_Collide is False:
                Px[self] = abs(ReqHB/PActHB) * SOpp[self]
                Py[self] = abs(ReqHB/PActHB) * SAdj[self]

            # For opposite Ball
            Cx = abs(ReqHB / CActHB) * OOpp
            Cy = abs(ReqHB / CActHB) * OAdj

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

            # # Second level collide detection
            # if collide_detection(BB.ballX[self], BB.ballY[self], BB.ballX, BB.ballY):
            #     # print('SecondCollideDetection')
            #     self2 = collide_detection(BB.ballX[self], BB.ballY[self], BB.ballX, BB.ballY)[1]
            #     mouse.Mouse.gen_attributes(BB.ballX[self2], BB.ballY[self2], BB.ballX[self], BB.ballY[self])
            #     SAdj[self2] = mouse.Mouse.Adj
            #     SOpp[self2] = mouse.Mouse.Opp
            #     Px[self2] = abs(ReqHB / PActHB) * SOpp[self2]
            #     Py[self2] = abs(ReqHB / PActHB) * SAdj[self2]
            #
            #     if lastBoundY is '':
            #         lastBoundPX = Ax.AxisEndX
            #         lastBoundPY = Ax.AxisEndY
            #     mouse.Mouse.gen_attributes(BB.ballX[self], BB.ballY[self], lastBoundPX, lastBoundPY)
            #     Control = mouse.Mouse.Opp + mouse.Mouse.Adj
            #     # if int(lastBoundPY) is 54 or 350:
            #     #     Control = mouse.Mouse.Opp - mouse.Mouse.Adj
            #     mouse.AxisLine.create_lines(BB.ballX[self], BB.ballY[self], BB.ballX[self2], BB.ballY[self2],
            #                                 BB.ballX[self], BB.ballY[self], Control, False)
            #     mouse.Mouse.gen_attributes(Ax.dir_lineX, Ax.dir_lineY, BB.ballX[self], BB.ballY[self])
            #     Adj = mouse.Mouse.Adj
            #     Opp = mouse.Mouse.Opp
            #     CActHB = mouse.Mouse.Hyp
            #     Px[self] = abs(ReqHB / CActHB) * Opp
            #     Py[self] = abs(ReqHB / CActHB) * Adj
                # Double_Collide = True

            # Assign ball attributes to PotBall
            for ball in range(BB.No_of_Balls):
                canvas.move(BB.Pool_[ball], Px[ball], Py[ball])
                BB.ballX[ball] += Px[ball]
                BB.ballY[ball] += Py[ball]

                if mouse.MouseHandler.AxisLine.CueMove is False:
                    moveCue = False
                # Trapping Balls on Holes
                # if Hole.fall(BB.ballX[ball], BB.ballY[ball]):
                #     canvas.delete(BB.Pool_[ball])
                #     BB.No_of_Balls -= 1
                #     BB.Pool_.pop(ball)
                #     Px.pop(ball)
                #     Py.pop(ball)
                #     BB.ballX.pop(ball)
                #     BB.ballY.pop(ball)
                #     break
                # print(BB.Pool_, Px, Py)

        # ReqHB -= 0.00005
        time += 0.0000001
        t.sleep(time)
        canvas.update()
        CU.reprint(canvas, root, 0, mouse.CueStickS.Stick)

    # Redraw components after shot
    mouse.CueStickS.create_stick(canvas)
    mouse.MouseHandler.isMoving = True
    mouse.Meter.meter(canvas)
    mouse.AxisLine.create_axis(canvas)


# Collision Detection
def collide_detection(Ball1x, Ball1y, Ball2x, Ball2y):
    for i in range(BB.No_of_Balls):
        if Ball1x is Ball2x[i] and Ball1y is Ball2y[i]:
            continue
        mouse.MouseHandler.gen_attributes(Ball1x, Ball1y, Ball2x[i], Ball2y[i])
        if mouse.MouseHandler.Hyp <= 20:
            return True, i
    return False


# Calculate the direction and Velocity of Balls
def get_matrix(SelfX, SelfY, otherX, otherY, ReqHB):
    pass




import time as t

import Balls.CueBall as BC
import Balls.Pool_Balls as BB
import Board.Potholes as Hole
import Board.Table as BT
import CanvasUpdate as CU
import CueStick as mouse


BallMoving = False
is_initialMoving = True
CueBallX = BC.CueBallX
CueBallY = BC.CueBallY
CueBall_Size = BB.Size_of_Ball
CueCtrX = CueBallX + (CueBall_Size / 2)
CueCtrY = CueBallY + (CueBall_Size / 2)
Thread = ''


def move_balls(canvas, root):
    global CueBallY, CueBallX, BallMoving, CueCtrX, CueCtrY
    # initializers
    Power = mouse.Meter.power
    ReqHB = 0.015 * Power
    Adj = mouse.MouseHandler.Adj
    Opp = mouse.MouseHandler.Opp
    CActHB = mouse.MouseHandler.Hyp
    PActHB = ''
    time = 0.0000000001

    # Booleans to control the Scopes
    MoveBalls = False
    moveCue = True
    Double_Collide = False
    self = ''
    Px, Py = [int(0) for x in range(BB.No_of_Balls)], [int(0) for x in range(BB.No_of_Balls)]
    SOpp, SAdj, OOpp, OAdj = [int(0) for x in range(BB.No_of_Balls)], [int(0) for x in range(BB.No_of_Balls)], '', ''
    lastBoundX = ''
    lastBoundY = ''
    lastBoundPX = ''
    lastBoundPY = ''
    Px = []
    Py = []
    Px.append(0.6)
    Py.append(0.6)
    Px.append(0.8)
    Py.append(0.7)
    Px.append(0.5)
    Py.append(0.7)
    target = ''
    # Framework for Handling Balls
    while ReqHB > 0.000:
        BallMoving = True

        # # initializing the direction of cueBall
        # if MoveBalls is not True:
        #     Cx = 1#abs(ReqHB / CActHB) * Opp
        #     Cy = 0.4#abs(ReqHB / CActHB) * Adj
        #     Bound for CueBall
        #     pos = canvas.coords(BC.CueBall)
        #     if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
        #         Cx = -Cx
        #         Opp = -Opp
        #         # Capture last Boundary
        #         lastBoundX = CueBallX
        #         lastBoundY = CueBallY
        #     if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
        #         Cy = -Cy
        #         Adj = -Adj
        #         Touchball = False
        #         # Capture last Boundary
        #         lastBoundX = CueBallX
        #         lastBoundY = CueBallY

        # if moveCue is True:
        #     canvas.move(BC.CueBall, Cx, Cy)

        # Update positions of CueBalls
        # pos = canvas.coords(BC.CueBall)
        # CueBallX = pos[0]
        # CueBallY = pos[1]
        # # Hole.fall(CueBallX, CueBallY)
        # CueCtrX = CueBallX + (CueBall_Size / 2)
        # CueCtrY = CueBallY + (CueBall_Size / 2)

        # check if ball collided with any
        # if collide_detection(CueBallX, CueBallY, BB.ballX, BB.ballY):
        #     self = collide_detection(CueBallX, CueBallY, BB.ballX, BB.ballY)[1]
        #     mouse.Mouse.gen_attributes(BB.ballX[self], BB.ballY[self], CueBallX, CueBallY)
        #     if Double_Collide is False:
        #         SAdj[self] = mouse.Mouse.Adj
        #         SOpp[self] = mouse.Mouse.Opp
        #         Ax = mouse.AxisLine
        #         Ctr = mouse.Mouse.Adj
        #         PActHB = mouse.Mouse.Hyp
        #     print(Ax.Touchball)
        #     if Ax.Touchball is False:
        #         print('redirect')
        #         if lastBoundY is '':
        #             lastBoundX = Ax.AxisEndX
        #             lastBoundY = Ax.AxisEndY
        #         mouse.Mouse.gen_attributes(lastBoundX, lastBoundY, BB.ballX[self], BB.ballY[self])
        #         Control = mouse.Mouse.Opp
        #         if int(lastBoundY) <= BT.Tb_Board_Y or int(lastBoundY) >= BT.Tb_Board_Y2:
        #             Control = -mouse.Mouse.Adj
        #         mouse.AxisLine.create_lines(lastBoundX, lastBoundY, BB.ballX[self], BB.ballY[self], CueBallX, CueBallY, Control, False)
        #         Ax.Touchball = False
        #         # return
        #
        #     mouse.Mouse.gen_attributes(Ax.dir_lineX, Ax.dir_lineY, CueBallX, CueBallY)
        #     OAdj = mouse.Mouse.Adj
        #     CActHB = mouse.Mouse.Hyp
        #     OOpp = mouse.Mouse.Opp
        #     MoveBalls = True
        #     MoveCue = False
        #
        # if MoveBalls:
            # if Double_Collide is False:
        for ball in range(BB.No_of_Balls):
            Px[ball] = abs(Px[ball]/PActHB) * SOpp[ball]
            Py[ball] = abs(Py[ball]/PActHB) * SAdj[ball]
        #
        #     # For opposite Ball
        #     Cx = abs(ReqHB / CActHB) * OOpp
        #     Cy = abs(ReqHB / CActHB) * OAdj
        #
        #     # Border for PotBalls
        for ball in range(BB.No_of_Balls):
            pos = canvas.coords(BB.Pool_[ball])
            if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
                Px[ball] = -Px[ball]
                SOpp[ball] = -SOpp[ball]
                # lastBoundPX = BB.ballX[ball]
                # lastBoundPY = BB.ballY[ball]
            # if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
                Py[ball] = -Py[ball]
                SAdj[ball] = -SAdj[ball]
                # lastBoundPX = BB.ballX[ball]
                # lastBoundPY = BB.ballY[ball]
        # #
        #     # Border for CueBall
        #     pos = canvas.coords(BC.CueBall)
        #     if pos[2] >= BT.Tb_Board_X2 or pos[0] <= BT.Tb_Board_X:
        #         Cx = -Cx
        #         OOpp = -OOpp
        #     if pos[3] >= BT.Tb_Board_Y2 or pos[1] <= BT.Tb_Board_Y:
        #         Cy = -Cy
        #         OAdj = -OAdj
        #
        #     # # Second level collide detection
        if collide_detection(BB.ballX, BB.ballY):
            self2 = collide_detection(BB.ballX, BB.ballY)[1]
            self = collide_detection(BB.ballX, BB.ballY)[2]
            # self2 = collide_detection(BB.ballX[self], BB.ballY[self], BB.ballX, BB.ballY)[1]
            mouse.MouseHandler.gen_attributes(BB.ballX[self2], BB.ballY[self], BB.ballX[self], BB.ballY[self])
            SAdj[self2] = mouse.MouseHandler.Adj
            SOpp[self2] = mouse.MouseHandler.Opp
            PActHB = mouse.MouseHandler.Hyp
            Px[self2] = abs(ReqHB / PActHB) * SOpp[self2]
            Py[self2] = abs(ReqHB / PActHB) * SAdj[self2]


        #     #
        #     #     if lastBoundY is '':
        #     #         lastBoundPX = Ax.AxisEndX
        #     #         lastBoundPY = Ax.AxisEndY
        #     #     mouse.Mouse.gen_attributes(BB.ballX[self], BB.ballY[self], lastBoundPX, lastBoundPY)
        #     #     Control = mouse.Mouse.Opp + mouse.Mouse.Adj
        #     #     # if int(lastBoundPY) is 54 or 350:
        #     #     #     Control = mouse.Mouse.Opp - mouse.Mouse.Adj
        #     #     mouse.AxisLine.create_lines(BB.ballX[self], BB.ballY[self], BB.ballX[self2], BB.ballY[self2],
        #     #                                 BB.ballX[self], BB.ballY[self], Control, False)
        #     #     mouse.Mouse.gen_attributes(Ax.dir_lineX, Ax.dir_lineY, BB.ballX[self], BB.ballY[self])
        #     #     Adj = mouse.Mouse.Adj
        #     #     Opp = mouse.Mouse.Opp
        #     #     CActHB = mouse.Mouse.Hyp
        #     #     Px[self] = abs(ReqHB / CActHB) * Opp
        #     #     Py[self] = abs(ReqHB / CActHB) * Adj
        #         # Double_Collide = True
        #
        #     # Assign ball attributes to PotBall
        for ball in range(BB.No_of_Balls):
            canvas.move(BB.Pool_[ball], Px[ball], Py[ball])
            BB.ballX[ball] += Px[ball]
            BB.ballY[ball] += Py[ball]
            # print(BB.ballY[ball], BB.ballX[ball])
        #
        #         if mouse.Mouse.AxisLine.CueMove is False:
        #             moveCue = False
        #         # Trapping Balls on Holes
        #         # if Hole.fall(BB.ballX[ball], BB.ballY[ball]):
        #         #     canvas.delete(BB.Pool_[ball])
        #         #     BB.No_of_Balls -= 1
        #         #     BB.Pool_.pop(ball)
        #         #     Px.pop(ball)
        #         #     Py.pop(ball)
        #         #     BB.ballX.pop(ball)
        #         #     BB.ballY.pop(ball)
        #         #     break
        #         # print(BB.Pool_, Px, Py)

        # ReqHB -= 0.00005
        time = 0.0029
        t.sleep(time)
        canvas.update()
        CU.reprint(canvas, root, 0, mouse.CueStickS.Stick)

    # Redraw components after shot
    mouse.CueStickS.create_stick(canvas)
    mouse.MouseHandler.isMoving = True
    mouse.Meter.meter(canvas)
    mouse.AxisLine.create_axis(canvas)


# Collision Detection
def collide_detection(Ballx, Bally):
    for i in range(BB.No_of_Balls):
        for j in range(BB.No_of_Balls):
            if Ballx[i] is Ballx[j] and Bally[i] is Bally[j]:
                continue
            mouse.MouseHandler.gen_attributes(Ballx[i], Bally[i], Ballx[j], Bally[j])
        if mouse.MouseHandler.Hyp <= 20:
            return True, i, j
    return False


# Calculate the direction and Velocity of Balls
def get_matrix(SelfX, SelfY, otherX, otherY, ReqHB):
    pass
