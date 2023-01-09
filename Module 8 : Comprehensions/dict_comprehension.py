numbers = [100, 200, 300, 400, 500]
students = ['Joe', 'Ronald', 'Ahmed', 'Marcelo', 'Alves']

new_dict = {x: y for (x, y) in zip(students, numbers)}
print(new_dict)

numbers = [1, 5, 10, 15, 20, 25]
my_dictionary = {x: x ** 2 for x in numbers if x ** 2 % 4 == 0}
print(my_dictionary)
