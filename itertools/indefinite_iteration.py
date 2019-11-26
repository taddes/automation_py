m = 5
while m > 0:
    m -= 1
    if (m % 2) == 0:
      print(m)
      continue

"""While Else"""
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')