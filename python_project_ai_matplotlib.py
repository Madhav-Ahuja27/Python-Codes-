import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os
import json

# Function to calculate balance and save data
def calculate_balance():
    try:
        income = float(income_entry.get())
        expenses = float(expense_entry.get())
        balance = income - expenses
        balance_label.config(text=f"Current Balance: ${balance:.2f}")

        # Save financial data to a JSON file
        user_data = {
            'Income': income,
            'Expenses': expenses,
            'Balance': balance
        }
        with open(f'{user_name.get()}.json', 'w') as file:
            json.dump(user_data, file)

        # Generate and display a simple bar chart
        generate_chart(income, expenses)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to generate and display a bar chart
def generate_chart(income, expenses):
    labels = ['Income', 'Expenses']
    values = [income, expenses]

    plt.bar(labels, values)
    plt.title('Income vs Expenses')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()

# Create the main window
root = tk.Tk()
root.title("AI-Powered Personal Finance Tracker")

# User Authentication
user_name_label = tk.Label(root, text="Enter Your Username:")
user_name_label.pack()
user_name = tk.StringVar()
user_name_entry = tk.Entry(root, textvariable=user_name)
user_name_entry.pack()

# Check if user data file exists, and load data if available
if os.path.isfile(f'{user_name.get()}.json'):
    with open(f'{user_name.get()}.json', 'r') as file:
        user_data = json.load(file)
        income_entry.insert(0, user_data['Income'])
        expense_entry.insert(0, user_data['Expenses'])

# Personal Finance Tracker
tk.Label(root, text="Income:").pack()
income_entry = tk.Entry(root)
income_entry.pack()

tk.Label(root, text="Expenses:").pack()
expense_entry = tk.Entry(root)
expense_entry.pack()

tk.Button(root, text="Calculate Balance", command=calculate_balance).pack()

balance_label = tk.Label(root, text="")
balance_label.pack()

root.mainloop()
