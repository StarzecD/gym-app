import json


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
    








def dodaj_cwiczenie():
    nazwa = str(input("Jak się nazywa to ćwiczenie? "))
    partia = str(input("Jaka jest to partia ciała? "))
    serie = int(input("Ile serii wykonałeś?"))
    return {
        "nazwa": nazwa,
        "partia": partia,
        "liczba serii": serie
    }      