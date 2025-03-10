import tkinter as tk
from tkinter import messagebox

def oblicz_wyrazenie():
    wyrazenie = entry.get()
    if wyrazenie.lower() == "koniec":
        root.destroy()  # Zamyka GUI
    else:
        try:
            wynik = eval(wyrazenie)
            messagebox.showinfo("Wynik", f"Wynik: {wynik}")
        except SyntaxError:
            messagebox.showerror("Błąd", "Nieprawidłowe wyrażenie: błąd składni")
        except ZeroDivisionError:
            messagebox.showerror("Błąd", "Nieprawidłowe wyrażenie: dzielenie przez zero")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nieprawidłowe wyrażenie: {e}")

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Kalkulator")

# Pola tekstowe i przyciski
label = tk.Label(root, text="Wpisz wyrażenie:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Oblicz", command=oblicz_wyrazenie)
button.pack()

koniec_button = tk.Button(root, text="Koniec", command=root.destroy)
koniec_button.pack()

# Uruchomienie aplikacji
root.mainloop()
