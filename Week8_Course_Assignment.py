### Introduction to Python Programming
### Lesson 08 Assignment
### Sample Solution

# Initialize variables, note the list needs to be declared this way

number_list = []
sum = 0.0

user_number = eval(input("Please enter a number (-999 quits): "))

# Loop until the user is ready to quit
while (user_number != -999):
    number_list.append(user_number)
    sum = sum + user_number
    user_number = eval(input("Please enter a number (-999 quits): "))

# Make sure teh user entered something
if (len(number_list) != 0):
    # Compute average
    average = sum / len(number_list)

    # Do output
    print("Using the numbers: ")

    for i in range(len(number_list)):
        # Note the end = "" at the end will keep the output on the same line
        print(number_list[i], end = " ")

    print("\nThe average is: ", average)
else:
    print("No values were entered.")
    
