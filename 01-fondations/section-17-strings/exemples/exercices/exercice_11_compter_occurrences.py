# Exercice 11 : Compter occurrences d'une lettre
# Section 17 - Formation Docstring
# Oualid - 16 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Compter le nombre de fois que "o" apparaît dans la phrase
# Résultat attendu : 4

# ==========================================
# CODE DE DÉPART
# ==========================================
# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"
# resultat = 

# ==========================================
# MA PREMIÈRE SOLUTION
# ==========================================
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.count("o")

print(f"Ma solution : {resultat}")  # 3 (compte seulement "o" minuscule)

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.lower().count(lettre_a_chercher)

print(f"Correction : {resultat}")  # 4 (compte "o" ET "O")

# ==========================================
# DIFFÉRENCES ET LEÇON
# ==========================================
# 1. J'ai écrit "o" en dur au lieu d'utiliser lettre_a_chercher
# 2. Je n'ai pas utilisé .lower() pour uniformiser la casse

# Pourquoi .lower() est important :
print("Bonjour".count("o"))         # 2 (ne compte pas le "O" majuscule)
print("Bonjour".lower().count("o")) # 3 (compte aussi le "O")

# Bonne pratique : toujours .lower() pour compter insensible à la casse

# ==========================================
# NOTE PERSONNELLE
# ==========================================
# J'ai dû retourner à la documentation pour trouver count().
# C'est une bonne compétence de savoir chercher !
# Leçon : Penser à .lower() pour insensibilité à la casse.
# Score : 95%