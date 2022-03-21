from CueStick import MouseHandler as Mouse
from Balls import Move_Balls as CueB

Stick = ''
dist = 13
Cue_StickLength = 150
Cue_StickBreadth = 5
Cue_StickFaceX = CueB.CueBallX - 1
Cue_StickFaceY = CueB.CueBallY + (CueB.CueBall_Size / 2)
Cue_StickTaleX = Cue_StickFaceX - Cue_StickLength
Cue_StickTaleY = CueB.CueBallY + (CueB.CueBall_Size / 2)
intStick = True


def create_stick(canvas):
    global Cue_StickFaceX, Cue_StickFaceY, Cue_StickTaleX, Cue_StickTaleY, Stick
    canvas.delete(Stick)
    if intStick is False:
        Mouse.gen_attributes(CueB.CueCtrX, CueB.CueCtrY, Mouse.X, Mouse.Y)
        Cue_StickFaceX = CueB.CueCtrX - ((dist / Mouse.Hyp) * Mouse.Opp)
        Cue_StickFaceY = CueB.CueCtrY - ((dist / Mouse.Hyp) * Mouse.Adj)
        Cue_StickTaleX = Cue_StickFaceX - ((Cue_StickLength / Mouse.Hyp) * Mouse.Opp)
        Cue_StickTaleY = Cue_StickFaceY - ((Cue_StickLength / Mouse.Hyp) * Mouse.Adj)
    Stick = canvas.create_line(Cue_StickFaceX, Cue_StickFaceY, Cue_StickTaleX, Cue_StickTaleY, fill='#FF0A10',
                               width=Cue_StickBreadth)
