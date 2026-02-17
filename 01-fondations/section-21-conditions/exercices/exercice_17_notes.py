# Exercice 17 : Structure conditionnelle avancée - Remettre dans l'ordre
# Section 21 - Formation Docstring
# Oualid - 17 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Remettre les if/elif dans le bon ordre
# sans modifier les conditions elles-mêmes
# Note < 3         → "Sans commentaire..."
# Note 3 à 6       → "Tu n'as rien compris !"
# Note 7 à 10      → "Il faut tout revoir..."
# Note 11 à 14     → "Peut mieux faire."
# Note 15 à 17     → "Bon travail !"
# Note 18 à 19     → "Excellent !!"
# Note 20          → "C'est un sans faute !"

# ==========================================
# MON CODE INITIAL (n'a pas fonctionné ❌)
# ==========================================
# Erreur 1 : J'ai modifié les conditions (ajouté des "and")
# Erreur 2 : Double print (un au début, un à la fin)
# Erreur 3 : Mauvaise façon de lancer le script (bouton Play VS Code)
#
# import sys
# note = int(sys.argv[-1])
# commentaire = ""
#
# print(commentaire)  # ❌ Print au mauvais endroit (avant les conditions !)
#
# if note == 20:
#     commentaire = "C'est un sans faute !"
# elif note >= 18 and note < 20:   # ❌ J'ai ajouté "and note < 20" (modifié la condition)
#     commentaire = "Excellent !!"
# elif note >= 15 and note < 18:   # ❌ J'ai ajouté "and note < 18" (modifié la condition)
#     commentaire = "Bon travail !"
# elif note >= 11 and note < 14:   # ❌ J'ai ajouté "and note < 14" (modifié la condition)
#     commentaire = "Peut mieux faire."
# elif note >= 7 and note < 10:    # ❌ J'ai ajouté "and note < 10" (modifié la condition)
#     commentaire = "Il faut tout revoir..."
# elif note >= 3 and note < 6:     # ❌ J'ai ajouté "and note < 6" (modifié la condition)
#     commentaire = "Tu n'as rien compris !"
# elif note < 3:
#     commentaire = "Sans commentaire..."
# print(commentaire)

# ==========================================
# CORRECTION OFFICIELLE ✅
# ==========================================
import sys
note = int(sys.argv[-1])
commentaire = ""

if note < 3:
    commentaire = "Sans commentaire..."
elif note >= 18 and note < 20:
    commentaire = "Excellent !!"
elif note == 20:
    commentaire = "C'est un sans faute !"
elif note > 14:
    commentaire = "Bon travail !"
elif note > 10:
    commentaire = "Peut mieux faire."
elif note > 6:
    commentaire = "Il faut tout revoir..."
elif note >= 3:
    commentaire = "Tu n'as rien compris !"

print(commentaire)

# ==========================================
# COMMENT LANCER CE SCRIPT CORRECTEMENT
# ==========================================
# Dans le terminal Git Bash :
# python exercice_17_notes.py 2   → "Sans commentaire..."
# python exercice_17_notes.py 5   → "Tu n'as rien compris !"
# python exercice_17_notes.py 8   → "Il faut tout revoir..."
# python exercice_17_notes.py 12  → "Peut mieux faire."
# python exercice_17_notes.py 16  → "Bon travail !"
# python exercice_17_notes.py 19  → "Excellent !!"
# python exercice_17_notes.py 20  → "C'est un sans faute !"
# ⚠️ NE PAS lancer avec le bouton Play VS Code !

# ==========================================
# ERREURS COMPRISES ET LEÇONS RETENUES
# ==========================================
# ❌ ERREUR 1 : Modifier les conditions avec "and"
#    → La consigne disait "ne pas modifier les conditions"
#    → J'ai ajouté des "and" inutiles car elif élimine déjà les cas précédents !
#
# ❌ ERREUR 2 : Double print
#    → print() avant les conditions = affiche chaîne vide
#    → Un seul print à la FIN obligatoire
#
# ❌ ERREUR 3 : Lancer avec bouton Play
#    → sys.argv[-1] prend le dernier argument du terminal
#    → Sans argument → prend le chemin du fichier → ValueError !
#
# ✅ LEÇON FONDAMENTALE :
#    Python s'arrête à la PREMIÈRE condition vraie (elif)
#    → Pas besoin de "and" dans la plupart des cas
#    → "and" uniquement si deux plages se chevauchent (ex: >= 18 et == 20)
#    → L'ordre des elif est CRITIQUE
