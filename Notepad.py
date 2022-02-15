import os
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showinfo

def SaveFile():
    global file 
    if file == None:
        file = asksaveasfile(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files", "*.*"),("Text Documents","*.txt")])
        if file == "":
            file =  None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def OpenFile():
    global file
    file = askopenfile(defaultextension=".txt",filetypes=[("All files", "*.*"),("Text Documents","*.txt")])
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f=open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def NewFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)

def exitFile():
    root.destroy()

def SaveFile():
    pass

def cutText():
    text.event_generate(("<<Cut>>"))

def copyText():
    text.event_generate(("<<Copy>>"))

def pasteText():
    text.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad" ,"This is made using tkinter")

root = Tk()
root.title("Untitled - Notepad")
root.wm_iconbitmap('notepad.ico')
root.geometry('644x788')

# writing area
text = Text(root, font="Lucida 10")
file = None
text.pack(expand = True, fill=BOTH)

# MenuBar
menu_ = Menu(root)
# File Menu 
file = Menu(menu_, tearoff = 0)
file.add_command(label = "New", command = NewFile) # create a new file
file.add_command(label =  "Open",command = OpenFile) #open a new file
file.add_command(label = "Save", command = SaveFile) # save a file
file.add_separator()
file.add_command(label = "Exit", command  = exitFile) #exit file
menu_.add_cascade(label = "File", menu = file)
#Edit Menu
edit = Menu(menu_, tearoff = 0)
edit.add_command(label = "Cut", command = cutText)
edit.add_command(label = "Copy", command = copyText)
edit.add_command(label = "Paste", command = pasteText)
menu_.add_cascade(label = "Edit", menu = edit)
# Help Menu
help=Menu(menu_, tearoff =  0)
help.add_command(label = "About Notepad", command = about)
menu_.add_cascade(label = "About", menu = help)


root.config(menu=menu_)

scrollBar = Scrollbar(text) # making a scroll bar
scrollBar.pack(side = RIGHT, fill = Y)
scrollBar.config(command = text.yview)
text.config(yscrollcommand=scrollBar.set)

root.mainloop()