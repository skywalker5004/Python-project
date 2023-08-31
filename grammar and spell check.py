####################################

# PYTHON MINI PROJECT
# GRAMMAR AND SPELLING CHECK
# Btech Mechatronics - Batch H2
# H027 - Shrikant Kothimbire
# H038 - Asmita Pai

####################################

from tkinter import *
# importing librabry for GUI

import tkinter as tk
import customtkinter as ctk

from gingerit.gingerit import GingerIt
# importing librabry for grammar and spelling check

####################################

app = tk.Tk()
# generate window for GUI

app.geometry("532x530")
# GUI window size

app.title("Grammar and spelling check")
# window title

ctk.set_appearance_mode("dark")
# window apprearance

####################################

label3 = Label(master = app, text = "Grammar and spelling check", fg = "Black", font = ("Bahnschrift", 20, "bold"), anchor = "center")
# Output
label3.place(x = 10, y = 10)

####################################

label4 = Label(master = app, text = "Enter text:", fg = "#1C82AD", font = ("Bahnschrift", 20))
# Output
label4.place(x = 10, y = 60)

####################################

prompt = ctk.CTkEntry(master = app, height = 40, width = 512, text_color = "black", fg_color = "white", font = ("Bahnschrift", 26))
# generates text box 

prompt.place(x = 10, y = 110)
# location: GUI app, x and y 

####################################

def generate():
    
    text = prompt.get()
    parser = GingerIt()
    dict = parser.parse(text)
    label1 = Label(master = app, text = dict["result"], fg = "black", font =("Bahnschrift", 20), wraplength = 510, anchor="w", justify = "left")
    label1.place(x = 10, y = 260)
    print(dict)

####################################

trigger = ctk.CTkButton(master = app, height = 40, width = 120, text_color = "white", fg_color = "#1C82AD", font = ("Bahnschrift", 24), command = generate)
# generates command button

trigger.configure(text = "Correct")
# command button confirguration

trigger.place(x = 206, y = 170)
# command button location

####################################

label2 = Label(master = app, text = "The Correct Sentence Is:", fg = "#1C82AD", font = ("Bahnschrift", 20))
# Output
label2.place(x = 10, y = 220)
# output location

####################################

app.mainloop()

####################################
