# Projet VTC #2 : Calculateur Tarif avec Validation

**Date :** 25 février 2026  
**Concepts :** Section 28 (Validation entrées, boucles while, isdigit)  
**Statut :** ✅ Complété  
**Score :** 100% (après corrections)

---

## 🎯 Objectif

Créer un calculateur de tarif VTC professionnel avec :
- ✅ Validation robuste des entrées utilisateur
- ✅ Calcul tarif de base (2€/km)
- ✅ Supplément nuit automatique (+15% entre 22h-6h)
- ✅ Affichage détaillé et formaté

---

## 💻 Exemple d'utilisation

### Cas normal avec supplément nuit
```
=== CALCULATEUR TARIF VTC ===

Entrez la distance en km : 15
Entrez l'heure de prise en charge (0-23) : 23

--- DÉTAILS DE LA COURSE ---
Distance : 15 km
Heure : 23h
Tarif de base : 30€
Supplément nuit (15%) : +4.5€
TARIF FINAL : 34.5€
```

### Gestion d'erreurs
```
Entrez la distance en km : abc
Veuillez entrer un nombre valide

Entrez la distance en km : 15

Entrez l'heure de prise en charge (0-23) : 25
Veuillez entrer une heure valide (0-23)

Entrez l'heure de prise en charge (0-23) : 10

--- DÉTAILS DE LA COURSE ---
Distance : 15 km
Heure : 10h
Tarif de base : 30€
TARIF FINAL : 30€
```

---

## 🛠️ Concepts Python utilisés

| Concept | Application |
|---------|-------------|
| `while True` + `break` | Boucle jusqu'à validation réussie |
| `isdigit()` | Vérifier que l'entrée est numérique |
| Conversion `int()` | Transformer string → nombre |
| Opérateurs `and`, `or` | Conditions multiples |
| Validation de plage | `0 <= heure <= 23` |
| Calculs conditionnels | Supplément selon heure |
| Initialisation variables | `tarif_final = prix_base` |

---

## 🐛 Bugs corrigés (Version initiale → Finale)

### Bug 1 : Variables pas converties
```python
# ❌ VERSION INITIALE
if distance.isdigit():
    break  # distance reste un string !
prix_base = distance * 2  # TypeError ou résultat bizarre

# ✅ VERSION CORRIGÉE
if distance.isdigit():
    distance = int(distance)  # Conversion !
    break
```

### Bug 2 : Validation heure acceptait 24
```python
# ❌ VERSION INITIALE
if heure.isdigit() and 0 <= int(heure) <= 24:  # 24 invalide !

# ✅ VERSION CORRIGÉE
if heure.isdigit() and 0 <= int(heure) <= 23:
```

### Bug 3 : Variable `nuit` pas toujours définie
```python
# ❌ VERSION INITIALE
if heure >= 22 or heure < 6:
    nuit = prix_base * 0.15
print(f"Supplément nuit : +{nuit}€")  # ❌ Erreur si pas de nuit !

# ✅ VERSION CORRIGÉE
tarif_final = prix_base  # Initialiser
if heure >= 22 or heure < 6:
    supplement_nuit = prix_base * 0.15
    tarif_final = prix_base + supplement_nuit
    print(f"Supplément nuit : +{supplement_nuit}€")
```

### Bug 4 : Tarif final = seulement supplément
```python
# ❌ VERSION INITIALE
print(f"TARIF FINAL : {nuit}€")  # Affiche 4.5€ au lieu de 34.5€

# ✅ VERSION CORRIGÉE
print(f"TARIF FINAL : {tarif_final}€")  # Base + supplément
```

---

## 🎓 Leçons apprises

### 1. Toujours convertir après validation
```python
# Pattern correct
if input_str.isdigit():
    input_num = int(input_str)  # ← Ne pas oublier !
    # Maintenant on peut faire des calculs
```

### 2. Initialiser variables avant conditions
```python
# Pattern correct
variable = valeur_par_defaut
if condition:
    variable = autre_valeur
# variable existe toujours
```

### 3. Validation de plages
```python
# Heure valide : 0 à 23 (pas 24 !)
if 0 <= heure <= 23:
    # OK
```

### 4. Tarif = base + tous les suppléments
```python
tarif_final = prix_base
if condition_supplement_1:
    tarif_final += supplement_1
if condition_supplement_2:
    tarif_final += supplement_2
```

---

## 🚕 Différenciation VTC

**Ce projet démontre :**
- ✅ Compréhension du métier VTC (tarifs, suppléments)
- ✅ Connaissance terrain (tarif nuit 22h-6h)
- ✅ Code robuste et professionnel
- ✅ UX pensée pour un chauffeur

**→ Portfolio unique qui se démarque ! 🎯**

---

## 📈 Évolution du projet

| Version | Ajout |
|---------|-------|
| **VTC #1** | Calculateur basique sans validation |
| **VTC #2** | Validation entrées + gestion erreurs ✅ |
| **VTC #3** | À venir : décimaux, autres suppléments |

---

## 🚀 Améliorations futures

1. Gérer distances décimales (12.5 km)
2. Autres suppléments (aéroport +10€, péage)
3. Choix type de véhicule (berline, van, premium)
4. Historique des courses du jour
5. Calcul revenu journalier total
6. Export données CSV

---

## 💡 Note technique

**Formatage des prix :**
- Version actuelle : Affichage simple (`30€`, `4.5€`)
- À venir (Section formatage avancé) : `.2f` pour 2 décimales (`30.00€`, `4.50€`)

**Choix actuel :** Rester sur concepts déjà vus (Section 28)

---

## ✅ Projet validé le 25 février 2026

**Prochains projets VTC :**
- **VTC #3** (après Section 29) : Liste courses journalières
- **VTC #4** (après Section 37) : Registre chauffeurs (dictionnaires)
- **VTC #5** (après Section 42) : Simulateur revenus (fonctions)