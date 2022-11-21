"""import random
import tkinter as tk

win = tk.Tk()
photo = tk.PhotoImage(file='2048_logo.svg.png')
win.iconphoto(False, photo)
win.title('2048')
win.geometry('500x400+625+200')
win.resizable(False, False)
win.config(background='#ECD699')

label = tk.Label(win, text='2042',
                         fg="black",
                         background='#ECD699',
                         font=('Arial', 20, 'italic'),
                         anchor='n')
label.grid(row=0,column=0)

class Code:
    the_matrix = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
    # Հարմար տեսքի համար

    # Խաղի սկզբում ընտրվում են կամայական 2 բջիջներ, որոնք ռանդոմ կլինեն կամ 4 կամ 2,
    # արդյունքւոմ return է անում այն մատրիցան, որով սկսվելու է խաղը
    def start(mtrx):
        rnd1 = random.randint(0, 3)
        rnd2 = random.randint(0, 3)
        rnd3 = random.randint(0, 3)
        rnd4 = random.randint(0, 3)
        while [rnd1, rnd2] == [rnd3, rnd4]:
            rnd3 = random.randint(0, 3)
            rnd4 = random.randint(0, 3)
        mtrx[rnd1][rnd2] = random.choice([2, 4])
        mtrx[rnd3][rnd4] = random.choice([2, 4])
        return mtrx
    def view(mtrx):
        for i in mtrx:
            print(i)

class Interface:

    def designe(mtrx):
        # Logo, background colour, title, window size


        # Buttons
        def left():
            lst = []
            a=0
            for i in range(len(mtrx)):
                for ii in range(len(mtrx)):
                    if mtrx[i][ii] !=0 and mtrx[i][ii+1]!=mtrx[i][ii]:
                        lst.append( mtrx[i][ii+1])
                        a+=1
                    if mtrx[mtrx[i][ii] !=0 and mtrx[i][ii+1]==mtrx[i][ii]]:
                        lst.append(2*mtrx[i][ii])
                        mtrx[i][ii+1] = 0
                        a += 1
            while len(lst) < 4:
                lst.append(0)
        #if a == 0 we cant use this button



        def right():
            lst = []
            a = 0
            for i in range(len(mtrx)):
                for ii in range(len(mtrx)):
                    if mtrx[i][ii] != 0 and mtrx[i][ii + 1] != mtrx[i][ii]:
                        lst.append(mtrx[i][ii + 1])
                        a += 1
                    if mtrx[mtrx[i][ii] != 0 and mtrx[i][ii + 1] == mtrx[i][ii]]:
                        lst.append(2 * mtrx[i][ii])
                        mtrx[i][ii + 1] = 0
                        a += 1
            while len(lst) < 4:
                lst.append(0)
            lst.reverse()

        def up():
            pass
        def down():
            pass
        window.bind("<Left>",left)
        window.bind("<Right>",right)
        window.bind("<Up>",up)
        window.bind("<Down>",down)
        window.mainloop()


class main:
    win = Interface()
    print(win.designe())

"""
import tkinter as tk
import random
from math import floor


class Game:
    def __init__(self):
        self.matrix = [[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
        self.win = tk.Tk()
        #self.win.grid()
        self.win.title('2048')
        photo = tk.PhotoImage(file='2048_logo.svg.png')
        self.win.iconphoto(False, photo)
        self.win.geometry('440x500+525+200')
        self.win.resizable(False, False)
        self.win.config(background='#ECD699')
        self.GUI()
        self.start()

        self.win.bind("<Left>", self.left)
        self.win.bind("<Right>", self.right)
        self.win.bind("<Up>", self.up)
        self.win.bind("<Down>", self.down)

        self.win.mainloop()


    def GUI(self):
        #Frame widget-ի միջոցով ստեղծում ենք բջիջների 4x4 մատրից, որոնց միջև կա 5 pixel տարածություն, cells list-ի մեջ
        #պահում ենք բոլոր բջիջների կոորդինատների և դրանց համապատասխանող թվերի կոորդինատների դիրքերն ու նախնական տեսքը,
        #որը մեզ պետք է գալու start ֆունկցիայում
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.win,
                    bg="#E9FFDB",
                    width=100,
                    height=100
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.win, bg = "#E9FFDB" )
                cell_number.grid(row=i, column=j)
                cell_data = {"frame":cell_frame, "number":cell_number}
                row.append(cell_data)
            self.cells.append(row)

    def start(self):
        #Խաղը սկսելուց ընտրում է կամայական 2 վանդակ, որոնց տալիս է 2 կամ 4 արժեքներից կամայականը
        row1 = random.randint(0, 3)
        clm1 = random.randint(0, 3)
        row2 = random.randint(0, 3)
        clm2 = random.randint(0, 3)
        while [row1, clm1] == [row2, clm2]:
            row2 = random.randint(0, 3)
            clm2 = random.randint(0, 3)
        a1 = random.choice([2, 4])
        a2 = random.choice([2, 4])
        self.matrix[row1][clm1] = a1
        self.matrix[row2][clm2] = a2
        self.cells[row1][clm1]["frame"].configure()
        self.cells[row2][clm2]["frame"].configure()
        self.cells[row1][clm1]["number"].configure(text=a1, font=('Arial', 20, 'bold', 'italic'))
        self.cells[row2][clm2]["number"].configure(text=a2, font=('Arial', 20, 'bold', 'italic'))
        return self.matrix

    def stack(self):
        new_matrix = [[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position+=1
        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j+1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j+1] = 0

    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    def add_new_tile(self):
        row = random.randint(0,3)
        col = random.randint(0,3)
        while (self.matrix[row][col]!=0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = random.choice([2,4])

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]['frame'].configure()
                    self.cells[i][j]["number"].configure(text="")
                else:
                    self.cells[i][j]['frame'].configure()
                    self.cells[i][j]["number"].configure(text=str(cell_value), font=('Arial', 20, 'bold', 'italic'))
        ###

    def left(self, event):
        self.start()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()

        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        return False
    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(game_over_frame, text="you Win",font=('Arial', 20, 'bold', 'italic')).pack()
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(game_over_frame, text="Game over", font=('Arial', 20, 'bold', 'italic')).pack()

def main():
    Game()

if __name__ == "__main__":
    main()
