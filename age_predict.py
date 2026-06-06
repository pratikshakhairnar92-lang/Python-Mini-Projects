# =========================================
# AGE PREDICTOR PROJECT (GUI VERSION)
# Python Tkinter Project
# =========================================

from tkinter import *
from tkinter import messagebox
from datetime import date
from dateutil.relativedelta import relativedelta

# Main Window
root = Tk()
root.title("Age Predictor")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# Function
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = date(year, month, day)
        today = date.today()

        age = relativedelta(today, birth_date)

        result_label.config(
            text=f"Your Exact Age is\n\n"
                 f"{age.years} Years\n"
                 f"{age.months} Months\n"
                 f"{age.days} Days",
            fg="yellow"
        )

    except:
        messagebox.showerror("Error", "Please Enter Valid Date!")

# Heading
heading = Label(
    root,
    text="AGE PREDICTOR",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="cyan"
)
heading.pack(pady=20)

# Frame
frame = Frame(root, bg="#2c2c3e")
frame.pack(pady=20)

# Day
Label(frame, text="Day", font=("Arial", 12),
      bg="#2c2c3e", fg="white").grid(row=0, column=0, padx=10)

day_entry = Entry(frame, width=8, font=("Arial", 14))
day_entry.grid(row=1, column=0, padx=10)

# Month
Label(frame, text="Month", font=("Arial", 12),
      bg="#2c2c3e", fg="white").grid(row=0, column=1, padx=10)

month_entry = Entry(frame, width=8, font=("Arial", 14))
month_entry.grid(row=1, column=1, padx=10)

# Year
Label(frame, text="Year", font=("Arial", 12),
      bg="#2c2c3e", fg="white").grid(row=0, column=2, padx=10)

year_entry = Entry(frame, width=10, font=("Arial", 14))
year_entry.grid(row=1, column=2, padx=10)

# Button
calc_btn = Button(
    root,
    text="Calculate Age",
    font=("Arial", 14, "bold"),
    bg="cyan",
    fg="black",
    padx=10,
    pady=5,
    command=calculate_age
)
calc_btn.pack(pady=20)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=20)

# Run Window
root.mainloop()