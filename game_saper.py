import tkinter as tk
from random import randint

window = tk.Tk()
window.title("сапёр")

game = True
bomb_num = 20
bomb_counter = 20
bomb_coords = []
num_list = []

#создаем нумлист
for i in range(10):
    num_list.append([])
    for j in range(10):
        num_list[i].append([0, 0])

#выбираем где бомбы
for i in range(20):
    boo = True
    while boo:
        check = 1
        x, y = randint(0, 9), randint(0, 9)
        for z, j in bomb_coords:
            if z == x and j == y: check = 0
        if check != 0: boo = False
    bomb_coords.append([x, y])
    num_list[x][y] = ['boomb', 0]

#проверяем где сколько соседей бомб
for i in range(1, 9):
    for j in range(1, 9):
        if num_list[i][j][0] != 'boomb':
            if num_list[i + 1][j + 1][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i + 1][j - 1][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i - 1][j - 1][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i - 1][j + 1][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i][j + 1][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i + 1][j][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i - 1][j][0] == 'boomb': num_list[i][j][0] += 1
            if num_list[i][j - 1][0] == 'boomb': num_list[i][j][0] += 1
for j in range(1, 9):
    if num_list[0][j][0] != 'boomb':
        if num_list[0][j + 1][0] == 'boomb': num_list[0][j][0] += 1
        if num_list[0][j - 1][0] == 'boomb': num_list[0][j][0] += 1
        if num_list[1][j - 1][0] == 'boomb': num_list[0][j][0] += 1
        if num_list[1][j + 1][0] == 'boomb': num_list[0][j][0] += 1
        if num_list[1][j][0] == 'boomb': num_list[0][j][0] += 1
    if num_list[9][j][0] != 'boomb':
        if num_list[9][j + 1][0] == 'boomb': num_list[9][j][0] += 1
        if num_list[9][j - 1][0] == 'boomb': num_list[9][j][0] += 1
        if num_list[8][j - 1][0] == 'boomb': num_list[9][j][0] += 1
        if num_list[8][j + 1][0] == 'boomb': num_list[9][j][0] += 1
        if num_list[8][j][0] == 'boomb': num_list[9][j][0] += 1
for i in range(1, 9):
    if num_list[i][0][0] != 'boomb':
        if num_list[i + 1][0][0] == 'boomb': num_list[i][0][0] += 1
        if num_list[i + 1][1][0] == 'boomb': num_list[i][0][0] += 1
        if num_list[i][1][0] == 'boomb': num_list[i][0][0] += 1
        if num_list[i - 1][1][0] == 'boomb': num_list[i][0][0] += 1
        if num_list[i - 1][0][0] == 'boomb': num_list[i][0][0] += 1
    if num_list[i][9][0] != 'boomb':
        if num_list[i + 1][9][0] == 'boomb': num_list[i][9][0] += 1
        if num_list[i + 1][8][0] == 'boomb': num_list[i][9][0] += 1
        if num_list[i][8][0] == 'boomb': num_list[i][9][0] += 1
        if num_list[i - 1][9][0] == 'boomb': num_list[i][9][0] += 1
        if num_list[i - 1][8][0] == 'boomb': num_list[i][9][0] += 1
if num_list[0][0][0] != 'boomb':
    if num_list[1][0][0] == 'boomb': num_list[0][0][0] += 1
    if num_list[1][1][0] == 'boomb': num_list[0][0][0] += 1
    if num_list[0][1][0] == 'boomb': num_list[0][0][0] += 1
if num_list[9][9][0] != 'boomb':
    if num_list[8][9][0] == 'boomb': num_list[9][9][0] += 1
    if num_list[9][8][0] == 'boomb': num_list[9][9][0] += 1
    if num_list[8][8][0] == 'boomb': num_list[9][9][0] += 1
if num_list[9][0][0] != 'boomb':
    if num_list[8][0][0] == 'boomb': num_list[9][0][0] += 1
    if num_list[8][1][0] == 'boomb': num_list[9][0][0] += 1
    if num_list[9][1][0] == 'boomb': num_list[9][0][0] += 1
if num_list[0][9][0] != 'boomb':
    if num_list[1][9][0] == 'boomb': num_list[0][9][0] += 1
    if num_list[1][8][0] == 'boomb': num_list[0][9][0] += 1
    if num_list[0][8][0] == 'boomb': num_list[0][9][0] += 1

