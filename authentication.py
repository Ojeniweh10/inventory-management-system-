from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
import time
import pyttsx3
from tkinter.ttk import LabelFrame, Label, Button, Entry, Frame, Scrollbar, Style
# import ttkthemes
from ttkthemes import themed_tk
from PIL import Image, ImageTk


root = Tk()

# Creating the window
height = 450
width = 600
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='#ffffff')

# Function to speak the login message
def login_message():
    engine = pyttsx3.init()
    engine.say("Please Enter Login Details Or sign Up if you Haven't yet")
    engine.runAndWait()

# Speak the login message
login_message()


 # Create login window with using themed_tk
# provides themed widgets and window styles for Tkinter
root = themed_tk.ThemedTk()
root.set_theme("scidpurple")
root.title("Alexander Enterprises Inventory Management System")
width = 1080
height = 700
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
 # get the dimensions of the screen, in pixels. The window is then positioned in the center of the screen by dividing these dimensions by 2 and subtracting half the width and height of the window.
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.columnconfigure(0, weight=1)
im = Image.open("images//icon.png")
icon = ImageTk.PhotoImage(im)
# Set the window icon using the PhotoImage object
root.wm_iconphoto(True, icon)
