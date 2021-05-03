import random
from tkinter import *
import center_tk_window
from tkinter import messagebox

root = 0

def start():
    global root
    root = Tk()
    root.title("GJ Industries")
    # root.geometry("290x640+0+0")
    w = 290
    h = 640
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    heading = Label(root, text='Library code', font=("calibri", 20, "bold"))
    heading.pack()
    application()

#Brain of the code starts now

lend_books = open('Lend_books.txt', 'a+')
total_books = open('Total_books.txt', 'a+')

def lend(num_days, code_of_book):
    code_of_book = str(code_of_book)
    num_days = int(num_days)
    price = (num_days * 4) + 10
    y = code_of_book + "\n"
    lend_books.write(y)
    total_books.seek(0)
    lines = total_books.readlines()
    temp = open('Total_books.txt', 'w+')
    for x in lines:
        if x == code_of_book + "\n":
            pass
        elif x == code_of_book:
            pass
        else:
            temp.write(x)
    temp.close()
    msg = "The amout to be paid will be " + str(price) + " No tips accepted."
    messagebox.showinfo('Billing', msg)

# lend(10, "ASFD")

def add_books():
    root = Tk()
    root.withdraw()
    messagebox.showwarning("Warning", "You are adding a book.")
    code = random.randrange(0, 100)
    total_books.write(str(code)+"\n")
    msg = str(code) + " is the code for the book."
    messagebox.showinfo("Done", msg)
    root.destroy()

def check():
    lend_books.seek(0)
    lines = lend_books.readlines()
    root = Tk()
    root.withdraw()
    for x in lines:
        x = x.rstrip()
        msg = "Book with code " + str(x) + " is missing!"
        messagebox.showinfo("Missing", msg)
    root.destroy()

def take_back(num_days, extnd_days, code_of_book):
    code_of_book = code_of_book + "\n"
    if extnd_days <= 0:
        price = 0
        msg = "The price you will have to pay is gonna be " + str(price)
        messagebox.showinfo("Billing", msg)
    elif extnd_days != 0 and extnd_days > 0:
        price = 10 + (extnd_days * 5)
        msg = "The price you will have to pay is gonna be " + str(price)
        messagebox.showinfo("Billing", msg)

    lend_books.seek(0)
    lines = lend_books.readlines()
    temp = open("Lend_books.txt", "w+")
    for x in lines:
        if x == code_of_book or x + "\n" == code_of_book:
            total_books.write(x + "\n")
        else:
            temp.write(x)

# Brain ends here


def lend_fuc():
    lend_app = Tk()
    lend_app.title("GJ Industires")
    w = 290
    h = 640
    ws = lend_app.winfo_screenwidth()
    print("0")
    hs = lend_app.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    lend_app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    heading = Label(lend_app, text='Lend a book', font=("calibri", 20, "bold"))
    heading.pack()
    num_days = Label(text="Num of days:")
    num_days.place(x=10, y=50)
    num_days_input = IntVar()
    x = Entry(lend_app, textvariable=num_days_input)
    x.place(x=95, y=50)
    code = Label(text="Code of book:")
    code.place(x=10, y=100)
    code_input = StringVar()
    y = Entry(lend_app, textvariable=code_input)
    y.place(x=95, y=100)

    def call():
        print(num_days_input.get(), code_input.get())
        lend(str(num_days_input.get()), str(code_input.get()))
        lend_app.destroy()
        start()

    submit = Button(lend_app, text='Submit', command=call, width=15, height=5, font=("calibri", 13, "bold"))
    submit.place(x=70, y=500)

def take_back_fuc():
    take_app = Tk()
    take_app.title("GJ Industires")
    w = 290
    h = 640
    ws = take_app.winfo_screenwidth()
    hs = take_app.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    take_app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    heading = Label(take_app, text='Take back a book', font=("calibri", 20, "bold"))
    heading.pack()
    num_days = Label(text="Num of days:")
    num_days.place(x=10, y=50)
    num_days_input = IntVar()
    x = Entry(take_app, textvariable=num_days_input)
    x.place(x=95, y=50)
    extnd_days = Label(text="Extnd num of days:")
    extnd_days.place(x=10, y=100)
    extnd_days_input = IntVar()
    y = Entry(take_app, textvariable=extnd_days_input)
    y.place(x=125, y=100)
    code = Label(text="Code of book:")
    code.place(x=10, y=150)
    code_input = StringVar()
    z = Entry(take_app, textvariable=code_input)
    z.place(x=95, y=150)
    def call():
        print(num_days_input.get(), code_input.get())
        take_back(num_days_input.get(), extnd_days_input.get(), code_input.get())
        take_app.destroy()
        start()

    submit = Button(take_app, text='Submit', command=call, width=15, height=5, font=("calibri", 13, "bold"))
    submit.place(x=70, y=500)


def lend_2():
    root.destroy()
    lend_fuc()

def tack_back_2():
    root.destroy()
    take_back_fuc()

def check_2():
    root.destroy()
    check()
    start()

def add_books_2():
    root.destroy()
    add_books()
    start()

def application():
    button_lend = Button(root, text='Lend a book', width=20, height=5, command=lend_2, font=("calibri", 13, "bold"))
    button_lend.place(x=50, y=50)

    button_check = Button(root, text='Check', width=20, height=5, command=check_2, font=("calibri", 13, "bold"))
    button_check.place(x=50, y=200)

    button_add_books = Button(root, text='Add a book', width=20, height=5, command=add_books_2, font=("calibri", 13, "bold"))
    button_add_books.place(x=50, y=350)

    button_take_back = Button(root, text='Take back a book', width=20, height=5, command=tack_back_2, font=("calibri", 13, "bold"))
    button_take_back.place(x=50, y=500)

start()

root.mainloop()
lend_books.close()
total_books.close()