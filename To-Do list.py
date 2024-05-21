import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        # Initialize tasks list
        self.tasks = []

        # Create GUI elements
        self.create_widgets()

        # Load tasks from file
        self.load_tasks()

    def create_widgets(self):
        # Task entry
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        # Add task button
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(self.master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Delete task button
        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def load_tasks(self):
        try:
            with open("todo.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                self.update_task_listbox()
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No to-do list file found.")

    def save_tasks(self):
        with open("todo.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
