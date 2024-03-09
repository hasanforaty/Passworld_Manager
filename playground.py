
try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print('File Not found error')
    file = open("test.txt", "w")
except KeyError as error_message:
    print(error_message)
    file = open("test.txt", "w")
except:
    print('we are getting all of error , its not recommended ')
else:
    content = file.read()
finally:
    file.close()

raise TypeError("it's a test for raising an error")
