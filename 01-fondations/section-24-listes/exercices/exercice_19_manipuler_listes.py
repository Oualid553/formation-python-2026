# Exercice 19 : Manipuler des listes
# Section 24 - Formation Docstring
# Oualid - 23 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# 1. Récupérer le premier et dernier nombre dans 'nombre_premier' et 'nombre_dernier'
# 2. Récupérer l'élément 'Python' dans la variable 'langage'
# 3. Déplacer 'Python' à la fin de la liste

# ==========================================
# PARTIE 1 : Premier et dernier élément
# ==========================================
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0]    # Premier élément (index 0)
nombre_dernier = nombres[-1]   # Dernier élément (index -1)

# ==========================================
# PARTIE 2 : Récupérer 'Python'
# ==========================================
langages = ["Java", "Python", "C++"]
langage = langages[1]  # Élément à l'index 1

# ==========================================
# PARTIE 3 : Déplacer 'Python' à la fin
# ==========================================
liste = ["Java", "Python", "C++"]
liste.remove("Python")   # Enlève "Python" de sa position actuelle
liste.append("Python")   # Ajoute "Python" à la fin
# Résultat : ["Java", "C++", "Python"]

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Identique à ma solution ✅

# ==========================================
# ERREURS INITIALES COMPRISES
# ==========================================
# ❌ ERREUR 1 : nombres.append[0]
#    → append n'est pas une liste, c'est une méthode !
#    → Pour ACCÉDER : nombres[0]
#    → Pour AJOUTER : nombres.append(element)
#
# ❌ ERREUR 2 : liste.remove(1)
#    → remove() cherche l'ÉLÉMENT, pas l'index !
#    → remove(1) cherche le NOMBRE 1
#    → remove("Python") cherche la CHAÎNE "Python"
#
# ❌ ERREUR 3 : liste = liste.append("Python")
#    → append() retourne None, pas la liste !
#    → append() modifie la liste directement
#    → Pas besoin de réassigner : liste.append("Python")

# ==========================================
# CONCEPTS CLÉS RETENUS
# ==========================================
# 1. Accès par index : liste[0], liste[-1]
# 2. remove(element) : cherche l'élément, pas l'index
# 3. append(element) : ajoute à la fin, retourne None

# ==========================================
# SCORE
# ==========================================
# 100% ✅ (identique à correction officielle)