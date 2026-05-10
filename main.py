from narzedzia_projektowe import dodaj_cwiczenie, wczytaj_dane, zapisz_dane

while True:
        print("\n--- MENU ---")
        print("1. Nowe ćwiczenie")
        print("2. Podgląd dostępnych ćwiczeń")
        print("3. Usuń ćwiczenie")
        print("4. Pokaż statystyki")
        print("5. Wyloguj się i wyjdź")
        try:
            wybor = int(input("Co chcesz dzisiaj zrobić? "))
        
            if wybor == 1:
                print("Wybrałeś dodanie nowego ćwiczenia do listy")
                nowe = dodaj_cwiczenie()
                lista = wczytaj_dane()
                lista.append(nowe)
                zapisz_dane(lista)
            elif wybor == 2:
                lista = wczytaj_dane()
                for element in lista: #wez kazdy element z listy
                    print(element["nazwa"])
                print(element["partia"])
                print(element["liczba serii"])
                print("-----")
            elif wybor == 3:
                print("Wybrałeś usunięcie starego ćwiczenia")
            elif wybor == 4:
                print("Wybrałeś pokazanie statystyk")
            elif wybor == 5:
                print("Wybrałeś wyłączenie programu.")
                break
            else:
                print("Stop! Wybrałes niepoprawną liczbę!")
        except ValueError:
            print("Błąd!")
