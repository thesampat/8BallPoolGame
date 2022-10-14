# attributes for moving Table
Tb_Width = 740
Tb_Height =340 #250
Tb_PosX = 25
Tb_PosY = 25

# table arc Attributes
a1x, a1y = Tb_PosX, Tb_PosY
a2x, a2y = Tb_Width, Tb_PosY
a3x, a3y = Tb_PosX, Tb_Height
a4x, a4y = Tb_Width, Tb_Height

# Table_Tb_Board Attributes
Tb_Board_X = a1x + 30
Tb_Board_Y = a1y + 30
Tb_Board_X2 = a2x + 30
Tb_Board_Y2 = a3y + 30
Tb_Board_Length = Tb_Board_X2 - Tb_Board_X
Tb_Board_Breadth = Tb_Board_Y2 - Tb_Board_Y
Tb_Board_color = 'blue'

def draw_table(canvas):
    # corner of upper left and right
    canvas.create_arc(a1x, a1y, a1x + 60, a1y + 60, start=90, fill='white', )
    canvas.create_arc(a2x, a2y, a2x + 60, a2y + 60, fill='white')
    # corner of lower left and right
    canvas.create_arc(a3x, a3y, a3x + 60, a3y + 60, start=180, fill='white')
    canvas.create_arc(a4x, a4y, a4x + 60, a4y + 60, start=270, fill='white')
    # long of upper and lower
    canvas.create_rectangle(a1x + 30, a1y, a2x + 30, a1y + 30, fill='white')
    canvas.create_rectangle(a1x + 30, a3y + 30, a2x + 30, a3y + 60, fill='white')
    # side of left and right
    canvas.create_rectangle(a1x, a1y + 30, a1x + 30, a3y + 30, fill='white')
    canvas.create_rectangle(a2x + 30, a1y + 30, a2x + 60, a3y + 30, fill='white')
    # main_Tb_Board
    canvas.create_rectangle(a1x + 30, a1y + 30, a2x + 30, a3y + 30, fill=Tb_Board_color)











