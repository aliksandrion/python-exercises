from tkinter import Tk, Button
from random import randint
from tkinter.messagebox import showinfo

root = Tk()
root.title('Tic-Tac-Toe-Reverse')
game_run = True
field = []
cross_count = 0


def new_game():
    global game_run, cross_count
    for x in range(10):
        for y in range(10):
            field[x][y]['text'] = ' '
    game_run = True
    cross_count = 0


def click(x, y):
    global cross_count
    if game_run and field[x][y]['text'] == ' ':
        field[x][y]['text'] = 'X'
        cross_count += 1
        check_defeat()
        if game_run and cross_count < 50:
            computer_move()
            check_defeat()


def check_defeat():
    for n in range(10):
        for i in range(10):

            if n <= 5:
                check_line(field[n][i], field[n + 1][i], field[n + 2][i], field[n + 3][i], field[n + 4][i])
                check_line(field[i][n], field[i][n + 1], field[i][n + 2], field[i][n + 3], field[i][n + 4])

            if i <= 5 and n <= 5:
                check_line(field[n][i], field[n + 1][i + 1], field[n + 2][i + 2], field[n + 3][i + 3],
                           field[n + 4][i + 4])

            if i <= 5 and n >= 4:
                check_line(field[n][i], field[n - 1][i + 1], field[n - 2][i + 2], field[n - 3][i + 3],
                           field[n - 4][i + 4])


def check_line(a, b, c, d, e):
    global game_run
    if a['text'] == b['text'] == c['text'] == d['text'] == e['text'] != " ":
        game_run = False
        if a['text'] == 'X':
            showinfo("Ouch!", "Computer won")
        elif a['text'] == 'O':
            showinfo("Congrats!", "You win!")
        elif cross_count == 50:
            showinfo("Awesome!", "It`s a draw!")


def check_for_comp(row, col):
    res = True
    field[row][col]['text'] = 'O'
    for n in range(10):
        for i in range(10):
            if n <= 5:
                if field[n][i]['text'] == field[n + 1][i]['text'] == field[n + 2][i]['text'] == field[n + 3][i]['text']\
                        == field[n + 4][i]['text'] == 'O':
                    res = False
                if field[i][n]['text'] == field[i][n + 1]['text'] == field[i][n + 2]['text'] == field[i][n + 3][
                    'text'] == field[i][n + 4]['text'] == 'O':
                    res = False
                if i <= 5:
                    if field[n][i]['text'] == field[n + 1][i + 1]['text'] == field[n + 2][i + 2]['text'] == \
                            field[n + 3][i + 3]['text'] == field[n + 4][i + 4]['text'] == 'O':
                        res = False
            if i <= 5 and n >= 4:
                if field[n][i]['text'] == field[n - 1][i + 1]['text'] == field[n - 2][i + 2]['text'] == \
                        field[n - 3][i + 3]['text'] == field[n - 4][i + 4]['text'] == 'O':
                    res = False
    field[row][col]['text'] = ' '
    return res


def computer_move():
    counter = 0
    while counter <= 50:
        x = randint(0, 9)
        y = randint(0, 9)
        if field[x][y]['text'] == ' ':
            counter += 1
        if field[x][y]['text'] == ' ' and check_for_comp(x, y) is True:
            field[x][y]['text'] = 'O'
            break
    else:
        field[x][y]['text'] = 'O'


for row in range(10):
    line = []
    for col in range(10):
        button = Button(root, text=' ', width=2, height=2, font=('Verdana', 20, 'bold'),
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
Button(root, text='Restart', command=new_game).grid(row=10, column=0, columnspan=10, sticky='nsew')
root.mainloop()
