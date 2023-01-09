numbers = [10, 20, 30, 40, 50, 60, 70]

new_iterator = iter(numbers)

print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))

seq = "Iterator tutorial in Python"

new_seq_iter = iter(seq)
print(next(new_seq_iter))
print(next(new_seq_iter))
print(next(new_seq_iter))
print(next(new_seq_iter))
print(next(new_seq_iter))
print(next(new_seq_iter))
print(next(new_seq_iter))
print(next(new_seq_iter))


def new_iterator(n):
    my_iterable = iter(n)

    while True:
        try:
            print(next(my_iterable))
        except StopIteration:
            break


new_iterator([1, 2, 3, 4, 5, 6])
new_iterator('Python')


# Building Iterator by OOP
class Incremeting:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        x = self.count
        self.count += 1
        return x

    # def __next__(self):
    #     if self.count <= 15:
    #         x = self.count
    #         self.count += 1
    #         return x
    #     else:
    #         raise StopIteration


new_obj = Incremeting()
new_iter = iter(new_obj)

print(next(new_iter))
print(next(new_iter))
print(next(new_iter))