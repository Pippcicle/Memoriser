from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title('Memoriser')

def add_item():
    listbox.insert(END, txt_input.get())
    txt_input.delete(0,END)


def delete_item(): 
    index = listbox.curselection()
    if index :
        listbox.delete(index)

def open_file(): 
    my_file = askopenfile(title = 'open file')
    if my_file is not None : 
        listbox.delete(0, END)
        items = my_file.readlines()
        for item in items :
            listbox.insert(END, item)

def save_file():
    my_file = asksaveasfile(defaultextension = '.txt')
    if my_file is not None : 
        for item in listbox.get(0, END) : 
            print(item, file = my_file)
        listbox.delete(0, END)

save_btn = Button(window, text = 'SAVE', width = 15, command = save_file)
save_btn.pack(padx = 5, pady = 5)
txt_input = Entry(window,  width = 35)
txt_input.pack(padx = 5, pady = 5)
add_btn = Button(window, text = 'ADD', width = 15,command = add_item)
add_btn.pack(padx = 5, pady = 5)
open_btn = Button(window, text = 'OPEN', width = 15, command = open_file)
open_btn.pack(side = LEFT, padx = 5, pady = 5)
delete_btn = Button(window, text = 'DELETE', width = 15, command = delete_item)
delete_btn.pack(side = RIGHT, padx = 5, pady = 5)

frame = Frame(window)
frame.pack(side = RIGHT)

#Scroll bar
scrollbar = Scrollbar(frame, orient = 'vertical')
scrollbar.pack(side = RIGHT, fill = Y )

#listbox
listbox = Listbox(frame, width = 70, yscrollcommand = scrollbar.set, bg = 'pink')
for i in range(1,21):
    listbox.insert(END, "List" + str(i))

listbox.pack(side = LEFT, padx = 5)
scrollbar.config(command = listbox.yview)



window.mainloop()