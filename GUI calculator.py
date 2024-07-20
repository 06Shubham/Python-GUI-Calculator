import tkinter as tk

# Function to update the input field
def update_expression(symbol):
    current_text = expression_entry.get()
    new_text = current_text + str(symbol)
    expression_entry.delete(0, tk.END)
    expression_entry.insert(0, new_text)

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(expression_entry.get())
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, str(result))
    except Exception as e:
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, "Error")

# Function to clear the input field
def clear_expression():
    expression_entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Creating the entry widget to display the expression
expression_entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 14))
expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

# Creating operator buttons
operators = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
]

# Creating special buttons
special_buttons = [
    ('C', 4, 1), ('=', 4, 2)
]

# Adding number buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                       command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

# Adding operator buttons to the window
for (text, row, col) in operators:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
                       command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

# Adding special buttons to the window
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_expression)
clear_button.grid(row=4, column=1)

equals_button = tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 14), command=evaluate_expression)
equals_button.grid(row=4, column=2)

# Running the main loop
root.mainloop()
