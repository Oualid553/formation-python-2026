import random

NOMBRE_MYSTERE = random.randint(0, 100) # Permet de choisir le nombre aléatoire en 0 et 100.
TENTATIVES = 5
print("🕹️🎮 Le jeu du nombre mystère 🎮🕹️") # Petit introduction explicatif du jeu.
print("-" * 50)
print("J'ai choisi un nombre entre 0 et 100. Devinez !")
print(f"Vous avez {TENTATIVES} essais !")
print("-" * 50)

while True:
    saisie = input("Devinez le nombre :") # On demande a l'utilisateur de choisir un nombre.
    
    if not saisie.isdigit(): # Vérification de intager seulement.
        print("Entrez un nombre !")
        continue

    saisie = int(saisie) # On convertie la saisie input en nombre entiers.
    TENTATIVES -= 1 # On décrémente afin de mettre fin a la boucle après 5 tentatives ratés.

    if saisie == NOMBRE_MYSTERE: # Si le chiffres de l'utilisateur == au nombre mystère, gagné et fin de la partie.
        print(f"🎉 Gagné en {5 - TENTATIVES} tentatives !") 
        print("Fin du jeu.")
        break
    elif TENTATIVES == 0: # Si la boucle arrive a 0, plus de tentatives. Le joueur a perdu.
        print("❌ Perdu ! Plus d'essais !")
        print(f"Le nombre mystère était {NOMBRE_MYSTERE}")
        print("Fin du jeu.")
        break
    elif saisie > NOMBRE_MYSTERE: # Si le nombre saisi est plus grand que le nombre mystère, on donne l'indice "trop grand".
        print("📉 Trop grand !")
        print(f"Il te reste {TENTATIVES} essai(s)") # On avertie le joueur du nombre tentatives restantes.
    else:
        print("📈 Trop petit !") # Si le nombre saisi est plus petit que le nombre mystère, on donne l'indice "trop petit".
        print(f"Il te reste {TENTATIVES} essai(s)") # On avertie le joueur du nombre tentatives restantes.








