import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('LOOP')
#labels
labels = ['What is your name : ', 'What is your age : ', 'What is your gender : ', 'Country : ', 'State',
 'City : ', 'address']

# name_label = ttk.Label(win, text = 'What is your name : ')
# name_label.grid(row = 0, column = 0, sticky = tk.W)

for i in range(len(labels)):
    current_label = 'label'+str(i)    #label0,label1,---
    current_label = ttk.Label(win, text = labels[i])
    current_label.grid(row = i, column = 0, sticky = tk.W, padx=20, pady=2) # x: left right padding, y: top bottom padding
#entery box
name_var = tk.StringVar()
user_info = {
    'name': tk.StringVar(), 
    'age': tk.StringVar(), 
    'gender': tk.StringVar(), 
    'country': tk.StringVar(), 
    'state': tk.StringVar(), 
    'city': tk.StringVar(),
    'address':tk.StringVar()
}
counter = 0
for i in user_info:
    current_entrybox = 'entry' + i # entryname  # entryage
    current_entrybox = ttk.Entry(win, width = 16, textvariable = user_info[i])
    current_entrybox.grid(row = counter, column = 1, padx=20, pady=2)
    counter += 1

# name_entry = ttk.Entry(win, width = 16, textvariable = name_var)
# name_entry.grid(row = 0, column = 1)

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get()) 
    print(user_info.get('state').get())
    print(user_info.get('city').get())
    print(user_info.get('address').get())

submit_btn = ttk.Button(win, text='Submit', command =submit)
l = len(labels)+1
submit_btn.grid(row=l, column=0, padx=20, pady=2)

win.mainloop()
