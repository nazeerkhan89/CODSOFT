import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x500")
        
        # Data file
        self.data_file = "todo_data.json"
        self.tasks = self.load_tasks()
        
        # UI Setup
        self.create_widgets()
        self.update_task_list()
        
    def create_widgets(self):
        # Frame for task entry
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(entry_frame, width=40, font=('Arial', 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)
        
        # Frame for task list
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.task_listbox = tk.Listbox(
            list_frame, 
            width=60, 
            height=15, 
            font=('Arial', 11), 
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        complete_button = tk.Button(
            button_frame, 
            text="Mark Complete", 
            command=self.mark_complete
        )
        complete_button.pack(side=tk.LEFT, padx=5)
        
        edit_button = tk.Button(
            button_frame, 
            text="Edit Task", 
            command=self.edit_task
        )
        edit_button.pack(side=tk.LEFT, padx=5)
        
        delete_button = tk.Button(
            button_frame, 
            text="Delete Task", 
            command=self.delete_task
        )
        delete_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(
            button_frame, 
            text="Clear All", 
            command=self.clear_tasks
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Total Tasks: 0 | Completed: 0")
        status_bar = tk.Label(
            self.root, 
            textvariable=self.status_var, 
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X)
    
    def load_tasks(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []
    
    def save_tasks(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f)
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")
        
        # Update status bar
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        self.status_var.set(f"Total Tasks: {total_tasks} | Completed: {completed_tasks}")
    
    def add_task(self):
        task_title = self.task_entry.get().strip()
        if task_title:
            new_task = {
                'title': task_title,
                'completed': False,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task title cannot be empty!")
    
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.tasks[index]['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_tasks()
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")
    
    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_title = simpledialog.askstring(
                "Edit Task", 
                "Edit task title:", 
                initialvalue=self.tasks[index]['title']
            )
            if new_title and new_title.strip():
                self.tasks[index]['title'] = new_title.strip()
                self.tasks[index]['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to edit!")
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            confirm = messagebox.askyesno(
                "Confirm Delete", 
                f"Are you sure you want to delete: {self.tasks[index]['title']}?"
            )
            if confirm:
                del self.tasks[index]
                self.save_tasks()
                self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def clear_tasks(self):
        if self.tasks:
            confirm = messagebox.askyesno(
                "Confirm Clear", 
                "Are you sure you want to delete ALL tasks?"
            )
            if confirm:
                self.tasks = []
                self.save_tasks()
                self.update_task_list()
        else:
            messagebox.showinfo("Info", "No tasks to clear!")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
