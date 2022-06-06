class Time:
    """ Blueprint for a Time object """
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
    
    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def print_time(self):
        print(self.hour, ":", self.minute, ":", self.second)
    
# First time object
myTime1 = Time()
myTime1.print_time()
myTime1.set_time(1, 2, 3)

# Second Time object
myTime2 = Time()
myTime2.set_time(12, 0, 0)

print("My two time objects are storing: ")
myTime1.print_time()
myTime2.print_time()


###########################################################################
class Time:
    """ Blueprint for a Time object """
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
    
    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
    def print_time(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)

    def set_second(self, second):
        self.__second = second

    def get_second(self):
        return self.__second
    
