print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+      Sollicitatieformulier  Circusdirecteur        +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen")
print("Als blijkt dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus sollicitatiegesprek!")
print("Ontspan maar blijf wakker, hier komen de vragen")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
print("")

aannemen = False

Vraag1 = input("Hoeveel jaar praktijkervaring heb je met dieren-dressuur? ")
Vraag2 = input("Hoeveel jaar ervaring heb je met jongleren? ")
Vraag3 = input("Hoeveel jaar praktijkervaring heb je met acrobatiek? ")
Vraag4 = input("Ben je in het bezit van een diploma MBO-4 ondernemen? ").lower()
Vraag5 = input("Ben je in het bezit van een vrachtwagen rijbewijs? ").lower()
Vraag13 = input("Heb je een strafblad? ")
Vraag6 = input("Ben je in het bezit van een hoge hoed? ").lower()
Vraag7 = input("Ben je een man of een vrouw? ").lower()
if Vraag7 == "man":
    Snor = input("Hoe breed is jouw snor in centimeter? Als je geen snor hebt vul je 0 in. ")
elif Vraag7 == "vrouw":
    Krulhaar = input("Draag je rood krulhaar? ")
    Krulcm = input("Hoelang is jouw haar in cm? ")
Vraag8 = input("Hoe lang ben je in cm? ")
Vraag9 = input("Hoeveel weeg je in KG? ")
Vraag14 = input("Hou je van dieren? ")
Vraag10 = input("Ben je in bezit van het certificaat 'Overleven met gevaarlijk personeel'? ").lower()
Vraag11 = input("Ben je single? ")
Vraag12 = input("Ben je een inwoner van Nederland? ")


if int(Vraag1) >= 4 or int(Vraag2) >= 5 or int(Vraag3) >= 3:
    if Vraag4 == "ja":
        if Vraag5 == "ja":
            if Vraag6 == "ja":
                if (Vraag7 == "Man" or "man" and int(Snor) >= 10) or (Vraag7 == "Vrouw" or "vrouw" and int(Krulcm) >= 20):
                    raise OSError("Hier vallen wij helaas niet op")
                    if int(Vraag8) >= 150:
                        if int(Vraag9) >= 90:
                            raise ValueError("Uw snor is niet goed genoeg, sukkel!")
                            if Vraag10 == "ja":
                                aannemen = True
                                print("Je mag solliciteren.")
                                raise ConnectionError("Grapje, je mag niet solliciteren")
else:
    aannemen = False    
    print("Je mag niet solliciteren.")

            