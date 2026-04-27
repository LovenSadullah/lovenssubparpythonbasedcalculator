import os
import math
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox #important tkinter modules as it was showing errors at first.
import sys #to export output as a file

import tkinter as tk  #tkinter template to start from, taken from python guis

root = tk.Tk() 
root.title("Frame Demo")
root.config(bg="skyblue")

# Create Frame widget
frame = tk.Frame(root, width=700, height=700) #todo; showing up and prompt windows, input bars too.
frame.pack(padx=10, pady=10)

log_file = open('calculator_output.txt', 'w')  # write the output to to the txt each time cause this assignment is weird.

def log_print(*args, **kwargs):
    """Print to both console and file"""
    message = ' '.join(str(arg) for arg in args)
    print(message)  # Print to console just to verify
    print(message, file=log_file)  # Print to file
    log_file.flush()  # Force write to disk

def log_input(prompt, value):
    """Log user inputs to the file"""
    log_print(f"INPUT: {prompt} -> {value}") #write input too, using alice to test, shows alice accessed the calculator for example and show sthe answer.

#i call this verify login, because what else am i meant to name it? churros, we need sensible variable names.
def VerifyLogin(input_user, input_password, filepath='UserPass.csv'): #csv, yes i know, i'm trying to get a better alternative, i need to either encrypt it or make a password manager systerm, which isn't that easy, i have the concept but not the knowhow.
    try:
        with open(filepath, 'r') as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) >= 2:
                    file_username = fields[0].strip()
                    file_password = fields[1].strip()
                    if file_username == input_user and file_password == input_password:
                        return True
    except FileNotFoundError:
        log_print(f"Error: {filepath} not found")
    except Exception as e:
        log_print(f"Unexpected error: {e}")
    return False

# User prompts, login 
username = simpledialog.askstring("Input", "Enter your username:", parent=root)
log_input("Username entered", username)
password = simpledialog.askstring("Input", "Enter your password:", parent=root, show='*')  # Fixed: was missing password variable
log_input("Password entered", "********")  # Don't log actual password for security

# Call the function
if VerifyLogin(username, password):
    log_print("Login successful!")
    root.destroy()  # Close the login window before showing math functions
else:
    log_print("Login failed!")
    log_file.close()
    root.destroy()  # Close the window
    quit()

# REMOVED root.mainloop() - it was blocking the math functions

# Create a new root window for the calculator
root = tk.Tk()
root.withdraw()  # Hide the main window, only show dialogs

while True:
    MathMode = simpledialog.askstring("Input", "type reg for regular operations, type complex for more functions", parent=root)
    log_input("Math mode selected", MathMode)
    if MathMode == ("reg"):
        try:
            FirstZ = simpledialog.askstring("Input", "what do you want to do with these two numbers? input from -, +, /, *(for multiply), %(for modulus) , **(for power of)", parent=root)
            log_input("Operation selected", FirstZ)
            x = float(simpledialog.askstring("Input", "enter your first number:", parent=root))
            log_input("First number", x)
            y = float(simpledialog.askstring("Input", "enter your second number:", parent=root))
            log_input("Second number", y)
            z = FirstZ.strip()
            if z == ("-"):
                log_print(x - y)      #basic function, all calculaotors need them, because i need to explain the obvious in this assignment smh
            elif z == ("+") :
                log_print(x + y)
            elif z == ("*") :
                log_print(x * y)
            elif z == ("/") :
                log_print(x / y)
            elif z == ("%") :
                log_print(x % y)
            elif z == ("**") :
                log_print(x ** y)
        except ZeroDivisionError:
            log_print("you can't do that!")
        except SyntaxError:
            log_print("your input doesn't make sense to my code :(")
        break
    
    elif MathMode == ("complex"):  # had some indent error, fixed it
        try:
            x = float(simpledialog.askstring("Input", "enter your number:", parent=root))
            log_input("Number entered", x)
            FirstZ = simpledialog.askstring("Input", "input a trig function: sin, cos, or tan, or you could type arc before each function for arc functions, log, or sqrt.", parent=root)
            log_input("Function selected", FirstZ)
            z = FirstZ.strip()          #basic complex trig functions, you need them in a calculator
            if z == ("sin"):
                log_print(math.sin(x))
            elif z == ("arcsin"):
                log_print(math.asin(x))
            elif z == ("cos"):
                log_print(math.cos(x))
            elif z == ("arccos"):
                log_print(math.acos(x))
            elif z == ("arctan"):
                log_print(math.atan(x))
            elif z == ("tan"):
                log_print(math.tan(x))
            elif z == ("log"):
                log_print(math.log(x))
            elif z == ("sqrt"):
                if x >= 0:
                    log_print(math.sqrt(x))
                else:
                    log_print("Error: Cannot take square root of a negative number!")
        except SyntaxError:
            log_print("your input doesn't make sense to my code :(") #just to make sure nobody puts junk in, also a sad face to make them feel sad.
        break
    log_print(z) #print the result after

root.destroy()  # Close the calculator window
log_file.close()
print(f"\nAll output has been saved to: {os.path.abspath('calculator_output.txt')}")
