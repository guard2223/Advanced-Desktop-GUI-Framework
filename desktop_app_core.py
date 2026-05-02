import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

# ADVANCED DESKTOP GUI FRAMEWORK
# Focused on modularity, modern aesthetics, and responsive performance.

class ModernApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enterprise Control Center v2.0")
        self.geometry("900x600")
        self.configure(bg="#121212") # Modern Dark Theme
        
        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#121212")
        self.style.configure("TLabel", background="#121212", foreground="#ffffff")
        self.style.configure("TButton", padding=10, font=('Segoe UI', 10, 'bold'))

    def create_widgets(self):
        # Navigation Panel
        nav_panel = ttk.Frame(self)
        nav_panel.pack(side="left", fill="y", padx=20, pady=20)
        
        ttk.Label(nav_panel, text="DASHBOARD", font=("Segoe UI", 16, "bold")).pack(pady=20)
        
        # Action Buttons
        actions = ["System Monitor", "Security Scan", "Data Sync", "Settings"]
        for action in actions:
            ttk.Button(nav_panel, text=action, command=lambda a=action: self.on_action(a)).pack(fill="x", pady=10)

        # Main Content Area
        self.content_area = ttk.Frame(self)
        self.content_area.pack(side="right", expand=True, fill="both", padx=20, pady=20)
        
        self.status_label = ttk.Label(self.content_area, text="Ready for operation...", font=("Segoe UI", 12))
        self.status_label.pack(pady=100)

    def on_action(self, action):
        """Asynchronous task handling to keep UI responsive."""
        self.status_label.config(text=f"Running {action} in background...")
        threading.Thread(target=self.simulate_task, args=(action,), daemon=True).start()

    def simulate_task(self, action):
        time.sleep(3) # Simulate work
        self.after(0, lambda: self.status_label.config(text=f"{action} completed successfully."))
        self.after(0, lambda: messagebox.showinfo("Task Done", f"Successfully executed: {action}"))

if __name__ == "__main__":
    app = ModernApp()
    app.mainloop()
