"""
GUI interface design
language: Python 3
Designed By: Tanmaya Prasad Mangaraj
Email: tanmaya.mangaraj@ltts.com
PS ID: 99005739
Designation: Intern, L&T Technology Services
"""
# Import module
import tkinter
import read
import converter
import input_check


# Create object
root = tkinter.Tk()
root.title("Currency Converter")

# Adjust size
root.geometry("300x100")



# YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
#url = str.__add__('http://data.fixer.io/api/latest?access_key=', "YOUR_ACCESS_KEY")
url = str.__add__('http://data.fixer.io/api/latest?access_key=', "2f06b767cd7d1cdbfa3343a3e26db44a")
c = converter.CurrencyConvertor(url)
d = read.read_rates_file()


def show():
    """Calculate output and show it"""
    cur1 = clicked.get()
    cur2 = clicked2.get()
    curr_input = a_var.get()

    if input_check.valid_input_check(curr_input):

        output= c.convert(cur1, cur2, float(curr_input))
    else:
        print("Invalid Input")
        output= "Invalid Input"
    label.config(text=output)


# Dropdown menu options
options = d

# datatype of menu text
clicked = tkinter.StringVar()
clicked2 = tkinter.StringVar()
a_var = tkinter.StringVar()

# initial menu text
clicked.set("INR")
clicked2.set("INR")


# Create Dropdown menu
drop = tkinter.OptionMenu(root, clicked, *options)
drop2 = tkinter.OptionMenu(root, clicked2, *options)

# creating a label for value input
a_label = tkinter.Label(root, text='Amount', font=('calibre', 10, 'bold'))
b_label = tkinter.Label(root, text='Amount', font=('calibre', 10, 'bold'))
a_entry = tkinter.Entry(root, textvariable=a_var, font=('calibre', 10, 'normal'))

# creating a entry for output
label = tkinter.Label(root, text=" ", bg="blue", width=20)
button = tkinter.Button(root, text="Convert", command=show)

a_label.grid(row=0, column=0)
a_entry.grid(row=0, column=1)
drop.grid(row=0, column=2)

b_label.grid(row=1, column=0)
label.grid(row=1, column=1)
drop2.grid(row=1, column=2)

button.grid(row=2, column=1)


root.mainloop()
