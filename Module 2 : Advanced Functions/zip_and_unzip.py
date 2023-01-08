for item in zip([1, 2, 4], ['a', 'b', 'c']):
    print(item)

x = set(zip())
print(x)

for item in zip([10, 20, 30]):
    print(item)

for item in zip(['Ali', 'Vali', 'Gani'], [18, 19, 20], [3, 5, 4]):
    print(item)

x = set(zip([10, 20], [30, 40, 50, 60]))
print(x)  # {(20, 40), (10, 30)}

from itertools import zip_longest as l1

x = set(l1([10, 20], [30, 40, 50, 60]))
print(x)  # {(10, 30), (20, 40), (None, 50), (None, 60)}

# unzipping values
unzipping = zip([1, 2, 3], ['a', 'b', 'c'], ['x', 'y', 'z'])
x, y, z = zip(*unzipping)
print(x, y, z)

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)

# Python code to demonstrate the working of
# unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)

# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player : %s	 Score : %d" % (pl, sc))
