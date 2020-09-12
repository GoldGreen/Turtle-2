from turtle import *
from math import *

class Drawer(object):
    _tur :Turtle
    _actions :[]

    def __init__(self, tur:Turtle):
        self._tur = tur
        self._actions = [self.DrawLine,
            self.DrawTriangle,
            self.DrawSquare,
            self.DrawCircle,
            self.DrawManyAngle]


    def Draw(self, index: int, arg):
        self._actions[index](arg)


    def DrawLine(self, arg):
        print("Рисую отрезок")
        start = arg[0]
        end = arg[1]

        self._tur.goto(start)
        self.Clear()

        self._tur.goto(end)


    def DrawTriangle(self, arg):
        print("Рисую Треугольник")
        start = arg[0]
        len = arg[1]

        start = (start[0], start[1] + len / 2)
        self._tur.goto(start)
        self.Clear()

        nextPoint = (start[0] + len / 2, start[1] - len / 2)
        self._tur.goto(nextPoint)
        nextPoint = (nextPoint[0] - len, nextPoint[1])
        self._tur.goto(nextPoint)
        self._tur.goto(start)


    def DrawSquare(self, arg):
        print("Рисую Квадрат")
        start = arg[0]
        len = arg[1]

        start = (start[0] - len / 2,  start[1] - len / 2)
        self._tur.goto(start)
        self.Clear()

        nextPoint = (start[0] + len, start[1])
        self._tur.goto(nextPoint)
        nextPoint = (nextPoint[0], nextPoint[1] + len)
        self._tur.goto(nextPoint)
        nextPoint = (nextPoint[0] - len, nextPoint[1])
        self._tur.goto(nextPoint)
        self._tur.goto(start)


    def DrawCircle(self, arg):
        print("Рисую Круг")
        start = arg[0]
        radius = arg[1]

        self._tur.goto(start)
        self.Clear()

        self._tur.circle(radius)


    def DrawManyAngle(self, arg):
        print("Рисую Многоугольник")
        start = arg[0]
        count = arg[1]
        radius = arg[2]

        mFunc = lambda x: (start[0] + radius * cos(2 * pi * x / count), start[1] + radius * sin(2 * pi * x / count))
        self._tur.goto(mFunc(0))
        self.Clear()

        for x in range(count)[1:]:
            self._tur.goto(mFunc(x))
        
        self._tur.goto(mFunc(0))

    def Clear(self):
        self._tur.clear()