

from tkinter import *
from tkcalendar import Calendar


# Create Object
root = Tk()


# Set geometry
root.geometry("400x400")
root.configure(background="yellow")


cal = Calendar(root, selectmode='day', year=2023, month=7, day=26)
cal.configure(background="red")
cal.pack(pady=100)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())


Button(root, text="Get Date", background="LightCoral", command=grad_date).pack(pady=20)

date = Label(root, text="Result", background="green")
date.pack(pady=10)
root.mainloop()