#создаем поле
canvas = tk.Canvas(width=355, height=355)
canvas.grid(row=0, column=0, columnspan=3)
canvas.create_rectangle(0, 0, 355, 355, fill="white")
lbl = tk.Label(text=f'бомб осталось: {bomb_counter}')
lbl.grid(row=1, column=2)

#создаем кнопки
for i in range(10):
    for j in range(10):
        canvas.create_rectangle(5*(i+1)+30*i, 5*(j+1)+30*j, 5*(i+1)+30*(i+1), 5*(j+1)+30*(j+1), fill='white')

#функция перезапуска
def start():
    global game
    global bomb_num
    global bomb_counter
    global bomb_coords
    global num_list
    if not game:
        game = True
        bomb_num = 20
        bomb_counter = 20
        bomb_coords = []
        num_list = []
        canvas.create_rectangle(0, 0, 355, 355, fill="white")
        for i in range(10):
            for j in range(10):
                canvas.create_rectangle(5 * (i + 1) + 30 * i, 5 * (j + 1) + 30 * j, 5 * (i + 1) + 30 * (i + 1),
                                        5 * (j + 1) + 30 * (j + 1), fill='white')

        for i in range(10):
            num_list.append([])
            for j in range(10):
                num_list[i].append([0, 0])

        for i in range(20):
            boo = True
            while boo:
                check = 1
                x, y = randint(0, 9), randint(1, 9)
                for z, j in bomb_coords:
                    if z == x and j == y: check = 0
                if check != 0: boo = False
            bomb_coords.append([x, y])
            num_list[x][y] = ['boomb', 0]

        for i in range(1, 9):
            for j in range(1, 9):
                if num_list[i][j][0] != 'boomb':
                    if num_list[i + 1][j + 1][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i + 1][j - 1][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i - 1][j - 1][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i - 1][j + 1][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i][j + 1][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i + 1][j][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i - 1][j][0] == 'boomb': num_list[i][j][0] += 1
                    if num_list[i][j - 1][0] == 'boomb': num_list[i][j][0] += 1
        for j in range(1, 9):
            if num_list[0][j][0] != 'boomb':
                if num_list[0][j + 1][0] == 'boomb': num_list[0][j][0] += 1
                if num_list[0][j - 1][0] == 'boomb': num_list[0][j][0] += 1
                if num_list[1][j - 1][0] == 'boomb': num_list[0][j][0] += 1
                if num_list[1][j + 1][0] == 'boomb': num_list[0][j][0] += 1
                if num_list[1][j][0] == 'boomb': num_list[0][j][0] += 1
            if num_list[9][j][0] != 'boomb':
                if num_list[9][j + 1][0] == 'boomb': num_list[9][j][0] += 1
                if num_list[9][j - 1][0] == 'boomb': num_list[9][j][0] += 1
                if num_list[8][j - 1][0] == 'boomb': num_list[9][j][0] += 1
                if num_list[8][j + 1][0] == 'boomb': num_list[9][j][0] += 1
                if num_list[8][j][0] == 'boomb': num_list[9][j][0] += 1
        for i in range(1, 9):
            if num_list[i][0][0] != 'boomb':
                if num_list[i + 1][0][0] == 'boomb': num_list[i][0][0] += 1
                if num_list[i + 1][1][0] == 'boomb': num_list[i][0][0] += 1
                if num_list[i][1][0] == 'boomb': num_list[i][0][0] += 1
                if num_list[i - 1][1][0] == 'boomb': num_list[i][0][0] += 1
                if num_list[i - 1][0][0] == 'boomb': num_list[i][0][0] += 1
            if num_list[i][9][0] != 'boomb':
                if num_list[i + 1][9][0] == 'boomb': num_list[i][9][0] += 1
                if num_list[i + 1][8][0] == 'boomb': num_list[i][9][0] += 1
                if num_list[i][8][0] == 'boomb': num_list[i][9][0] += 1
                if num_list[i - 1][9][0] == 'boomb': num_list[i][9][0] += 1
                if num_list[i - 1][8][0] == 'boomb': num_list[i][9][0] += 1
        if num_list[0][0][0] != 'boomb':
            if num_list[1][0][0] == 'boomb': num_list[0][0][0] += 1
            if num_list[1][1][0] == 'boomb': num_list[0][0][0] += 1
            if num_list[0][1][0] == 'boomb': num_list[0][0][0] += 1
        if num_list[9][9][0] != 'boomb':
            if num_list[8][9][0] == 'boomb': num_list[9][9][0] += 1
            if num_list[9][8][0] == 'boomb': num_list[9][9][0] += 1
            if num_list[8][8][0] == 'boomb': num_list[9][9][0] += 1
        if num_list[9][0][0] != 'boomb':
            if num_list[8][0][0] == 'boomb': num_list[9][0][0] += 1
            if num_list[8][1][0] == 'boomb': num_list[9][0][0] += 1
            if num_list[9][1][0] == 'boomb': num_list[9][0][0] += 1
        if num_list[0][9][0] != 'boomb':
            if num_list[1][9][0] == 'boomb': num_list[0][9][0] += 1
            if num_list[1][8][0] == 'boomb': num_list[0][9][0] += 1
            if num_list[0][8][0] == 'boomb': num_list[0][9][0] += 1
        lbl.config(text=f'бомб осталось: {bomb_counter}')
        window.update()

