try:
    outfile = open('data.txt', 'r')
    outfile.write("Hello")
    print("Complete")
    outfile.close()    
except IOError:
    print("Error with the file")
except Exception:
    print("An error occured")

print("Have a nice day")
