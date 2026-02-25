# Exercice 25 : Sortir d'une boucle infinie
# Section 27 - Formation Docstring
# Oualid - 25 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Corriger la boucle while infinie
# Faire en sorte que resultat soit assigné

# ==========================================
# CODE DE DÉPART (bugué)
# ==========================================
# i = 0
# while i < 10:
#     pass  # ❌ i jamais incrémenté → boucle infinie !
# resultat = "Exercice réussi !"

# ==========================================
# MA SOLUTION
# ==========================================
i = 0
while i < 10:
    i += 1  # Incrémenter pour sortir de la boucle
resultat = "Exercice réussi !"
print(resultat)

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# i = 0
# while i < 10:
#     i += 1
# resultat = "Exercice réussi !"

# ==========================================
# BLOCAGE INITIAL
# ==========================================
# J'ai bien galéré à cause du "pass" que je n'ai pas osé supprimer au début
# Une fois compris que pass = instruction vide, tout est devenu clair

# ==========================================
# LEÇON RETENUE
# ==========================================
# 1. pass = instruction vide, placeholder temporaire
# 2. Toujours prévoir condition de sortie avec while
# 3. Incrémenter variable de contrôle : i += 1

# ==========================================
# ASTUCE PRO
# ==========================================
# Toujours prévoir une "porte de sortie" dans une boucle while :
# - Incrémenter une variable
# - Ou condition qui devient False
# → Évite boucles infinies accidentelles

# ==========================================
# SCORE
# ==========================================
# 95% ✅ (Hésitation avec pass)