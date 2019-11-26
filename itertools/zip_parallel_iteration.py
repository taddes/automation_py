"""

    zip(*iterables)
    [(numbers[0], letters[0]), (numbers[1], letters[1]),...,

"""

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))
print(zipped)
for i in zipped:
    print(i)

"""To use zip(*) to seperate elements of each iterator tuple into independent sequences
"""
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers, letters, sep='\n')