import szoba

class kezeles:
    @staticmethod
    def olvasas():
        osszes_szoba = []
        utvonal = "adatok/szobak.txt"
        with open(utvonal, "r") as olvaso:
            for i in olvaso:
                adatom = i.strip().split(";")
                if len(adatom) < 7:
                    alapertek = szoba.fulkek.alapertekek()
                    adatom = [alapertek[key] if key not in adatom else adatom[adatom.index(key)] for key in alapertek.keys()]
                atadas = szoba.fulkek(adatom[0], adatom[1], adatom[2], adatom[3], adatom[4], adatom[5], adatom[6])
                osszes_szoba.append(atadas)
        return osszes_szoba
    
    @staticmethod
    def felvete(osszes_szoba, felhasznalo_adatai):
        szoba_szam, felhasznalo_neve, felhasznalo_kezdete, felhasznalo_vege = felhasznalo_adatai
        for szoba in osszes_szoba:
            if int(szoba.szoba_szam) == int(szoba_szam):
                szoba.foglalt = 1
                szoba.kezdet = felhasznalo_kezdete
                szoba.vege = felhasznalo_vege
                szoba.foglalo_neve = felhasznalo_neve
                print("A foglalás sikeresen megtörtént.")
                break
        else:
            print("A megadott szobaszám nem létezik.")
            
        utvonal = "adatok/szobak.txt"
        with open(utvonal, "w") as iras:
            for szoba in osszes_szoba:
                iras.write(f"{szoba.szoba_szam};{szoba.agyak_szama};{szoba.ar};{szoba.foglalt};{szoba.kezdet};{szoba.vege};{szoba.foglalo_neve}\n")

        
    @staticmethod
    def lemondas(osszes_szoba, felhasznalo_dontese):
        for szoba in osszes_szoba:
            if int(szoba.szoba_szam) == int(felhasznalo_dontese):
                szoba.foglalt = 0
                szoba.kezdet = ""
                szoba.vege = ""
                szoba.foglalo_neve = ""
                print("A foglalás sikeresen lemondva.")
                break
        else:
            print("A megadott szobaszám nem létezik.")
        
        # Write the changes back to the file
        utvonal = "adatok/szobak.txt"
        with open(utvonal, "w") as iras:
            for szoba in osszes_szoba:
                iras.write(f"{szoba.szoba_szam};{szoba.agyak_szama};{szoba.ar};{szoba.foglalt};{szoba.kezdet};{szoba.vege};{szoba.foglalo_neve}\n")
