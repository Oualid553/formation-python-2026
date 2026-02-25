# Exercice 9 : Remplacer des boucles par des compréhensions de listes
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Remplacer les boucles classiques par des compréhensions de liste

# ==========================================
# EXEMPLE 1 : Filtrer les nombres pairs
# ==========================================

# Code classique
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = []
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)
print(nombres_pairs)

# Ma solution - Compréhension
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

# ==========================================
# EXEMPLE 2 : Filtrer les nombres positifs
# ==========================================

# Code classique
nombres = range(-10, 10)
nombres_positifs = []
for i in nombres:
    if i >= 0:
        nombres_positifs.append(i)
print(nombres_positifs)

# Ma solution - Compréhension
nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)

# ==========================================
# EXEMPLE 3 : Doubler les nombres
# ==========================================

# Code classique
nombres = range(5)
nombres_doubles = []
for i in nombres:
    nombres_doubles.append(i * 2)
print(nombres_doubles)

# Ma solution - Compréhension
nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]  # ⚠️ J'avais oublié le *2 !
print(nombres_doubles)

# ==========================================
# EXEMPLE 4 : Transformation conditionnelle ⭐
# ==========================================

# Code classique
nombres = range(10)
nombres_inverses = []
for i in nombres:
    if i % 2 == 0:
        nombres_inverses.append(i)
    else:
        nombres_inverses.append(-i)
print(nombres_inverses)

# Ma solution - Compréhension avec opérateur ternaire
nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses)

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Toutes mes solutions sont identiques à la correction ! ✅

# ==========================================
# BLOCAGES RENCONTRÉS
# ==========================================
# 1. Exemple 3 : J'avais oublié le * 2 dans la compréhension
# 2. Exemple 4 : Le else dans une compréhension m'a bloqué
#    → J'ai dû chercher sur internet
#    → Trouvé : opérateur ternaire dans compréhensions

# ==========================================
# STRUCTURE OPÉRATEUR TERNAIRE
# ==========================================
# Sans condition (filtrage) :
# [expression for item in liste if condition]
#
# Avec condition (transformation) :
# [valeur_si_vrai if condition else valeur_si_faux for item in liste]
#
# Différence clé :
# - if à la FIN = filtrage (garde ou enlève)
# - if au DÉBUT = transformation (change valeur)

# ==========================================
# LEÇON RETENUE
# ==========================================
# 1. Compréhensions = boucles + append en 1 ligne
# 2. if à la fin = filtrer
# 3. if...else au début = transformer conditionnellement
# 4. C'est OK de chercher sur internet quand bloqué !

# ==========================================
# SCORE
# ==========================================
# 95% ✅ (Réussi, else ternaire cherché sur internet)
