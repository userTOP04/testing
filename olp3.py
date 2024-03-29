# Задание 3

my_list = input('Введите элементы через пробел: ').split()
for index, elements in enumerate(my_list):
	my_list[index] = int(my_list[index])


def bubble_sort(my_list: list) -> None:
	counter = 0
	for element in my_list:
		repeat = False
		for index in range(len(my_list) - 1):
			counter += 1
			if my_list[index] < my_list[index + 1]:
				my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
				repeat = True 
		if not repeat:
			return counter
	return counter

	


counter = bubble_sort(my_list)
print(my_list)
print(counter)


