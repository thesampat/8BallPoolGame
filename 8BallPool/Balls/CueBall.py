import Board.Table as BT
import Balls.Pool_Balls as BB

# cueBall attributes
CueBallX = BT.Tb_Board_X+140
CueBallY = BT.Tb_Board_Y + 1#(BT.Tb_Board_Breadth / 2)
CueBall_Size = BB.Size_of_Ball
CueCtrX = CueBallX + (CueBall_Size / 2)
CueCtrY = CueBallY + (CueBall_Size / 2)
CueBall = ''


def cue_ball(canvas):
    global Thread, CueBall, CueBallX, CueBallY
    CueBall = canvas.create_oval(CueBallX, CueBallY, CueBallX + CueBall_Size, CueBallY + CueBall_Size, fill='White')


