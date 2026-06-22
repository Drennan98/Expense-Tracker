import tkinter as tk
from tkinter import ttk, messagebox


class ExpenseTracker:

    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.transactions = []

        # Labels
        tk.Label(root, text="Description").grid(row=0, column=0)
        tk.Label(root, text="Amount").grid(row=1, column=0)
        tk.Label(root, text="Category").grid(row=2, column=0)
        tk.Label(root, text="Type").grid(row=3, column=0)

        # Entries
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=0, column=1)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=2, column=1)

        self.type_combo = ttk.Combobox(
            root,
            values=["Income", "Expense"]
        )
        self.type_combo.grid(row=3, column=1)

        # Buttons
        tk.Button(
            root,
            text="Add",
            command=self.add_transaction
        ).grid(row=4, column=0)

        tk.Button(
            root,
            text="Update",
            command=self.update_transaction
        ).grid(row=4, column=1)

        tk.Button(
            root,
            text="Delete",
            command=self.delete_transaction
        ).grid(row=4, column=2)

        # Treeview
        self.tree = ttk.Treeview(
            root,
            columns=("Description",
                     "Amount",
                     "Category",
                     "Type"),
            show="headings"
        )

        for col in ("Description",
                    "Amount",
                    "Category",
                    "Type"):
            self.tree.heading(col, text=col)

        self.tree.grid(
            row=5,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

    def add_transaction(self):
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        transaction_type = self.type_combo.get()

        if not description or not amount:
            messagebox.showerror(
                "Error",
                "Please complete all fields."
            )
            return

        self.tree.insert(
            "",
            "end",
            values=(
                description,
                amount,
                category,
                transaction_type
            )
        )

        self.clear_fields()

    def select_record(self, event):
        selected = self.tree.focus()

        if selected:
            values = self.tree.item(
                selected,
                "values"
            )

            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, values[0])

            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, values[1])

            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, values[2])

            self.type_combo.set(values[3])

    def update_transaction(self):
        selected = self.tree.focus()

        if selected:
            self.tree.item(
                selected,
                values=(
                    self.description_entry.get(),
                    self.amount_entry.get(),
                    self.category_entry.get(),
                    self.type_combo.get()
                )
            )

    def delete_transaction(self):
        selected = self.tree.focus()

        if selected:
            self.tree.delete(selected)

    def clear_fields(self):
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.type_combo.set("")


root = tk.Tk()
app = ExpenseTracker(root)
root.mainloop()