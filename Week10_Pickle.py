class Time:
        """ The blueprint for a Time Class object"""
        def __init__ (self, hour, minute, second):
            self.__hour = hour
            self.__minute = minute
            self.__second = second
        def print_time(self):
            print (self.__hour, ":", self.__minute, ":", self.__second)

import pickle
from Time import Time

myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
print (pickled_time)


### Write the pickled result to a file
myTime1 = Time(1, 2, 3)
out_file = open('data.txt', 'wb')
pickled_time = pickle.dump(myTime1, out_file)
out_file.close()


### Unpickled
import pickle
from Time import Time
myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
unpickled_time = pickle.loads(pickled_time)
unpickled_time.print_time()


### Open teh file for reading bytes with 'rb'
import pickle
from Time import Time

in_file = open('data.txt', 'rb')

unpickled_time = pickle.load(in_file)

unpickled_time.print_time()


######
import shelve
db_file = shelve.open('letters.txt', 'c')
db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file ['end'] = ['x', 'y', 'z']
db_file.close()


######
import shelve
db_file = shelve.open('letters.txt', 'c')
print ( list(db_file.keys( )))
print ("Original containing vowels:", 'vowels' in db_file )
del db_file ['vowels']
print ("After deleting vowels:", 'vowels' in db_file )
print ( list(db_file.keys( )))
db_file.close()
