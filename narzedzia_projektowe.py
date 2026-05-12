import json
from datetime import datetime

def wczytaj_dane():
    try:
        with open("exercises.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
            return dane
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nie można wczytać pliku!")
        return [] #zwraca pusta liste w przypadku gdy plik nie istnieje albo nie moze zostac odczytany
    

def zapisz_dane(lista):
    try:
        with open("exercises.json", "w", encoding="utf-8") as plik:
            json.dump(lista, plik, indent=4) #uzywamy istniejacej juz zmiennej lista i dodajemu do listy nasze nowe dane "plik"
            return True
    except Exception as e:
        print(f"Błąd zapisu {e}")
        return False # informujemy program, ze nie udalo sie zrobic zapisu pliku
    
def wczytaj_trening():
    try:
        with open("training_log.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
            return dane
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nie można wczytać pliku!")
        return []
    
def zapisz_trening(lista):
    try:
        with open("training_log.json", "w", encoding="utf-8") as plik:
            json.dump(lista, plik, indent=4) #uzywamy istniejacej juz zmiennej lista i dodajemu do listy nasze nowe dane "plik"
            return True
    except Exception as e:
        print(f"Błąd zapisu {e}")
        return False






def dodaj_cwiczenie():
    lista = wczytaj_dane()
    if not lista:
        id = 1
    else:
        nowy = [element["id"] for element in lista]
        id = max(nowy) + 1
    nazwa = str(input("Jak się nazywa to ćwiczenie? "))
    partia = str(input("Jaka jest to partia ciała? "))
    return {
        "id": id,
        "nazwa": nazwa,
        "partia": partia,
    }

def dodaj_trening():
    lista = wczytaj_dane()
    nowy = [element["id"] for element in lista]
    maksymalny = max(nowy)
    x = int(input("Podaj które ćwiczenie chcesz dodać?"))
    if x > maksymalny:
        print("Stop! Nie ma takiego cwiczenia w katalogu.")
        return 
    else:

        for element in lista:
            if element["id"] == x:
                znalezione = element
        id = znalezione["id"]

        serie = int(input("Ile serii zrobiles? "))
        powtorzenia = int(input("Ile powtorzen zrobiles? "))
        data = datetime.now().strftime("%Y-%m-%d")

        return {
            "id": id,
            "serie": serie,
            "powtorzenia": powtorzenia,
            "data": data
        }


