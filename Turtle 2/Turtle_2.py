from turtle import * 
from Drawer import *
from ArgCreator import *

argType = [ArgType.LINE, ArgType.TRIANGLE, ArgType.SQUARE, ArgType.CIRCLE, ArgType.MANY_ANGLE]

def ChooseFigure():
    return int(input("1: Отрезок\n2: Треугольник\n3: Квадрат\n4: Круг\n5: Многоугольник\n\nНомер:"))

tr = Turtle()
tr.begin_fill()

drawer = Drawer(tr)
argCreator = ArgCreator()

choosen = ChooseFigure()
while(choosen >= 1 and choosen <= 5):
    index = choosen - 1
    drawer.Draw(index, argCreator.CreateArg(argType[index]))
    choosen = ChooseFigure()

tr.end_fill()
print("Выход из программы...")
