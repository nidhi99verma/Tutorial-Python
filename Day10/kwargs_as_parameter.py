#kwargs(keyword argument)gether all argumentas a dictionary
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(first_name = "Nidhi",last_name = "Verma")#dict    