# Exercice 20 : Récupérer des éléments avec les slices
# Section 24 - Formation Docstring
# Oualid - 23 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Récupérer différents morceaux d'une liste avec les slices :
# - Les 3 premiers employés dans 'trois_premiers'
# - Les 3 derniers employés dans 'trois_derniers'
# - Tous sauf le premier et le dernier dans 'milieu'
# - Le premier et le dernier dans 'premier_dernier'

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
#        ↑        ↑          ↑              ↑        ↑          ↑
# Index: 0        1          2              3        4          5

# ==========================================
# MA SOLUTION
# ==========================================
trois_premiers = liste[0:3]   # Indices 0, 1, 2
trois_derniers = liste[3:]    # Indices 3, 4, 5
milieu = liste[1:5]           # Indices 1, 2, 3, 4
premier_dernier = liste[::5]  # Pas de 5 → indices 0 et 5

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
trois_premiers = liste[:3]     # Plus court que [0:3]
trois_derniers = liste[3:]     # ✅ Identique
milieu = liste[1:-1]           # Plus robuste que [1:5]
premier_dernier = liste[::5]   # ✅ Identique

# ==========================================
# EXPLICATION DÉTAILLÉE DES SLICES
# ==========================================

# RÈGLE D'OR : liste[début:fin:pas]
# - début : INCLUS (on prend cet élément)
# - fin : EXCLU (on s'arrête JUSTE AVANT)
# - pas : intervalle entre les éléments

# VISUALISATION DES "FRONTIÈRES" :
#    |  Maxime  |  Martine  |  Christopher  |  Carlos  |  Michael  |  Eric  |
#    ↑          ↑           ↑               ↑          ↑           ↑        ↑
#    0          1           2               3          4           5        6

# liste[:3] = "Coupe à la frontière 3"
# → Prend tout AVANT la frontière 3
# → Résultat : ["Maxime", "Martine", "Christopher"]

# EXEMPLES COMMENTÉS :

# 1. Trois premiers : [:3]
# Signification : Du début jusqu'à l'index 3 (exclu)
# Indices pris : 0, 1, 2
# Résultat : ["Maxime", "Martine", "Christopher"]

# 2. Trois derniers : [3:]
# Signification : De l'index 3 jusqu'à la fin
# Indices pris : 3, 4, 5
# Résultat : ["Carlos", "Michael", "Eric"]
# ⚠️ PROBLÈME : Si on ajoute un élément, on aura 4 derniers, pas 3 !
# ✅ MIEUX : [-3:] (toujours les 3 derniers)

# 3. Milieu : [1:-1]
# Signification : De l'index 1 jusqu'à l'avant-dernier (exclu)
# Indices pris : 1, 2, 3, 4
# -1 = dernier élément, donc on s'arrête avant
# Résultat : ["Martine", "Christopher", "Carlos", "Michael"]
# ✅ AVANTAGE sur [1:5] : Fonctionne même si la liste change de taille !

# 4. Premier et dernier : [::5]
# Signification : De début à fin, avec un pas de 5
# Pas de 5 = longueur liste - 1 (6 - 1 = 5)
# Indices pris : 0, puis 0+5=5
# Résultat : ["Maxime", "Eric"]
# ✅ ENCORE MIEUX : [::len(liste)-1] (s'adapte automatiquement)

# ==========================================
# COMPARAISON MA SOLUTION vs CORRECTION
# ==========================================
# trois_premiers :
#   Moi : [0:3]  ✅ Fonctionne
#   Correction : [:3]  ✅ Plus court (début implicite = 0)
#
# milieu :
#   Moi : [1:5]  ✅ Fonctionne pour cette liste
#   Correction : [1:-1]  ✅ Plus robuste (fonctionne même si liste change)

# ==========================================
# AUTRES EXEMPLES DE SLICES
# ==========================================
exemple = ["A", "B", "C", "D", "E"]

# Tous les éléments
exemple[:]      # ["A", "B", "C", "D", "E"]

# Un élément sur deux
exemple[::2]    # ["A", "C", "E"]

# Inverser la liste
exemple[::-1]   # ["E", "D", "C", "B", "A"]

# Du 2ème au 4ème
exemple[1:4]    # ["B", "C", "D"]

# Les 2 derniers
exemple[-2:]    # ["D", "E"]

# Tous sauf les 2 derniers
exemple[:-2]    # ["A", "B", "C"]

# ==========================================
# LEÇON RETENUE : SLICES [début:fin]
# ==========================================
# 1. début est INCLUS
# 2. fin est EXCLU (on s'arrête juste avant)
# 3. Penser aux "frontières" entre les éléments
# 4. Utiliser -1, -2, etc. pour compter depuis la fin
# 5. [:n] = n premiers, [-n:] = n derniers
# 6. [1:-1] = tous sauf premier et dernier

# ==========================================
# SCORE
# ==========================================
# 100% ✅ (solution fonctionnelle, correction plus robuste)