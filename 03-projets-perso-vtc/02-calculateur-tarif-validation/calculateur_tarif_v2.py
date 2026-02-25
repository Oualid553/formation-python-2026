# Projet VTC #2 : Calculateur Tarif avec Validation
# Oualid - 25 février 2026
# Concepts : Section 28 (while, isdigit, validation)

# ==========================================
# OBJECTIF DU PROJET
# ==========================================
# Créer un calculateur de tarif VTC avec :
# 1. Validation des entrées utilisateur
# 2. Calcul tarif base (distance × 2€/km)
# 3. Supplément nuit (+15% entre 22h et 6h)
# 4. Affichage détaillé

# ==========================================
# MA VERSION INITIALE (avec bugs)
# ==========================================
# # 1. Boucle validation distance
# while True:
#     distance = input("Entrez la distance en km : ")
#     if distance.isdigit():
#         print(f"Entrez la distance en km : {int(distance)}")  # ❌ Print inutile
#         break
#     else:
#         print("Veuillez entrer un nombre valide")
#     
# # 2. Boucle validation heure
# while True:
#     heure = input("Entrez l'heure de prise en charge (00 - 23) : ")
#     if heure.isdigit() and 0 <= int(heure) <= 24:  # ❌ 24 invalide
#         print(f"Entrez l'heure de prise en charge (0-23) : {int(heure)}")
#         break
#     else:
#         print("Veuillez entrer une heure valide (0-23)")
# 
# if distance and heure:  # ❌ Condition inutile
#     print(" --- DETAILS DE LA COURSE --- ")
# 
# # 3. Calcul tarif
# prix_base = distance * 2  # ❌ distance encore un string !
# 
# print(f"Distance : {distance} km")
# print(f"Heure : {heure}h")
# print(f"Tarif de base : {float(prix_base)} ")
# if heure >= 22 or heure < 6:  # ❌ heure encore un string !
#     nuit = prix_base * 0.15
# print(f"Supplément nuit (15%) : +{nuit}")  # ❌ nuit pas toujours défini
# print(f"TARIF FINAL : {nuit}€")  # ❌ Affiche seulement le supplément

# ==========================================
# BUGS IDENTIFIÉS
# ==========================================
# Bug 1 : Print de confirmation inutile après validation
# Bug 2 : Validation heure accepte 24 (devrait être 0-23)
# Bug 3 : Variables distance et heure jamais converties en int
# Bug 4 : Condition "if distance and heure" inutile
# Bug 5 : Calcul tarif nuit incomplet (variable nuit pas toujours définie)
# Bug 6 : Tarif final affiche seulement le supplément au lieu du total

# ==========================================
# VERSION CORRIGÉE FINALE
# ==========================================

print("=== CALCULATEUR TARIF VTC ===\n")

# 1. Validation distance
while True:
    distance = input("Entrez la distance en km : ")
    if distance.isdigit():
        distance = int(distance)  # ✅ Conversion après validation
        break
    else:
        print("Veuillez entrer un nombre valide\n")

# 2. Validation heure
while True:
    heure = input("Entrez l'heure de prise en charge (0-23) : ")
    if heure.isdigit() and 0 <= int(heure) <= 23:  # ✅ Max 23
        heure = int(heure)  # ✅ Conversion après validation
        break
    else:
        print("Veuillez entrer une heure valide (0-23)\n")

# 3. Calculs
print("\n--- DÉTAILS DE LA COURSE ---")
print(f"Distance : {distance} km")
print(f"Heure : {heure}h")

prix_base = distance * 2
print(f"Tarif de base : {prix_base}€")

# Supplément nuit
tarif_final = prix_base  # ✅ Initialiser avec valeur par défaut
if heure >= 22 or heure < 6:
    supplement_nuit = prix_base * 0.15
    tarif_final = prix_base + supplement_nuit  # ✅ Total complet
    print(f"Supplément nuit (15%) : +{supplement_nuit}€")

print(f"TARIF FINAL : {tarif_final}€")

# ==========================================
# EXEMPLE D'EXÉCUTION
# ==========================================
# === CALCULATEUR TARIF VTC ===
# 
# Entrez la distance en km : abc
# Veuillez entrer un nombre valide
# 
# Entrez la distance en km : 15
# Entrez l'heure de prise en charge (0-23) : 25
# Veuillez entrer une heure valide (0-23)
# 
# Entrez l'heure de prise en charge (0-23) : 23
# 
# --- DÉTAILS DE LA COURSE ---
# Distance : 15 km
# Heure : 23h
# Tarif de base : 30€
# Supplément nuit (15%) : +4.5€
# TARIF FINAL : 34.5€

# ==========================================
# CONCEPTS UTILISÉS
# ==========================================
# 1. while True + break : Boucle jusqu'à validation
# 2. isdigit() : Vérifier que l'entrée est un nombre
# 3. Conversion int() : Transformer string en nombre
# 4. Conditions multiples : and, or
# 5. Validation de plage : 0 <= x <= 23
# 6. Calculs conditionnels : Supplément selon heure
# 7. Variables initialisées : tarif_final = prix_base

# ==========================================
# LEÇONS RETENUES
# ==========================================
# 1. TOUJOURS convertir après validation :
#    if x.isdigit():
#        x = int(x)  # ← Ne pas oublier !
#
# 2. Initialiser variables avant if :
#    variable = valeur_defaut
#    if condition:
#        variable = autre_valeur
#
# 3. Vérifier plages de valeurs :
#    0 <= heure <= 23 (pas 24 !)
#
# 4. Tarif final = base + suppléments (pas juste supplément)

# ==========================================
# DIFFÉRENCIATION VTC
# ==========================================
# Ce projet démontre :
# - Compréhension métier VTC (tarifs, suppléments nuit)
# - Validation robuste des entrées
# - Calculs tarifaires réalistes
# - UX claire pour le chauffeur

# ==========================================
# AMÉLIORATIONS FUTURES POSSIBLES
# ==========================================
# 1. Gérer décimaux (12.5 km)
# 2. Autres suppléments (aéroport, péage)
# 3. Historique des courses
# 4. Calcul revenu journalier
# 5. Export des données

# ==========================================
# SCORE
# ==========================================
# Version initiale : 85% (bonne logique, bugs de conversion)
# Version corrigée : 100% ✅