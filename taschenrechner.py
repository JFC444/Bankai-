import tkinter as tk
from tkinter import messagebox
 
class Rechner:
    def __init__(self, root):
        self.root = root
        self.root.title("Rechner")
        self.root.configure(bg='#f0f0f0')
        self.create_widgets()
 
    def create_widgets(self):
        tk.Label(self.root, text="Zahl 1:", bg='#f0f0f0').grid(row=0, column=0, pady=5, padx=5)
        self.entry1 = tk.Entry(self.root)
        self.entry1.grid(row=0, column=1, pady=5)
 
        tk.Label(self.root, text="Zahl 2:", bg='#f0f0f0').grid(row=1, column=0, pady=5, padx=5)
        self.entry2 = tk.Entry(self.root)
        self.entry2.grid(row=1, column=1, pady=5)
 
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
 
        tk.Button(button_frame, text="+", width=5, command=self.add).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="-", width=5, command=self.subtract).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="*", width=5, command=self.multiply).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="/", width=5, command=self.divide).grid(row=0, column=3, padx=5)
 
        self.result_label = tk.Label(self.root, text="Ergebnis: ", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
 
        tk.Button(self.root, text="Clear", command=self.clear_entries, bg="lightcoral").grid(row=4, column=0, columnspan=2, pady=5)
 
    def get_input(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Eingabefehler", "Bitte gültige Zahl eingeben.")
            return None, None
 
    def add(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            result = num1 + num2
            self.result_label.config(text=f"Ergebnis: {result}")
 
    def subtract(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            result = num1 - num2
            self.result_label.config(text=f"Ergebnis: {result}")
 
    def multiply(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            result = num1 * num2
            self.result_label.config(text=f"Ergebnis: {result}")
 
    def divide(self):
        num1, num2 = self.get_input()
        if num1 is not None:
            if num2 == 0:
                messagebox.showerror("Eingabefehler", "Division durch Null ist nicht erlaubt.")
                return
            result = num1 / num2
            self.result_label.config(text=f"Ergebnis: {result}")
 
    def clear_entries(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="Ergebnis: ")
 
if __name__ == "__main__":
    root = tk.Tk()
    app = Rechner(root)
    root.mainloop()