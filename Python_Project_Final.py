# # import tkinter as tk
# # from tkinter import messagebox

# # # Functions for Expense Splitting Calculator
# # def calculate_shares():
# #     try:
# #         total_expense = float(total_expense_entry.get())
# #         num_people = int(num_people_entry.get())
# #         result_label.config(text=f"Each person owes: ₹{total_expense / num_people:.2f}")
# #     except ValueError:
# #         messagebox.showerror("Error", "Please enter valid numbers.")

# # # Functions for Personal Finance Tracker
# # def calculate_balance():
# #     try:
# #         income = float(income_entry.get())
# #         expenses = float(expense_entry.get())
# #         balance = income - expenses
# #         balance_label.config(text=f"Current Balance: ₹{income - expenses:.2f}")
# #      # AI-inspired recommendation for budgeting
# #         if balance < 0:
# #             recommendation = "You're spending more than you're earning. Consider reducing expenses."
# #         else:
# #             recommendation = "You're doing well in managing your finances. Consider saving or investing."

# #         recommendation_label.config(text=recommendation)
# #     except ValueError:
# #         messagebox.showerror("Error", "Please enter valid numbers.")

# # def switch_calculator():
# #     selected_calculator = calculator_var.get()
# #     if selected_calculator == "Expense Splitting Calculator":
# #         personal_finance_frame.pack_forget()
# #         expense_splitting_frame.pack()
# #     elif selected_calculator == "Personal Finance Tracker":
# #         expense_splitting_frame.pack_forget()
# #         personal_finance_frame.pack()

# # root = tk.Tk()
# # root.title("Finance Tools")

# # # Choose Calculator
# # calculator_var = tk.StringVar(value="Expense Splitting Calculator")
# # calculator_label = tk.Label(root, text="Choose Calculator:")
# # calculator_label.pack()
# # expense_calculator_radio = tk.Radiobutton(root, text="Expense Splitting Calculator", variable=calculator_var, value="Expense Splitting Calculator", command=switch_calculator)
# # expense_calculator_radio.pack()
# # finance_calculator_radio = tk.Radiobutton(root, text="Personal Finance Tracker", variable=calculator_var, value="Personal Finance Tracker", command=switch_calculator)
# # finance_calculator_radio.pack()

# # # Expense Splitting Calculator Frame
# # expense_splitting_frame = tk.Frame(root)

# # tk.Label(expense_splitting_frame, text="Total Expense:").pack()
# # total_expense_entry = tk.Entry(expense_splitting_frame)
# # total_expense_entry.pack()

# # tk.Label(expense_splitting_frame, text="Number of People:").pack()
# # num_people_entry = tk.Entry(expense_splitting_frame)
# # num_people_entry.pack()

# # tk.Button(expense_splitting_frame, text="Calculate", command=calculate_shares).pack()

# # result_label = tk.Label(expense_splitting_frame, text="")
# # result_label.pack()

# # # Personal Finance Tracker Frame
# # personal_finance_frame = tk.Frame(root)

# # tk.Label(personal_finance_frame, text="Income:").pack()
# # income_entry = tk.Entry(personal_finance_frame)
# # income_entry.pack()

# # tk.Label(personal_finance_frame, text="Expenses:").pack()
# # expense_entry = tk.Entry(personal_finance_frame)
# # expense_entry.pack()

# # tk.Button(personal_finance_frame, text="Calculate Balance", command=calculate_balance).pack()

# # balance_label = tk.Label(personal_finance_frame, text="")
# # balance_label.pack()

# # # Initial choice
# # switch_calculator()

# # recommendation_label = tk.Label(root, text="")
# # recommendation_label.pack()

# # root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt

# def calculate_shares():
#     try:
#         total_expense = float(total_expense_entry.get())
#         num_people = int(num_people_entry.get())
#         result_label.config(text=f"Each person owes: ₹{total_expense / num_people:.2f}")

#         generate_chart("Expense Splitting", [total_expense], ['Total Expense'])

#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers.")

# def calculate_balance():
#     try:
#         income = float(income_entry.get())
#         expenses = float(expense_entry.get())
#         balance = income - expenses
#         balance_label.config(text=f"Current Balance: ₹{income - expenses:.2f}")

#         if balance < 0:
#             recommendation = "You're spending more than you're earning. Consider reducing expenses."
#         else:
#             recommendation = "You're doing well in managing your finances. Consider saving or investing."
#         recommendation_label.config(text=recommendation)

#         generate_chart("Personal Finance", [income, expenses], ['Income', 'Expenses'])

#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers.")

# def generate_chart(chart_title, values, labels):
#     plt.bar(labels, values)
#     plt.title(f'{chart_title} Chart')
#     plt.xlabel('Category')
#     plt.ylabel('Amount')
#     plt.show()

