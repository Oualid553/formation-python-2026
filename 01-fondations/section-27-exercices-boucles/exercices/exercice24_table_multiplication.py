# Exercice 24 : Afficher la table de multiplication d'un nombre
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Afficher la table de multiplication du nombre 7
# De 0 × 7 à 10 × 7

# ==========================================
# MA SOLUTION
# ==========================================
nombre = 7
for i in range(11):  # 0 à 10
    print(f"{i} * {nombre} = {nombre * i}")

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# nombre = 7
# for i in range(11):
#     print(f"{i} x {nombre} = {i * nombre}")

# ==========================================
# COMPARAISON
# ==========================================
# Ma solution : {nombre * i}
# Correction : {i * nombre}
# → Les deux identiques (multiplication commutative)
# Symbole : * vs x (les deux acceptés)

# ==========================================
# LEÇON RETENUE
# ==========================================
# Calculs possibles directement dans f-strings
# range(11) génère 0 à 10 (11 éléments)

# ==========================================
# SCORE
# ==========================================
# 100% ✅