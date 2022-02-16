from backpack import Backpack
from timeit import default_timer as timer
import random
import pandas as pd
import xlsxwriter

# b - ładowność plecaka
# n - liczba przedmiotow
# a - ciężar przedmiotu
# c - wartość przedmiotu

bb      = []
nb      = []
bn      = []
nn      = []
bDTime  = []
nDTime  = []
bGtime  = []
nGtime  = []
bGRe    = []
nGRe    = []

def timeIt(s, n, b):

    startD = timer()
    outputD = s.dynamic(n, b)
    endD = timer()-startD

    startG = timer()
    outputG = s.greedy(n, b)
    endG = timer()-startG

    relativeError = round((outputD - outputG)/outputD, 5)

    return endD, endG, relativeError

def data_creator(b, n):
    a = []
    c = []
    for x in range(n):
        a.append(random.randrange(1, int(b*4/n)))
        c.append(random.randrange(1, int(b*4/n)))
    return a, c

def data_input(b, n, steps, stepSize, changingVar):

    for x in range(steps):
        b_step = 0
        n_step = 0
        if changingVar == "b":
            b_step = stepSize
        else:
            n_step = stepSize

        b += b_step
        n += n_step

        a, c = data_creator(b, n)

        s = Backpack(a, c, b)

        timeD, timeG, relativeError = timeIt(s, n, b)

        if changingVar=="b":
            bb.append(b)
            bn.append(n)
            bDTime.append(timeD)
            bGtime.append(timeG)
            bGRe.append(relativeError)
        else:
            nb.append(b)
            nn.append(n)
            nDTime.append(timeD)
            nGtime.append(timeG)
            nGRe.append(relativeError)

if __name__ == '__main__':
    b = 500
    n = 20
    steps = 15
    stepSize =2000
    data_input(b, n, steps, stepSize, "b")

    b = 10000
    n = 10
    steps = 15
    stepSize = 20
    data_input(b, n, steps, stepSize, "n")

df = pd.DataFrame.from_dict(
    {
        'Pojemność plecaka'             :   bb      ,
        'Ilość przedmiotów'             :   bn      ,
        'Czas algorytmu dynamicznego'   :   bDTime  ,
        'Czas algorytmu zachłannego'    :   bGtime  ,
        'Błąd względny'                 :   bGRe
    }
)
df.to_excel('capacitychange1.xlsx', header=True, index=False)

df = pd.DataFrame.from_dict(
    {
        'Pojemność plecaka'             :   nb      ,
        'Ilość przedmiotów'             :   nn      ,
        'Czas algorytmu dynamicznego'   :   nDTime  ,
        'Czas algorytmu zachłannego'    :   nGtime  ,
        'Błąd względny'                 :   nGRe
    }
)
df.to_excel('itemschange2.xlsx', header=True, index=False)
