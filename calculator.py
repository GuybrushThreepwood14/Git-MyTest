def calculatrice():
    print("=== MENU CALCULATRICE ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "5":
        print("Au revoir")
        return

    try:
        a = float(input("Valeur pour a : "))
        b = float(input("Valeur pour b : "))
    except ValueError:
        print("Erreur : vous devez entrer des nombres.")
        return

    # Operations
    if choix == "1":
        print("Résultat :", a + b)

    elif choix == "2":
        print("Résultat :", a - b)

    elif choix == "3":
        print("Résultat :", a * b)

    elif choix == "4":
        if b == 0:
            print("Erreur : division par zéro impossible.")
        else:
            print("Résultat :", a / b)

    else:
        print("Option invalide.")


def sss():
    return True
    
