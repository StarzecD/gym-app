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
                lista.append(nowe) #Dodaje na koniec wczesniej juz istniejacej listy, nowe dane
                zapisz_dane(lista)
            elif wybor == 2:
                lista = wczytaj_dane()
                print("-----")
                for element in lista: #wez kazdy element z listy         
                    print(element["nazwa"])
                    print(element["partia"])
                    print(element["liczba serii"])
                    print("-----\n")
            elif wybor == 3:
                print("Wybrałeś usunięcie starego ćwiczenia")
                lista = wczytaj_dane()
                if lista == []:
                    print("Błąd! Lista jest pusta!")
                else:
                    try:
                        x = int(input("Które cwiczenie chcesz usunąć? "))       
                        if x <= 0 or x > len(lista):
                            print("Błąd! Nie ma takiego numeru ćwiczenia!!")
                        else:
                            wynik = x-1
                            del lista[wynik]
                            zapisz_dane(lista)
                    except ValueError:
                        print("Błąd! Niepoprawna liczba!")
            elif wybor == 4:
                print("Wybrałeś pokazanie statystyk")
            elif wybor == 5:
                print("Wybrałeś wyłączenie programu.")
                break
            else:
                print("Stop! Wybrałes niepoprawną liczbę!")
        except ValueError:
            print("Błąd!")
