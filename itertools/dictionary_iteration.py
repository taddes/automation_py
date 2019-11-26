from collections import ChainMap

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

for key in a_dict:
    print(f"{key} -> {a_dict[key]}")

# Reverse keys and values to create new dictionary
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
print(new_dict)


# Filtering
nw_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
filter_dict = {}
for key, value in nw_dict.items():
    if value <= 2:
        filter_dict[key] = value
print(filter_dict)


# Calculations
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = 0.00
for value in incomes.values():
    total_income += value
print(total_income)
income_gen = (income for income in incomes.values())
print(income_gen)

income_full = sum(income_gen)
print(income_full)

# Dict Comprehension>>> 
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
# Using zip and converting to dict
combined_dict = dict(zip(categories, objects))
print(combined_dict)
# Using comprehension
comprehended_dict = {key:value for key, value in zip(categories, objects)}
print(comprehended_dict)

# Summation operations
incomes2 = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# List
total_income_list_sum = sum([value for value in incomes2.values()])
print(total_income_list_sum)
# Generator
total_income_gen_sum = sum(value for value in incomes2.values())
print(total_income_gen_sum)

# Removing items using dict generator with filter
non_citric = {k: incomes2[k] for k in incomes.keys() - {'orange'}}
print(non_citric)

# Sorting
sorted_incomes = {k: incomes2[k] for k in sorted(incomes2)}
print(sorted_incomes)

# File: dict_popitem.py

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break
print(a_dict)


# Built Ins
# Map map(function, iterable) returns an iterator that applies function to every item of iterable, yielding results on demand
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))
new_prices = dict(map(discount, prices.items()))
print(new_prices)

# filter filter(function, iterable )
def has_low_price(price):
    return prices[price] < 0.4

low_price = list(filter(has_low_price, prices.keys()))
print(low_price)

# Collections ChainMap
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)
print(chained_dict)