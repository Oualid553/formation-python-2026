# Exercice 5 : Validation de mot de passe
# Section 25 - Formation Docstring
# Oualid - 24 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Créer un script qui valide un mot de passe selon ces règles :
# 1. Si len = 0 : Afficher message en MAJUSCULES
# 2. Si len < 8 : Afficher message avec première lettre en majuscule
# 3. Si que des chiffres : Afficher "Votre mot de passe ne contient que des nombres."
# 4. Sinon : Afficher "Inscription terminée."

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

# ==========================================
# MA SOLUTION
# ==========================================
if len(mdp) == 0: 
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court.title())  # ⚠️ Différent de la correction
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
# if len(mdp) == 0:
#     print(mdp_trop_court.upper())
# elif len(mdp) < 8:
#     print(mdp_trop_court.capitalize())  # ← capitalize() pas title()
# elif mdp.isdigit():
#     print("Votre mot de passe ne contient que des nombres.")
# else:
#     print("Inscription terminée.")

# ==========================================
# COMPARAISON title() vs capitalize()
# ==========================================
# MA MÉTHODE : title()
# "votre mot de passe est trop court.".title()
# → "Votre Mot De Passe Est Trop Court."
# (Première lettre de CHAQUE mot en majuscule)

# CORRECTION : capitalize()
# "votre mot de passe est trop court.".capitalize()
# → "Votre mot de passe est trop court."
# (SEULEMENT la première lettre de la phrase)

# CONSIGNE : "une majuscule sur la première lettre"
# → capitalize() est plus précis ! ✅

# ==========================================
# RAPPEL MÉTHODES DE CASSE
# ==========================================
texte = "bonjour tout le monde"

# upper() - TOUT EN MAJUSCULES
texte.upper()       # "BONJOUR TOUT LE MONDE"

# lower() - tout en minuscules
texte.lower()       # "bonjour tout le monde"

# capitalize() - Première lettre seulement
texte.capitalize()  # "Bonjour tout le monde"

# title() - Première De Chaque Mot
texte.title()       # "Bonjour Tout Le Monde"

# ==========================================
# TESTS EFFECTUÉS
# ==========================================
# Test 1 : Input vide ""
# Résultat : "VOTRE MOT DE PASSE EST TROP COURT." ✅

# Test 2 : Input court "fdhdfh"
# Ma solution : "Votre Mot De Passe Est Trop Court."
# Correction : "Votre mot de passe est trop court."
# → Les deux fonctionnent, capitalize() plus précis

# Test 3 : Que des chiffres "12345789"
# Résultat : "Votre mot de passe ne contient que des nombres." ✅

# Test 4 : Valide "dfogidfogihoind094343"
# Résultat : "Inscription terminée." ✅

# ==========================================
# MÉTHODE DE TRAVAIL
# ==========================================
# 1. Analyse sur papier avant de coder ✅
# 2. Identification des 4 cas de figure ✅
# 3. Choix des méthodes (.upper(), .title(), .isdigit()) ✅
# 4. Structure if/elif/else correcte ✅
# 5. Tests manuels des 4 scénarios ✅

# ==========================================
# CONCEPTS UTILISÉS
# ==========================================
# - input() : Récupérer saisie utilisateur
# - len() : Calculer longueur d'une chaîne
# - .upper() : Convertir en majuscules
# - .title() / .capitalize() : Capitaliser
# - .isdigit() : Vérifier si que des chiffres
# - if/elif/else : Structures conditionnelles
# - Ordre des conditions (cas spécifique d'abord)

# ==========================================
# LEÇON RETENUE
# ==========================================
# Différence title() vs capitalize() :
# - title() = Chaque Mot Commence Par Une Majuscule
# - capitalize() = Seulement la première lettre
# 
# Pour "une majuscule sur la première lettre" → capitalize() ✅

# ==========================================
# SCORE
# ==========================================
# 100% ✅ (fonctionne parfaitement)
# Méthode légèrement différente mais tout aussi valide