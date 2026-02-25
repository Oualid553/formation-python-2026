# Exercice 23 : Fixer l'erreur dans la boucle
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Modifier le script pour afficher l'index de chaque lettre de "Python"
# Résultat attendu : 0, 1, 2, 3, 4, 5

# ==========================================
# CODE DE DÉPART (bugué)
# ==========================================
# mot = "Python"
# for i in range(mot):  # ❌ TypeError: range() attend un entier !
#     print(i)

# ==========================================
# MA SOLUTION
# ==========================================
mot = "Python"
for i in range(len(mot)):  # len() retourne 6
    print(i)

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Identique à ma solution ✅

# ==========================================
# EXPLICATIONS
# ==========================================
# range() nécessite un NOMBRE entier
# "Python" est une STRING, pas un nombre
# len("Python") retourne 6
# range(6) crée [0, 1, 2, 3, 4, 5]

# ==========================================
# LEÇON RETENUE
# ==========================================
# Pour parcourir les indices d'une séquence :
# range(len(sequence))

# ==========================================
# SCORE
# ==========================================
# 100% ✅
