
"""
out_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'w')
out_file.write('Hello\n')
out_file.write('world!')
out_file.close()
"""

"""
out_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'w')
weekends = ['Saturday', 'Sunday']
out_file.writelines(weekends)
out_file.writelines(weekends)
out_file.close()
"""

"""
in_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'r')

print(in_file.read(1))
print(in_file.read())

in_file.close()

"""


"""
in_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'r')

print(in_file.readlines())

in_file.close()
"""

"""
out_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'a')
out_file.write('\nHello')
out_file.close()

out_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'a')
out_file.write('\nHello')
out_file.close()
"""

"""
in_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'r+')
print (in_file.read(1))
print (in_file.tell())
in_file.close()
"""

"""
in_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'r+')
print (in_file.readline())
print (in_file.tell())
in_file.close()
"""

"""
in_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'r+')
print (in_file.readline())
in_file.seek(12)

print (in_file.readline())
in_file.close()
"""

in_file = open('C:/Users/heart/Desktop/Python_Fun/mydata.txt', 'r+')
print (in_file.readline())
in_file.seek(0)

in_file.write('Hi!')
in_file.seek(0)
print (in_file.readline())
in_file.close()
