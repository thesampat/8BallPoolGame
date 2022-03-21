from Balls import Move_Balls, Pool_Balls
from Board import Table
from CueStick import MouseHandler as mouse

ctr_ofBallX = Move_Balls.CueBallX + (Move_Balls.CueBall_Size * 0.5)
ctr_ofBallY = Move_Balls.CueBallY + (Move_Balls.CueBall_Size * 0.5)
AxisFaceX = Move_Balls.CueCtrX + 10
AxisFaceY = Move_Balls.CueCtrY + 10
AxisEndX = 2000
AxisEndY = AxisFaceY

AxisLength = 2000
Axis = ''
CtrBall = 0
cue_circle = ''
intAxis = True
ReqCut = ''
Touchball = False
lineX = ''
lineY = ''
Ctr_line = ''
collide = ''
dir_lineY, dir_lineX = '', ''
Dir_line = ''
BallX = ''
Bally = ''
CueMove = True


# Control = ''


def catch_ball():
    global AxisEndX, AxisEndY, ReqCut, lineX, lineY, collide, dir_lineY, dir_lineX, Bally, BallX, Touchball
    Targets = {}
    for i in range(Pool_Balls.No_of_Balls):
        BallX = Pool_Balls.ballX[i]
        Bally = Pool_Balls.ballY[i]
        BallX2, Bally2 = BallX, Bally
        mouse.gen_attributes(Move_Balls.CueCtrX, Move_Balls.CueCtrY, BallX2 + 10, Bally2 + 10)
        RHB = mouse.Hyp
        Control = -mouse.Opp
        mouse.gen_attributes(Move_Balls.CueCtrX, Move_Balls.CueCtrY, AxisEndX, AxisEndY)
        AHB = mouse.Hyp
        X = Move_Balls.CueCtrX - abs(RHB / AHB) * mouse.Opp
        Y = Move_Balls.CueCtrY - abs(RHB / AHB) * mouse.Adj

        if Bally - 9 <= Y <= Bally + 29 and BallX - 9 <= X <= BallX + 29:
            Targets.update({RHB: i})
            Touchball = True
            collide = True

        if len(Targets.keys()) > 0:
            selected = Targets.get(sorted(Targets.keys())[0])
            BallX = Pool_Balls.ballX[selected]
            Bally = Pool_Balls.ballY[selected]

        if Bally - 9 <= Y <= Bally + 29 and BallX - 9 <= X <= BallX + 29:
            X = Move_Balls.CueCtrX - abs((RHB - 20) / AHB) * mouse.Opp
            Y = Move_Balls.CueCtrY - abs((RHB - 20) / AHB) * mouse.Adj
            AxisEndX = X
            AxisEndY = Y
            mouse.gen_attributes(Move_Balls.CueCtrX, Move_Balls.CueCtrY, BallX2 + 10, Bally2 + 10)

            # Reduce the gap between Balls
            mouse.gen_attributes(X, Y, BallX + 10, Bally + 10)
            Gapx = ((mouse.Hyp - 20) / mouse.Hyp) * mouse.Opp
            Gapy = ((mouse.Hyp - 20) / mouse.Hyp) * mouse.Adj
            AxisEndX -= Gapx
            AxisEndY -= Gapy

        create_lines(Move_Balls.CueCtrX, Move_Balls.CueCtrY, BallX + 10, Bally + 10, AxisEndX, AxisEndY, True)


