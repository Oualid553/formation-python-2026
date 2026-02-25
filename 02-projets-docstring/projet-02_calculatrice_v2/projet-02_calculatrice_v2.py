# Projet Docstring #2 : La Calculatrice (avec gestion erreurs)
# Section 28 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Créer une calculatrice en ligne de commande
# - Demander deux nombres à l'utilisateur
# - Afficher le résultat de l'addition
# - Gérer les erreurs (si l'utilisateur entre autre chose que des nombres)

# ==========================================
# MA SOLUTION
# ==========================================
while True:
    # Demander deux nombres
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    # Vérifier que ce sont bien des nombres
    if a.isdigit() and b.isdigit():
        # Calculer et afficher le résultat
        resultat = int(a) + int(b)
        print(f"Le résultat de l'addition de {int(a)} avec {int(b)} est égal à {resultat}")
        break  # Sortir de la boucle
    else:
        # Message d'erreur et redemander
        print("Veuillez entrer deux nombres valides")

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# # Initialiser les variables
# a = b = ""
# 
# # Boucle tant que a et b ne sont pas des nombres
# while not (a.isdigit() and b.isdigit()):
#     # Demander deux nombres
#     a = input("Entrez un premier nombre : ")
#     b = input("Entrez un deuxième nombre : ")
#     
#     # Afficher erreur si invalides
#     if not (a.isdigit() and b.isdigit()):
#         print("Veuillez entrer deux nombres valides")
# 
# # Afficher le résultat (hors boucle)
# print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")

# ==========================================
# COMPARAISON DES APPROCHES
# ==========================================
# 
# MA SOLUTION (while True + break) :
# ✅ Logique simple et claire
# ✅ Tout dans la boucle
# ⚠️ Conversion int() répétée 3 fois dans le print
# 
# CORRECTION (while not) :
# ✅ Condition directe dans while
# ✅ Conversion int() seulement à la fin
# ✅ Séparation validation/affichage
# ⚠️ Nécessite initialisation a = b = ""
# 
# LES DEUX SONT CORRECTES ! ✅

# ==========================================
# VERSION OPTIMISÉE (combinaison des deux)
# ==========================================
# while True:
#     a = input("Entrez un premier nombre : ")
#     b = input("Entrez un deuxième nombre : ")
#     
#     if a.isdigit() and b.isdigit():
#         # Conversion une seule fois
#         a, b = int(a), int(b)
#         print(f"Le résultat de l'addition de {a} avec {b} est égal à {a + b}")
#         break
#     else:
#         print("Veuillez entrer deux nombres valides")

# ==========================================
# CONCEPTS UTILISÉS
# ==========================================
# 1. Boucle while infinie (while True)
# 2. input() pour saisie utilisateur
# 3. isdigit() pour valider entrée
# 4. Opérateurs logiques (and)
# 5. Structures conditionnelles (if/else)
# 6. break pour sortir de boucle
# 7. Conversion int()
# 8. f-strings pour affichage

# ==========================================
# AMÉLIORATION POSSIBLE
# ==========================================
# ⚠️ LIMITATION : isdigit() ne gère PAS :
# - Les nombres négatifs : "-5".isdigit() → False
# - Les décimaux : "3.14".isdigit() → False
# 
# Pour gérer ces cas, il faudrait utiliser try/except
# (vu plus tard dans la formation)

# ==========================================
# LEÇON RETENUE
# ==========================================
# 1. "is True" est redondant dans conditions
#    if condition is True: ❌
#    if condition: ✅
# 
# 2. Deux styles de boucles valides :
#    - while True + break (mon style)
#    - while not condition (correction)
# 
# 3. isdigit() valide uniquement entiers positifs

# ==========================================
# SCORE
# ==========================================
# 95% ✅ (Logique parfaite, petite optimisation possible)