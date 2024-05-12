import sys
import szobakezelo
from datetime import datetime
from tabulate import tabulate
from szobakezelo import kezeles


# Call the olvasas method to populate the szoba list
szoba = kezeles.olvasas()


def display_menu():
    print("A menü használatakor ügyeljen a megfelelő szám beütésére!"
          + "Kérjük csak a kívánt menüpont számát adja meg!")
    print("-----------------------")
    print("1 - Szoba foglalok")
    print("2 - Szoba lemondok")
    print("3 - Összes szoba")
    print("4 - Kilépés")

    felhasznalo_dontese = int(input("Adja meg a kivant menupont szamat: \n"))

    if felhasznalo_dontese == 1:
        foglalok()
    elif felhasznalo_dontese == 2:
        lemondok()
    elif felhasznalo_dontese == 3:
        osszes()
    elif felhasznalo_dontese == 4:
        kilepes()
    else:
        print("Figyeljen az utasításra")
        return display_menu()


def kilepes():
    sys.exit()


def foglalok():
    table = []
    szabadok = []
    for item in szoba:
        if item.foglalt == False or item.foglalt == 0 or item.foglalt == "0":
            table.append([item.szoba_szam, item.agyak_szama, item.ar, item.foglalt])
            szabadok.append(int(item.szoba_szam))
        else: print()
    
    print("Szabad szobáink")
    print(tabulate(table, headers=["Szoba szám", "Ágyak száma", "Ár", "Foglalt"]))
    
    felhaszo_adatai = []
    #szoba valasztas
    felhasznalo_dontese = int(input("Melyik szobat szeretne lefoglalni ?: "))
    if felhasznalo_dontese in szabadok: felhaszo_adatai.append(felhasznalo_dontese)
    else : print("A megadott szoba nincs a listában")
    
    #nev
    felhasznalo_neve = input("Milyen neven foglalom a szobát ?")
    if felhasznalo_neve != " " or felhasznalo_neve != "" or len(felhasznalo_neve) < 3 or len(felhasznalo_neve) > 50: felhaszo_adatai.append(felhasznalo_neve)
    else: print("A név nem megfelelően lett kitöltve!")
    
    #dátumok
    felhasznalo_kezdete = input("Mikortol foglalja a szobat ? (yyyy-mm-dd)")
    felhasznalo_vege = input("Meddig foglalja a szobat ? (yyyy-mm-dd)")
    felhaszo_adatai.append(felhasznalo_kezdete)
    felhaszo_adatai.append(felhasznalo_vege)
    
    kezeles.felvete(szoba, felhaszo_adatai)

    return display_menu

def lemondok():
    table = []
    foglaltak = []
    for item in szoba:
        if item.foglalt == True or item.foglalt == 1 or item.foglalt == "1":
            table.append([item.szoba_szam, item.agyak_szama, item.ar, item.foglalt, item.kezdet, item.vege, item.foglalo_neve])
            foglaltak.append(int(item.szoba_szam))
        else:
            print()
        
    print("Foglalt szobáink")
    print(tabulate(table, headers=["Szoba szám", "Ágyak száma", "Ár", "Foglalt", "Kezdet", "Vége", "Foglaló neve"]))
    
    felhasznalo_dontese = int(input("Melyik szobat szeretne lefoglalni ?: "))
    if felhasznalo_dontese in foglaltak: 
        biztos = input("Biztos szeretné törölni a foglalást? (i/n): ")
        if biztos == "i": 
            print("A szobafoglalás törölve lett")
            kezeles.lemondas(szoba, felhasznalo_dontese)
            # Pass both arguments to lemondas method
        else: 
            print("A foglalás nem lett törölve")
    else: 
        print("ilyen szoba nem létezik")
            
    return display_menu


def osszes():
    print("\n Összes foglalás: \n")
    table = []
    for item in szoba:
        table.append([item.szoba_szam, item.agyak_szama, item.ar, item.foglalt, item.kezdet, item.vege, item.foglalo_neve])
    print(tabulate(table, headers=["Szoba szám", "Ágyak száma", "Ár", "Foglalt", "Kezdet", "Vége", "Foglaló neve"]))
    
    return display_menu

display_menu()
