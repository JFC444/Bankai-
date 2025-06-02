import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("BERSERK")
root.geometry("400x400")  
 

bilddatei = "Guts.png.jpg"
 
try:
    image = Image.open(bilddatei)

    image = image.resize((300, 300))

    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.pack(pady=20)  
    print("Bild erfolgreich geöffnet und angezeigt!")

except FileNotFoundError:
    print(f"Bild '{"bilddatei"}' nicht gefunden!")
    label = tk.Label(root, text="Bild nicht gefunden!", bg="red", fg="white")
    label.pack(pady=20)
    
except Exception as e:
    print("Ein anderer Fehler ist aufgetreten:", e)
    label = tk.Label(root, text="Fehler beim Laden!", bg="red", fg="white")
    label.pack(pady=20)

root.mainloop()