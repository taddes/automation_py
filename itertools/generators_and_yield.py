"""
Generator
A lazy-iterator/call by need
Delays the evaluation of an expression until needed, avoids repeated evaluations.
Lazy iterators do not store contents in memory
"""
import sys
import cProfile


with open('somefile.csv', 'w') as somefile:
    somefile.write('Yo')

# Generator comprehension
gen_comp = (line for line in open('somefile.csv'))
"""
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
        """

def inf_sequence():
    num = 0
    while True:
        yield num
        num += 1

"""Palindrome detector"""
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

# for i in inf_sequence():
#     pal = is_palindrome(i)
#     if pal:
#       pass
        # print(pal)


nums_squared_lc = [num**2 for num in range(10000)]
nums_squared_gc = (num**2 for num in range(10000))
print(sys.getsizeof(nums_squared_lc))
print(sys.getsizeof(nums_squared_gc))


print(cProfile.run('[num**2 for num in range(10000)]'))
print(cProfile.run('(num**2 for num in range(10000))'))