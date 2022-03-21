import Board.Table as BT

UpHole = ''
DownHole = ''
UprightHole = ''
DownrightHole = ''
FirstH, SecondH, ThirdH, FourthH = '', '', '', ''


def draw_holes(canvas):
    global UpHole, DownHole, UprightHole, DownrightHole, FirstH, SecondH, ThirdH, FourthH
    x = BT.Tb_Board_X
    y = BT.Tb_Board_Y
    y2 = BT.Tb_Board_Y2
    x2 = BT.Tb_Board_X2
    UpHole = canvas.create_oval(x+2, y+2, x+32, y+32, fill='black')
    DownHole = canvas.create_oval(x+2, y2-32, x+32, y2-2, fill='black')
    UprightHole = canvas.create_oval(x2-2, y+2, x2-32, y+32, fill='black')
    DownrightHole = canvas.create_oval(x2-32, y2-32, x2-2, y2-2, fill='black')
    FirstH = canvas.coords(UpHole)
    SecondH = canvas.coords(DownHole)
    ThirdH = canvas.coords(UprightHole)
    FourthH = canvas.coords(DownrightHole)


def fall(ballX, bally):
    if FirstH[0] < ballX < FirstH[2] and FirstH[1] < bally < FirstH[3]:
        return True
    if SecondH[0] < ballX < SecondH[2] and SecondH[1] < bally < SecondH[3]:
        return True
    if ThirdH[0] < ballX < ThirdH[2] and ThirdH[1] < bally < ThirdH[3]:
        return True
    if FourthH[0] < ballX < FourthH[2] and FourthH[1] < bally < FourthH[3]:
        return True
    return False
