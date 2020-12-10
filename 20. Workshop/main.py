import tkinter
from tkcalendar import DateEntry
from tkinter import scrolledtext
import json


def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()


def create_task(**kwargs):
    with open("db.txt", "w") as file:
        json.dump(kwargs, file)


def render_create_task_view(tk):
    clear_view(tk)
    tkinter.Label(tk, text="Enter your task name:").grid(row=0, column=0, padx=20, pady=20)
    task_name = tkinter.Entry(tk)
    task_name.grid(row=0, column=1)
    tkinter.Label(tk, text="Due date:").grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk)
    date.grid(row=1, column=1)
    tkinter.Label(tk, text="Description:").grid(row=2, column=0, padx=20, pady=20)
    description = scrolledtext.ScrolledText(tk, width=30, height=5)
    description.grid(row=2, column=1, padx=20, pady=20)
    tkinter.Label(tk, text="Select priority").grid(row=3, column=0, padx=20, pady=20)
    selected_priority_num = tkinter.IntVar()
    tkinter.Radiobutton(tk, text="Low", value=1, variable=selected_priority_num).grid(row=3, column=1, padx=20, pady=20)
    tkinter.Radiobutton(tk, text="Medium", value=2, variable=selected_priority_num).grid(row=3, column=2, padx=0, pady=20)
    tkinter.Radiobutton(tk, text="High", value=3, variable=selected_priority_num).grid(row=3, column=3, padx=60, pady=20)
    tkinter.Label(tk, text="Check if completed:").grid(row=4, column=0, padx=20, pady=20)
    is_completed = tkinter.BooleanVar()
    tkinter.Checkbutton(tk, text="Check", variable=is_completed).grid(row=4, column=1, padx=20, pady=20)
    tkinter.Button(
        tk, text="Create tasks", bg="green", fg="white",
        command=lambda: create_task(
            name=task_name.get(), date=date.get(), description=description.get("1.0", "END"),
            selected_priority=selected_priority_num.get(), is_completed=is_completed.get())
    ).grid(row=5, column=0, padx=20, pady=80)


def render_main_view(tk):
    tkinter.Button(tk, text="List tasks", bg="blue", fg="white").grid(row=0, column=0, padx=200, pady=200)
    tkinter.Button(tk, text="Create tasks", bg="green", fg="white", command=lambda: render_create_task_view(tk)).grid(row=0, column=1, padx=0, pady=200)


tk = tkinter.Tk()
tk.geometry("700x500")
render_main_view(tk)


tk.mainloop()
