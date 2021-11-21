def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
d= {"name":"Nidhi", "age":25}# dict
func(**d)
#func(d)