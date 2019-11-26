"""
    Key iteration protocols in Python are __iter__ and __next__.
    Implemented using iter(<class/object>) and next(<iterator>)
    1. Setting up and retrieving an iterator object with iter() call.
    2. Repeatedly fetching values from iterator via next()
    * In iterator protocol, all that matters is that __iter__ returns
    any object with a __next__ method on it, doesn't matter from where.
"""

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    
    def __next__(self):
        return self.source.value

class RepeaterOne:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


"""
    How an iterator strops generating new values instead of iterating forever. Fire StopIteration exception to signal we've exhausted all available values in the iterator. Once exhausted, they're supposed to raise the StopIteration exception every time next() is called.

    >>> my_list = [1, 2, 3]
    >>> iterator = iter(my_list)

    >>> next(iterator)
    1
    >>> next(iterator)
    2
    >>> next(iterator)
    3
    >>> next(iterator)
    StopIteration

"""


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

"""
    repeater = BoundedRepeater('Hello', 3)
    iterator = iter(repeater)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        print(item)
"""
