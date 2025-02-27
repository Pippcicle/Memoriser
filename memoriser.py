from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title('Memoriser')

def add_item():
    listbox.insert(END, txt_input.get())
    txt_input.delete(0,END)

    

save_btn = Button(window, text = 'SAVE', width = 15)
save_btn.pack(padx = 5, pady = 5)
txt_input = Entry(window,  width = 35)
txt_input.pack(padx = 5, pady = 5)
add_btn = Button(window, text = 'ADD', width = 15,command = add_item)
add_btn.pack(padx = 5, pady = 5)
open_btn = Button(window, text = 'OPEN', width = 15)
open_btn.pack(side = LEFT, padx = 5, pady = 5)
delete_btn = Button(window, text = 'DELETE', width = 15)
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