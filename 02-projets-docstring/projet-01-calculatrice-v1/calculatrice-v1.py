# Projet Docstring #1 : La Calculatrice
# Oualid - 17 février 2026
# Section 20 - Formation Docstring
# Sections utilisées : 15 (input), 19 (f-strings)

# ==========================================
# CONSIGNE
# ==========================================
# Créer une calculatrice en ligne de commande
# qui additionne deux nombres saisis par l'utilisateur
# Résultat attendu :
# "Le résultat de l'addition du nombre 5 avec le nombre 10 est égal à 15"

# ==========================================
# MA SOLUTION
# ==========================================

# Étape 1 : Demander premier nombre
a = int(input("Veuillez entrer un premier nombre : "))

# Étape 2 : Demander deuxième nombre
b = int(input("Veuillez entrer un deuxième nombre : "))

# Étape 3 : Calculer
resultat = a + b

# Étape 4 : Afficher
print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {resultat}")

# ==========================================
# CORRECTION OFFICIELLE DOCSTRING
# ==========================================
# a = input("Entrez un premier nombre : ")
# b = input("Entrez un deuxième nombre : ")
# print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")

# ==========================================
# COMPARAISON MA SOLUTION vs CORRECTION
# ==========================================
# MA SOLUTION :
#   - Conversion int() AVANT le calcul : a = int(input(...))
#   - Variable resultat séparée : resultat = a + b
#   - Affichage simple : {resultat}
#
# CORRECTION OFFICIELLE :
#   - Conversion str (input retourne str) gardée dans a et b
#   - Conversion + calcul DANS la f-string : {int(a) + int(b)}
#   - Plus compact (3 lignes vs 4)
#
# LES DEUX SONT CORRECTES !
# Ma solution : plus lisible, meilleure pour déboguer
# Correction : plus compacte, expression directe dans f-string

# ==========================================
# LEÇON IMPORTANTE RETENUE
# ==========================================
# ❌ ERREUR INITIALE : Tout mélanger sur une ligne
#    resultat = print(f"...{resultat}...")
#
# ✅ BONNE PRATIQUE : Séparer calcul et affichage
#    resultat = a + b       # Calcul
#    print(f"...{resultat}") # Affichage
#
# RÈGLE : Une ligne = Une responsabilité !

# ==========================================
# BONUS : VERSION AMÉLIORÉE (à faire plus tard)
# ==========================================
# Avec validation (Section 21 - Conditions) :
#
# a = input("Veuillez entrer un premier nombre : ")
# b = input("Veuillez entrer un deuxième nombre : ")
#
# if a.isdigit() and b.isdigit():
#     resultat = int(a) + int(b)
#     print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {resultat}")
# else:
#     print("Erreur : veuillez entrer des nombres valides !")