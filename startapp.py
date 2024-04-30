from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
import time
import pyttsx3

root = Tk()

# Creating the window
height = 450
width = 600
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='#0c71b9')

# Function to speak the welcome message
def speak_welcome_message():
    engine = pyttsx3.init()
    engine.say("Welcome to Alexander's Inventory Management System, the best and easiest to use Inventory management system out there")
    engine.runAndWait()


# Label showing the creator
created_by_label = Label(text='Created By Alexander Ojeniweh', bg='black', font=("arial", 15, "bold"), fg='white')
created_by_label.place(x=170, y=50)

# Speak the welcome message
speak_welcome_message()

# Progress bar and label
progress_label = Label(root, text="Please Wait...", font=('arial', 13, 'bold'), fg='white',bg='black')
progress_label.place(x=225, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=550, mode='determinate')
progress.place(x=25, y=390)

# Exit button
exit_btn = Button(text='x', bg='red', command=lambda: exit_window(), bd=0, font=("arial", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
exit_btn.place(x=570, y=0)

def exit_window():
    sys.exit(root.destroy())

def top():
    root.withdraw()
    os.system("python LoginAndRegistrationPage.py")
    root.destroy()

i = 0

def loadsystem():
    global i
    if i <= 100:
        if i == 90:
            time.sleep(0.02)
        txt = 'Please Wait...  ' + (str(i)+'%')
        progress_label.config(text=txt)
        progress_label.after(10, loadsystem)
        progress['value'] = i
        i += 1
    else:
        top()

loadsystem()

# Display the window
root.mainloop()
    