#кнопка перезапуска
btn = tk.Button(text="начать игру", command=start)
btn.grid(row=2, column=0)

#событие ЛКМ - проверка точки
def check1(x, y):
    num_list[x][y][1] = 1
    if num_list[x][y][0] != 0:
        canvas.create_rectangle(5 * (x + 1) + 30 * x, 5 * (y + 1) + 30 * y, 5 * (x + 1) + 30 * (x + 1),5 * (y + 1) + 30 * (y + 1), fill='chartreuse1')
        canvas.create_text(5 * (x + 1) + 30 * x + 15, 5 * (y + 1) + 30 * y + 15,text=f'{num_list[x][y][0]}')
    else: #проверяем соседей если квадрат равен нулю
        canvas.create_rectangle(5 * (x + 1) + 30 * x, 5 * (y + 1) + 30 * y,5 * (x + 1) + 30 * (x + 1), 5 * (y + 1) + 30 * (y + 1), fill='chartreuse1')
        if x==0:
            if y==0:
                if num_list[x+1][y+1][1] == 0: check1(x+1, y+1)
                if num_list[x][y+1][1] == 0: check1(x, y+1)
                if num_list[x+1][y][1] == 0: check1(x+1, y)
            elif y == 9:
                if num_list[x+1][y-1][1] == 0: check1(x + 1, y - 1)
                if num_list[x][y - 1][1] == 0: check1(x, y - 1)
                if num_list[x+1][y][1] == 0: check1(x + 1, y)
            else:
                if num_list[x+1][y+1][1] == 0: check1(x+1, y+1)
                if num_list[x][y+1][1] == 0: check1(x, y+1)
                if num_list[x+1][y][1] == 0:check1(x+1, y)
                if num_list[x+1][y-1][1] == 0: check1(x + 1, y - 1)
                if num_list[x][y-1][1] == 0: check1(x, y - 1)
        elif x==9:
            if y==0:
                if num_list[x-1][y+1][1] == 0: check1(x-1, y+1)
                if num_list[x][y + 1][1] == 0:  check1(x, y+1)
                if num_list[x-1][y][1] == 0: check1(x-1, y)
            elif y == 9:
                if num_list[x-1][y-1][1] == 0: check1(x - 1, y - 1)
                if num_list[x][y-1][1] == 0: check1(x, y - 1)
                if num_list[x - 1][y][1] == 0:  check1(x - 1, y)
            else:
                if num_list[x-1][y+1][1] == 0: check1(x-1, y+1)
                if num_list[x][y + 1][1] == 0:  check1(x, y+1)
                if num_list[x-1][y][1] == 0: check1(x-1, y)
                if num_list[x - 1][y - 1][1] == 0:  check1(x - 1, y - 1)
                if num_list[x][y-1][1] == 0: check1(x, y - 1)
        else:
            if y==0:
                if num_list[x - 1][y + 1][1] == 0:  check1(x-1, y+1)
                if num_list[x][y+1][1] == 0: check1(x, y+1)
                if num_list[x-1][y][1] == 0: check1(x-1, y)
                if num_list[x+1][y+1][1] == 0: check1(x + 1, y + 1)
                if num_list[x+1][y][1] == 0:check1(x + 1, y)
            elif y == 9:
                if num_list[x+1][y-1][1] == 0: check1(x + 1, y - 1)
                if num_list[x][y-1][1] == 0: check1(x, y - 1)
                if num_list[x-1][y][1] == 0: check1(x - 1, y)
                if num_list[x-1][y-1][1] == 0: check1(x - 1, y - 1)
                if num_list[x+1][y][1] == 0:check1(x + 1, y)
            else:
                if num_list[x - 1][y + 1][1] == 0:  check1(x-1, y+1)
                if num_list[x - 1][y][1] == 0:  check1(x - 1, y)
                if num_list[x-1][y-1][1] == 0: check1(x - 1, y-1)
                if num_list[x][y + 1][1] == 0:  check1(x, y+1)
                if num_list[x][y-1][1] == 0: check1(x, y - 1)
                if num_list[x+1][y-1][1] == 0: check1(x+1, y-1)
                if num_list[x + 1][y + 1][1] == 0: check1(x + 1, y + 1)
                if num_list[x+1][y][1] == 0:check1(x + 1, y)