def create_lines(p1x, p1y, p2x, p2y, p3x, p3y, Straight):
    global lineX, lineY, dir_lineX, dir_lineY, CueMove
    mouse.gen_attributes(p1x, p1y, p2x, p2y)
    PointX = p2x + abs((mouse.Hyp - (mouse.Hyp - 20)) / mouse.Hyp) * mouse.Opp
    PointY = p2y + abs((mouse.Hyp - (mouse.Hyp - 20)) / mouse.Hyp) * mouse.Adj

    # Mechanism for direction lines
    mouse.gen_attributes(p3x, p3y, p2x, p2y)
    lineX = p3x - (50 / mouse.Hyp) * mouse.Opp
    lineY = p3y - (50 / mouse.Hyp) * mouse.Adj

    mouse.gen_attributes(p3x, p3y, PointX, PointY)
    RegX = mouse.Opp
    RegY = mouse.Adj

    mouse.gen_attributes(lineX, p2y, p2x, lineY)
    dir_lineX = p3x + abs(50 / mouse.Hyp) * abs(mouse.Adj) * (RegX/abs(RegX))
    dir_lineY = p3y + abs(50 / mouse.Hyp) * abs(mouse.Opp) * (RegY/abs(RegY))

    # Disappearing the direction lines if axis line is straight
    mouse.gen_attributes(PointX, PointY, AxisEndX, AxisEndY)
    if int(mouse.Hyp) is 0:
        dir_lineX = lineX
        dir_lineY = lineY
        CueMove = False
    CueMove = True
    # print(p3x, p3y, dir_lineX, dir_lineY, 'Check')


def create_axis(canvas):
    global Axis, AxisEndX, AxisEndY, cue_circle, collide, Ctr_line, Dir_line
    # initializing axis
    mouse.gen_attributes(Move_Balls.CueCtrX, Move_Balls.CueCtrY, mouse.X, mouse.Y)
    if intAxis is False:
        AxisEndX = Move_Balls.CueCtrX + ((AxisLength / mouse.Hyp) * mouse.Opp)
        AxisEndY = Move_Balls.CueCtrY + ((AxisLength / mouse.Hyp) * mouse.Adj)
    corner_collision()
    Axis = canvas.create_line(Move_Balls.CueCtrX, Move_Balls.CueCtrY, AxisEndX, AxisEndY, fill='black', width=1)
    cue_circle = canvas.create_oval(AxisEndX - 10, AxisEndY - 10, AxisEndX + 10, AxisEndY + 10)

    if collide is True:
        Ctr_line = canvas.create_line(AxisEndX, AxisEndY, lineX, lineY, fill='black')
        Dir_line = canvas.create_line(AxisEndX, AxisEndY, dir_lineX, dir_lineY, fill='black')

    collide = False


def get_corner():
    def getx():
        if AxisEndX < Table.Tb_Board_X + 10:  # LEFT SIDE
            return Table.Tb_Board_X + 10
        if AxisEndX > Table.Tb_Board_X2:  # RIGHT SIDE
            return Table.Tb_Board_X2 - 10
        else:
            return abs(AxisEndX)

    def gety():
        if AxisEndY < Table.Tb_Board_Y + 10:  # UP SIDE
            return Table.Tb_Board_Y + 10
        if AxisEndY > Table.Tb_Board_Y2 - 10:  # DOWN SIDE
            return Table.Tb_Board_Y2 - 10
        else:
            return int(abs(AxisEndY))

    return getx(), gety()


def corner_collision():
    global AxisEndX, AxisEndY, Touchball
    catch_ball()
    mouse.gen_attributes(AxisEndX, AxisEndY, Move_Balls.CueCtrX, Move_Balls.CueCtrY)
    ReqHB = Move_Balls.CueCtrX - get_corner()[0]
    ActHB = mouse.Opp
    cal(ReqHB, ActHB)
    if check_corner(AxisEndX, AxisEndY) is True:
        Touchball = False
        ReqHB = Move_Balls.CueCtrY - get_corner()[1]
        ActHB = mouse.Adj
        cal(ReqHB, ActHB)


def cal(ReqHB=None, ActHB=None):
    global AxisEndX, AxisEndY
    AxisEndX = Move_Balls.CueCtrX + abs(ReqHB / ActHB) * mouse.Opp
    AxisEndY = Move_Balls.CueCtrY + abs(ReqHB / ActHB) * mouse.Adj


def check_corner(AxisX, AxisY):
    if AxisX < 55 or AxisX > Table.Tb_Board_X2 or AxisY <= Table.Tb_Board_Y + 10 or AxisY > Table.Tb_Board_Y2 - 10:
        return True
    else:
        return False
