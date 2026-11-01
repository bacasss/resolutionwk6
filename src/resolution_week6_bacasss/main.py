import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_task(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task():
    task_text = entry.get()
    if task_text == "":
        messagebox.showwarning("warning", "please enter a task")
        return
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    priority = priority_entry.get()
    tasks.append({"id": new_id, "task": task_text, "done": False, "priority": priority})
    save_task(tasks)

    listbox.delete(0, tk.END)
    for task in tasks:
        if task["done"]:
            status  = "x"
        else:
            status = " "
        listbox.insert(tk.END, f"[{status}]{task['id']}: {task['task']}, Priority: {task['priority']}")
    entry.delete(0, tk.END)

def complete_task():
    selection =  listbox.curselection()
    if len(selection) == 0:
        messagebox.showerror("error", "no task selected")
        return
    index = selection[0]
    tasks[index]["done"] = not tasks[index]["done"]
    save_task(tasks)
    
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["done"]:
            status = "x"
        else:
            status = " "
        listbox.insert(tk.END, f"[{status}]{task['id']}: {task['task']}, Priority: {task['priority']}")

def delete_task():
    selection = listbox.curselection()
    if len(selection) == 0:
        messagebox.showerror("error", "no task selected")
        return
    if messagebox.askyesno("confirm", "are you sure you want to delete this?"):
        index = selection[0]
        tasks.pop(index)
        save_task(tasks)
        listbox.delete(0, tk.END)
        for task in tasks:
            if task["done"]:
                status = "x"
            else:
                status = " "
            listbox.insert(tk.END, f"[{status}]{task['id']}: {task['task']}, Priority: {task['priority']}")

def on_enter(event):
    add_task()

def main():
    global tasks, entry, priority_entry, listbox
    tasks = load_tasks()
    root = tk.Tk()
    root.title("to do listtttttt")
    root.geometry("500x400")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    tk.Label(root, text="to do listttt").grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    main_frame = tk.Frame(root)
    main_frame.grid(row=1, column=0, padx=10, pady = 10, sticky="nsew")
    main_frame.columnconfigure(0, weight = 1)
    main_frame.rowconfigure(1, weight = 1)
    input_frame = tk.Frame(main_frame)
    input_frame.grid(row=0, column=0, sticky= "ew")
    input_frame.columnconfigure(1, weight=1)
    tk.Label(input_frame, text="task: ").grid(row=0, column=0, padx=5, pady=5)
    entry = tk.Entry(input_frame)
    entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    tk.Label(input_frame,text="priority: ").grid(row=1, column=0, padx=5, pady=5)
    priority_entry = tk.Entry(input_frame)
    priority_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    listbox_frame = tk.Frame(main_frame)
    listbox_frame.grid(row = 1, column=0, sticky="nsew")
    listbox_frame.columnconfigure(0, weight=1)
    listbox_frame.rowconfigure(0, weight=1)
    scrollbar = tk.Scrollbar(listbox_frame)
    scrollbar.grid(row=0, column=1, sticky="ns")
    listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set)
    listbox.grid(row=0, column=0, sticky="nsew")
    scrollbar.config(command=listbox.yview)
    tk.Button(main_frame, text="add task", command=add_task).grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(main_frame, text="complete/incomplete", command=complete_task).grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(main_frame, text="delete task", command=delete_task).grid(row=4, column=0, padx =5, pady=5, sticky="ew")
    entry.bind("<Return>", on_enter)
    for task in tasks:
        if task["done"]:
            status = "x"
        else:
            status = " "
        listbox.insert(tk.END, f"[{status}]{task['id']}: {task['task']}, priority: {task['priority']}")
    root.mainloop()

if __name__ == "__main__":
    main()
