import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from csv import DictWriter
import os

win = tk.Tk()

#label frame
label_frame = ttk.LabelFrame(win, text='Contact Detail')
label_frame.grid(row=0, column=0, padx=40, pady=10)

#labels
name_label = ttk.Label(label_frame, text='Enter Your Name Please : ', font=('Helvetica', 10,'bold'))
age_label = ttk.Label (label_frame, text='Enter Your Age Please : ',font=('Helvetica', 10,'bold'))

#entery box variables
name_var = tk.StringVar()
age_var = tk.StringVar()

#entery boxes
name_entery = ttk.Entry(label_frame, width=36, textvariable=name_var)
age_entery = ttk.Entry(label_frame, width=36, textvariable=age_var)

#grid
name_label.grid(row=0, column=0, pady=5, sticky=tk.W)
name_entery.grid(row=1, column=0, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, pady=5, sticky=tk.W)
age_entery.grid(row=1, column=1, pady=5, sticky=tk.W)

def submit():
    # m_box.showinfo('title_info', 'content of this message box !')
    # m_box.showwarning('title_warning', 'content of this message box !')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age =='':
        m_box.showerror('Error', 'Please fill both name and age !')
    else:
        try:
            age = int(age) 
        except ValueError:
            m_box.showerror('Error', 'Only digits are allowed in age !')
        else:
            if age < 18:
                m_box.showwarning('Warning', 'You are not 18 , visit this content on your own risk !')
        #print(f'{name} : {age}') 
        # fun to write
        with open('file.csv', 'a', newline='') as f:
            dict_writer = DictWriter(f, fieldnames=['User Name', 'User Age'])
            if os.stat('file.csv').st_size==0:
                dict_writer.writeheader()
            dict_writer.writerow({'User Name': name, 'User Age': age})

submit_btn = ttk.Button(win, text = 'Submit', command=submit)
submit_btn.grid(row=1, columnspan=2, padx=40)

win.mainloop()