#make a function that divide two number with handle all exception
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("numbers must be int or float")
    except:
        print("Unexpected error")
#print(divide(10,'2'))
print(divide(10,2))                    