def event1(event):
    global game
    if game:
        x, y = event.x, event.y
        numx = (x-5)//35
        numy = (y - 5) // 35
        global bomb_counter
        if num_list[numx][numy][1] == -1:
            bomb_counter += 1
            lbl.config(text=f'бомб осталось: {bomb_counter}')
        if num_list[numx][numy][0] == 'boomb':
            for x2 in range(10):
                for y2 in range(10):
                    if num_list[x2][y2][1] == -1 and num_list[x2][y2][0] != 'boomb':
                        canvas.create_line(5 * (x2 + 1) + 30 * x2, 5 * (y2 + 1) + 30 * y2,
                                           5 * (x2 + 1) + 30 * (x2 + 1), 5 * (y2 + 1) + 30 * (y2 + 1), fill='brown2', width=2)
                        canvas.create_line(5 * (x2 + 1) + 30 * (x2 + 1), 5 * (y2 + 1) + 30 * y2,
                                           5 * (x2 + 1) + 30 * x2, 5 * (y2 + 1) + 30 * (y2 + 1),
                                           fill='brown2', width=2)
            for x1, y1 in bomb_coords:
                if num_list[x1][y1][1] == 0:
                    canvas.create_rectangle(5 * (x1 + 1) + 30 * x1, 5 * (y1 + 1) + 30 * y1,
                                            5 * (x1 + 1) + 30 * (x1 + 1),
                                            5 * (y1 + 1) + 30 * (y1 + 1), fill='brown2')
            canvas.create_rectangle(5 * (numx + 1) + 30 * numx, 5 * (numy + 1) + 30 * numy,
                                    5 * (numx + 1) + 30 * (numx + 1),
                                    5 * (numy + 1) + 30 * (numy + 1), fill='red')
            canvas.create_text(345/2, 345/2,
                               text='Ты проиграл', font='bold 30', fill = 'red4')

            game = False

        if num_list[numx][numy][0] != 'boomb' and num_list[numx][numy][0] != 0:
            canvas.create_rectangle(5 * (numx + 1) + 30 * numx, 5 * (numy + 1) + 30 * numy, 5 * (numx + 1) + 30 * (numx + 1),
                                    5 * (numy + 1) + 30 * (numy + 1), fill='chartreuse1')
            canvas.create_text(5*(numx+1)+30*numx+15, 5*(numy+1)+30*numy+15, text=f'{num_list[numx][numy][0]}')
            num_list[numx][numy][1] = 1
        if num_list[numx][numy][0] == 0:
            check1(numx, numy)

def event2(event):
    global game
    global bomb_counter
    x, y = event.x, event.y
    numx = (x - 5) // 35
    numy = (y - 5) // 35
    if game and bomb_counter>0 and num_list[numx][numy][1] != -1:
        canvas.create_rectangle(5 * (numx + 1) + 30 * numx, 5 * (numy + 1) + 30 * numy,
                                5 * (numx + 1) + 30 * (numx + 1),
                                5 * (numy + 1) + 30 * (numy + 1), fill='yellow')
        num_list[numx][numy][1] = -1
        bomb_counter -= 1
        lbl.config(text=f'бомб осталось: {bomb_counter}')
        bomb_num = 20
        for x1, y1 in bomb_coords:
            if num_list[x1][y1][1] == -1: bomb_num -= 1
        if bomb_num == 0:
            canvas.create_text(345 / 2, 345 / 2,
                                             text='Ты выиграл', font='bold 30', fill='dark green')
            game = False

canvas.bind('<Button-1>', event1)
canvas.bind('<Button-3>', event2)

window.mainloop()