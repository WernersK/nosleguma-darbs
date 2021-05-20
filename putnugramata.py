import json
#c. tiek saglabati dati json formata
with open("putnugramata.json", "r", encoding='utf-8') as fails:
    dati = fails.read()
putni = json.loads(dati)
def izvelne():
    
    print("Izvelne")
    print("1: meklēt putnu")
    print("2: parādīt putnu vērojumu datus")    
    print("3: pievienot jaunus datus")
    print("4: saglabāt")
    izv = input("Izvēlies!")
    if izv == "1":
        meklesana()
    elif izv == "2":
        visidati()
    elif izv == "3":
        pievienosana()
    elif izv == "4":
        beigas()
    else:
        print("Mēģini vēlreiz!")
        izvelne()
#b. ievaditie dati ierakstiti vardnica vai masiva
def visidati():
    putni = [{"vārds": "Mājas Zvirbulis", "latīņu vārds": "Passer domesticus", "datums": "5/19/2021", "laiks": "12:00", "vieta":"Rīga", "piezīmes":"Mājas zvirbulis ir neliels vai vidēji liels, kompakts dziedātājputns ar lielu, apaļu galvu un spēcīgu knabi."}]
    for p in putni:
        for putni in p:
            print(f"{putni}: {p[putni]}")
        print()
    izvelne()

#f. meklesanas iespeja, rezultatiem paradas uz ekrana
def meklesana():
    putni = input("Raksti meklējamo vārdu! ")
    putni = putni.capitalize()
    meklesana = False
    for p in putni:        
        if putni in p["vārds"]:
            print("Atrasts!")
            meklesana = True
            for atslega in p:
                print(f"{atslega}: {p[atslega]}")
    if not meklesana:
        print("Informācija nav atrasta\n")
    izvelne()    

#a. datu ievades iespeja lietotajam
def pievienosana():
    putni = {}    
    vards = input("Raksti putna vārdu...")
    vards2 = input("Raksti putna latīnisko vārdu...")
    datums = input("Raksti datumu...") 
    laiks = input("Raksti laiku...")
    vieta = input("Raksti putna lokāciju...")
    piezimes = input("Raksturo putnu...")

    putni["vārds"] = vards
    putni["vārds2"] = vards2
    putni["datums"] = datums
    putni["laiks"] = laiks
    putni["vieta"] = vieta
    putni["piezīmes"] = piezimes

    putni.append(putni)
    izvelne()

def beigas():

    with open("putnugramata.json", "w", encoding='utf-8') as fails:
        fails.write(dati)
    print("\nDarbs saglabāts!\n")
#c. tiek saglabati dati json formata
izvelne()
#e. visi dati vai to dala tiek paraditi
