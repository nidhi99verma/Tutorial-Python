#def user_info(first_name,last_name,age):
#def user_info(first_name,last_name,age = None):
#def user_info(first_name,last_name = "Unknown",age):                                  #wrong
#def user_info(first_name = "Unknown",last_name,age):                                  #wrong 
#def user_info(first_name = "Unknown",last_name = "Unknown",age):                      #wrong 
def user_info(first_name = "Unknown",last_name = "Unknown",age = None):        
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")
user_info("Nidhi","Verma",25)
user_info()    
    