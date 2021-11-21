#use else to enhance readablity of try exception block
#else block tab chalega jab try block sucessfully chalega
#chae exception aae ya na aae finally walla block chalega

while True:
    try:
        number = int(input('enter a number : '))
    except ValueError:
        print("Please type integer !! s")
    except:
        print("unexpected error !!!")
    else:
        print(f"use input = {number}")
        break
    finally:
        print("finally block.......")            