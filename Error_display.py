from tkinter import *

def choice(option):
    if option == "ok":
        pop.destroy()
    elif option == 'oka':
        gpop.destroy()

def Error(er_txt):
    global pop
    pop=Tk()
    pop.title("ERROR")
    pop.config(bg='black')

    screen_width = pop.winfo_screenwidth()  # Width of the screen
    screen_height = pop.winfo_screenheight()
    x = (screen_width/2) - (650/2)
    y = (screen_height/2) - (150/2)

    pop.geometry('%dx%d+%d+%d' % (650,130, x, y))

    my_label = Label(pop,text=er_txt,bg='black',fg='purple',font=("hellvetica",15))
    my_label.pack(pady=20)

    my_frame = Frame(pop,bg="black")
    my_frame.pack(pady=5)

    yes = Button(my_frame,text="Okay",command=lambda: choice("ok"),bg='purple',height=2,width=8)
    yes.grid(row = 2,column=2,padx='10') 

    pop.mainloop()

def guideline():
    global gpop
    gpop=Tk()
    gpop.title("Guidelines")
    gpop.config(bg='black')

    screen_width = gpop.winfo_screenwidth()  
    screen_height = gpop.winfo_screenheight()
    x = (screen_width/2) - (900/2)
    y = (screen_height/2) - (600/2)

    gpop.geometry('%dx%d+%d+%d' % (750,450, x, y))

    gdlns='''Please read the following guidelines carefully\n
    1. Types of cells \n Classical cell - Contains X or O in them \n Quantum cell - do not have X or O in them

    2. Types of moves \n Classical move - played on a quantum cell 
    \n Quantum move - 2 cells should be selected \n\t a.First cell has to be a quantum cell which will act as a control cell \n\t b. Second cell has to be a classical cell which will be the target cell
    \n Entangle move - After selecting the control and target cell proceed to entangle'''

    my_label = Label(gpop,text=gdlns,bg='black',fg='purple',font=("hellvetica",15),justify="left")
    my_label.pack(pady=20)

    my_frame = Frame(gpop,bg="black")
    my_frame.pack(pady=5)

    yes = Button(my_frame,text="Okay",command=lambda: choice("oka"),bg='purple',height=2,width=8)
    yes.grid(row = 2,column=2,padx='10') 

    gpop.mainloop()