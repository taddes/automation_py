"""
    CHARACTER CLASSES
    \d - any numeric digit 0-9
    \D - any character that is NOT a digit from 0-9
    \w - any letter, numeric digit, or underscore ('words')
    \W - any character that is not a letter, digit or underscore
    \s - any space, tab or newline character
    \S - any character that is NOT a space, tab, or newline
    [ ] - to index value options within a regex,
          [0-5] same as [0|1|2|3|4|5]
"""
import re

"""
The regular expression \d+\s\w+ will match text that has one or more
numeric digits (\d+), followed by a whitespace character (\s), followed by
one or more letter/digit/underscore characters (\w+). The findall() method
returns all matching strings of the regex pattern in a list.
"""
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

"""
    MAKE YOUR OWN CHAR CLASSES
    USE [ ] to define
    [aeiouAEIOU] will match any vowel, upper or lower
    Ranges are also feasible [a-zA-Z0-9], matching all lower/upper letters and numbers
"""
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))


"""
    Negative Character class ^
    ^ symbol negates a value, returning what is NOT in that char class
"""
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))


"""
    Caret ^ and dollar-sign $
    ^ at regex start indiates that a match must occur at BEGINNING of text
    $ at regex end to indicate string must end with that pattern
"""
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.') == None)

# r'\d$' Matches a string that ends with a numeric character
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)

# r'^\d+$ matches string that begin and end with one or more numeric chars
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12 34567890') == None)