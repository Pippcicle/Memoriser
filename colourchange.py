from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.title('colours')

def add_item():
    listbox.insert(END, txt_input.get())
    txt_input.delete(0,END)


save_btn = Button(window, text = 'SAVE COLOURS', width = 15, bg = '#242038', fg = '#CAC4CE')
save_btn.pack(padx = 5, pady = 5)
txt_input = Entry(window,  width = 35, bg = '#8D86C9')
txt_input.pack(padx = 5, pady = 5)
add_btn = Button(window, text = 'ADD COLOUR', width = 15,command = add_item, bg = '#242038', fg = '#CAC4CE')
add_btn.pack(padx = 5, pady = 5)
delete_btn = Button(window, text = 'DELETE COLOIR', width = 15, bg = '#242038', fg = '#CAC4CE')
delete_btn.pack(side = RIGHT, padx = 5, pady = 5)

frame = Frame(window)
frame.pack(side = RIGHT)

scrollbar = Scrollbar(frame, orient = 'vertical')
scrollbar.pack(side = RIGHT, fill = Y )

listbox = Listbox(frame, width = 70, yscrollcommand = scrollbar.set, bg = '#725AC1')
colours = ("Pink", "Blue", "Green", "Yellow", "Purple", "Red", "Orange")
for color in colours:
    listbox.insert(END, color)

listbox.pack(side = LEFT, padx = 5)
scrollbar.config(command = listbox.yview)



window.mainloop()
