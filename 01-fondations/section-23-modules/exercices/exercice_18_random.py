# Exercice 18 : Module random - Comparer deux nombres aléatoires
# Section 23 - Formation Docstring
# Oualid - 17 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Générer deux nombres aléatoires a et b
# Afficher lequel est le plus grand
# Phrases exactes attendues :
# - "Le nombre b est plus grand que le nombre a."
# - "Le nombre a est plus grand que le nombre b."
# - "Le nombre a et le nombre b sont égaux."

# ==========================================
# MA SOLUTION
# ==========================================
import random

a = random.randint(1, 100)
b = random.randint(1, 100)

if b > a:
    print("Le nombre b est plus grand que le nombre a.")
elif a > b:
    print("Le nombre a est plus grand que le nombre b.")
else:
    print("Le nombre a et le nombre b sont égaux.")

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# import random
# 
# a = random.randint(0, 2)
# b = random.randint(0, 2)
# 
# if a > b:
#     print("Le nombre a est plus grand que le nombre b.")
# elif a < b:
#     print("Le nombre b est plus grand que le nombre a.")
# elif a == b:
#     print("Le nombre a et le nombre b sont égaux.")

# ==========================================
# COMPARAISON
# ==========================================
# MA SOLUTION :
#   - Intervalle 1-100 (plus réaliste)
#   - Teste b > a en premier
#   - else pour l'égalité (implicite)
#
# CORRECTION :
#   - Intervalle 0-2 (maximise chances d'égalité pour tests)
#   - Teste a > b en premier
#   - elif a == b (explicite)

# ==========================================
# ERREUR INITIALE CORRIGÉE
# ==========================================
# ❌ J'avais nommé les variables nombre_a et nombre_b
# ❌ Udemy attendait exactement a et b
# 
# Erreur : module 'exercice' has no attribute 'a'
# → Udemy cherchait une variable nommée 'a', pas 'nombre_a'
# 
# Leçon : Respecter exactement les noms de variables demandés !

# ==========================================
# SCORE
# ==========================================
# 100% ✅