with open('index1.html','r') as weabpage:
    with open('output1.txt','a') as wf:
        page = weabpage.read()
        link_exit = True
        while link_exit:
            pos = page.find('<a href=')
            if pos == -1:
                link_exit = False
            else:
                first_quote = page.find('\"',pos)
                secon_quote = page.find('\"',first_quote+1)
                url = page[first_quote+1 : secon_quote]
                wf.write(url+'\n')
                page = page[secon_quote:]    