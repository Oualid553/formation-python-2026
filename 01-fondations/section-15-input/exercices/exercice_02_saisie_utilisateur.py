# Exercice 2 : Récupérer la saisie de l'utilisateur
# Section 15 - Formation Docstring
# Oualid - 16 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Demander à l'utilisateur :
# - Son prénom
# - Sa ville de naissance
# - Son âge
# Puis afficher ces informations

# ==========================================
# MA SOLUTION
# ==========================================
prenom = input("Quel est votre prénom ? ")
ville = input("De quelle ville venez-vous ? ")
age = int(input("Quel âge avez-vous ? "))

print(prenom)
print(ville)
print(age)

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# prenom = input("Comment vous appelez-vous ? ")
# ville_de_naissance = input("Quelle est votre ville de naissance ? ")
# age = input("Quel est votre âge ? ")
# print(prenom)
# print(ville_de_naissance)
# print(age)

# ==========================================
# NOTE PERSONNELLE
# ==========================================
# J'ai converti age en int(), mais pas nécessaire ici
# car on affiche juste la valeur (pas de calcul).
# Les deux fonctionnent !
#
# Différence :
# - input() → str (texte)
# - int(input()) → int (nombre)
# Mais print() affiche pareil visuellement : 23
#
# Conversion int() utile SEULEMENT si calculs après.