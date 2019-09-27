def custom_iterator(iterable, action_to_do):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item)

nums = {1, 2, 3, 4, 5}
custom_iterator(nums, print)

numbers = [1, 2, 3]
squares = [1, 4, 9]
# iterator = zip(numbers, squares)
# newlist = zip(numbers, squares)
# print(newlist)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
squared = map(lambda x: x**2, numbers)
print(next(squared))
print(next(squared))

filter_numbers = [-1, -2, 3, -4, 5]
positive = filter(lambda x: x > 0, filter_numbers)
print(next(positive))
print(next(positive))
