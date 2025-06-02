import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Für Bildanzeige

# Hauptfenster erstellen
root = tk.Tk()
root.title("BERSERK")
root.geometry("500x500")

# === Tkinter-Variablen ===
string_var = tk.StringVar(value="Standardtext")
int_var = tk.IntVar(value=1)
double_var = tk.DoubleVar(value=0.5)
bool_var = tk.BooleanVar(value=False)

# === Bild laden und anzeigen ===
try:
    image = Image.open("Guts.png.jpg")  # Stelle sicher, dass das Bild existiert!
    image = image.resize((200, 150))  # Bild skalieren
    photo = ImageTk.PhotoImage(image)
    image_label = ttk.Label(root, image=photo)
    image_label.image = photo  # Referenz halten!
    image_label.pack(pady=10)
except FileNotFoundError:
    image_label = ttk.Label(root, text="Bild nicht gefunden.")
    image_label.pack(pady=10)

# === Label und Eingabefeld mit StringVar ===
ttk.Label(root, text="Name eingeben:").pack()
entry = ttk.Entry(root, textvariable=string_var)
entry.pack(pady=5)

# === Radiobuttons mit IntVar ===
ttk.Label(root, text="Wähle eine Option:").pack()
ttk.Radiobutton(root, text="Option 1", variable=int_var, value=1).pack()
ttk.Radiobutton(root, text="Option 2", variable=int_var, value=2).pack()

# === Checkbutton mit BooleanVar ===
check = ttk.Checkbutton(root, text="Ich stimme zu", variable=bool_var)
check.pack(pady=10)

# === Scale (Schieberegler) mit DoubleVar ===
ttk.Label(root, text="Lautstärke:").pack()
scale = ttk.Scale(root, from_=0.0, to=1.0, variable=double_var, orient="horizontal")
scale.pack()

# === Funktion zum Anzeigen der aktuellen Werte ===
def anzeigen():
    info = (
        f"Name: {string_var.get()}\n"
        f"Option: {int_var.get()}\n"
        f"Zustimmung: {'Ja' if bool_var.get() else 'Nein'}\n"
        f"Lautstärke: {double_var.get():.2f}"
    )
    messagebox.showinfo("Aktuelle Werte", info)

# === Button zum Anzeigen der Werte ===
ttk.Button(root, text="Werte anzeigen", command=anzeigen).pack(pady=20)

# === Mainloop starten ===
root.mainloop()