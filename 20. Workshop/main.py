import tkinter
from tkcalendar import DateEntry
from tkinter import scrolledtext
from tkinter.ttk import Combobox
import json

all_tasks_to_write = []


def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()


def all_tasks_from_file():
    with open("db.txt", "r") as file:
        try:
            all_existing_tasks = json.load(file)
        except json.decoder.JSONDecodeError:
            existing_tasks = []
    return existing_tasks


def write_tasks_to_file(all_tasks_to_write, existing_tasks=None):
    with open("db.txt", "r+") as file:
        if not existing_tasks:
            existing_tasks = all_tasks_from_file()
        file.seek(0)
        file.truncate()
        all_tasks_to_write.extend(existing_tasks)
        json.dump(*all_tasks_to_write, file)


def edit_task(tk, value):
    pass


def delete_task(tk, value):
    existing_tasks = all_tasks_from_file()
    existing_tasks.remove(eval(value))
    write_tasks_to_file(all_tasks_to_write, existing_tasks)


def render_list_task_view(tk):
    clear_view(tk)
    box = Combobox(tk)
    existing_tasks = all_tasks_from_file()
    box['values'] = existing_tasks
    box.grid(row=0, column=0)
    tkinter.Button(tk, text="Edit", bg="yellow", command=lambda: edit_task(tk, box.get())).grid(row=1, column=0, pady=20)
    tkinter.Button(tk, text="Delete", bg="red", command=lambda: delete_task(tk, box.get())).grid(row=1, column=1, padx=20, pady=30)


def create_task(**kwargs):
    all_tasks_to_write.append(kwargs)


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
    tkinter.Button(tk, text="List tasks", bg="blue", fg="white", command=lambda: render_list_task_view(tk)).grid(
        row=0, column=0, padx=200, pady=200)
    tkinter.Button(tk, text="Create tasks", bg="green", fg="white", command=lambda: render_create_task_view(tk)).grid(
        row=0, column=1, padx=0, pady=200)


tk = tkinter.Tk()
tk.geometry("700x500")
render_main_view(tk)

tk.mainloop()
write_tasks_to_file(all_tasks_to_write)
