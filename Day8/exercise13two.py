#make a function that coutn char in word 
def word_counter(s):
    count = {}
    for char in s:
        count [char] = s.count(char)
    return count
print(word_counter('NidhiVerma'))        