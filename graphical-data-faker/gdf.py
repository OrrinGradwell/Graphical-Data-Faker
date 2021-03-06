""" Libraries """
import random
import tkinter as tk
import pyperclip
import datetime

from tkinter import *
from tkinter import ttk
from random import randrange
from faker import Faker
fake = Faker()


def luhn(year):
    def luhn_checksum(idnum):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(idnum)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    def calculate_luhn(partial_id):
        check_digit = luhn_checksum(int(partial_id) * 10)
        return check_digit if check_digit == 0 else 10 - check_digit


    if __name__ == "__main__":
        while True:
            number = year + f'{random.randint(1, 12):02d}' + f'{random.randint(1, 28):02d}' + str(random.randint(0000, 9999)) + '0' + str(random.randint(0, 9))
            parity = calculate_luhn(number)
            IdNumber = number + str(parity)
            if len(IdNumber) != 13:
                continue
            elif not len(IdNumber):
                # print("EMPTY")
                continue
            global Generated
            Generated = IdNumber
            break


def cell():
    carrier = ['072', '073', '074', '082', '083', '084']
    threeDigit = str(random.choice(carrier))
    sevenDigit = str(randrange(1111111, 9999999))
    global Cell
    Cell = threeDigit + sevenDigit


def clear():
    Firstname_Field.delete(0, END)
    Lastname_Field.delete(0, END)
    RSA_ID_Field.delete(0, END)
    Cell_Field.delete(0, END)
    Email_Field.delete(0, END)


def clear_button():
    clear()


def generate_data():
    clear()

    first = fake.first_name()
    Firstname_Field.insert(0, first)

    last = fake.last_name()
    Lastname_Field.insert(0, last)

    email = first + '_' + last + '@midev.co.za'
    Email_Field.insert(0, email)

    cell()
    Cell_Field.insert(0, Cell)

    current_year = datetime.datetime.today().strftime("%Y")
    required_age = Choose_Age_Field.get()

    a = int(current_year)

    if not required_age.isdigit():
        luhn(f'{random.randint(70, 99):02d}')
    else:
        b = int(required_age)
        c = a - b
        luhn(str(c)[2:])

    RSA_ID_Field.insert(0, Generated)


def copy_first_name():
    firstname = Firstname_Field.get()
    pyperclip.copy('')
    pyperclip.copy(firstname)


def copy_last_name():
    lastname = Lastname_Field.get()
    pyperclip.copy('')
    pyperclip.copy(lastname)

def copy_rsa_id():
    rsa_id = RSA_ID_Field.get()
    pyperclip.copy('')
    pyperclip.copy(rsa_id)


def copy_cell():
    cellphone = Cell_Field.get()
    pyperclip.copy('')
    pyperclip.copy(cellphone)


def copy_email():
    email = Email_Field.get()
    pyperclip.copy('')
    pyperclip.copy(email)


gdf = Tk()
gdf.wm_attributes('-topmost', 1)
gdf.geometry('400x320')
gdf.title('Graphical Data Faker')

tab_control = ttk.Notebook(gdf)
personal = ttk.Frame(tab_control)
tab_control.add(personal, text='Personal Details')

Generate_Button = tk.Button(personal, text='Generate Data', command=generate_data, width=15, height=1)
Clear_Button = tk.Button(personal, text='Clear All Fields', command=clear_button, width=15, height=1)
Copy_First_Name_Button = tk.Button(personal, text='Copy Firstname', command=copy_first_name, width=15, height=1)
Copy_Last_Name_Button = tk.Button(personal, text='Copy Lastname', command=copy_last_name, width=15, height=1)
Copy_RSA_ID_Button = tk.Button(personal, text='Copy RSA ID', command=copy_rsa_id, width=15, height=1)
Copy_Cell_Number_Button = tk.Button(personal, text='Copy Cell Number', command=copy_cell, width=15, height=1)
Copy_Email_Button = tk.Button(personal, text='Copy Email Address', command=copy_email, width=15, height=1)

Generate_Button.grid(column=0, row=0, pady=10, padx=10)
Clear_Button.grid(column=1, row=0, pady=10, padx=10)
Copy_First_Name_Button.grid(column=0, row=1, pady=10, padx=10)
Copy_Last_Name_Button.grid(column=0, row=2, pady=10, padx=10)
Copy_RSA_ID_Button.grid(column=0, row=4, pady=10, padx=10)
Copy_Cell_Number_Button.grid(column=0, row=5, pady=10, padx=10)
Copy_Email_Button.grid(column=0, row=6, pady=10, padx=10)

Firstname_Field = tk.Entry(personal, width=30)
Lastname_Field = tk.Entry(personal, width=30)
RSA_ID_Field = tk.Entry(personal, width=30)
Choose_Age_Field = tk.Entry(personal, width=30)
Cell_Field = tk.Entry(personal, width=30)
Email_Field = tk.Entry(personal, width=30)

Firstname_Field.grid(column=1, row=1)
Lastname_Field.grid(column=1, row=2)
RSA_ID_Field.grid(column=1, row=4)
Choose_Age_Field.grid(column=1, row=3)
Cell_Field.grid(column=1, row=5)
Email_Field.grid(column=1, row=6)

Choose_Age_Label = tk.Label(personal, text='Select Age:')
Choose_Age_Label.grid(column=0, row=3)

tab_control.pack(expand=1, fill='both')
gdf.mainloop()
