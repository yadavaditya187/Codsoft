from tkinter import*
from tkinter import messagebox


# Create the main window
root = Tk()
root.title("TO-DO LIST")
root.geometry("620x420")
tasks=[]

# Create functions

def update_listbox():
    # Clear the current list
    clear_listbox()

    # update items to list
    for task in tasks:
        list_box.insert("end", task)


def clear_listbox():
    list_box.delete(0, "end")


def add_task():
    # Get the task
    task = entry1.get()
    # Append the task to list
    if task != '':
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Alert!", "Please write a task to add")
        # display['text'] = "Please enter a task!"
        entry1.delete(0, 'end')
    entry1.delete(0, 'end')



def clear():
    task = list_box.get('active')
    if task in tasks:
        tasks.remove(task)
    else:
        messagebox.showwarning("Alert!","Please select a task to delete")
    # Update list box
    update_listbox()


def clear_all():
    global tasks
    # Clear the list
    tasks = []

    update_listbox()

def exit():
    quit()




#creating labels
lab1 = Label(text="",bg="purple")
lab1.place(x=0,y=0,height=90,width=620)

lab1 = Label(text="",bg="sky blue")
lab1.place(x=0,y=91,height=330,width=620)

a = Label(text="To-Do List",font=('calibre',30, 'italic'),bg="purple")
a.place(x=60,y=20)
b = Label(text="Add Items",font=('calibre',15),bg="sky blue")
b.place(x=60,y=90)

#Entry Box
entry1= Entry(root,font=('italic',10, 'bold'),relief=RIDGE,bg="white")
entry1.place(x=50,y=130,height=50,width=420,relx=0,rely=0)
entry1.focus()

#Creating buttons

button1 = Button(root,text="Add",bg="light blue",font=('calibre',10, 'bold'),command=add_task)
button1.place(x=450,y=130,height=50,width=80)

button2 = Button(root,text="Delete",bg="light blue",font=('calibre',10, 'bold'),command=clear)
button2.place(x=450,y=200,height=50,width=80)

button3 = Button(root,text="Clear All",bg="light blue",font=('calibre',10, 'bold'),command=clear_all)
button3.place(x=450,y=250,height=50,width=80)

button4 = Button(root,text="Exit X ",bg="light blue",font=('calibre',10, 'bold'),command=exit)
button4.place(x=450,y=300,height=50,width=80)



list_box=Listbox(root,font="calibre,15,bold",activestyle="underline",relief=RIDGE)
list_box.place(x=50,y=200,height=300,width=400)

root.mainloop()