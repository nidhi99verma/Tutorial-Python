# Tkinter
# from tkinter import *                                                # import all class(__init)
# import tkinter

# import tkinter as tk
# win = tk.Tk()
# win.mainloop()

import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title('GUI')
# create labels
# widgets--> label, buttons, radio-buttons...all available in tk
# above all above widgets available in subclass of tk --ttk (but ttk looks better then tk)
name_label = ttk.Label(win, text='Enter your name : ')
name_label.grid(row = 0, column = 0, sticky=tk.W)           # pack or grid : for layout

email_label = ttk.Label(win, text='Enter your email : ')
email_label.grid(row = 1, column = 0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row = 2, column = 0, sticky=tk.W)

gender_label = ttk.Label(win, text='Select your gender : ')
gender_label.grid(row = 3, column = 0, sticky=tk.W)

# create entry box
name_var = tk.StringVar()                                       # for store users input
name_entery = ttk.Entry(win, width=16, textvariable = name_var)
name_entery.grid(row = 0, column = 1)
name_entery.focus()

email_var = tk.StringVar()                                       
email_entery = ttk.Entry(win, width=16, textvariable = email_var)
email_entery.grid(row = 1, column = 1)

age_var = tk.StringVar()
age_entery = ttk.Entry(win, width=16, textvariable = age_var)
age_entery.grid(row = 2, column = 1)

# create combobox

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14 , textvariable = gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(1)
gender_combobox.grid(row = 3, column = 1)

# radio button

usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value= 'Student', variable = usertype)
radiobtn1.grid(row = 4, column = 0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher', value= 'Teacher', variable = usertype)
radiobtn2.grid(row = 4, column = 1)

# check button

checkbtn_var = tk.IntVar()
checkbtn1 = ttk.Checkbutton(win, text='Check if you want to subscribe to our newsletter', variable=checkbtn_var)
checkbtn1.grid(row = 5, columnspan = 3)

# # create button

# def action():
#     username = name_var.get()
#     userage = age_var.get()
#     useremail = email_var.get()
#     print(f'{username} is {userage} years old , {useremail}')

#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         subscribed = 'No'
#     else:  
#         subscribed = 'Yes'   
#     print(user_gender, user_type, subscribed)  

#     with open('file.txt', 'a') as f:
#         f.write(f'{username},{userage},{useremail},{user_gender},{user_type},{subscribed}\n')   

#     name_entery.delete(0, tk.END)
#     email_entery.delete(0, tk.END)
#     age_entery.delete(0, tk.END)

#     name_label.configure(foreground='#b388ff')
#     email_label.configure(foreground='#88ffb3')
#     age_label.configure(foreground='#ffb388')

#     Submit_button.configure(foreground='Blue')    

# write to csv files

def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:  
        subscribed = 'Yes'   

# write to csv file

    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['User Name', 'User Email', 'User Age', 'User Gender', 'User Type', 'Subcribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'User Name': username,
            'User Email': useremail,
            'User Age': userage,
            'User Gender': user_gender,
            'User Type': user_type,
            'Subcribed': subscribed
        })

    name_entery.delete(0, tk.END)
    email_entery.delete(0, tk.END)
    age_entery.delete(0, tk.END)

    name_label.configure(foreground='#b388ff')
    email_label.configure(foreground='#88ffb3')
    age_label.configure(foreground='#ffb388')

    Submit_button.configure(foreground='Blue')    
    

Submit_button = tk.Button(win, text='Submit', command=action)
Submit_button.grid(row = 6, column = 0)

win.mainloop()                                                   # infinet time show

# C:\Users\Nidhi\.conda\pkgs\python-3.8.5-he1778fa_0\Lib\tkinter


