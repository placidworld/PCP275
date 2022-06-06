def change_value(value):
    """ This function changes the value passed in to 1 """
    print("Inside, value is: ", value)
    value = 1
    print("Inside, value is changed to: ", value)
    
number = 5
print("Outside, number is: ", number)
change_value(number)
print("Outside, number is now: ", number)


####################
def print_value(value):
    """ This function prints two lines of text"""
    print("Your value is: ", value)

print_value(5)
print_value("number")

name = "Pat"
print_value(name)

###################
def change_number():
    """ This function changes the value passed in to 1 """
    global number
    number = 1
    
number = 5
print("Outside, number is: ", number)
change_number()
print("Outside, number is now: ", number)



###################
def square(num):
    """ This function calcualtes the square of a number """
    result = num * num
    return result
    
for i in range(1, 11):
    print(square(i))


###########################
def print_welcome():
    """ This function prints two lines of text"""
    print("Welcome to my program")
    print("I hope you like it")

print(print_welcome())


##################################
def square(num = 1):
    """ This function calculates the squared of a number"""
    result = num * num
    return result

print(square())


##################################
def prompt_user(prompt, num_tries = 2):
    """ This function prompts the user a certain number of times"""
    answer = input(prompt)
    
    while (answer != "yes" and answer != "no" and num_tries > 1):
        num_tries = num_tries - 1
        print("Try again")
        answer = input(prompt)

prompt_user("Enter yes or no: ")
prompt_user("Enter yes or no: ", 3)




