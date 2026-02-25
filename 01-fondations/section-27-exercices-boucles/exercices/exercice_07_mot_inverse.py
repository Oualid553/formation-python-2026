# Exercice 7 : Afficher un mot à l'envers
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Afficher les lettres de "Python" en sens inverse
# Résultat attendu : n, o, h, t, y, P

# ==========================================
# MON CODE INITIAL (faux ❌)
# ==========================================
# mot = "Python"
# for mot in "Python":
#     print(f"{reversed} {mot}")
# 
# Erreur : reversed n'est pas une variable, c'est une fonction !
# J'ai aussi écrasé la variable 'mot' dans la boucle

# ==========================================
# MA SOLUTION FINALE (après aide)
# ==========================================
mot = "Python"
for lettre in reversed(mot):
    print(lettre)

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Solution #1 : reversed()
# mot = "Python"
# for lettre in reversed(mot):
#     print(lettre)

# Solution #2 : Slice [::-1]
# mot = "Python"
# for lettre in mot[::-1]:
#     print(lettre)

# ==========================================
# LEÇONS RETENUES
# ==========================================
# 1. reversed() est une FONCTION qui retourne un itérateur inversé
# 2. Alternative : slice [::-1] inverse une séquence
# 3. Ne pas réutiliser le nom de variable dans la boucle for

# ==========================================
# BLOCAGE INITIAL
# ==========================================
# Le concept de reversed() m'a embrouillé
# Après explication, c'est assez simple et logique

# ==========================================
# SCORE
# ==========================================
# 90% ✅ (Réussi après aide)