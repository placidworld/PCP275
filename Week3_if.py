age = 10

if age == 10:
    print("ten")
print("How's that?")

age1 = 20

if age1 != 10:
    print("ten")
print("How's that?")


name = "me"
if name == "me":
    print("The same")


letter = "C"
if letter < "D":
    print("Less than D")

if letter > "B":
    print("Greater than B")


letter = "C"
if letter < "a":
    print("less than a")


if age >= 18:
    print("Congratulations!")
    print("You are old enough to vote.")
else:
    print("I'm sorry.")
    print("You are not old enough to vote.")


year = int(input("Enter year: "))
if year == 1:
    print("Freshman")
if year == 2:
    print("Sophomore")
if year == 3:
    print("Junior")
if year == 4:
    print("Senior")

year = int(input("Enter year: "))
if year == 1:
    print("Freshman")
elif year == 2:
    print("Sophomore")
elif year == 3:
    print("Junior")
elif year == 4:
    print("Senior")
else:
    print("Not a valid year")
    
