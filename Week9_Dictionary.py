days_in_month = {'Jan': 31, 'Feb':28, 'Mar': 31}

#days_in_month['Apr'] = 30
#days_in_month['May'] = 31
#days_in_month['Jun'] = 30

days_in_month2 = {'Apr': 30, 'May': 31, 'Jun': 30}

days_in_month.update(days_in_month2)


print (days_in_month.items())
print (days_in_month.values())



print(days_in_month)

print (days_in_month.keys())
print (days_in_month.values())

print ('Feb' in days_in_month)

print ("Is Feb present: ", 'Feb' in days_in_month)


#####################################

odds = {1:'one', 3:'three', 5:'five'}
evens = {2:'two', 4:'four', 6:'six'}
odds.clear()

print ("After clearing odds:")
print (odds)

#del evens  -- 
print ("After clearing evens:")
print (evens)



######################################
words = {}
value = input("Please enter a word (or -999 to quit): ")
while (value != '-999'):
   if value in words:
      words [value] = words [value] + 1
   else:
       words [value] = 1

   value = input("Please enter a word (or -999 to quit): ")

for current_key in words.keys():
   print (current_key, 't', words [current_key] )



###################################################

words = {}
value = input("Please enter a word (or -999 to quit): ")

while (value != '-999'):
    if value in words:
        words [value] = words [value] + 1
    else:
        words [value] = 1

    value = input("Please enter a word (or -999 to quit): ")

print ("The ordered list of words are:")

my_keys = list(words.keys())

my_keys.sort()

for current_key in my_keys:
    print(current_key, 't', words [current_key] )
    print(words)   



################################################
################################################
################################################

words = {}
value = input("Please enter a word (or -999 to quit): ")

while (value != '-999'):
    if value in words:
        words [value] = words [value] + 1
    else:
        words [value] = 1

    value = input("Please enter a word (or -999 to quit): ")

print ("The ordered list of words are:")

my_keys = list(words.keys())

my_keys.sort()

for current_key in my_keys:
    print(current_key, 't', words [current_key] )
    print(words)   

print ()

print ("Ordered by number of times entered:")

temp_list = []

# Select a key in the dictionary
for current_key in words.keys():
    # determine the number of words in the sorted list
    list_length = len(temp_list)

    # start looking at position 0
    placeholder = 0

    # As long as there are still items in the list
    while placeholder < list_length:

        # Get the word in the sorted list
        list_key = temp_list [placeholder]

        # Determine if this word has been entered
        # more times than the current word
        if words [list_key] > words [current_key] :
            break

        # It wasn't, so let's look at the next word
        # in the sorted list
        placeholder = placeholder + 1

    # We found the location in the sorted list for
    # this word, insert it
    temp_list.insert(placeholder, current_key)

for current_key in temp_list:
    print (current_key, 't', words [current_key] )
