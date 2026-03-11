import random

# === INTRODUCTION ===
print("=" * 60)
print("🚕 DUEL DE CHAUFFEURS VTC 🚕")
print("=" * 60)
print("Vous démarrez votre activité VTC.")
print("Un concurrent agressif tente de vous écraser !")
print("Défendez votre réputation et vos clients !")
print("=" * 60)
print()

# === VARIABLES ===
REPUTATION_JOUEUR = 50
REPUTATION_CONCURRENT = 50
BONUS_COURSES = 3

# === BOUCLE PRINCIPALE ===
while REPUTATION_JOUEUR > 0 and REPUTATION_CONCURRENT > 0:
    choix = input("Souhaitez-vous : (1) Réaliser une course de qualité ⭐ (2) Activer un bonus course 💰 ? ")

    # Validation
    if choix not in ["1", "2"]:
        print("❌ Choix invalide !")
        continue

    # === COURSE DE QUALITÉ ===
    if choix == "1":
        clients_gagnes = random.randint(5, 10)
        REPUTATION_CONCURRENT -= clients_gagnes
        print(f"✅ Vous réalisez une course excellente !")
        print(f"⭐ Le client vous met 5 étoiles et vous recommande !")
        print(f"📉 Votre concurrent perd {clients_gagnes} clients !")

        # Vérifier victoire
        if REPUTATION_CONCURRENT <= 0:
            print("=" * 60)
            print("🎉 VICTOIRE ! Le concurrent abandonne le secteur !")
            print("Vous dominez le marché VTC ! 🏆")
            print("=" * 60)
            break

        # Concurrent contre-attaque
        clients_perdus = random.randint(5, 15)
        REPUTATION_JOUEUR -= clients_perdus
        print(f"💸 Le concurrent casse les prix !")
        print(f"📉 Il vous vole {clients_perdus} clients avec du dumping !")

        # Vérifier défaite
        if REPUTATION_JOUEUR <= 0:
            print("=" * 60)
            print("💔 DÉFAITE ! Vous avez perdu tous vos clients...")
            print("Le concurrent domine le marché.")
            print("Tentez votre chance ailleurs ! 🚪")
            print("=" * 60)
            break

    # === BONUS COURSE ===
    elif choix == "2":
        # Vérifier stock
        if BONUS_COURSES <= 0:
            print("❌ Vous n'avez plus de bonus disponibles !")
            continue
        
        # Utiliser bonus
        BONUS_COURSES -= 1
        nouveaux_clients = random.randint(15, 50)
        REPUTATION_JOUEUR += nouveaux_clients
        print(f"💰 Vous activez un bonus parrainage !")
        print(f"🎁 Vous gagnez {nouveaux_clients} nouveaux clients !")
        print(f"📊 ({BONUS_COURSES} bonus restants)")
        print("⏭️  Vous passez votre tour...")

        # Concurrent attaque quand même
        clients_perdus = random.randint(5, 15)
        REPUTATION_JOUEUR -= clients_perdus
        print(f"💸 Le concurrent vous vole {clients_perdus} clients pendant ce temps !")

        # Vérifier défaite
        if REPUTATION_JOUEUR <= 0:
            print("=" * 60)
            print("💔 DÉFAITE ! Vous avez perdu tous vos clients...")
            print("Le concurrent domine le marché.")
            print("Tentez votre chance ailleurs ! 🚪")
            print("=" * 60)
            break

    # === AFFICHAGE RÉPUTATION ===
    print()
    print(f"📊 Votre réputation : {REPUTATION_JOUEUR} clients")
    print(f"📊 Réputation concurrent : {REPUTATION_CONCURRENT} clients")
    print("-" * 60)
    print()

# === FIN DU JEU ===
print("Fin du jeu.")