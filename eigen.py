while True:
    # Hier wordt de code geprobeerd.
    try:
        getal = int(input("Voer een getal in: "))
    # De onderstaande code onder except wordt uitgevoerd wanneer er een ValueError is. Er zijn allerlei errors die je in de plaats van ValueError kan neerzetten.
    except ValueError:
        print("Dit is geen getal")
    # De onderstsaande code onder else wordt uitgevoerd wanneer er geen errors boven zijn gevonden.
    else:
        print(f"Het getal is {getal}")
        break
    # De onderstaande code onder finally wordt ALTIJD uitgevoerd.
    finally:
        print("Dankuwel voor het invullen!")