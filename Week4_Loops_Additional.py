# Basic loops
a = 0
while a < 5:
    a += 1 # Same as a = a + 1
    print(a)


# Additional loops
a = 1
s = 0
print('Enter numbers to add to the sum.')
print('Enter 0 to quit.')

while a != 0:
    print('Current Sum: ', s)
    a = input('Number? ')   # raw_input() will not work anymore
    a = float(a)
    s += a
print('Total Sum = ', s)


"""
# infinite loop 
while 1 == 1:
    print("Help, I'm stuck in a loop.")
"""

# Calculate the Fibonacci sequence
a = 0
b = 1
count = 0
max_count = 20

while count < max_count:
    count += 1

    old_a = a
    old_b = b

    a = old_b
    b = old_a + old_b

    print(old_a)


# Calculate the Fibonacci sequence
a = 0
b = 1
count = 0
max_count = 20

while count < max_count:
    count += 1

    old_a = a
    old_b = b

    a = old_b
    b = old_a + old_b

    print(old_a),


# password.py

# Waits until a password has been entered. Use control-C to break out
# without the password

# Note that this must not be the password so that the while loop runs at least once

password = 'foobar'

while password != 'unicorn':
    password = input("Password is: ")

print("Welcome in")





