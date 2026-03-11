import random

# === INTRODUCTION ===
#  Print description du jeu
print("🎮 JEU DE RÔLE - COMBAT TERMINAL 🎮")
print("=" * 50)
print("Vous : 50 PV ❤️ | 3 Potions 🧪")
print("Ennemi : 50 PV ❤️")
print("Que la bataille commence !")
print("=" * 50)
print()

# === VARIABLES DE DÉPART ===
PV_JOUEUR = 50
PV_ENNEMI = 50
POTIONS = 3

# === BOUCLE PRINCIPALE ===
while PV_JOUEUR > 0 and PV_ENNEMI > 0:
    # 1. DEMANDER CHOIX
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    # 2. VALIDER CHOIX
    if choix not in ["1", "2"]:
        print("Choix invalide !")
        continue

    # 3. SI ATTAQUE
    if choix == "1":
        degats_joueur = random.randint(5, 10)
        PV_ENNEMI -= degats_joueur
        print(f"Vous avez infligé {degats_joueur} points de dégâts à l'ennemi ⚔")

        # Vérifier si ennemi mort
        if PV_ENNEMI <= 0:
            print("Victoire !")
            break

        # Ennemi contre-attaque (si vivant)
        degats_ennemi = random.randint(5, 15)
        PV_JOUEUR -= degats_ennemi
        print(f"L'ennemi vous a infligé {degats_ennemi} points de dégâts ⚔")

        # Vérifier si joueur mort
        if PV_JOUEUR <= 0:
            print("Défaite !")
            break

    # 4. SI POTION
    elif choix == "2":
        # Vérifier stock
        if POTIONS <= 0:
            print("Plus de potions !")
            continue
        # Utiliser potion
        POTIONS -= 1
        pv_recuperes = random.randint(15, 50)
        PV_JOUEUR += pv_recuperes
        print(f"Vous récupérez {pv_recuperes} points de vie ❤ ({POTIONS} 🧪 restantes)")
        print("Vous passez votre tour !")

        # Ennemi attaque quand même
        degats_ennemi = random.randint(5, 15)
        PV_JOUEUR -= degats_ennemi
        print(f"L'ennemi vous a infligé {degats_ennemi} de dégats !")

        # Vérifier si joueur mort
        if PV_JOUEUR <= 0:
            print("Défaite !")
            break
    # 5. AFFICHER PV RESTANTS
    print(f"Il vous reste {PV_JOUEUR} points de vie.")
    print(f"Il reste {PV_ENNEMI} points de vie à l'ennemi.")
    print("-" * 50)

# === FIN DU JEU ===
print("Fin du jeu.")



