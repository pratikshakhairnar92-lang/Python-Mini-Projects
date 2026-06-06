import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Percentage & Percentile Calculator")
root.geometry("500x400")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="Percentage & Percentile Calculator",
    font=("Arial", 20, "bold"),
    fg="#00ffcc",
    bg="#1e1e2f"
)
title.pack(pady=20)

# Frame
frame = tk.Frame(root, bg="#2b2b40", padx=20, pady=20)
frame.pack(pady=20)

# Obtained Marks
marks_label = tk.Label(
    frame,
    text="Obtained Marks",
    font=("Arial", 14),
    fg="white",
    bg="#2b2b40"
)
marks_label.grid(row=0, column=0, pady=10)

marks_entry = tk.Entry(frame, font=("Arial", 14), width=15)
marks_entry.grid(row=0, column=1, pady=10)

# Total Marks
total_label = tk.Label(
    frame,
    text="Total Marks",
    font=("Arial", 14),
    fg="white",
    bg="#2b2b40"
)
total_label.grid(row=1, column=0, pady=10)

total_entry = tk.Entry(frame, font=("Arial", 14), width=15)
total_entry.grid(row=1, column=1, pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    fg="#ffff66",
    bg="#1e1e2f"
)
result_label.pack(pady=20)

# Calculate Function
def calculate():
    try:
        marks = float(marks_entry.get())
        total = float(total_entry.get())

        percentage = (marks / total) * 100

        # Estimated Percentile Formula
        percentile = percentage * 0.95 + 5

        if percentile > 100:
            percentile = 100

        result_label.config(
            text=f"Percentage = {percentage:.2f}%\nEstimated Percentile = {percentile:.2f}"
        )

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Button
calc_btn = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 15, "bold"),
    bg="#00ffcc",
    fg="black",
    padx=20,
    pady=10,
    relief="flat",
    command=calculate
)
calc_btn.pack(pady=20)

# Run Window
root.mainloop()