import tkinter as tk
from tkinter import ttk

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Tracker")
        self.root.geometry("600x500")

        self.day_vars = []

        # Input for number of days
        tk.Label(root, text="Enter Number of Days:", font=("Arial", 12)).pack(pady=10)
        self.days_entry = tk.Entry(root)
        self.days_entry.pack()

        tk.Button(root, text="Generate Table", command=self.generate_table).pack(pady=10)

        self.table_frame = tk.Frame(root)
        self.table_frame.pack()

        tk.Button(root, text="Calculate Attendance", command=self.calculate).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def generate_table(self):
        # clear previous table
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        self.day_vars.clear()

        try:
            days = int(self.days_entry.get())
        except:
            self.result_label.config(text="Enter valid number")
            return

        tk.Label(self.table_frame, text="Day").grid(row=0, column=0)
        tk.Label(self.table_frame, text="Status").grid(row=0, column=1)

        for i in range(days):
            tk.Label(self.table_frame, text=f"Day {i+1}").grid(row=i+1, column=0)

            var = tk.StringVar(value="P")
            dropdown = ttk.Combobox(self.table_frame, textvariable=var)
            dropdown['values'] = ("P", "A", "L")
            dropdown.grid(row=i+1, column=1)

            self.day_vars.append(var)

    def calculate(self):
        if not self.day_vars:
            self.result_label.config(text="Generate table first")
            return

        present = 0
        total = len(self.day_vars)

        for var in self.day_vars:
            if var.get() == "P":
                present += 1

        percentage = (present / total) * 100

        self.result_label.config(
            text=f"Present: {present}/{total} | Attendance: {percentage:.2f}%"
        )

# Run app
root = tk.Tk()
app = AttendanceApp(root)
root.mainloop()