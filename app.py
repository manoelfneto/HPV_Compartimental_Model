from tkinter import *
import random
import copy

class Cell:

    def __init__(self, infect_time, state, age, gender):

        self.infect_time = infect_time
        self.state = state
        self.age = age
        self.gender = gender

    def getinfect_time(self):
        return self.infect_time

    def setinfect_time(self, time):
        self.infect_time = time

    def getstate(self):
        return self.state

    def setstate(self, state):
        self.state = state

    def getage(self):
        return self.age

    def setage(self, age):
        self.age = age

    def getgender(self):
        return self.gender

    def setgender(self, gender):
        self.gender = gender


cell = [[0 for row in range(-1, 61)] for col in range(-1, 81)]
firstGen = [[0 for row in range(-1, 61)] for col in range(-1, 81)]
temporary = [[0 for row in range(-1, 61)] for col in range(-1, 81)]


def make_frames():
    processing()
    paint_cells()
    root.after(1000, make_frames)


def put_cells():
    ages = []
    aleatory_cells = [Cell(0, 0, 13, 0), Cell(1, 2, 22, 0), Cell(1, 1, 33,0 ), Cell(0, 0, 45, 0), Cell(0, 0, 25, 0),
                 Cell(0, 0, 13, 1), Cell(0, 0, 13, 1), Cell(0, 0, 13, 1), Cell(0, 0, 13, 1), Cell(0, 0, 13, 1)]
    for y in range(-1, 61):
        for x in range(-1, 81):
            firstGen[x][y] = random.choice(aleatory_cells)
            temporary[x][y] = 0
            cell[x][y] = canvas.create_oval((x*10, y*10, x*10+10, y*10+10), outline="gray50", fill="black")


def processing():
    contador: 0
    pessoas_susc = 0
    pessoas_estado1 = 0
    pessoas_estado2 = 0

    for y in range(0, 60):
        for x in range(0, 80):
            infected_neighbors = search_neigh(x, y)  # vizinhos contaminados

            if firstGen[x][y].getinfect_time() > 18:
                temporary[x][y] = Cell(0, 0, 16, 0)

            else:
                if firstGen[x][y].getstate() == 0:
                    if infected_neighbors > 3:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(1)
                    else:
                        temporary[x][y] = copy.copy(firstGen[x][y])

                if firstGen[x][y].getstate() == 1:
                    if firstGen[x][y].getinfect_time() > 6 and firstGen[x][y].getinfect_time() < 12:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(2)
                        temporary[x][y].setinfect_time(firstGen[x][y].getinfect_time() + 1)
                    else:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setinfect_time(temporary[x][y].getinfect_time() + 1)


                if firstGen[x][y].getstate() == 2:
                    if firstGen[x][y].getinfect_time() > 12:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(1)
                        temporary[x][y].setinfect_time(temporary[x][y].getinfect_time() + 1)
                        #print(temporary[x][y].getinfect_time())
                    else:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setinfect_time(temporary[x][y].getinfect_time() + 1)
                print(temporary[x][y].getinfect_time())

                # if contador == 11:
                #     if temp[x][y].getstate() == 0:
                #         pessoas_susc += 1
                #     elif temp[x][y].getstate() == 1:
                #         pessoas_estado1 += 1
                #     elif temp[x][y].getstate() == 2:
                #         pessoas_estado2 += 1
                #     print("suscetiveis: %d" % pessoas_susc)
                #     print("estado1: %d" % pessoas_estado1)
                #     print("estado2: %d" % pessoas_estado2)

    # contador += 1
    print("--------------------------------------------------------")

    for y in range(0, 60):
        for x in range(0, 80):
            firstGen[x][y] = temporary[x][y]


def search_neigh(a, b):  #vizinhos contaminados
    infectted_neigh = 0
    if firstGen[a - 1][b + 1].getstate() == 1 or firstGen[a - 1][b + 1].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a][b + 1].getstate() == 1 or firstGen[a][b + 1].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a + 1][b + 1].getstate() == 1 or firstGen[a + 1][b + 1].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a - 1][b].getstate() == 1 or firstGen[a - 1][b].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a + 1][b].getstate() == 1 or firstGen[a + 1][b].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a - 1][b - 1].getstate() == 1 or firstGen[a - 1][b - 1].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a][b - 1].getstate() == 1 or firstGen[a][b - 1].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    if firstGen[a + 1][b - 1].getstate() == 1 or firstGen[a + 1][b - 1].getstate() == 2:
        infectted_neigh = infectted_neigh + 1
    return infectted_neigh


def paint_cells():
    for y in range(60):
        for x in range(80):
            if firstGen[x][y].getstate() == 0:
                canvas.itemconfig(cell[x][y], fill="black")
            if firstGen[x][y].getstate() == 1:
                canvas.itemconfig(cell[x][y], fill="yellow")
            if firstGen[x][y].getstate() == 2:
                canvas.itemconfig(cell[x][y], fill="red")


root = Tk()
canvas = Canvas(root, width=800, height=600, highlightthickness=0, bd=0, bg='black')
canvas.pack()
put_cells()

make_frames()
root.mainloop()
