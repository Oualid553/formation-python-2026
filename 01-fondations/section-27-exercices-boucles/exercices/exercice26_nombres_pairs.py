# Exercice 26 : Récupérer seulement les nombres pairs
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Extraire uniquement les nombres pairs de 0 à 50
# Résultat attendu : [0, 2, 4, 6, ..., 48, 50]

# ==========================================
# CODE DE DÉPART
# ==========================================
# nombres = range(51)
# nombres_pairs = []

# ==========================================
# MA SOLUTION - Compréhension de liste
# ==========================================
nombres = range(51)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

# ==========================================
# CORRECTION OFFICIELLE - Boucle classique
# ==========================================
# nombres = range(51)
# nombres_pairs = []
# for i in nombres:
#     if i % 2 == 0:
#         nombres_pairs.append(i)

# ==========================================
# COMPARAISON
# ==========================================
# Ma solution : Compréhension de liste (1 ligne)
# Correction : Boucle classique (4 lignes)
# → Les deux sont correctes !
# → Ma solution plus "pythonique" ✅

# ==========================================
# EXPLICATIONS MODULO
# ==========================================
# L'opérateur modulo (%) retourne le RESTE d'une division
#
# Exemples :
# 10 % 2 = 0  (10 ÷ 2 = 5, reste 0) → PAIR
# 11 % 2 = 1  (11 ÷ 2 = 5, reste 1) → IMPAIR
# 12 % 2 = 0  (12 ÷ 2 = 6, reste 0) → PAIR
#
# Règle : Si (nombre % 2 == 0) → nombre est PAIR

# ==========================================
# LEÇON RETENUE
# ==========================================
# Modulo (%) = opérateur parfait pour tester parité
# nombre % 2 == 0 → pair
# nombre % 2 == 1 → impair

# ==========================================
# SCORE
# ==========================================
# 100% ✅