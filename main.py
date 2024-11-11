import tkinter
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(width=200, height=200, padx=20, pady=20)
window.title("Password Manager")

canvas=Canvas(width=200, height=200)
logo=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website=Label(text="Website")
website.grid(row=1, column=0)

web_box=Entry(width=50)
web_box.grid(row=1, column=1, columnspan=2)
web_box.focus()

email=Label(text="Email/Username")
email.grid(row=2, column=0)

mail_box=Entry(width=50)
mail_box.grid(row=2, column=1, columnspan=2)
mail_box.insert(0, "personal.jonathanthomas@gmail.com")

password=Label(text="Password")
password.grid(row=3, column=0)

pass_box=Entry(width=50)
pass_box.grid(row=3, column=1, columnspan=2)



def random_pass():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pyperclip.copy(password)
    pass_box.insert(0, password)


def add_data():
    passdata = pass_box.get()
    webdata = web_box.get()
    emaildata = mail_box.get()
    ok=messagebox.askokcancel(title="Confirm", message="Save the password?")
    print(ok)
    if ok:
        with open("data.txt", "a") as f:
            f.write(f"{webdata} | {emaildata} | {passdata} \n")
            web_box.delete(0,END)
            pass_box.delete(0,END)



pass_button=Button(text="Generate Password", command=random_pass)
pass_button.grid(row=4, column=1)



pass_button=Button(text="Add",width=11, command=add_data)
pass_button.grid(row=4, column=2)

window.mainloop()