# def switch_calculator():
#     selected_calculator = calculator_var.get()
#     if selected_calculator == "Expense Splitting Calculator":
#         personal_finance_frame.pack_forget()
#         expense_splitting_frame.pack()
#     elif selected_calculator == "Personal Finance Tracker":
#         expense_splitting_frame.pack_forget()
#         personal_finance_frame.pack()

# root = tk.Tk()
# root.title("Finance Tools")

# calculator_var = tk.StringVar(value="Expense Splitting Calculator")
# calculator_label = tk.Label(root, text="Choose Calculator:")
# calculator_label.pack()
# expense_calculator_radio = tk.Radiobutton(root, text="Expense Splitting Calculator", variable=calculator_var, value="Expense Splitting Calculator", command=switch_calculator)
# expense_calculator_radio.pack()
# finance_calculator_radio = tk.Radiobutton(root, text="Personal Finance Tracker", variable=calculator_var, value="Personal Finance Tracker", command=switch_calculator)
# finance_calculator_radio.pack()

# expense_splitting_frame = tk.Frame(root)

# tk.Label(expense_splitting_frame, text="Total Expense:").pack()
# total_expense_entry = tk.Entry(expense_splitting_frame)
# total_expense_entry.pack()

# tk.Label(expense_splitting_frame, text="Number of People:").pack()
# num_people_entry = tk.Entry(expense_splitting_frame)
# num_people_entry.pack()

# tk.Button(expense_splitting_frame, text="Calculate", command=calculate_shares).pack()

# result_label = tk.Label(expense_splitting_frame, text="")
# result_label.pack()

# personal_finance_frame = tk.Frame(root)

# tk.Label(personal_finance_frame, text="Income:").pack()
# income_entry = tk.Entry(personal_finance_frame)
# income_entry.pack()

# tk.Label(personal_finance_frame, text="Expenses:").pack()
# expense_entry = tk.Entry(personal_finance_frame)
# expense_entry.pack()

# tk.Button(personal_finance_frame, text="Calculate Balance", command=calculate_balance).pack()

# balance_label = tk.Label(personal_finance_frame, text="")
# balance_label.pack()

# switch_calculator()

# recommendation_label = tk.Label(root, text="")
# recommendation_label.pack()

# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os
import json
from PIL import Image, ImageTk 


def calculate_shares():
  try:
    total_expense = float(total_expense_entry.get())
    num_people = int(num_people_entry.get())
    result_label.config(
        text=f"Each person owes: ₹{total_expense / num_people:.2f}")

    generate_chart("Expense Splitting", [total_expense], ['Total Expense'])

  except ValueError:
    messagebox.showerror("Error", "Please enter valid numbers.")


def calculate_balance():
  try:
    income = float(income_entry.get())
    expenses = float(expense_entry.get())
    balance = income - expenses
    balance_label.config(text=f"Current Balance: ₹{income - expenses:.2f}")

    if balance < 0:
      recommendation = "You're spending more than you're earning. Consider reducing expenses."
    else:
      recommendation = "You're doing well in managing your finances. Consider saving or investing."
    recommendation_label.config(text=recommendation)
    generate_chart("Personal Finance", [income, expenses], ['Income', 'Expenses'])

  except ValueError:
    messagebox.showerror("Error", "Please enter valid numbers.")


def generate_chart(chart_title, values, labels):
  plt.bar(labels, values)
  plt.title(f'{chart_title} Chart')
  plt.xlabel('Category')
  plt.ylabel('Amount')
  plt.show()


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
root.configure(bg="#202630")
root.geometry("700x700")

logo_image = Image.open("logo.png")  
logo_image = logo_image.resize((100, 100)) 
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image=logo_photo, bg="#202630")
logo_label.pack()

financial_label = tk.Label(root, text="Financial Tools", fg="white", bg="#202630", font=("Arial", 20, "bold"))
financial_label.pack()



user_name_label = tk.Label(root, text="Enter Your Username:", bg="teal", font=("Helvetica", 13, 'bold'))
user_name_label.pack()
user_name = tk.StringVar()
user_name_entry = tk.Entry(root, textvariable=user_name)
user_name_entry.pack()


def save_user_data():
    user_data = {
        "Username": user_name.get(),
        "Calculator": calculator_var.get(),
        "Total Expense": total_expense_entry.get(),
        "Number of People": num_people_entry.get(),
        "Income": income_entry.get(),
        "Expenses": expense_entry.get(),
        "Balance": balance_label.cget("text"),
        "Recommendation": recommendation_label.cget("text")
    }


    file_path = "user_data.json"


    with open(file_path, "w") as json_file:
        json.dump(user_data, json_file)

    messagebox.showinfo("Info", "User data has been saved to user_data.json")


save_data_button = tk.Button(root, text="Save Data", command=save_user_data)
save_data_button.configure(bg="#710193",fg="#FFFFFF")
save_data_button.config(font=("Helvetica", 13, 'bold'))
save_data_button.pack()



