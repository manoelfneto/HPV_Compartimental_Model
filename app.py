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
    # man = 0  woman = 1
    aleatory_cells = [Cell(1, 2, 15, 0), Cell(0, 0, 22, 0), Cell(1, 1, 52, 0), Cell(0, 0, 59, 0), Cell(0, 0, 26, 0),
                      Cell(0, 1, 17, 1), Cell(0, 0, 19, 1), Cell(0, 0, 57, 1), Cell(0, 0, 61, 1), Cell(0, 0, 28, 1),
                      Cell(0, 0, 33, 0), Cell(1, 2, 45, 0), Cell(1, 1, 29, 0), Cell(0, 0, 45, 0), Cell(0, 0, 25, 0),
                      Cell(0, 0, 35, 1), Cell(0, 0, 43, 1), Cell(0, 0, 36, 1), Cell(0, 0, 13, 1), Cell(0, 0, 24, 1)]

    for y in range(-1, 61):
        for x in range(-1, 81):
            firstGen[x][y] = random.choice(aleatory_cells)
            temporary[x][y] = 0
            cell[x][y] = canvas.create_oval((x * 10, y * 10, x * 10 + 10, y * 10 + 10), outline="gray50", fill="black")


def processing():
    cells_state_0 = 0
    cells_state_1 = 0
    cells_state_2 = 0

    for y in range(0, 60):
        for x in range(0, 80):
            infected_neighbors_state1 = search_neigh_state1(x, y)
            infected_neighbors_state2 = search_neigh_state2(x, y)
            aleatory_cells = [Cell(1, 2, 15, 0), Cell(0, 0, 22, 0), Cell(1, 1, 52, 0), Cell(0, 0, 59, 0),
                              Cell(0, 0, 26, 0), Cell(0, 1, 17, 1), Cell(0, 0, 19, 1), Cell(0, 0, 57, 1),
                              Cell(0, 0, 61, 1), Cell(0, 0, 28, 1), Cell(0, 0, 33, 0), Cell(1, 2, 45, 0),
                              Cell(1, 1, 29, 0), Cell(0, 0, 45, 0), Cell(0, 0, 25, 0), Cell(0, 0, 35, 1),
                              Cell(0, 0, 43, 1), Cell(0, 0, 36, 1), Cell(0, 0, 13, 1), Cell(0, 0, 24, 1)]

            if firstGen[x][y].getinfect_time() > 12:
                temporary[x][y] = random.choice(aleatory_cells)

            else:
                if firstGen[x][y].getstate() == 0:
                    cells_state_0 += 1
                    if (infected_neighbors_state1 > 5 or infected_neighbors_state2 > 5) and \
                            (16 < firstGen[x][y].getage() > 25):
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(1)
                    elif infected_neighbors_state1 > 3 or infected_neighbors_state2 > 2:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(1)
                    else:
                        temporary[x][y] = copy.copy(firstGen[x][y])

                elif firstGen[x][y].getstate() == 1:
                    cells_state_1 += 1
                    if firstGen[x][y].getinfect_time() == 5:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(2)
                        temporary[x][y].setinfect_time(firstGen[x][y].getinfect_time() + 1)
                    else:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setinfect_time(temporary[x][y].getinfect_time() + 1)

                elif firstGen[x][y].getstate() == 2:
                    cells_state_2 += 1
                    if firstGen[x][y].getinfect_time() > 8:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setstate(1)
                        temporary[x][y].setinfect_time(temporary[x][y].getinfect_time() + 1)
                    else:
                        temporary[x][y] = copy.copy(firstGen[x][y])
                        temporary[x][y].setinfect_time(temporary[x][y].getinfect_time() + 1)

    archive = open("info.txt", "a")
    archive2 = open("info.txt", "r")
    content = archive2.readlines()
    number_of_lines = len(content)
    archive.write("round: %d" % ((number_of_lines / 5) + 1) + "\n")
    archive.write("cells state 0: %d" % cells_state_0 + "\n")
    archive.write("cells state 1: %d" % cells_state_1 + "\n")
    archive.write("cells state 2: %d" % cells_state_2 + "\n")
    archive.write("----------------------------" + "\n")

    for y in range(0, 60):
        for x in range(0, 80):
            firstGen[x][y] = temporary[x][y]


def search_neigh_state1(a, b):
    neigh_state1 = 0

    if firstGen[a - 1][b + 1].getstate() == 1:
        neigh_state1 += 1

    if firstGen[a][b + 1].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    if firstGen[a + 1][b + 1].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    if firstGen[a - 1][b].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    if firstGen[a + 1][b].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    if firstGen[a - 1][b - 1].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    if firstGen[a][b - 1].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    if firstGen[a + 1][b - 1].getstate() == 1:
        neigh_state1 = neigh_state1 + 1

    return neigh_state1


def search_neigh_state2(a, b):
    neigh_state2 = 0

    if firstGen[a - 1][b + 1].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a][b + 1].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a + 1][b + 1].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a - 1][b].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a + 1][b].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a - 1][b - 1].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a][b - 1].getstate() == 2:
        neigh_state2 += 1

    if firstGen[a + 1][b - 1].getstate() == 2:
        neigh_state2 += 1

    return neigh_state2


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
