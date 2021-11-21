import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Menubar')

def func():
    print("Func call")

# menu
#menubar  = tk.Menu(win)
# simple menubar
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save As', command=func)
# menubar.add_command(label='Copy', command=func)
# menubar.add_command(label='Paste', command=func)

main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff=0)
edit_menu = tk.Menu(main_menu, tearoff=0)
selection_menu = tk.Menu(main_menu, tearoff=0)
view_menu = tk.Menu(main_menu, tearoff=0)
# go_menu = tk.Menu(main_menu, tearoff=0)
# run_menu = tk.Menu(main_menu, tearoff=0)
# terminal_menu = tk.Menu(main_menu, tearoff=0)
# help_menu = tk.Menu(main_menu, tearoff=0)
#file_menu
file_menu.add_command(label='New File', command=func)
file_menu.add_separator()
file_menu.add_command(label='New Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Save', command=func)
#edit_menu
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_separator()
edit_menu.add_command(label='Redo', command=func)
#Selection
selection_menu.add_command(label='Select All', command=func)
selection_menu.add_separator()
selection_menu.add_command(label='Copy Line Up', command=func)
selection_menu.add_separator()
selection_menu.add_command(label='Copy Line Down', command=func)
#view
view_menu.add_command(label='Run', command=func)
view_menu.add_separator()
view_menu.add_command(label='Output', command=func)
#cascade
main_menu.add_cascade(label ='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='Selection', menu=selection_menu)
main_menu.add_cascade(label='View', menu=view_menu)
# main_menu.add_cascade(label='Go', menu=go_menu)
# main_menu.add_cascade(label='Run', menu=run_menu)
# main_menu.add_cascade(label='Terminal', menu=terminal_menu)
# main_menu.add_cascade(label='Help', menu=help_menu)

win.config(menu= main_menu)
#win.config(menu= menubar)
win.mainloop()