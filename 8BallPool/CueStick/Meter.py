import threading as thr

import Board.Table as BT
import CanvasUpdate as CU

Y = BT.Tb_Board_Y
thread = thr.Thread
M_pin = ''
power = 1
isPulled = True


def meter(canvas):
    global M_pin
    canvas.delete(M_pin)
    meterWidth = BT.Tb_Board_X2 + 70
    canvas.create_rectangle(BT.Tb_Board_X2 + 50, BT.Tb_Board_Y, meterWidth, BT.Tb_Board_Y2, fill='white')
    M_pin = canvas.create_rectangle(BT.Tb_Board_X2 + 35, BT.Tb_Board_Y + 1, BT.Tb_Board_X2 + 85, BT.Tb_Board_Y + 10,
                                    fill='red')


def create_ned(canvas, root, y=Y):
    global power, isPulled, move
    power = 1
    y = 1
    power_value = 0.328
    while isPulled is True:
        pos = canvas.coords(M_pin)
        if pos[1] + 10 == BT.Tb_Board_Y2 or pos[1] == BT.Tb_Board_Y:
            y = -y
            power_value = -power_value
        power += power_value

        canvas.move(M_pin, 0, y)
        CU.reprint(canvas, root, 3)