calculator_var = tk.StringVar(value="Expense Splitting Calculator")

calculator_label = tk.Label(root, text="Choose Calculator:", bg="teal", font=("Helvetica", 13, 'bold'))

calculator_label.pack()

expense_calculator_radio = tk.Radiobutton(root,
                                          text="Expense Splitting Calculator",
                                          variable=calculator_var,
                                          value="Expense Splitting Calculator",
                                          command=switch_calculator, selectcolor="black")
expense_calculator_radio.configure(bg="#710193",fg="#FFFFFF")
expense_calculator_radio.config(font=("Helvetica", 13, 'bold'))
expense_calculator_radio.pack()

finance_calculator_radio = tk.Radiobutton(root,
                                          text="Personal Finance Tracker",
                                          variable=calculator_var,
                                          value="Personal Finance Tracker",
                                          command=switch_calculator, selectcolor="black")
finance_calculator_radio.configure(bg="#710193", fg="#FFFFFF")
finance_calculator_radio.config(font=("Helvetica", 13, 'bold'))
finance_calculator_radio.pack()





expense_splitting_frame = tk.Frame(root)

expense_splitting_frame.configure(bg="#202630")

tk.Label(expense_splitting_frame, text="Total Expense:", bg="teal", font=("Helvetica", 13, 'bold')).pack()
total_expense_entry = tk.Entry(expense_splitting_frame)
total_expense_entry.pack()

tk.Label(expense_splitting_frame, text="Number of People:", bg="teal",font=("Helvetica", 13, 'bold') ).pack()
num_people_entry = tk.Entry(expense_splitting_frame)
num_people_entry.pack()

calculate_button = tk.Button(expense_splitting_frame,
                             text="Calculate",
                             command=calculate_shares,
                             bg="#FF0000",
                             fg="#FFFFFF", font=("Helvetica", 13, 'bold'))
calculate_button.pack()
result_label = tk.Label(expense_splitting_frame, text="")
result_label.pack()

personal_finance_frame = tk.Frame(root)
personal_finance_frame.configure(bg="#202630")

tk.Label(personal_finance_frame, text="Income:", bg="yellow", font=("Helvetica", 13, 'bold')).pack()
income_entry = tk.Entry(personal_finance_frame)
income_entry.pack()

tk.Label(personal_finance_frame, text="Expenses:", bg="yellow", font=("Helvetica", 13, 'bold')).pack()
expense_entry = tk.Entry(personal_finance_frame)
expense_entry.pack()

calc_button2=tk.Button(personal_finance_frame,
          text="Calculate Balance",
          command=calculate_balance, bg="#FF0000",
                       fg="#FFFFFF")
calc_button2.pack()
balance_label = tk.Label(personal_finance_frame, text="")
balance_label.pack()

switch_calculator()

recommendation_label = tk.Label(root, text="")
recommendation_label.pack()


def reset_fields():
    total_expense_entry.delete(0, 'end')
    num_people_entry.delete(0, 'end')
    result_label.config(text="")

    income_entry.delete(0, 'end')
    expense_entry.delete(0, 'end')
    balance_label.config(text="")
    recommendation_label.config(text="")


def load_user_data():
    try:
        file_path = "user_data.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                user_name.set(data.get("Username", ""))
                calculator_var.set(data.get("Calculator", ""))
                total_expense_entry.insert(0, data.get("Total Expense", ""))
                num_people_entry.insert(0, data.get("Number of People", ""))
                income_entry.insert(0, data.get("Income", ""))
                expense_entry.insert(0, data.get("Expenses", ""))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load user data: {str(e)}")


def display_summary():
    summary = f"Username: {user_name.get()}\n"
    summary += f"Calculator Selected: {calculator_var.get()}\n"
    summary += f"Total Expense: {total_expense_entry.get()}\n"
    summary += f"Number of People: {num_people_entry.get()}\n"
    summary += f"Income: {income_entry.get()}\n"
    summary += f"Expenses: {expense_entry.get()}\n"

    messagebox.showinfo("User Data Summary", summary)

reset_button = tk.Button(root, text="Reset Fields", command=reset_fields, bg="#FF0000", fg="#FFFFFF")
reset_button.config(font=("Helvetica", 13, 'bold'))
reset_button.pack()

load_data_button = tk.Button(root, text="Load User Data", command=load_user_data, bg="#FF0000", fg="#FFFFFF")
load_data_button.config(font=("Helvetica", 13, 'bold'))
load_data_button.pack()

summary_button = tk.Button(root, text="Display Summary", command=display_summary, bg="#FF0000", fg="#FFFFFF") 
summary_button.config(font=("Helvetica", 13, 'bold'))
summary_button.pack()


root.mainloop()

