# Naam: Hamza Hammouti
# Opdracht: Pizza Calculator

print("----------------------------------------------------")
while True:
    try:
        aantalSmall = int(input("| Aantal pizza's small (25cm - prijs: €9.49)   : "))
        aantalMedium = int(input("| Aantal pizza's medium (30cm - prijs: €11.49)   : "))
        aantalLarge = int(input("| Aantal pizza's large (35cm - prijs: €14.49)    : "))
        break
    except ValueError:
        print("Voer alleen hele getallen in!")

print("----------------------------------------------------")

prijsSmall = 9.49
prijsMedium = 11.49
prijsLarge = 14.49

totaalSmall = aantalSmall * prijsSmall
totaalMedium = aantalMedium * prijsMedium
totaalLarge = aantalLarge * prijsLarge

totaalprijs = (aantalSmall * prijsSmall) + (aantalMedium * prijsMedium) + (aantalLarge * prijsLarge)
print (f"Je hebt {aantalSmall} pizza small besteld (€{totaalSmall}), {aantalMedium} pizza medium (€{totaalMedium}) en {aantalLarge} pizza large (€{totaalLarge}). Totaalprijs: €{totaalprijs}")