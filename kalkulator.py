import tkinter as tk
from tkinter import messagebox

def oblicz_wyrazenie(event=None):  # Dodano opcjonalny argument event
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

def wstaw_tekst(tekst):
    entry.insert(tk.END, tekst)

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Kalkulator")

# Pola tekstowe i przyciski
label = tk.Label(root, text="Wpisz wyrażenie:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()
entry.bind('<Return>', oblicz_wyrazenie)  # Przypisanie Enter do funkcji oblicz_wyrazenie

# Przyciski cyfr i operatorów
frame = tk.Frame(root)
frame.pack()

przyciski = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('.', 3, 0), ('0', 3, 1), ('+', 3, 2), ('=', 3, 3)
]

for (tekst, wiersz, kolumna) in przyciski:
    button = tk.Button(frame, text=tekst, width=5, command=lambda t=tekst: wstaw_tekst(t))
    button.grid(row=wiersz, column=kolumna)

# Przyciski dodatkowe
button = tk.Button(root, text="Oblicz", command=oblicz_wyrazenie)
button.pack()

koniec_button = tk.Button(root, text="Koniec", command=root.destroy)
koniec_button.pack()

# Uruchomienie aplikacji
root.mainloop()
