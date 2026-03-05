# Projet VTC #3 : Gestionnaire de Courses Journalières
# Oualid - 5 mars 2026
# Concepts : Section 29 (Menu interactif, Listes, enumerate)

import sys

COURSES_JOUR = []  # Liste vide qui servira à être remplie

# Boucle principale, pour réafficher le menu jusqu'à "quitter"
while True:
    print("\n=== GESTIONNAIRE COURSES VTC ===")
    print("\nChoisissez parmi les 5 options suivantes :")
    print("1: Ajouter une course")
    print("2: Retirer une course")
    print("3: Afficher les courses du jour")
    print("4: Vider la journée")
    print("5: Quitter")

    # Interaction avec l'utilisateur
    choix = input("👉 Votre choix : ")

    # Validation
    if choix not in ["1", "2", "3", "4", "5"]:
        print("❌ Choix invalide, réessayez.")
        continue

    # CHOIX 1 : Ajouter une course
    if choix == "1":
        trajet = input("Entrez le trajet de la course (ex: Paris-CDG) : ")
        COURSES_JOUR.append(trajet)
        print(f"✅ Course {trajet} ajoutée.")

        # Afficher la liste après ajout
        print("\n📋 Courses du jour :")
        for index, course in enumerate(COURSES_JOUR, start=1):
            print(f"{index}. {course}")

    # CHOIX 2 : Retirer une course
    elif choix == "2":
        trajet = input("Entrez le trajet de la course à annuler : ")

        if trajet in COURSES_JOUR:
            COURSES_JOUR.remove(trajet)
            print(f"❌ Course {trajet} annulée.")
        else:
            print(f"⚠️ Course {trajet} non trouvée.")

    # CHOIX 3 : Afficher les courses
    elif choix == "3":
        if COURSES_JOUR:
            print("\n📋 Courses du jour :")
            for index, course in enumerate(COURSES_JOUR, start=1):
                print(f"{index}. {course}")
        else:
            print("📭 Aucune course pour aujourd'hui.")

    # CHOIX 4 : Vider la journée
    elif choix == "4":
        COURSES_JOUR.clear()
        print("🏁 Journée terminée. Toutes les courses ont été effacées.")

    # CHOIX 5 : Quitter
    elif choix == "5":
        print("👋 Bonne route !")
        sys.exit()

    print("-" * 50)  # Séparateur visuel

# ==========================================
# DIFFÉRENCIATION VTC
# ==========================================
# Ce projet démontre :
# - Application métier VTC (gestion courses journalières)
# - Adaptation code générique → cas d'usage réel
# - Compréhension terrain (vocabulaire VTC)
# - Portfolio unique et personnel

# ==========================================
# CONCEPTS RÉUTILISÉS (Section 29)
# ==========================================
# 1. Menu interactif avec 5 choix
# 2. Boucle while True + sys.exit()
# 3. Validation par liste de choix
# 4. Gestion liste dynamique (append, remove, clear)
# 5. enumerate() pour affichage numéroté
# 6. Vérification existence (in)
# 7. Messages utilisateur clairs

# ==========================================
# ADAPTATION AU THÈME VTC
# ==========================================
# Liste de courses → Courses journalières VTC
# "article" → "trajet"
# "Pomme", "Pain" → "Paris-CDG", "CDG-Paris"
# "liste vidée" → "journée terminée"
# Emojis adaptés : ✅ 📋 🏁 👋

# ==========================================
# EXEMPLES DE TRAJETS RÉELS
# ==========================================
# - Paris-CDG
# - CDG-Paris
# - Boulogne-Neuilly
# - Paris-Versailles
# - Neuilly-La Défense
# - Paris-Orly
# - Gare du Nord-Gare de Lyon

# ==========================================
# VERSION
# ==========================================
# VTC #3 - Version basique (gestion trajets uniquement)
# À venir : VTC #3 v2 avec tarifs et calcul revenu journalier
