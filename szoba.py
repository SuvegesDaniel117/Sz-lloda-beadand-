class fulkek: 
    def __init__(self,szoba_szam,agyak_szama,ar,foglalt,kezdet,vege,foglalo_neve):
        self.szoba_szam = szoba_szam
        self.agyak_szama = agyak_szama
        self.ar = ar
        self.foglalt = foglalt
        self.kezdet = kezdet
        self.vege = vege
        self.foglalo_neve = foglalo_neve
        #int,int,float,bool,date,date,string
    
    def alapertekek():
        return{
            "szoba_szam" : "",
            "agyak_szama" : 0,
            "ar" : 0.0,
            "foglalt" : 0,
            "kezdet" : "",
            "vege" : "",
            "foglalo_neve" : ""
        }