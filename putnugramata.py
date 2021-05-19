import json

with open("putnugramata.json", "r", encoding='utf-8') as fails:
    dati = fails.read()

def izvelne():
    print("Izvelne")
    print("1: parādīt putnu vērojumu datus")
    print("2: pievienot jaunus datus")
    print("3: meklēt putnu")
    print("4: saglabāt")
    izv = input("Izvēlies!")
    if izv == "1":
        radit()
    elif izv == "2":
        meklet()
    elif izv == "3":
        pievienot()
    elif izv == "4":
        beigas()
    else:
        print("Mēģini vēlreiz!")
        izvelne()

def radit():
    putni = [{"vārds": "Mājas Zvirbulis", "latīņu vārds": "Passer domesticus", "datums": "5/19/2021", "laiks": "12:00", "vieta":"Rīga", "piezīmes":"Mājas zvirbulis ir neliels vai vidēji liels, kompakts dziedātājputns ar lielu, apaļu galvu un spēcīgu knabi."}]
    for p in putni:
        for atslega in p:
            print(f'{atslega}: {p[atslega]}')
        print()
    izvelne()

def pievienot():
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

    putni = [] 
    putni.append(putni)
    print("\nDati saglabāti!\n")
    izvelne()

def meklet():
    putni = input("Raksti meklējamo vārdu! ")
    putni = putni.capitalize()
    meklet = False
    for p in putni:        
        if putni in p["vārds"]:
            print("Atrasts:")
            meklet = True
            for atslega in p:
                print(f'{atslega}: {p[atslega]}')
    if not meklet:
        print("Informācija nav atrasta\n")
    izvelne()     

def beigas():

    with open("putnugramata.json", "w", encoding='utf-8') as fails:
        fails.write(dati)
    print("Fails saglabāts. Programmas beigas.\n")

izvelne()
