def kalkulator():
    while True:
        # Pobranie wyrażenia od użytkownika
        wyrazenie = input("Wpisz wyrażenie'koniec', aby zakończyć: ")

        # Sprawdzenie, czy użytkownik chce zakończyć
        if wyrazenie.lower() == "koniec":
            print("koniec programu")
            break

        try:
            # Obliczenie wyniku za pomocą funkcji eval
            wynik = eval(wyrazenie)
            print(f"Wynik: {wynik}")
        except Exception as e:
            print(f"Nieprawidłowe wyrażenie: {e}")

# Uruchomienie kalkulatora
kalkulator()
