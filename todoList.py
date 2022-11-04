from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("to-do_list")
root.geometry("400x630+400+50")
root.resizable(False, False)
bg = Image.open('bg.jpg')
bground = ImageTk.PhotoImage(bg)
bg_lbl = Label(root, image=bground)
# bg_lbl.place(x=0,y=0)
bg_lbl.pack(padx=0, pady=0)

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
        listbox.insert(END, "\n")

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
                listbox.insert(END, "\n")

    except:
        file=open('tasklist.txt','w')
        file.close()

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

task_list = []

img_icon = PhotoImage(file="task.png")
root.iconphoto(False, img_icon)

# heading
heading = Label(root, width="400", height="3", bg="purple")
heading.place(x=0,y=10)

noteImage = PhotoImage(file="task.png")
icn=Label(heading, image=noteImage, bg="purple")
icn.place(x=30, y=3)
Label(heading, text="To-Do List", font="courier 20 underline", bg="purple", fg="white").place(x=140, y=3)

# entry_frame
frame1=Frame(root,width="400",height="48",bg="white",bd=0)
frame1.place(x=0,y=160)

task=StringVar()
task_entry=Entry(frame1,width=18,font="courier 20 bold", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame1,text="ADD",font="courier 20 bold",width=6,bg="#5a95ff", fg="white",bd=0,command=addTask)
button.place(x=300,y=0)

# list

frame2=Frame(bg_lbl,bd=0,width=700,height=280,bg="white")
frame2.pack(pady=(240,0),padx=10)

sb = Scrollbar(frame2)
sb.pack(side = RIGHT, fill = Y)

listbox=Listbox(frame2,font=('courier', 12),width=40,height=16,bg="white",cursor="hand2",bd=0, yscrollcommand = sb.set )
listbox.pack(side=LEFT,fill=BOTH,padx=8,pady=8)

openTaskFile()

# delete
# delete_icon=PhotoImage(file="delete.png")
frame3=Frame(bg_lbl,bd=0,width=400,height=100,bg="red")
frame3.pack(pady=(19,23))
Button(frame3,text="DELETE",font=('courier', 15),bd=0,bg="red",padx=5,pady=0,command=deleteTask).pack(side=BOTTOM,fill=BOTH,padx=0)


root.mainloop()
