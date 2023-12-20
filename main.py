from dolgozo import Dolgozo

class Ber:
    def __init__(self):
        self.filename = "berkft.txt"
        self.dolgozoLista=[]
        
    def fileread(self):
        f = open(self.filename,"r",encoding="utf-8")
        lines = f.readlines()
        f.close()
        for i in lines:
            i = i.rstrip()
            (nev,telepules,cim,szuletes,fizetes) = i.split(":")
            dolgozo = Dolgozo(nev,telepules,cim,szuletes,fizetes)
            self.dolgozoLista.append(dolgozo)
            #print(i)
            
    def szolnoki(self):
        szolnokLista = []
        for dolgozo in self.dolgozoLista:
            if dolgozo.telepules == "Szolnok":
                szolnokLista.append(dolgozo)
        max_szolnoki = szolnokLista[0]
        for dolgozo in szolnokLista:
            if dolgozo.szuletes > max_szolnoki.szuletes:   
                max_szolnoki=dolgozo
        print(max_szolnoki.szuletes)
        
    def hatvani_fizetes(self):
        osszeg = 0
        for dolgozo in self.dolgozoLista:
            if dolgozo.telepules == "Hatvan":
                osszeg = osszeg + int(dolgozo.fizetes)
        print(f"hatvaniak fizetese: {osszeg}")        
        

                
                
        
ber = Ber()
ber.fileread()
ber.szolnoki()
ber.hatvani_fizetes()
        