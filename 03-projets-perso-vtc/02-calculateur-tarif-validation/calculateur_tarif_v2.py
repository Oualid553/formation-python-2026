import random 

NOMBRE_MYSTERE = random.randint(0, 100)
TENTATIVES = 5

print("🕹️🎮 Le jeu du nombre mystère 🎮🕹️")
print("-" * 50)
print("J'ai choisi un nombre entre 0 et 100. Devinez !")
print(f"Vous avez {TENTATIVES} essais !")
print("-" * 50)

while True:
    saisie = input("Devine le nombre : ")

    if not saisie.isdigit():
        print("Entrez un nombre !")
        continue

    saisie = int(saisie)
    TENTATIVES -= 1  # ← Diminuer !

    if saisie == NOMBRE_MYSTERE:
        print(f"🎉 Gagné en {5 - TENTATIVES} tentatives !")
        break
    elif TENTATIVES == 0:
        print("❌ Perdu ! Plus d'essais !")
        print(f"Le nombre mystère était {NOMBRE_MYSTERE}")
        break
    elif saisie > NOMBRE_MYSTERE:
        print("📉 Trop grand !")
        print(f"Il te reste {TENTATIVES} essai(s)")
    else:
        print("📈 Trop petit !")
        print(f"Il te reste {TENTATIVES} essai(s)")