# Exercice 21 : Vérifier qu'un élément est dans une liste
# Section 24 - Formation Docstring
# Oualid - 23 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# 1. Ajouter le nombre 6 dans la liste
# 2. Vérifier que 6 a bien été ajouté
# Si présent, afficher : "Le nombre 6 a bien été ajouté à la liste."

liste = [1, 2, 3, 4, 5]

# ==========================================
# MA SOLUTION
# ==========================================
liste.append(6)

if 6 in liste:
    print("Le nombre 6 a bien été ajouté à la liste.")

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Identique à ma solution ✅

# ==========================================
# CONCEPTS UTILISÉS
# ==========================================
# 1. append(element) : Ajouter un élément à la fin
# 2. in : Opérateur d'appartenance (vérifier présence)
# 3. if : Structure conditionnelle

# ==========================================
# ⚠️ PIÈGE À ÉVITER
# ==========================================
# ❌ ERREUR CLASSIQUE :
# liste = liste.append(6)
# → append() retourne None !
# → La liste devient None au lieu de [1,2,3,4,5,6]
#
# ✅ CORRECT :
# liste.append(6)  # Modifie directement, pas besoin d'assigner

# ==========================================
# SCORE
# ==========================================
# 100% ✅ (identique à correction officielle)
