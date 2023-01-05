#Oma tehtävä
#Tee peli, jossa tietokone arpoo luvun väliltä 1-10 ja pelaaja yrittää arvata luvun oikein. Pelaajalla on kaksi yritystä.
#Ensimmäisen yrityksen jälkeen kone kertoo oliko arvattu luku suurempi, pienempi vai oikein. Tämän jälkeen pelaaja saa
#arvata uudestaan, jos ensimmäinen arvaus ei ollut oikea. Toisen arvauksen jälkeen kone kertoo oikean vastauksen. Mikäli
#pelaaja arvaa ensimmäisellä oikein, saa hän kolme pistettä. Jos pelaaja arvaa toisella oikein, hän saa yhden pisteen.
#Toisella kierroksella pelaaja saa päättää luvun väliltä 1-10 ja kone yrittää arvata oikein. Kierrosta pelataan kunnes
#toisella on 5 tai -10 pistettä. Jos molemmat arvaukset menevät väärin, saa yhden miinuspisteen. Peliä pelataan paras
#kolmesta menetelmällä, eli yhden kierroksen voitosta saa yhden pisteen. Aloittaja arvotaan "heittämällä kolikkoa" ja sen
#jälkeen kierrokset aloitetaan vuorotellen.

#Tehtävän vaikeusaste on tähän asti opitun perusteella vaikeahko, sillä tehtävän suorittaakseen on hyödynnettävä sujuvasti
#useita muuttujia sekä etsittävä itse netistä kuinka käytetään random operaattoria. Tehtävässä tulee hyödyntää monipuolisesti
#silmukoita ja ehtolauseita, jotta tehtävän saa ratkaistua.

import random

def peli(aloittaja, koneenPisteet, pelaajanPisteet):
    #Kone aloittaa arvaamisen
    if aloittaja == "kone":
        print("Koneen vuoro arvata!")
        #Pyydetään pelaajaa syöttämään luku väliltä 1-10
        arvattavaLuku = int(input("Anna kokonaisluku väliltä 1-10: "))
    elif aloittaja == "pelaaja":
        print("Pelaajan vuoro arvata!")
        #Kone arpoo luvun väliltä 1-10
        arvattavaLuku = random.randint(1,10)
    #Jos syötetty luku vastaa pyydettyä lukua, jatketaan peliä. Muuten pyydetään
    #syöttämään uusi luku
    if type(arvattavaLuku) == int and (arvattavaLuku >= 1 and arvattavaLuku <= 10):
        #Kone tekee ensimmäisen arvauksen
        if aloittaja == "kone":
            arvaus = random.randint(1,10)
        elif aloittaja == "pelaaja":
            arvaus = int(input("Arvaa kokonaisluku väliltä 1-10: "))
        #Jos oikein, kone saa kolme pistettä ja siirrytään pelaajan arvausvuoroon
        if arvaus == arvattavaLuku:
            if aloittaja == "kone":
                koneenPisteet += 3
                #Asetetaan pelaaja aloittajaksi
                aloittaja = "pelaaja"
                print(f"Koneen arvaus: {arvaus}")
            elif aloittaja == "pelaaja":
                pelaajanPisteet += 3
                #Asetetaan kone aloittajaksi
                aloittaja == "kone"
            print(f"Oikein! Pistetilanne on: Pelaaja: {pelaajanPisteet} ja Kone: {koneenPisteet}")
        #Täytyy arvata uudestaan, mutta tietää nyt että luku on suurempi
        elif arvaus < arvattavaLuku:
            if aloittaja == "kone":
                print(f"Koneen arvaus: {arvaus}")
            print("Oikea vastaus on suurempi kuin arvaus.")
            if aloittaja == "kone":
                #Koneen toinen arvaus
                uusiArvaus = random.randint(arvaus+1,10)
            elif aloittaja == "pelaaja":
                uusiArvaus = int(input("Arvaa uusi luku: "))
            #Jos arvaus on oikein, vuorossa oleva saa yhden pisteen ja siirrytään seuraavan arvaukseen
            if uusiArvaus == arvattavaLuku:
                if aloittaja == "kone":
                    koneenPisteet += 1
                    #Asetetaan pelaaja aloittajaksi
                    aloittaja = "pelaaja"
                    print(f"Koneen arvaus: {uusiArvaus}")
                elif aloittaja == "pelaaja":
                    pelaajanPisteet += 1
                    #Asetetaan kone aloittajaksi
                    aloittaja = "kone"
                print(f"Oikein! Pistetilanne on: Pelaaja: {pelaajanPisteet} ja Kone: {koneenPisteet}")
            #Jos arvaus on väärin, vuorossa oleva saa yhden miinuspisteen ja siirrytään seuraavan arvaukseen
            else:
                if aloittaja == "kone":
                    koneenPisteet -= 1
                    #Asetetaan pelaaja aloittajaksi
                    aloittaja = "pelaaja"
                    print(f"Koneen arvaus: {uusiArvaus}")
                elif aloittaja == "pelaaja":
                    pelaajanPisteet -= 1
                    #Asetetaan kone aloittajaksi
                    aloittaja = "kone"
                print(f"Oikea vastaus oli {arvattavaLuku}. Pistetilanne on: Pelaaja: {pelaajanPisteet} ja Kone: {koneenPisteet}")
        #Kone joutuu arvaamaan uudestaan, mutta tietää että luku on pienempi
        else:
            if aloittaja == "kone":
                print(f"Koneen arvaus: {arvaus}")
            print("Oikea vastaus on pienempi kuin arvaus.")
            if aloittaja == "kone":
                #Koneen toinen arvaus
                uusiArvaus = random.randint(1,arvaus-1)
            elif aloittaja == "pelaaja":
                uusiArvaus = int(input("Anna uusi luku: "))
            #Jos arvaus on oikein, kone saa yhden pisteen ja siirrytään pelaajan arvaukseen
            if uusiArvaus == arvattavaLuku:
                if aloittaja == "kone":
                    koneenPisteet += 1
                    #Asetetaan pelaaja aloittajaksi
                    aloittaja = "pelaaja"
                    print(f"Koneen arvaus: {uusiArvaus}")
                elif aloittaja == "pelaaja":
                    pelaajanPisteet += 1
                    #Asetetaan kone aloittajaksi
                    aloittaja = "kone"
                print(f"Oikein! Pistetilanne on: Pelaaja: {pelaajanPisteet} ja Kone: {koneenPisteet}")
            #Jos arvaus on väärin, kone saa yhden miinuspisteen siirrytään pelaajan arvaukseen
            else:
                if aloittaja == "kone":
                    koneenPisteet -= 1
                    #Asetetaan pelaaja aloittajaksi
                    aloittaja = "pelaaja"
                    print(f"Koneen arvaus: {uusiArvaus}")
                elif aloittaja == "pelaaja":
                    pelaajanPisteet -= 1
                    #Asetetaan kone aloittajaksi
                    aloittaja = "kone"
                print(f"Oikea vastaus oli {arvattavaLuku}. Pistetilanne on: Pelaaja: {pelaajanPisteet} ja Kone: {koneenPisteet}")
    else:
            print("Annettu luku ei ole kokonaisluku väliltä 1-10")

    return (aloittaja, koneenPisteet, pelaajanPisteet)

