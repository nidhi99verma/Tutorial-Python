#extract web link from html file
with open('index .html','r') as weabpage:
    with open('output.txt','a') as wf:
        for line in weabpage.readlines():
            if "<a href=" in line:
                pos = line.find('<a href=')
                first_quote = line.find('\"',pos)
                second_quote = line.find('\"',first_quote+1)
                url = line[first_quote+1 : second_quote]
                wf.write(url+'\n')