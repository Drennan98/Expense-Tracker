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

        tk.Label(root, text="Description").grid(row=0, column=0)
        tk.Label(root, text="Amount").grid(row=1, column=0)
        tk.Label(root, text="Category").grid(row=2, column=0)
        tk.Label(root, text="Type").grid(row=3, column=0)