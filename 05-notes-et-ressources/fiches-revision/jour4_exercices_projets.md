# 📚 FICHE RÉVISION JOUR 4 - Dimanche 1er Mars 2026

**Durée : 20-30 min**  
**Sections à réviser : 27-28 (Exercices boucles, Projet Calculatrice v2)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Comment parcourir les indices d'une string "Python" ?  
   **R:** `for i in range(len("Python")):`

2. **Q:** Que fait `reversed("Python")` ?  
   **R:** Retourne itérateur inversé ("nohtyP")

3. **Q:** Alternative à `reversed()` ?  
   **R:** Slice `[::-1]`

4. **Q:** Syntaxe opérateur ternaire ?  
   **R:** `valeur_si_vrai if condition else valeur_si_faux`

5. **Q:** Opérateur ternaire dans compréhension ?  
   **R:** `[x if x > 0 else 0 for x in liste]`

6. **Q:** `"123".isdigit()` retourne quoi ?  
   **R:** `True`

7. **Q:** `"-5".isdigit()` retourne quoi ?  
   **R:** `False` (ne gère pas négatifs)

8. **Q:** Pattern validation avec while ?  
   **R:** `while True: ... if valide: break`

9. **Q:** Différence `is True` vs juste `if` ?  
   **R:** `is True` redondant, `if condition:` suffit

10. **Q:** Comment incrémenter une variable ?  
    **R:** `i += 1`

### Lecture Cheatsheet (5 min)

**Relire :** `01-fondations/section-27-exercices-boucles/notes.md`

**Points clés à retenir :**
- Opérateur ternaire
- reversed() vs [::-1]
- Validation avec isdigit()

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Résultat de :** `[i if i % 2 == 0 else -i for i in range(5)]` ?
   <details><summary>Réponse</summary>[0, -1, 2, -3, 4]</details>

2. **Que fait ce code ?**
   ```python
   while True:
       x = input("Nombre : ")
       if x.isdigit():
           break
   ```
   <details><summary>Réponse</summary>Redemande jusqu'à avoir un nombre valide</details>

3. **Bug dans ce code ?**
   ```python
   if x.isdigit():
       break
   resultat = x * 2
   ```
   <details><summary>Réponse</summary>x est toujours un string, pas converti en int !</details>

4. **Correction du bug ?**
   <details><summary>Réponse</summary>Ajouter `x = int(x)` après validation</details>

5. **"15".isdigit() vs int("15") ?**
   <details><summary>Réponse</summary>isdigit() vérifie, int() convertit</details>

### Lecture Code (10 min)

**Relis ton Projet VTC #2 :**

```python
# Validation distance
while True:
    distance = input("Entrez la distance en km : ")
    if distance.isdigit():
        distance = int(distance)  # ← CRUCIAL !
        break
    else:
        print("Veuillez entrer un nombre valide\n")

# Calcul avec condition
tarif_final = prix_base
if heure >= 22 or heure < 6:
    supplement_nuit = prix_base * 0.15
    tarif_final = prix_base + supplement_nuit
```

**Questions à te poser :**
- ✅ Pourquoi convertir APRÈS validation ?
- ✅ Pourquoi initialiser `tarif_final = prix_base` ?
- ✅ Que se passe si on oublie le `int()` ?
- ✅ Pourquoi `>=` et `<` pour les heures nuit ?

---

## 📖 CONCEPTS CLÉS SECTIONS 27-28

### Exercices Section 27

**1. range() avec len()**
```python
mot = "Python"
for i in range(len(mot)):  # 0 à 5
    print(i)
```

**2. reversed()**
```python
for lettre in reversed("Python"):
    print(lettre)  # n, o, h, t, y, P

# Alternative
for lettre in "Python"[::-1]:
    print(lettre)
```

**3. Opérateur ternaire**
```python
# Dans variable
resultat = "pair" if x % 2 == 0 else "impair"

# Dans compréhension
nombres = [x if x > 0 else 0 for x in liste]
```

**4. Modulo pour parité**
```python
10 % 2  # 0 → pair
11 % 2  # 1 → impair
```

### Projet Section 28

**Pattern validation entrée :**
```python
while True:
    entree = input("Valeur : ")
    
    # Validation
    if entree.isdigit():
        entree = int(entree)  # Convertir !
        break
    else:
        print("Erreur, recommencez")

# Maintenant entree est un int
```

**Pattern calcul conditionnel :**
```python
# Initialiser avec valeur par défaut
resultat = valeur_base

# Ajouter suppléments selon conditions
if condition_1:
    supplement_1 = calcul1
    resultat += supplement_1

if condition_2:
    supplement_2 = calcul2
    resultat += supplement_2

# resultat contient le total
```

---

## 🚕 RÉVISION PROJET VTC

**Relis mentalement ton calculateur tarif VTC :**

**Structure complète :**
1. Validation distance (while + isdigit + int)
2. Validation heure (while + isdigit + plage 0-23 + int)
3. Calcul tarif base (distance × 2)
4. Condition supplément nuit (22h-6h)
5. Affichage formaté

**Bugs corrigés :**
- ✅ Conversion int() après validation
- ✅ Validation heure max 23 (pas 24)
- ✅ Initialisation tarif_final
- ✅ Tarif final = base + supplément (pas juste supplément)

---

## 🎯 SYNTHÈSE 4 JOURS

**Tu as révisé :**

| Jour | Sections | Concepts clés |
|------|----------|---------------|
| Jour 1 | 21-23 | Conditions, erreurs, modules |
| Jour 2 | 24-25 | Listes, slices, méthodes |
| Jour 3 | 26 | Boucles, break, continue, compréhensions |
| Jour 4 | 27-28 | Validation, projets pratiques |

**Score révision : 14 sections en 4 jours ! 🎉**

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Notes Section 27 relues (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Projet VTC #2 analysé (10 min)

**Total : 30 min ✅**

---

## 💡 ASTUCE FINALE

**Pattern UNIVERSEL de validation :**

```python
while True:
    entree = input("...")
    
    # Validation (isdigit, plage, etc.)
    if valide:
        # Conversion si nécessaire
        entree = int(entree)
        break
    else:
        print("Erreur...")

# Utiliser entree (déjà convertie)
```

**Ce pattern fonctionne pour TOUT ! 🎯**

---

## 🎊 BRAVO POUR CES 4 JOURS !

**Tu as maintenu ta continuité pendant tes jours VTC ! 💪**

**Prochain bloc OFF (2-5 mars) :**
- Section 29 : Projet Liste de courses
- Section 30 : Projet Nombre mystère
- Section 31 : Projet Jeu de rôle

**Tu vas reprendre en force ! 🚀**

---

**Bon courage pour tes 4 jours VTC ! 🚕💨**