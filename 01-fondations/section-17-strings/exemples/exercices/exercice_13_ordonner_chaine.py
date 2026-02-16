# Exercice 13 : Ordonner une chaîne de caractères
# Section 17 - Formation Docstring
# Oualid - 16 février 2026

# ==========================================
# CONSIGNE
# ==========================================
# Trier les prénoms par ordre alphabétique
# Résultat attendu : "Anne, Julien, Lucien, Marie, Pierre"

# ==========================================
# CODE DE DÉPART
# ==========================================
chaine = "Pierre, Julien, Anne, Marie, Lucien"

# ==========================================
# MA SOLUTION
# ==========================================
chaine_en_ordre = chaine.split(", ")   # 1. Séparer en liste
chaine_en_ordre.sort()                 # 2. Trier la liste
chaine_en_ordre = ", ".join(chaine_en_ordre)  # 3. Rejoindre en chaîne

print(chaine_en_ordre)
# Résultat : "Anne, Julien, Lucien, Marie, Pierre" ✅

# ==========================================
# CORRECTION OFFICIELLE
# ==========================================
chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaine.split(", ")      # 1. Séparer
chaine_liste.sort()                    # 2. Trier
chaine_en_ordre = ", ".join(chaine_liste)  # 3. Rejoindre

# ==========================================
# DIFFÉRENCES
# ==========================================
# Ma solution : Réutilise la même variable chaine_en_ordre
# Correction : Utilise une variable intermédiaire chaine_liste
# Les deux sont corrects !

# ==========================================
# DÉTAIL DU PROCESSUS
# ==========================================
print("\nÉtape par étape :")

# Étape 1 : Chaîne originale
print(f"Original : {chaine}")

# Étape 2 : Après split (liste)
liste = chaine.split(", ")
print(f"Après split : {liste}")
# ['Pierre', 'Julien', 'Anne', 'Marie', 'Lucien']

# Étape 3 : Après sort (liste triée)
liste.sort()
print(f"Après sort : {liste}")
# ['Anne', 'Julien', 'Lucien', 'Marie', 'Pierre']

# Étape 4 : Après join (chaîne triée)
resultat = ", ".join(liste)
print(f"Après join : {resultat}")
# "Anne, Julien, Lucien, Marie, Pierre"

# ==========================================
# POINTS CLÉS (Docstring)
# ==========================================
# • On ne peut pas trier une chaîne directement
# • split() : STRING → LISTE
# • sort() : Trie la liste (modifie directement)
# • join() : LISTE → STRING

# Différence sort() vs sorted() :
liste1 = [3, 1, 2]
liste1.sort()        # Modifie directement
print(liste1)        # [1, 2, 3]

liste2 = [3, 1, 2]
liste2 = sorted(liste2)  # Retourne nouvelle liste
print(liste2)        # [1, 2, 3]

# ==========================================
# NOTE PERSONNELLE
# ==========================================
# J'ai un peu bloqué car j'ai oublié de stocker join() dans la variable.
# Mais je m'en suis rappelé grâce aux explications de Claude !
# Leçon retenue : Les méthodes NE MODIFIENT PAS l'original.
# Score : 100%