"""
    Regex check for phone numbers
    Regex format for US/CA Number \d{3}-\d{3}-\d{4}
"""

import re

# raw string representation which does not escape characters
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phone_regex)

"""
    - MO indicates match object
    - .search() method looks for a matching result and returns a re.Match object
    - .group() method returns a value that matches passed search value, as 
      returned from the .search() method object
"""
mo = phone_regex.search('My number is 456-852-6985')
print(mo)
print(f'Number found: {mo.group()}')


"""
    Matching groups
"""
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phone_num_regex.search('My number is 415-555-4242.')
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))
print(mo2.group())


""" 
    Retrieve all groups at once mo.groups()
    Returns a tuple with the returned groups
    Can use tuple unpacking to seperate groups
""" 
print(mo2.groups())
area_code, main_number = mo2.groups()
print(area_code, main_number)


"""
    Using and escaping parenthesis
"""
paren_phone_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
print(paren_phone_regex)
mo3 = paren_phone_regex.search('My tellie number is (704) 789-3456')
print(mo3)
print(mo3.group(0))
print(mo3.group(1))
print(mo3.groups())

"""
    Regex Matching with Pipe
    Grabs first occurance of either or
"""
hero_regex = re.compile(r'Batman|Captain Kirk')
hero_mo = hero_regex.search('Captain Kirk can kick Batman Ass')
print(hero_mo.group())

# Returns a list of occurances
all_hero = hero_regex.findall('Captain Kirk can kick Batman Ass')
print(all_hero)

"""
    Pipe - Multi pattern matching parts of strings
"""
bat_regex = re.compile(r'Bat(man|mobile|copter|tering ram)')
bat_mo = bat_regex.search('The Batmobile lost a wheel and Joker quit Ballet, HEY!')
print(bat_mo.group())
print(bat_mo.group(1))
print(bat_mo.groups())


"""
    Optional Matching with ?
    Regex should match whether it is there or not
"""
bat_regex2 = re.compile('Bat(wo)?man')
bat_mo_2 = bat_regex2.search('The Adventures of Batman')
print(bat_mo_2.group())


bat_mo_3 = bat_regex2.search('The Adventures of Batwoman')
print(bat_mo_3.group())


"""
    Regex check to see if there is an area code or not
"""
phone_regex2 = re.compile(r'(\d\d\d-)?\d{3}-\d{4}')
mo_phone = phone_regex2.search('My number is 455-456-6839')
print(mo_phone.group())
mo_phone2 = phone_regex2.search('My number is 456-6839')
print(mo_phone2.group())

"""
    Matching zero or more with *
    Group that precedes star can occur any number of times in the text
    Can be absent, or repeated over and over
"""
spider_re = re.compile(r'Spider(wo)*man')
spider_mo = spider_re.search('The Adventures of Spiderman')
print(spider_mo.group())

spider_re2 = re.compile(r'Spider(wo)*man')
spider_mo2 = spider_re2.search('The Adventures of Spiderwowowoman')
print(spider_mo2.group())

"""
    Matching one or more with +
    Match one or more
    the group preceding the + must occur at least once, NOT OPTIONAL
"""

super_re = re.compile(r'Super(wo)+man')
super_mo = super_re.search('The Adventures of Superwoman')
print(super_mo.group())
super_mo2 = super_re.search('The Adventures of Superwowoman')
print(super_mo2.group())

"""
    Matching specific repetitions with {}
    If you have a large pattern you want to repeat numerous times, follow
    your regex with a numer inside a set of {}
    - You can also provide a numeric range of occurances {1,4}
    - leaving one value unbounded either goes on, or goes before
    {,5} (0-5) or {4,} (4 onwards)
    (Ha){3} -> (Ha)(Ha)(Ha)
"""
haRegex = re.compile(r'(HA){3}')
hamo = haRegex.search('HAHAHA')
print(hamo.group())


hamo2 = haRegex.search('HA')
print(hamo2 == None)

"""
    Greedy/Nongreedy Matching
    All regex in Python greedy by default, meaning that in abmbiguous sitations
    it will match the longest string possible.  
    Non greedy version matches the shortest string possible. 
"""

# Greedy
greedyHaRegex = re.compile(r'(HA){3,5}')
gmo = greedyHaRegex.search('HAHAHAHAHA')
print(gmo.group())

# Non Greedy
nonGreedyHaRegex = re.compile(r'(HA){3,5}?')
ngmo = nonGreedyHaRegex.search('HAHAHAHAHA')
print(ngmo.group())


"""
    findall() Method
    search() returns a Match object of the first matched text
    findall() returns the string sof every match in the search
    returns a list of strings that match all regex
    *As long as there are no groups in the regex.  Each string in
    list is a piece of the searched text matched 
    -returns a list of tuples corresponding to groups
"""
phone_regex3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_mo3 = phone_regex3.search('Cell:458-456-9856 Home: 456-851-6985')
print(phone_mo3.group())
print(phone_regex3.findall('Cell:458-456-9856 Home: 456-851-6985'))
phone_mo_findall = phone_regex3.findall('Cell:458-456-9856 Home: 456-851-6985')
print(phone_mo_findall)

# Groups
phone_regex3_groups = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phone_mo3_groups = phone_regex3_groups.search('Cell:458-456-9856 Home: 456-851-6985')
print(phone_mo3_groups.group())
print(phone_regex3_groups.findall('Cell:458-456-9856 Home: 456-851-6985'))
phone_mo_findall_groups = phone_regex3_groups.findall('Cell:458-456-9856 Home: 456-851-6985')
print(phone_mo_findall_groups)
