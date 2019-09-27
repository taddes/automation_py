import os
import shelve

test = os.path.join(os.getcwd(), 'taddes', 'pepper')
print(test)

# print(os.path.abspath('../'))
# print(os.path.relpath('/', './'))
# print(os.path.dirname(test))
# print(os.path.basename(test))
# print(os.path.split(test))
# print(os.path.exists('/'))
# print(os.path.isfile('./'))
# print(os.path.isdir('./'))

testfile = open('file.txt')
thing = testfile.readlines()
for line in thing:
    print(line)

shelffile = shelve.open('mycats')
# cats = ['Pepper', 'Pamina', 'Pip']
# shelffile['cats'] = cats
# shelffile.close()
print(type(shelffile))
print(shelffile['cats'])