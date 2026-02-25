# Exercice 8 : Sortir d'une boucle while avec input
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Permettre à l'utilisateur de sortir de la boucle
# en modifiant les lignes dans la boucle while

# ==========================================
# CODE DE DÉPART
# ==========================================
# continuer = "o"
# while continuer == "o":
#     print("On continue !")
#     input("Voulez-vous continuer ? o/n ")  # ❌ Résultat non stocké !

# ==========================================
# MA SOLUTION
# ==========================================
continuer = "o"
while continuer == "o":
    print("On continue !")
    response = input("Voulez-vous continuer ? o/n ")
    if response == "n":
        break

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Solution #1 : Réassigner continuer
# continuer = "o"
# while continuer == "o":
#     print("On continue !")
#     continuer = input("Voulez-vous continuer ? o/n ")

# Solution #2 : break avec condition
# continuer = "o"
# while continuer == "o":
#     print("On continue !")
#     resultat = input("Voulez-vous continuer ? o/n ")
#     if resultat != "o":
#         break

# Solution #3 : Python 3.8+ (walrus operator)
# while (continuer := "o") == "o":
#     print("On continue !")
#     if (resultat := input("Voulez-vous continuer ? o/n ")) != "o":
#         break

# ==========================================
# COMPARAISON SOLUTIONS
# ==========================================
# Ma solution : break avec if response == "n"
# → Simple et claire ✅
#
# Solution 1 (correction) : Réassigner continuer
# → Élégante, pas besoin de break ✅
#
# Les deux sont valides !

# ==========================================
# LEÇON RETENUE
# ==========================================
# Deux approches pour sortir d'une boucle while :
# 1. Modifier la variable de condition (continuer)
# 2. Utiliser break avec condition

# ==========================================
# SCORE
# ==========================================
# 100% ✅