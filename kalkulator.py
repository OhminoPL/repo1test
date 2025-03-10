def kalkulator():
    while True:
        # Pobranie wyrażenia od użytkownika
        wyrazenie = input("Wpisz wyrażenie lub 'koniec', aby zakończyć: ")

        # Sprawdzenie, czy użytkownik chce zakończyć
        if wyrazenie.lower() == "koniec":
            print("Koniec programu")
            break

        try:
            # Obliczenie wyniku za pomocą funkcji eval
            wynik = eval(wyrazenie)
            print(f"Wynik: {wynik}")
        except SyntaxError:
            print("Nieprawidłowe wyrażenie: błąd składni")
        except ZeroDivisionError:
            print("Nieprawidłowe wyrażenie: dzielenie przez zero")
        except Exception as e:
            print(f"Nieprawidłowe wyrażenie: {e}")

# Uruchomienie kalkulatora
kalkulator()
