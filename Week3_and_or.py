age = int(input("How old are you? " ))
registered = input("Are you registered? (Y/N) ")

if age >= 18 and registered == 'Y':
    print("You are ready to vote!")
else:
    print("You are not ready to vote.")

answer = input("Please enter a letter: ")
if answer == 'y' or 'Y':
    print("You entered 'y' or 'Y'")
          
