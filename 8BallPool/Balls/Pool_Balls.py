# Creating Balls
import Board.Table as BT

No_of_Balls = 1
Size_of_Ball = 20
ballX = []
ballY = []
ball_color = []
Pool_ = [int(x) for x in range(No_of_Balls+1)]


def ball_pos():
    dis_x = BT.Tb_Board_X
    dis_Y = BT.Tb_Board_Y

    ballX.append(dis_x+150)
    ballX.append(dis_x+380)
    ballX.append(dis_x+150)
    # ballX.append(dis_x+280)
    # ballX.append(dis_x+540)
    # ballX.append(dis_x+540)

    ballY.append(dis_Y+200)
    ballY.append(dis_Y+152)
    ballY.append(dis_Y+145)
    # ballY.append(dis_Y+160)
    # ballY.append(dis_Y+150)
    # ballY.append(dis_Y+130)

    # color_of_balls
    ball_color.append('Red')
    ball_color.append('yellow')
    ball_color.append('black')
    # ball_color.append('green')
    # ball_color.append('orange')
    # ball_color.append('purple')
    # ball_color.append('cyan')
    # ball_color.append('white')
    # ball_color.append('pink')
    # ball_color.append('grey')

    # for balls in range(No_of_Balls):
    #     ballX.append(dis_x)
    #     ballY.append(dis_Y)
    #     dis_x += 400

    #     dis_Y += 1


def create_balls(canvas):
    global Pool_
    for ball in range(No_of_Balls):
        Pool_[ball] = canvas.create_oval(ballX[ball], ballY[ball], ballX[ball] + Size_of_Ball, ballY[ball] + Size_of_Ball, fill=ball_color[ball])
        # Pool_[1] = canvas.create_oval(ballX[1], ballY[1], ballX[1] + Size_of_Ball, ballY[1] + Size_of_Ball, fill=ball_color[1])
        # Pool_[2] = canvas.create_oval(ballX[2], ballY[2], ballX[2] + Size_of_Ball, ballY[2] + Size_of_Ball, fill=ball_color[2])
        # Pool_[3] = canvas.create_oval(ballX[3], ballY[3], ballX[3] + Size_of_Ball, ballY[3] + Size_of_Ball, fill=ball_color[3])
        # Pool_[4] = canvas.create_oval(ballX[4], ballY[4], ballX[4] + Size_of_Ball, ballY[4] + Size_of_Ball, fill=ball_color[4])
        # Pool_[5] = canvas.create_oval(ballX[5], ballY[5], ballX[5] + Size_of_Ball, ballY[5] + Size_of_Ball, fill=ball_color[5])




