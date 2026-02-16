# Entraînement Split & Join - Section 17
# Oualid - 16 février 2026
# Méthodes essentielles pour manipuler les chaînes

# ==========================================
# EXERCICE 1 : Split basique
# ==========================================
# Objectif : Séparer une phrase en liste de mots

phrase = "Bonjour je suis chauffeur VTC"

# Ma solution
mots = phrase.split(" ")

print("=== EXERCICE 1 ===")
print(mots)
# Résultat attendu : ['Bonjour', 'je', 'suis', 'chauffeur', 'VTC']
print()

# Correction officielle
# mots = phrase.split()
# Note : split() sans argument sépare automatiquement sur les espaces
# Les deux fonctionnent, mais split() est plus courant

print()
print()

# ==========================================
# EXERCICE 2 : Split avec séparateur personnalisé
# ==========================================
# Objectif : Séparer une date au format JJ/MM/AAAA

date = "16/02/2026"

# Ma solution
parties = date.split("/")

print("=== EXERCICE 2 ===")
print(parties)
# Résultat attendu : ['16', '02', '2026']
print()

# Correction officielle
# parties = date.split("/")
# ✅ Parfait ! On utilise "/" comme séparateur

# Application : Récupérer le jour, mois, année séparément
jour = parties[0]    # "16"
mois = parties[1]    # "02"
annee = parties[2]   # "2026"
print(f"Jour : {jour}, Mois : {mois}, Année : {annee}")

print()
print()

# ==========================================
# EXERCICE 3 : Join basique
# ==========================================
# Objectif : Joindre une liste de mots en phrase

mots = ['Bonjour', 'je', 'suis', 'Oualid']

# Ma solution
phrase = " ".join(mots)

print("=== EXERCICE 3 ===")
print(phrase)
# Résultat attendu : "Bonjour je suis Oualid"
print()

# Correction officielle
# phrase = " ".join(mots)
# ✅ Parfait ! Le " " met un espace entre chaque mot

# Note importante : Syntaxe de join()
# "séparateur".join(liste)
# Le séparateur est DEVANT le .join()

print()
print()

# ==========================================
# EXERCICE 4 : Join avec séparateur personnalisé
# ==========================================
# Objectif : Créer une date au format JJ/MM/AAAA

jour = "16"
mois = "02"
annee = "2026"

parties = [jour, mois, annee]

# Ma solution
date = "/".join([jour, mois, annee])

print("=== EXERCICE 4 ===")
print(date)
# Résultat attendu : "16/02/2026"
print()

# Correction officielle
# date = "/".join(parties)
# ✅ Parfait ! On peut utiliser directement la liste "parties"
# Ou comme tu as fait : "/".join([jour, mois, annee])
# Les deux fonctionnent

print()
print()

# ==========================================
# EXERCICE 5 : Combo Split + Join
# ==========================================
# Objectif : Remplacer les espaces par des tirets

phrase = "Je suis chauffeur VTC"

# Ma solution
resultat = "-".join(phrase.split(" "))

print("=== EXERCICE 5 ===")
print(resultat)
# Résultat attendu : "Je-suis-chauffeur-VTC"
print()

# Correction officielle
# resultat = "-".join(phrase.split())
# ✅ Excellent ! Tu as utilisé la syntaxe en une ligne !
# Note : split() sans argument fonctionne aussi (plus court)

# Explication du processus :
# 1. phrase.split(" ") → ['Je', 'suis', 'chauffeur', 'VTC']
# 2. "-".join(...) → "Je-suis-chauffeur-VTC"

print()
print()

# ==========================================
# EXERCICE BONUS VTC : Parser données CSV
# ==========================================
# Objectif : Séparer des données de course au format CSV

donnees_course = "Pierre,15.5,25,oui"

# Ma première tentative (ne marchait pas)
# donnees_course.split(",")  # ❌ Résultat non stocké
# print(donnees_course)      # Affiche l'original (pas séparé)

