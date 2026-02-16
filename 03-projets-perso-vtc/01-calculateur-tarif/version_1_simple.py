# Calculateur de Tarif VTC - Version 1
# Oualid - Projet VTC Personnel #1
# Date : 16 février 2026
# Sections utilisées : 12-16

# ==========================================
# CONSTANTES (valeurs fixes)
# ==========================================
TARIF_KM = 2.0  # 2€ par kilomètre
POURBOIRE_STANDARD = 5.0  # 5€ de pourboire

# ==========================================
# 1. TITRE DU PROGRAMME
# ==========================================
print("=== CALCULATEUR DE TARIF VTC ===")
print()

# ==========================================
# 2. COLLECTE DES INFORMATIONS
# ==========================================
nom_client = input("Quel est votre nom ? ")
distance = float(input("Quelle est la distance de votre trajet (km) ? "))
duree = int(input("Quelle est la durée du trajet (min) ? "))
reponse_pourboire = input("Pourboire (oui/non) : ")

# ==========================================
# 3. CALCULS
# ==========================================
tarif_de_base = distance * TARIF_KM
pourboire = 0

if reponse_pourboire == "oui":
    pourboire = POURBOIRE_STANDARD

total = tarif_de_base + pourboire

# ==========================================
# 4. AFFICHAGE RÉSULTAT
# ==========================================
print()
print("--- RÉCAPITULATIF COURSE ---")
print(f"Client : {nom_client}")
print(f"Distance : {distance} km")
print(f"Durée : {duree} minutes")
print(f"Tarif de base : {tarif_de_base} €")
print(f"Pourboire : {pourboire} €")
print(f"TOTAL : {total} €")
print()
print("Merci et bonne journée !")