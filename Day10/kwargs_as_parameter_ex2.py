def func(name,**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
func("Ajai",first_name = "Nidhi",last_name = "Verma")#name = Ajai,kwargs(dict)=first_name = "Nidhi",last_name = "Verma