# Ma solution corrigée
infos = donnees_course.split(",")

print("=== EXERCICE BONUS VTC ===")
print("Données brutes :", donnees_course)
print()
print("=== DONNÉES COURSE SÉPARÉES ===")
print(f"Nom : {infos[0]}")
print(f"Distance : {infos[1]} km")
print(f"Durée : {infos[2]} min")
print(f"Pourboire : {infos[3]}")
print()

# Correction officielle
# infos = donnees_course.split(",")
# ✅ Parfait ! Tu STOCKES le résultat dans une variable

# ⚠️ LEÇON IMPORTANTE :
# Les méthodes de chaînes NE MODIFIENT PAS l'original !
# Tu DOIS stocker le résultat dans une variable

# Exemple pour comprendre :
texte_original = "hello"
texte_original.upper()  # ❌ Résultat perdu, rien ne se passe
print("Original après upper() :", texte_original)  # Affiche : hello

texte_maj = texte_original.upper()  # ✅ Résultat stocké
print("Stocké dans nouvelle variable :", texte_maj)  # Affiche : HELLO

print()
print()

# ==========================================
# RÉCAPITULATIF SPLIT & JOIN
# ==========================================

print("=== RÉCAPITULATIF ===")
print()

# SPLIT : Transformer STRING en LISTE
print("SPLIT : STRING → LISTE")
exemple_split = "a,b,c"
resultat_split = exemple_split.split(",")
print(f"  '{exemple_split}'.split(',') → {resultat_split}")
print()

# JOIN : Transformer LISTE en STRING
print("JOIN : LISTE → STRING")
exemple_join = ['a', 'b', 'c']
resultat_join = ",".join(exemple_join)
print(f"  ','.join({exemple_join}) → '{resultat_join}'")
print()

# COMBO : Split puis Join (remplacer séparateur)
print("COMBO : Remplacer séparateur")
original = "a b c"
etape1 = original.split(" ")  # ['a', 'b', 'c']
etape2 = ",".join(etape1)     # "a,b,c"
print(f"  '{original}' → {etape1} → '{etape2}'")
print(f"  En une ligne : ','.join('{original}'.split()) → '{','.join(original.split())}'")
print()

# ==========================================
# POINTS CLÉS À RETENIR
# ==========================================

print("=== POINTS CLÉS ===")
print()
print("1. split() : Sépare une chaîne en liste")
print("   - Sans argument : sépare sur les espaces")
print("   - Avec argument : sépare sur le caractère donné")
print()
print("2. join() : Joint une liste en chaîne")
print("   - Syntaxe : 'séparateur'.join(liste)")
print("   - Le séparateur est AVANT le .join()")
print()
print("3. Les méthodes NE MODIFIENT PAS l'original")
print("   - Toujours STOCKER le résultat dans une variable")
print()
print("4. Split et Join sont INVERSES")
print("   - split() : STRING → LISTE")
print("   - join() : LISTE → STRING")
print()

# ==========================================
# APPLICATION VTC CONCRÈTE
# ==========================================

print("=== APPLICATION VTC ===")
print()

# Imaginons un fichier CSV de courses
courses_csv = """Pierre,15.5,25,oui
Marie,8.2,15,non
Ahmed,22.3,40,oui"""

# Parser chaque ligne
lignes = courses_csv.split("\n")  # Sépare sur les retours à la ligne

print("Courses du jour :")
print()

for i, ligne in enumerate(lignes, 1):
    infos = ligne.split(",")
    nom = infos[0]
    distance = infos[1]
    duree = infos[2]
    pourboire = infos[3]
    
    print(f"Course {i} :")
    print(f"  Client : {nom}")
    print(f"  Distance : {distance} km")
    print(f"  Durée : {duree} min")
    print(f"  Pourboire : {pourboire}")
    print()

# Note : On verra les boucles "for" en Section 26
# Pour l'instant, retiens juste que split() permet de parser du CSV !

print("✅ Entraînement Split & Join terminé !")