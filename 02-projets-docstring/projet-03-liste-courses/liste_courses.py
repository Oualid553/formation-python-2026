# Projet Docstring #3 : Liste de Courses
# Section 29 - Formation Docstring
# Oualid - 5 mars 2026

import sys

LISTE_COURSES = []  # Liste vide qui servira à être remplie

# Boucle principale, pour réafficher le menu jusqu'à "quitter"
while True:
    print("\nChoisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

    # Interaction avec l'utilisateur
    choix = input("👉 Votre choix : ")

    # Validation du choix
    if choix not in ["1", "2", "3", "4", "5"]:
        print("❌ Choix invalide, réessayez.")
        continue

    # CHOIX 1 : Ajouter un élément
    if choix == "1":
        article = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE_COURSES.append(article)
        print(f"L'élément {article} a bien été ajouté à la liste.")

        # Afficher la liste après ajout
        print("\nVoici le contenu de votre liste :")
        for index, item in enumerate(LISTE_COURSES, start=1):
            print(f"{index}. {item}")

    # CHOIX 2 : Retirer un élément
    elif choix == "2":
        article = input("Entrez le nom d'un élément à retirer de la liste de courses : ")

        if article in LISTE_COURSES:
            LISTE_COURSES.remove(article)
            print(f"L'élément {article} a bien été retiré de la liste.")
        else:
            print(f"L'élément {article} n'est pas dans la liste.")

    # CHOIX 3 : Afficher la liste
    elif choix == "3":
        if LISTE_COURSES:
            print("\nVoici le contenu de votre liste :")
            for index, item in enumerate(LISTE_COURSES, start=1):
                print(f"{index}. {item}")
        else:
            print("La liste est vide.")

    # CHOIX 4 : Vider la liste
    elif choix == "4":
        LISTE_COURSES.clear()
        print("La liste a été vidée de son contenu.")

    # CHOIX 5 : Quitter
    elif choix == "5":
        print("Au revoir !")
        sys.exit()

# ==========================================
# CONCEPTS UTILISÉS
# ==========================================
# 1. while True : Boucle infinie avec sortie conditionnelle
# 2. Liste vide : LISTE_COURSES = []
# 3. Validation : if choix not in ["1", "2", "3", "4", "5"]
# 4. continue : Retourne au début de la boucle
# 5. enumerate(liste, start=1) : Numérotation automatique
# 6. append() : Ajouter élément à la fin
# 7. remove() : Retirer élément par valeur
# 8. clear() : Vider toute la liste
# 9. if element in liste : Vérifier existence
# 10. sys.exit() : Quitter le programme

# ==========================================
# DIFFÉRENCES AVEC CALCULATRICE V2
# ==========================================
# - Menu avec 5 choix (vs 2 nombres)
# - Gestion de liste dynamique (vs calcul simple)
# - Affichage avec enumerate() (nouveau concept)
# - Validation par liste de choix (vs isdigit())
# - Structure if/elif/else complète

# ==========================================
# SCORE
# ==========================================
# 95% identique à la correction officielle ✅
