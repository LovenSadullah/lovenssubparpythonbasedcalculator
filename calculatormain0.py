import os
import math
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox
import sys


# Create main window
root = tk.Tk()
root.title("Frame Demo")
root.config(bg="skyblue")

# Create Frame widget
frame = tk.Frame(root, width=700, height=700)
frame.pack(padx=10, pady=10)

log_file = open('calculator_output.txt', 'w')

def log_print(*args, **kwargs):
    """Print to both console and file"""
    message = ' '.join(str(arg) for arg in args)
    print(message)
    print(message, file=log_file)
    log_file.flush()

def log_input(prompt, value):
    """Log user inputs to the file"""
    log_print(f"INPUT: {prompt} -> {value}")

def VerifyLogin(input_user, input_password, filepath='UserPass.csv'):
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

# User prompts for login
username = simpledialog.askstring("Input", "Enter your username:", parent=root)
log_input("Username entered", username)
password = simpledialog.askstring("Input", "Enter your password:", parent=root, show='*')
log_input("Password entered", "********")

# Verify login
if VerifyLogin(username, password):
    log_print("Login successful!")
    root.destroy()
else:
    log_print("Login failed!")
    log_file.close()
    root.destroy()
    quit()

# Create new window for calculator
root = tk.Tk()
root.withdraw()

while True:
    MathMode = simpledialog.askstring("Input", "type reg for regular operations, type complex for more functions", parent=root)
    log_input("Math mode selected", MathMode)
    
    if MathMode == "reg":
        try:
            FirstZ = simpledialog.askstring("Input", "what do you want to do with these two numbers? input from -, +, /, *(for multiply), %(for modulus) , **(for power of)", parent=root)
            log_input("Operation selected", FirstZ)
            x = float(simpledialog.askstring("Input", "enter your first number:", parent=root))
            log_input("First number", x)
            y = float(simpledialog.askstring("Input", "enter your second number:", parent=root))
            log_input("Second number", y)
            z = FirstZ.strip()
            
            if z == "-":
                log_print(x - y)
            elif z == "+":
                log_print(x + y)
            elif z == "*":
                log_print(x * y)
            elif z == "/":
                log_print(x / y)
            elif z == "%":
                log_print(x % y)
            elif z == "**":
                log_print(x ** y)
        except ZeroDivisionError:
            log_print("you can't do that!")
        except SyntaxError:
            log_print("your input doesn't make sense to my code :(")
        break
    
    elif MathMode == "complex":
        try:
            x = float(simpledialog.askstring("Input", "enter your number:", parent=root))
            log_input("Number entered", x)
            FirstZ = simpledialog.askstring("Input", "input a trig function: sin, cos, or tan, or you could type arc before each function for arc functions, log, or sqrt.", parent=root)
            log_input("Function selected", FirstZ)
            z = FirstZ.strip()
            
            if z == "sin":
                log_print(math.sin(x))
            elif z == "arcsin":
                log_print(math.asin(x))
            elif z == "cos":
                log_print(math.cos(x))
            elif z == "arccos":
                log_print(math.acos(x))
            elif z == "arctan":
                log_print(math.atan(x))
            elif z == "tan":
                log_print(math.tan(x))
            elif z == "log":
                log_print(math.log(x))
            elif z == "sqrt":
                if x >= 0:
                    log_print(math.sqrt(x))
                else:
                    log_print("Error: Cannot take square root of a negative number!")
        except SyntaxError:
            log_print("your input doesn't make sense to my code :(")
        break
    
    log_print(z)

root.destroy()
log_file.close()
print(f"\nAll output has been saved to: {os.path.abspath('calculator_output.txt')}")
