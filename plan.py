import os

DATEI = "aufgaben.txt"


def laden():
    if os.path.exists(DATEI):
        with open(DATEI, "r", encoding="utf-8") as f:
            return [zeile.strip() for zeile in f if zeile.strip()]
    return []


def speichern(aufgaben):
    with open(DATEI, "w", encoding="utf-8") as f:
        for aufgabe in aufgaben:
            f.write(aufgabe + "\n")


aufgaben = laden()

while True:
    print("\n--- Mein Plan ---")
    print("1. Neue Aufgabe")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe löschen")
    print("4. Beenden")
    wahl = input("Was möchtest du tun? ").strip()

    if wahl == "1":
        text = input("Neue Aufgabe: ")
        aufgaben.append(text)
        speichern(aufgaben)
        print("Gespeichert!")
    elif wahl == "2":
        if len(aufgaben) == 0:
            print("Keine Aufgaben.")
        else:
            for nummer, aufgabe in enumerate(aufgaben, start=1):
                print(nummer, aufgabe)
    elif wahl == "3":
        if len(aufgaben) == 0:
            print("Keine Aufgaben zum Löschen.")
        else:
            for nummer, aufgabe in enumerate(aufgaben, start=1):
                print(nummer, aufgabe)
            nummer = input("Welche Nummer löschen? ").strip()
            if nummer.isdigit() and 1 <= int(nummer) <= len(aufgaben):
                gelöscht = aufgaben.pop(int(nummer) - 1)
                speichern(aufgaben)
                print("Gelöscht:", gelöscht)
            else:
                print("Ungültige Nummer.")
    elif wahl == "4":
        print("Tschüss!")
        break
    else:
        print("Bitte 1, 2, 3 oder 4 eingeben.")
