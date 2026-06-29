# Import the tkinter GUI library.
import tkinter as tk

# Importing tkinter widgets.
from tkinter import ttk, messagebox

# Expense Tracker class.
class ExpenseTracker:
    
    # Constructor methods that runs automatically when the application starts. 
    def __init__(self, root):

        # Store the main application.
        self.root = root
        self.root.title("Expense Tracker")

        # Empty list for storing transactions. 
        self.transactions = []

        # Labels for GUI.
        tk.Label(root, text="Description").grid(row = 0, column = 0)
        tk.Label(root, text="Amount").grid(row = 1, column = 0)
        tk.Label(root, text="Category").grid(row = 2, column = 0)
        tk.Label(root, text="Type").grid(row = 3, column = 0)

        # Entry fields.
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row = 1, column = 1)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row = 1, column = 1)

        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row = 2, column = 1)

        self.type_combo = ttk.Combobox(
            root,
            values=["Income", "Expense"]
        )

        self.type_combo.grid(row=3, column=1)

        # Text box for entering description.
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row = 0, column = 1)

        # Text box for entering amount.
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row = 1, column = 1)

        # Text box for entering category. 
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row = 2, column = 1)

        # Dropdown menu for selecting Income and Expense. 
        self.type_combo = ttk.Combobox(
            root,
            values = ["Income", "Expense"]
        )
        self.type_combo.grid(row = 3, column = 1)