from enum import Enum

class ArgType(Enum):
	LINE = 1
	TRIANGLE = 2
	SQUARE = 3
	CIRCLE = 4
	MANY_ANGLE = 5

class ArgCreator(object):

	def CreateArg(self, argType: ArgType):
		if argType == ArgType.LINE:
			startX = float(input("Стартовая точка X:"))
			startY = float(input("Стартовая точка Y: "))

			endX = float(input("Конечная точка X: "))
			endY = float(input("Конечная точка Y: "))

			return ((startX, startY), (endX, endY))

		elif argType in [ArgType.TRIANGLE, ArgType.SQUARE]:
			startX = float(input("Стартовая точка X: "))
			startY = float(input("Стартовая точка Y: "))

			len = float(input("Длина стороны: "))

			return ((startX, startY), len)

		elif argType == ArgType.CIRCLE:
			startX = float(input("Стартовая точка X: "))
			startY = float(input("Стартовая точка Y: "))

			radius = float(input("Радиус: "))

			return ((startX, startY), radius)

		elif argType == ArgType.MANY_ANGLE:
			startX = float(input("Стартовая точка X: "))
			startY = float(input("Стартовая точка Y: "))

			count = int(input("Количество углов: "))
			radius = float(input("Радиус: "))

			return ((startX, startY), count, radius)
		else:
			return None