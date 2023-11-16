#-------
#Imports
#-------
import sys
import tkinter as tk
import random as rand
from tkinter import ttk

#---------
#Variables
#---------

background_color = '#d9cfe8'

#----------------------------
#Tkinter window configuration
#----------------------------
root = tk.Tk()
style = ttk.Style()

root.title('Dice Roll')
root.geometry('450x175')
root.minsize(width=450, height=175)

style.configure('.', background=background_color)


container = ttk.Frame(root)
container.pack(expand=True, fill='both')

container_button = ttk.Frame(container)
container_button.pack(side='bottom', pady=10)

container_labelentry = ttk.Frame(container_button)
container_labelentry.pack(side='top', pady=10)


#---------
#Functions
#---------
def validate_entry(entry_input):
    if entry_input.isdigit():
        return True
    else:
        return False
    
def roll_die(die_count, die_amt):
    result = ''
    sum = 0
    try:
        die_amt = int(die_amt)
   
        if die_count == 'd20':     
            for i in range(die_amt):
                roll = rand.randint(1,20)
                result += str(roll) + ' '
                sum += roll

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Sum:' + str(sum))
            else:
                label_sum.config(text='')

        if die_count == 'd12':
            for i in range(die_amt):
                roll = rand.randint(1,12)
                result += str(roll) + ' '
                sum += roll

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Sum:' + str(sum))
            else:
                label_sum.config(text='')

        if die_count == 'd10':
            for i in range(die_amt):
                roll = rand.randint(1,10)
                result += str(roll) + ' '
                sum += roll

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Sum:' + str(sum))
            else:
                label_sum.config(text='')

        if die_count == 'd8':
            for i in range(die_amt):
                roll = rand.randint(1,8)
                result += str(roll) + ' '
                sum += roll

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Sum:' + str(sum))
            else:
                label_sum.config(text='')

        if die_count == 'd6':
            for i in range(die_amt):
                roll = rand.randint(1,6)
                result += str(roll) + ' '
                sum += roll

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Sum:' + str(sum))
            else:
                label_sum.config(text='')

        if die_count == 'd4':
            for i in range(die_amt):
                roll = rand.randint(1,4)
                result += str(roll) + ' '
                sum += roll

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Sum:' + str(sum))
            else:
                label_sum.config(text='')

        if die_count == 'coin':
            heads = 0
            tails = 0
            for i in range(die_amt):
                side = rand.randint(1,2)
                if side == 1:
                    result += 'Heads '
                    heads += 1
                else: 
                    result += 'Tails '
                    tails += 1

            label_result.config(text=result)
            if die_amt != 1:
                label_sum.config(text='Heads - ' + str(heads) + ' Tails - ' + str(tails))
            else:
                label_sum.config(text='')
                    

    except ValueError:
        label_result.config(text='Enter a whole number')
    

#---------------
#Tkinter widgets
#---------------
label = ttk.Label(container, text='Select a Die to roll:')
label.pack(pady=10)

label_result = ttk.Label(container, text='')
label_result.pack()

label_sum = ttk.Label(container, text='')
label_sum.pack()

label_entry = ttk.Label(container_labelentry, text='Amount to roll:')
label_entry.pack(side='left')

entry = ttk.Entry(container_labelentry, width=3)
entry.pack(side='right')

button = ttk.Button(container_button, text='d20', width=5, command=lambda: roll_die('d20', entry.get()))
button.pack(side='left', padx=5)
button = ttk.Button(container_button, text='d12', width=5,command=lambda: roll_die('d12', entry.get()))
button.pack(side='left', padx=5)
button = ttk.Button(container_button, text='d10', width=5,command=lambda: roll_die('d10', entry.get()))
button.pack(side='left', padx=5)
button = ttk.Button(container_button, text='d8', width=5,command=lambda: roll_die('d8', entry.get()))
button.pack(side='left', padx=5)
button = ttk.Button(container_button, text='d6', width=5,command=lambda: roll_die('d6', entry.get()))
button.pack(side='left', padx=5)
button = ttk.Button(container_button, text='d4', width=5,command=lambda: roll_die('d4', entry.get()))
button.pack(side='left', padx=5)
button = ttk.Button(container_button, text='coin', width=5,command=lambda: roll_die('coin', entry.get()))
button.pack(side='left', padx=5)
