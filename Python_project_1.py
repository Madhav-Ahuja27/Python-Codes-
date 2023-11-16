import tkinter as tk
from tkinter import messagebox

# Functions for Expense Splitting Calculator
def calculate_shares():
    try:
        total_expense = float(total_expense_entry.get())
        num_people = int(num_people_entry.get())
        result_label.config(text=f"Each person owes: ${total_expense / num_people:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Functions for Personal Finance Tracker
def calculate_balance():
    try:
        income = float(income_entry.get())
        expenses = float(expense_entry.get())
        balance = income - expenses
        balance_label.config(text=f"Current Balance: ${income - expenses:.2f}")
     # AI-inspired recommendation for budgeting
        if balance < 0:
            recommendation = "You're spending more than you're earning. Consider reducing expenses."
        else:
            recommendation = "You're doing well in managing your finances. Consider saving or investing."

        recommendation_label.config(text=recommendation)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def switch_calculator():
    selected_calculator = calculator_var.get()
    if selected_calculator == "Expense Splitting Calculator":
        personal_finance_frame.pack_forget()
        expense_splitting_frame.pack()
    elif selected_calculator == "Personal Finance Tracker":
        expense_splitting_frame.pack_forget()
        personal_finance_frame.pack()

root = tk.Tk()
root.title("Finance Tools")

# Choose Calculator
calculator_var = tk.StringVar(value="Expense Splitting Calculator")
calculator_label = tk.Label(root, text="Choose Calculator:")
calculator_label.pack()
expense_calculator_radio = tk.Radiobutton(root, text="Expense Splitting Calculator", variable=calculator_var, value="Expense Splitting Calculator", command=switch_calculator)
expense_calculator_radio.pack()
finance_calculator_radio = tk.Radiobutton(root, text="Personal Finance Tracker", variable=calculator_var, value="Personal Finance Tracker", command=switch_calculator)
finance_calculator_radio.pack()

# Expense Splitting Calculator Frame
expense_splitting_frame = tk.Frame(root)

tk.Label(expense_splitting_frame, text="Total Expense:").pack()
total_expense_entry = tk.Entry(expense_splitting_frame)
total_expense_entry.pack()

tk.Label(expense_splitting_frame, text="Number of People:").pack()
num_people_entry = tk.Entry(expense_splitting_frame)
num_people_entry.pack()

tk.Button(expense_splitting_frame, text="Calculate", command=calculate_shares).pack()

result_label = tk.Label(expense_splitting_frame, text="")
result_label.pack()

# Personal Finance Tracker Frame
personal_finance_frame = tk.Frame(root)

tk.Label(personal_finance_frame, text="Income:").pack()
income_entry = tk.Entry(personal_finance_frame)
income_entry.pack()

tk.Label(personal_finance_frame, text="Expenses:").pack()
expense_entry = tk.Entry(personal_finance_frame)
expense_entry.pack()

tk.Button(personal_finance_frame, text="Calculate Balance", command=calculate_balance).pack()

balance_label = tk.Label(personal_finance_frame, text="")
balance_label.pack()

# Initial choice
switch_calculator()

recommendation_label = tk.Label(root, text="")
recommendation_label.pack()

root.mainloop()
