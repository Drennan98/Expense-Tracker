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

        # Entry fields
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

        # Buttons
        # Calls add_transaction() when clicked.
        tk.Button(
            root,
            text = "Add",
            command = self.add_transaction
        ).grid(row = 4, column = 0)

        # Calls update_transaction when clicked. 
        tk.Button(
            root,
            text = "Update",
            command = self.update_transaction
        ).grid(row = 4, column = 1)

        # Calls delete transaction when clicked. 
        tk.Button(
            root,
            text = "Delete",
            command = self.delete_transaction
        ).grid(row = 4, column = 2)

        # Calls clear_fields() when clicked.
        tk.Button(
            root,
            text="Clear",
            command=self.clear_fields
        ).grid(row=4, column=3)

        # Treeview -> Create table to display all transactions.
        self.tree = ttk.Treeview(
            root,
            columns = (
                "Description",
                "Amount",
                "Category",
                "Type"
            ),
            show = "headings"
        )

        # Create headings in each column of the table.
        for col in (
            "Description",
            "Amount",
            "Category",
            "Type"
        ):
            self.tree.heading(col, text = col)

        # Position Treeview in the window. 
        self.tree.grid(
            row = 5,
            column = 0,
            columnspan = 4, 
            padx = 10,
            pady = 10
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

    def add_transaction(self):
        """
        Get the values entered by the user.
        """
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        transaction_type = self.type_combo.get()

        if not description or not amount:
            messagebox.showerror(
                "Error",
                "Please complete all required fields."
            )
            return
        
        self.tree.insert(
            "",
            "end",
            values = (
                description,
                amount,
                category,
                transaction_type
            )
        )
        # Clear the input fields. 
        self.clear_fields()

    
    
    def select_record(self, event):
        """
        Get the selected row.
        """
        selected = self.tree.focus()

        if selected: 
            # Retrieve the values from the selected rows. 
            values = self.tree.item(selected, "values")

            # Display the values inside.
            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, values[0])

            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, values[1])

            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, values[2])

            self.type_combo.set(values[3])

    
    def update_transaction(self):
        """
        Update transaction function.
        """
        #  Get the selected row.
        selected = self.tree.focus()

        self.tree.item(
            selected,
            values = (
                self.description_entry.get(),
                self.amount_entry.get(),
                self.category_entry.get(),
                self.type_combo.get()
            )
        )

    
    def delete_transaction(self):
        """
        Delete transaction function.
        """
        # Get the selected row.
        selected = self.tree.focus()

        if selected:
            self.tree.delete(selected)


    
    def clear_fields(self):
        """
        Clear all input fields.
        """
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

        self.type_combo.set("")

