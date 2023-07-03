#Muhammad Farooq Naeem (SP23-BCS-036)
#Muhammad Ehsan Mumtaz (sp23-BCS-039) 

import tkinter as tk
from math import *
import numexpr as ne



#Evaluate Function
def evaluate():
    expression = input_entry.get()
    try:
        result =ne.evaluate(expression)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Clear screen
def clear():
    input_entry.delete(0, tk.END)
    result_label.configure(text="")

#Square root 
def calculate_square_root():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = sqrt(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")
        
#sin Function
def calculate_sin():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = sin(radians(value))
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Cos Function
def calculate_cos():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = cos(radians(value))
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Tan Function
def calculate_tan():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = tan(radians(value))
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Sin inverse Function
def calculate_sin_inverse():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = asin(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Cos inverse Function
def calculate_cos_inverse():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = acos(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Tan inverse Function
def calculate_tan_inverse():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = atan(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Exponential Function
def calculate_exponential():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = exp(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Log Function
def calculate_log():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = log10(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Natural Log Function
def calculate_natural_log():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = log(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Factorial Function
def calculate_factorial():
    expression = input_entry.get()
    try:
        value = int(expression)
        result = factorial(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Add Digit Function
def add_digit(digit):
    current_expression = input_entry.get()
    new_expression = current_expression + str(digit)
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, new_expression)

#Add Operator Function
def add_operator(operator):
    current_expression = input_entry.get()
    new_expression = current_expression + operator
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, new_expression)

#Absolute Function
def absolute():
    expression = input_entry.get()
    try:
        value = float(expression)
        result = abs(value)
        result_label.configure(text=result)
    except:
        result_label.configure(text="Error")

#Backspace Function
def backspace():
    current_text = input_entry.get()
    if len(current_text) > 0:
        new_text = current_text[:-1]  # Remove the last character
        input_entry.delete(0, tk.END)  # Clear the current text
        input_entry.insert(0, new_text)  # Set the new text








#Window Creation
root = tk.Tk()
root.geometry("365x450")
root.title("Scientific Calculator")
root.configure(bg='#4A4E69')
root.resizable(False, False)


#Frames
#Main Frames 
main_button_frame = tk.Canvas(root, width=345, height=320, bg='grey', highlightthickness=0)
main_button_frame.place(x=10, y=115)

#Input Frame
in_frame = tk.Label(root, bg='grey', highlightthickness=0)
in_frame.place(x=10, y=10.5, width=345, height=28)

#Result Box
result_label = tk.Label(root, bg='white', highlightthickness=0, font=('Arial', 18))
result_label.place(x=10, y=50, width=344, height=53)

#Entry Box
input_entry = tk.Entry(in_frame, font=('Arial', 14), width=34, bd=0, justify=tk.RIGHT)
input_entry.pack()




# 1st row from top
sin_button = tk.Button(main_button_frame, text='sin', font=15, height=1, bg='light grey', fg='black',command=calculate_sin) 
sin_button.place(x=5, y=10, width=80)

sini_button = tk.Button(main_button_frame,text='sin^-1',font=15,height=1,bg='light grey',fg='black',command=calculate_sin_inverse) 
sini_button.place(x=90,y=10,width=80)

power_button = tk.Button(main_button_frame,text='^',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit('**')) 
power_button.place(x=175,y=10,width=80)

log_button = tk.Button(main_button_frame,text='log',font=15,height=1,bg='light grey',fg='black',command=calculate_log) 
log_button.place(x=260,y=10,width=80)



# 2nd row from top
cos_button = tk.Button(main_button_frame, text='cos', font=15, height=1, bg='light grey', fg='black', command=calculate_cos) 
cos_button.place(x=5, y=48, width=80)

cosi_button = tk.Button(main_button_frame,text='cos^-1',font=15,height=1,bg='light grey',fg='black', command=calculate_cos_inverse) 
cosi_button.place(x=90,y=48,width=80)

square_button = tk.Button(main_button_frame,text='√',font=15,height=1,bg='light grey',fg='black', command=calculate_square_root) 
square_button.place(x=175,y=48,width=80)

factorial_button = tk.Button(main_button_frame,text='x!',font=15,height=1,bg='light grey',fg='black', command=calculate_factorial) 
factorial_button.place(x=260,y=48,width=80)


# 3rd row from top
tan_button = tk.Button(main_button_frame, text='tan', font=15, height=1, bg='light grey', fg='black',command=calculate_tan) 
tan_button.place(x=5, y=86, width=80)

tani_button = tk.Button(main_button_frame,text='tan^-1',font=15,height=1,bg='light grey',fg='black', command=calculate_tan_inverse) 
tani_button.place(x=90,y=86,width=80)

e_button = tk.Button(main_button_frame,text='e',font=15,height=1,bg='light grey',fg='black', command=calculate_exponential) 
e_button.place(x=175,y=86,width=80)

ln_button = tk.Button(main_button_frame,text='ln',font=15,height=1,bg='light grey',fg='black', command=calculate_natural_log) 
ln_button.place(x=260,y=86,width=80)


# 4rth row from top
seven_button = tk.Button(main_button_frame, text='7', font=15, height=1, bg='light grey', fg='black', command=lambda: add_digit(7)) 
seven_button.place(x=5, y=124, width=80)

eight_button = tk.Button(main_button_frame,text='8',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit(8)) 
eight_button.place(x=90,y=124,width=80)

nine_button = tk.Button(main_button_frame,text='9',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit(9)) 
nine_button.place(x=175,y=124,width=80)

subtract_button = tk.Button(main_button_frame,text='-',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit('-')) 
subtract_button.place(x=260,y=124,width=80)



# 5th row from top
four_button = tk.Button(main_button_frame, text='4', font=15, height=1, bg='light grey', fg='black', command=lambda: add_digit(4)) 
four_button.place(x=5, y=162, width=80)

five_button = tk.Button(main_button_frame,text='5',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit(5)) 
five_button.place(x=90,y=162,width=80)

six_button = tk.Button(main_button_frame,text='6',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit(6)) 
six_button.place(x=175,y=162,width=80)

add_button = tk.Button(main_button_frame,text='+',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit('+')) 
add_button.place(x=260,y=162,width=80)



# 6th row from top
one_button = tk.Button(main_button_frame, text='1', font=15, height=1, bg='light grey', fg='black', command=lambda: add_digit(1)) 
one_button.place(x=5, y=200, width=80)

two_button = tk.Button(main_button_frame,text='2',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit(2)) 
two_button.place(x=90,y=200,width=80)

three_button = tk.Button(main_button_frame,text='3',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit(3)) 
three_button.place(x=175,y=200,width=80)

divide_button = tk.Button(main_button_frame,text='÷',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit('/')) 
divide_button.place(x=260,y=200,width=80)


# 7th row from bottom
point_button = tk.Button(main_button_frame, text='.', font=15, height=1, bg='light grey', fg='black', command=lambda: add_digit('.')) 
point_button.place(x=5, y=238, width=80)

zero_button = tk.Button(main_button_frame,text='0',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit('0')) 
zero_button.place(x=90,y=238,width=80)

equal_button = tk.Button(main_button_frame,text='=',font=15,height=1,bg='light grey',fg='black', command=evaluate) 
equal_button.place(x=175,y=238,width=80)

multiply_button = tk.Button(main_button_frame,text='',font=15,height=1,bg='light grey',fg='black', command=lambda: add_digit('')) 
multiply_button.place(x=260,y=238,width=80)

# Last row 
clear_button = tk.Button(main_button_frame, text='C', font=15, height=1, bg='light grey', fg='black', command=clear)
clear_button.place(x=5, y=276, width=80)

absolute_button = tk.Button(main_button_frame, text='abs', font=15, height=1, bg='light grey', fg='black', command=absolute)
absolute_button.place(x=260, y=276, width=80)

backspace_button = tk.Button(main_button_frame, text='←', font=15, height=1, bg='light grey', fg='black', command=backspace)
backspace_button.place(x=175, y=276, width=80)

doublezero_button = tk.Button(main_button_frame, text='00', font=15, height=1, bg='light grey', fg='black',command=lambda:add_digit('00'))
doublezero_button.place(x=90, y=276, width=80)


root.mainloop()