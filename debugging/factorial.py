#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Corrige la boucle infinie en décrémentant n
    return result

f = factorial(int(sys.argv[1]))
print(f)  # Assurez-vous d'imprimer la valeur de f
