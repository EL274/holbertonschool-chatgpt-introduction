#!/usr/bin/python3

import sys

def print_arguments(args):
    """
    Affiche les arguments passés au script.
    
    :param args: Liste des arguments, y compris le nom du script.
    """
    # Vérifie si des arguments ont été passés
    if len(args) == 1:
        print("Aucun argument fourni.")
    else:
        # Itère sur les arguments (en excluant le nom du script)
        for arg in args[1:]:
            print(arg)

if __name__ == "__main__":
    # Appelle la fonction avec les arguments du script
    print_arguments(sys.argv)
