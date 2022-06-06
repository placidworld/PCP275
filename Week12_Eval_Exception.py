### eval evaluate the expression
value = eval(input("Enter a number: "))


### Try except blocks
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except NameError:
    print("You must enter a number for your age")

print("Have a nice day. Good bye. ")

### Interesting way
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except SyntaxError:
    print("You must enter a number for your age")

print("Have a nice day. Good bye. ")


### Will run no matter what
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except NameError:
    print("You must enter a number for your age")
except SyntaxError:
    print("You must enter a number for your age")

print("Have a nice day. Good bye. ")


### Multiple or even more Try/Except blocks
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except (NameError, SyntaxError):
    print("You must enter a number for your age")

print("Have a nice day. Good bye. ")


### Better way to handle all Exceptions
### NameError, SyntaxError, ZeroDivisionError, KeyError, SystemError,
### IndexError, IOError ...
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except Exception:
    print("You must enter a number for your age")

print("Have a nice day. Good bye. ")

### Even better solution
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except NameError:
    print("You must enter a number for your age")
except Exception:
    print("Something unexpected has happened")

print("Have a nice day. Good bye. ")


### Exception order is important
### or it will show interesting thing
try:
    age = eval(input("Please enter your age: "))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except Exception:
    print("Something unexpected has happened")
except NameError:
    print("You must enter a number for your age")


### IndexError
try:
    my_list = [0, 1, 2]
    print(my_list[4])
except IndexError as ie:
    print(ie)

###
try:
    infilw = open('datafile.txt', 'r')
    infile.write("hello")
    
    infile.close()

except IOError as ioe:
    print("filename:", ioe.filename)
    print("strerror:", ioe.strerror)


###
try:
    user_num = eval(input("Please enter a number: "))
    result = 10 /user_num
except(NameError, SyntaxError):
    print("The value you entered was not a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("The result of dividing 10 by your number is", result)

####
try:
    infile = open('data.txt', 'r')
    try:
        value = infile.readline()
        number = int(value)
        print(number)
    finally:
        infile.close()
        print("The data file was closed")
except IOError as io:
    print("Could not open file:", io.filename)
except ValueError:
    print("Could not convert", value, "to a number")
