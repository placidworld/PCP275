# Introduction to Python Programming
# Lesson 04 Assignment

count = 0
sum = 0.0
average = 0.0
value = int(input("Please enter a number (-1 quits): "))

while (value != -1):
    sum =+ value
    count =+ 1

    value = int(input("Please enter a number (-1 quits): "))

# This is necessary, in case the user doesn't enter any values
if (count != 0):
    average = sum / count

print ("The sum of these numbers is", sum)
print ("The average of these numbers is", average)