#Asetetaan molempien kokonaispisteet alussa nollaksi
pelaajanKokPisteet = 0
koneenKokPisteet = 0

#Arvotaan aloittaja
aloitusArvaus = input("\"kruuna\" vai \"klaava\": ")
#kruuna = 0, klaava = 1
kolikonHeitto = random.randint(0,1)
#Asetetaan aloittaja-muuttuja tyhjäksi
aloittaja = ""
if kolikonHeitto == 0 and aloitusArvaus == "kruuna" or kolikonHeitto == 1 and aloitusArvaus == "klaava":
    #Asetetaan aloittajaksi pelaaja
    aloittaja = "pelaaja"
else:
    #Asetetaan aloittajaksi kone
    aloittaja = "kone"

#Silmukka joka kestää kunnes toisella on kolme pistettä
while pelaajanKokPisteet < 3 and koneenKokPisteet < 3:

    #Tulostetaan kokonaispistetilanne
    print(f"Kokonaispistetilanne on: Pelaaja: {pelaajanKokPisteet}, Kone: {koneenKokPisteet}")

    #Asetetaan molempien kierrospisteet nollaksi
    pelaajanPisteet = 0
    koneenPisteet = 0

    #Luodaan muuttuja "seuraavaAloittaja" johon voidaan tallentaa seuraavan kierroksen aloittaja
    #edellisen kierroksen aloittajan perusteella
    if aloittaja == "kone":
        seuraavaAloittaja = "pelaaja"
        print("Kone aloittaa arvaamisen.")
    else:
        seuraavaAloittaja = "kone"
        print("Pelaaja aloittaa arvaamisen.")

    #Pelataan kierrosta kunnes toisella on 5 tai -10 pistettä
    while pelaajanPisteet < 5 and pelaajanPisteet > -10 and koneenPisteet < 5 and koneenPisteet > -10:

        peli(aloittaja, koneenPisteet, pelaajanPisteet)

        

    #Jaetaan pisteet kierroksen voittajalle
    if pelaajanPisteet == 5:
        pelaajanKokPisteet += 1
    elif pelaajanPisteet == -10:
        koneenKokPisteet += 1
    elif koneenPisteet == -10:
        pelaajanKokPisteet += 1
    else:
        koneenKokPisteet += 1
    
    #Asetetaan seuraavan kierroksen aloittaja edellisen kierroksen aloittajan perusteella
    if seuraavaAloittaja == "pelaaja":
        aloittaja = "pelaaja"
        seuraavaAloittaja = "kone"
    else:
        aloittaja = "kone"
        seuraavaAloittaja = "pelaaja"

#Tulostetaan kiitosviesti ja pelin tulos
if pelaajanKokPisteet > koneenKokPisteet:
    print(f"Kiitos pelistä! Pelaaja voitti pistein {pelaajanKokPisteet}, {koneenKokPisteet}")
else:
    print(f"Kiitos pelistä! Kone voitti pistein {koneenKokPisteet}, {pelaajanKokPisteet}")