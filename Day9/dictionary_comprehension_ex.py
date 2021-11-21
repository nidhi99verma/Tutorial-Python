#count char in string
#simple way

def char_count(n):
    count = {}
    for char in n:
        count[char] = n.count(char)
    return(count)
print(char_count("NidhiVerma"))

#comprehension

string = "NidhiVerma"
char_count = {char:string.count(char) for char in string}
print(char_count)

