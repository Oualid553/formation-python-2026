# Exercice 14 : Créer une URL avec f-string
# Section 19 - Formation Docstring
# Oualid - 16 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Recréer l'URL : https://www.docstring.fr/glossaire/
# En utilisant les variables fournies et une f-string

# ==========================================
# CODE DE BASE
# ==========================================
# Ne modifiez pas les variables ci-dessous
protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"

# ==========================================
# MA SOLUTION
# ==========================================
URL = f"{protocole}www.{nom_du_site}.{extension}/{page}/"
print(URL)
# https://www.docstring.fr/glossaire/ ✅

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# Identique à ma solution ✅

# ==========================================
# DÉTAIL F-STRING
# ==========================================
# Structure URL : protocole + www. + nom_du_site + . + extension + / + page + /
# f"{protocole}     → "https://"
# www.              → texte fixe
# {nom_du_site}     → "docstring"
# .                 → texte fixe
# {extension}       → "fr"
# /                 → texte fixe
# {page}            → "glossaire"
# /                 → texte fixe (slash final obligatoire)

# ==========================================
# NOTE PERSONNELLE
# ==========================================
# Exercice facile, les f-strings sont déjà vues en Section 17 (projets)
# Attention au slash final "/" qui est obligatoire
# Score : 100%