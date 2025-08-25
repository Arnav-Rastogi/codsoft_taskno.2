import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Select a valid operation.")
            return

        result_label.config(text=f"Result: {result}", font=("Arial", 16))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Big Arithmetic Calculator")
root.geometry("500x500")  # Larger window
root.resizable(False, False)

# Title Label
tk.Label(root, text="Arithmetic Calculator", font=("Arial", 22, "bold")).pack(pady=20)

# First number
tk.Label(root, text="Enter first number:", font=("Arial", 14)).pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 14), width=20)
entry1.pack(pady=5)

# Second number
tk.Label(root, text="Enter second number:", font=("Arial", 14)).pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 14), width=20)
entry2.pack(pady=5)

# Operation selection
tk.Label(root, text="Select Operation:", font=("Arial", 14)).pack(pady=10)
operation_var = tk.StringVar()
operation_var.set('+')

# Radio buttons with spacing and larger font
frame = tk.Frame(root)
frame.pack()
for op in ['+', '-', '*', '/']:
    tk.Radiobutton(frame, text=op, variable=operation_var, value=op,
                   font=("Arial", 14), padx=20).pack(side=tk.LEFT)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, font=("Arial", 16), bg="lightblue", width=15).pack(pady=20)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.pack(pady=20)

# Run the app
root.mainloop()
