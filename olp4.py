def calculates_the_equation():
	a = input('Введите коэффициент a ')
	b = input('Введите коэффициент b ')
	c = input('Введите коэффициент c ')
	a = int(a)
	b = int(b)
	c = int(c)


	D = (b * b) - (4 * a * c)
	kD = D ** 0.5
	if D < 0:
		return print('Корней нет')
	elif D == 0:
		x1 = ((-1) * b) / (2 * a)
		return print(f'Корни квадратного уравнения: {x1}')
	else:
		x1 = ((-1) * b + kD) / (2 * a)
		x2 = ((-1) * b - kD) / (2 * a)
		return print(f'Корни квадратного уравнения: {x1} и {x2}')

calculates_the_equation()
