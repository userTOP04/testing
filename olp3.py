from random import randint

amount = 10
my_list = []
count = 0
for elements in range(amount):
	my_list.append(randint(1, 100))

for cycle in range(amount - 1):
	for idx in range(amount - 1 - cycle):
		if my_list[idx] > my_list[idx + 1]:
			count += 1
			my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]

print(my_list)
print(count)

