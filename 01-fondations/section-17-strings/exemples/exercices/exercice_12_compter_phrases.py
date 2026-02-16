# Exercice 12 : Compter le nombre de phrases dans un texte
# Section 17 - Formation Docstring
# Oualid - 16 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Compter le nombre de phrases dans le texte (4 phrases)
# Résultat attendu : 4

# ==========================================
# CODE DE DÉPART
# ==========================================
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
           Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
           Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

# ==========================================
# MA SOLUTION
# ==========================================
resultat = lorem.count(".")

print(f"Nombre de phrases : {resultat}")  # 4

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Identique à ma solution ✅

# ==========================================
# NOTE PERSONNELLE
# ==========================================
# Logique simple : 1 phrase = 1 point
# Donc compter les points = compter les phrases
# Score : 100%