### List

days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for count in range(len(days_of_week)):
    print(days_of_week[count])


### Update List elements
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

days_of_week[0] = 'Sunday'
print(days_of_week)


### Slicing a list
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

print(days_of_week[2:5]

### Nesting a list
child1 = ['Pat', 5, 6.5]
family = [child1]
print(family[0][1])

# or
family = [['Pat', 5, 6.5]]
print(family[0][1])


### Adding items to the list
my_list = [ ]
my_list.append(10)
my_list.append('ten')
my_list.extend([20, 'twenty'])
      
print(my_list)


### Adding items with Concatenation and Inserts
my_list = [ ]
my_list.append(10)
my_list.append('ten')
my_list.extend([20, 'twenty'])

my_list = my_list + [30, 'thirty']
my_list.insert(3, 'Hi there!')
my_list.remove('Hi there!')

print(my_list)

"""
An interesting twist to the remove function is that when you call it,
only the first item with the value you specify is removed. This means
that if I had the value 'hi there!' in multiple index positions in my_list,
for example at index 3 and index 6, then only the instance located
at index 3 would be removed.
"""

### Finding the largest value
my_numbers = [16, 8, 15, 42, 23, 4]

print(max(my_numbers))

### Sort the list
my_numbers = [16, 8, 15, 42, 23, 4]
my_numbers.sort()

print(my_numbers)


### Reversing the list order
my_numbers = [16, 8, 15, 42, 23, 4]
my_numbers.reverse()

print(my_numbers)


