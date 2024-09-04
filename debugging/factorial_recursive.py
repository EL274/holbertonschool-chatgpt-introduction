#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    try:
        # Vérification qu'un argument a été fourni
        if len(sys.argv) < 2:
            raise ValueError("Veuillez fournir un nombre entier comme argument.")
        
        # Conversion de l'argument en entier
        n = int(sys.argv[1])

        # Vérification que l'entier est positif ou nul
        if n < 0:
            raise ValueError("Le nombre doit être un entier positif ou nul.")

        # Calcul et affichage du factoriel
        f = factorial(n)
        print(f)

    except ValueError as e:
        print(f"Erreur : {e}")
        
    except Exception as e:
        print(f"Erreur inattendue : {e}")
