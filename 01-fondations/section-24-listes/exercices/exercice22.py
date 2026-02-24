# Exercice 22 : Récupérer des éléments dans une liste imbriquée
# Section 24 - Formation Docstring
# Oualid - 23 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Récupérer dans des listes imbriquées :
# - "Python" dans variable python
# - 2 dans variable deux
# - 7 dans variable sept

langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

# ==========================================
# MA SOLUTION
# ==========================================
python = langages[0][0]
deux = nombres[1][1][0]
sept = nombres[-1][-1][0]

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# python = langages[0][0]  # ✅ Identique
# deux = nombres[1][1][0]  # ✅ Identique
# sept = nombres[-1][0][0] # ⚠️ Différent mais les deux fonctionnent !

# ==========================================
# EXPLICATION DÉTAILLÉE - DÉCOMPOSITION PAS À PAS
# ==========================================

# -----------------------------
# RÉCUPÉRER "Python"
# -----------------------------
# langages = [["Python", "C++"], "Java"]
#             ↑ Index 0        ↑ Index 1

# Étape 1 : Récupérer la première sous-liste
# langages[0] → ["Python", "C++"]

# Étape 2 : Dans cette sous-liste, récupérer le premier élément
# langages[0][0] → "Python" ✅

# -----------------------------
# RÉCUPÉRER 2
# -----------------------------
# nombres = [1, [4, [2, 3]], 5, [6], [[7]]]
#            ↑   ↑           ↑  ↑    ↑
#            0   1           2  3    4

# Étape 1 : Récupérer l'élément à l'index 1
# nombres[1] → [4, [2, 3]]

# Étape 2 : Dans cette sous-liste, récupérer l'élément à l'index 1
# nombres[1][1] → [2, 3]

# Étape 3 : Dans cette sous-sous-liste, récupérer le premier élément
# nombres[1][1][0] → 2 ✅

# -----------------------------
# RÉCUPÉRER 7
# -----------------------------
# nombres = [1, [4, [2, 3]], 5, [6], [[7]]]
#            ↑   ↑           ↑  ↑    ↑
#            0   1           2  3    4 (ou -1 depuis la fin)

# MA MÉTHODE (avec index négatif) :
# Étape 1 : Récupérer le DERNIER élément
# nombres[-1] → [[7]]

# Étape 2 : Dans cette sous-liste, récupérer le DERNIER élément
# nombres[-1][-1] → [7]

# Étape 3 : Dans cette sous-sous-liste, récupérer le premier élément
# nombres[-1][-1][0] → 7 ✅

# MÉTHODE CORRECTION (avec index positif) :
# nombres[-1] → [[7]]
# nombres[-1][0] → [7]  (premier élément de [[7]])
# nombres[-1][0][0] → 7 ✅

# Les DEUX fonctionnent car :
# [-1] sur [[7]] = dernier élément = [7]
# [0] sur [[7]] = premier élément = [7]
# Résultat identique !

# ==========================================
# VISUALISATION ARBORESCENCE
# ==========================================
# langages structure :
# [
#   ["Python", "C++"],  ← Index 0
#   "Java"              ← Index 1
# ]

# nombres structure :
# [
#   1,              ← Index 0
#   [               ← Index 1
#     4,            ← Index [1][0]
#     [2, 3]        ← Index [1][1]
#   ],
#   5,              ← Index 2
#   [6],            ← Index 3
#   [[7]]           ← Index 4 (ou -1)
# ]

# ==========================================
# MÉTHODE POUR RÉSOUDRE CES EXERCICES
# ==========================================
# 1. Identifier l'élément cible (ex: 2)
# 2. Partir de la liste principale
# 3. Descendre niveau par niveau :
#    - Quel index pour atteindre la sous-liste qui contient 2 ?
#    - Dans cette sous-liste, quel index pour 2 ?
# 4. Empiler les indices : nombres[1][1][0]

# ==========================================
# ASTUCE POUR S'ENTRAÎNER
# ==========================================
# Pour bien comprendre, décompose en plusieurs étapes :
# 
# niveau1 = nombres[1]      # [4, [2, 3]]
# print(niveau1)
# 
# niveau2 = niveau1[1]      # [2, 3]
# print(niveau2)
# 
# resultat = niveau2[0]     # 2
# print(resultat)
# 
# Puis regroupe : nombres[1][1][0]

# ==========================================
# EXERCICES SUPPLÉMENTAIRES RECOMMANDÉS
# ==========================================
# Pour maîtriser les listes imbriquées, créer des exercices perso :
# 
# data = [
#     [1, 2, [3, 4]],
#     [[5], 6],
#     [7, [8, [9, 10]]]
# ]
# 
# Exercice : Récupérer 3, 5, 9, 10

# ==========================================
# DIFFICULTÉ RENCONTRÉE
# ==========================================
# Cette exercice était complexe, j'ai demandé des indices à Gemini
# sans qu'il me donne la solution directe.
# → À réviser et refaire des exercices similaires !

# ==========================================
# SCORE
# ==========================================
# 100% ✅ (solution fonctionnelle, légèrement différente de correction)
