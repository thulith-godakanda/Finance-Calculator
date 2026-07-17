# 2024/03/02
# Project 1.1
# Thulith Godakanda

import tkinter as tk
from tkinter import messagebox
import math


def calculate():

    pv_value = entry_pv.get()
    fv_value = entry_fv.get()
    rate_value = entry_rate.get()
    time_value = entry_time.get()

    blank_count = 0

    if pv_value == "":
        blank_count += 1
    if fv_value == "":
        blank_count += 1
    if rate_value == "":
        blank_count += 1
    if time_value == "":
        blank_count += 1

    if blank_count != 1:
        messagebox.showerror(
            "Input Error",
            "Enter three values and leave one field blank."
        )
        return

    try:

        if pv_value == "":
            fv = float(fv_value)
            rate = float(rate_value) / 100
            time = float(time_value)

            pv = fv / ((1 + rate) ** time)

            entry_pv.insert(0, round(pv, 2))
            messagebox.showinfo("Answer", "Present Value calculated.")

        elif fv_value == "":
            pv = float(pv_value)
            rate = float(rate_value) / 100
            time = float(time_value)

            fv = pv * ((1 + rate) ** time)

            entry_fv.insert(0, round(fv, 2))
            messagebox.showinfo("Answer", "Future Value calculated.")

        elif rate_value == "":
            pv = float(pv_value)
            fv = float(fv_value)
            time = float(time_value)

            if pv <= 0 or fv <= 0 or time == 0:
                messagebox.showerror(
                    "Math Error",
                    "PV and FV must be positive, and time cannot be zero."
                )
                return

            rate = ((fv / pv) ** (1 / time) - 1) * 100

            entry_rate.insert(0, round(rate, 4))
            messagebox.showinfo("Answer", "Interest Rate calculated.")

        elif time_value == "":
            pv = float(pv_value)
            fv = float(fv_value)
            rate = float(rate_value) / 100

            if pv <= 0 or fv <= 0 or rate <= -1 or rate == 0:
                messagebox.showerror(
                    "Math Error",
                    "Check the PV, FV and interest rate values."
                )
                return

            time = math.log(fv / pv) / math.log(1 + rate)

            entry_time.insert(0, round(time, 4))
            messagebox.showinfo("Answer", "Time calculated.")

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter numbers only."
        )

    except ZeroDivisionError:
        messagebox.showerror(
            "Math Error",
            "A value cannot be divided by zero."
        )


def clear_fields():
    entry_pv.delete(0, tk.END)
    entry_fv.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_time.delete(0, tk.END)


window = tk.Tk()
window.title("Finance Calculator")
window.geometry("400x350")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Finance Calculator",
    font=("Arial", 18, "bold")
)
title.grid(row=0, column=0, columnspan=2, pady=20)

name_label = tk.Label(
    window,
    text="Thulith Godakanda - Project 1.1"
)
name_label.grid(row=1, column=0, columnspan=2, pady=5)

label_pv = tk.Label(window, text="Present Value:")
label_pv.grid(row=2, column=0, padx=20, pady=10, sticky="w")

entry_pv = tk.Entry(window, width=20)
entry_pv.grid(row=2, column=1, padx=20, pady=10)

label_fv = tk.Label(window, text="Future Value:")
label_fv.grid(row=3, column=0, padx=20, pady=10, sticky="w")

entry_fv = tk.Entry(window, width=20)
entry_fv.grid(row=3, column=1, padx=20, pady=10)

label_rate = tk.Label(window, text="Interest Rate (%):")
label_rate.grid(row=4, column=0, padx=20, pady=10, sticky="w")

entry_rate = tk.Entry(window, width=20)
entry_rate.grid(row=4, column=1, padx=20, pady=10)

label_time = tk.Label(window, text="Time (Years):")
label_time.grid(row=5, column=0, padx=20, pady=10, sticky="w")

entry_time = tk.Entry(window, width=20)
entry_time.grid(row=5, column=1, padx=20, pady=10)

calculate_button = tk.Button(
    window,
    text="Calculate",
    width=12,
    command=calculate
)
calculate_button.grid(row=6, column=0, pady=20)

clear_button = tk.Button(
    window,
    text="Clear",
    width=12,
    command=clear_fields
)
clear_button.grid(row=6, column=1, pady=20)

instruction = tk.Label(
    window,
    text="Leave the value you want to calculate blank."
)
instruction.grid(row=7, column=0, columnspan=2)

window.mainloop()