from tkinter import *
import random
import string

# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry('400x200')

# Label for password length
label = Label(window, text="Length of the password:", font=("Arial", 15))
label.place(x=10, y=20)

# Entry for password length
entry = Entry(window)
entry.place(x=200, y=20)

# Label to display password result
result_label = Label(window, text="", font=("Arial", 15))
result_label.place(x=10, y=100)

# Function to generate password
def pass_generate():
    try:
        length = int(entry.get())
        if length <= 4:
            result_label.config(text="Password too short (min 5 chars)")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            random_string = ''.join(random.choices(characters, k=length))
            result_label.config(text="Password: " + random_string)
    except ValueError:
        result_label.config(text="Please enter a valid number")


# Button to generate password
b = Button(window, text="Generate Password", command=pass_generate)
b.place(y=60, x=130)

window.mainloop()
