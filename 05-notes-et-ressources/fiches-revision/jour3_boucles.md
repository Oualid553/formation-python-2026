# 📚 FICHE RÉVISION JOUR 3 - Samedi 28 Février 2026

**Durée : 20-30 min**  
**Sections à réviser : 26 (Les Boucles)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Syntaxe boucle while ?  
   **R:** `while condition: ...`

2. **Q:** Syntaxe boucle for ?  
   **R:** `for element in sequence: ...`

3. **Q:** Que fait `break` ?  
   **R:** Sort complètement de la boucle

4. **Q:** Que fait `continue` ?  
   **R:** Saute l'itération actuelle, continue la boucle

5. **Q:** `range(5)` génère quoi ?  
   **R:** 0, 1, 2, 3, 4 (5 éléments, de 0 à 4)

6. **Q:** `range(2, 7)` génère quoi ?  
   **R:** 2, 3, 4, 5, 6

7. **Q:** Syntaxe `enumerate()` ?  
   **R:** `for index, valeur in enumerate(liste):`

8. **Q:** Syntaxe compréhension de liste ?  
   **R:** `[expression for element in liste]`

9. **Q:** `any([False, True, False])` retourne quoi ?  
   **R:** `True` (au moins un True)

10. **Q:** `all([True, True, False])` retourne quoi ?  
    **R:** `False` (pas tous True)

### Lecture Cheatsheet (5 min)

**Relire :** `05-notes-et-ressources/cheatsheets/09-boucles.md`

**Points clés à retenir :**
- while vs for
- break vs continue
- Compréhensions de liste

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Que fait ce code ?**
   ```python
   for i in range(5):
       if i == 3:
           break
       print(i)
   ```
   <details><summary>Réponse</summary>Affiche 0, 1, 2 (s'arrête à 3)</details>

2. **Et celui-ci ?**
   ```python
   for i in range(5):
       if i == 3:
           continue
       print(i)
   ```
   <details><summary>Réponse</summary>Affiche 0, 1, 2, 4 (saute 3)</details>

3. **Résultat de :** `[x * 2 for x in range(3)]` ?
   <details><summary>Réponse</summary>[0, 2, 4]</details>

4. **Résultat de :** `[x for x in range(10) if x % 2 == 0]` ?
   <details><summary>Réponse</summary>[0, 2, 4, 6, 8] (nombres pairs)</details>

5. **Différence `for` vs `while` ?**
   <details><summary>Réponse</summary>for = séquence connue, while = condition à vérifier</details>

### Lecture Code (10 min)

**Relis ce code de ton Exercice 9 (Section 27) :**

```python
# Compréhension simple
nombres_pairs = [i for i in nombres if i % 2 == 0]

# Transformation
nombres_doubles = [i * 2 for i in range(5)]

# Opérateur ternaire dans compréhension
nombres_inverses = [i if i % 2 == 0 else -i for i in range(10)]
```

**Questions à te poser :**
- ✅ Quelle est la différence entre les 3 ?
- ✅ Où se place le `if` selon l'usage ?
- ✅ Comment fonctionne `if...else` dans une compréhension ?

---

## 📖 CONCEPTS CLÉS SECTION 26

### Boucle while
```python
while condition:
    # code
    # IMPORTANT : modifier la condition !

# Exemple
i = 0
while i < 5:
    print(i)
    i += 1  # Ne pas oublier !
```

### Boucle for
```python
# Parcourir liste
for element in liste:
    print(element)

# Avec range
for i in range(10):
    print(i)

# Avec enumerate
for index, valeur in enumerate(liste):
    print(f"{index}: {valeur}")
```

### break et continue
```python
# break = SORTIR de la boucle
for i in range(10):
    if i == 5:
        break  # S'arrête à 5
    print(i)

# continue = SAUTER cette itération
for i in range(10):
    if i == 5:
        continue  # Saute 5, continue
    print(i)
```

### Compréhensions de liste
```python
# Simple
[x * 2 for x in range(5)]
# [0, 2, 4, 6, 8]

# Avec filtrage (if à la fin)
[x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Avec transformation conditionnelle (if...else au début)
[x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]]
# [0, 0, 0, 1, 2]
```

### any() et all()
```python
# any() = AU MOINS UN True
any([False, True, False])  # True
any([False, False])        # False

# all() = TOUS True
all([True, True, True])    # True
all([True, False, True])   # False

# Avec condition
nombres = [1, 3, 5, 8]
any(n % 2 == 0 for n in nombres)  # True (8 est pair)
all(n % 2 == 0 for n in nombres)  # False (pas tous pairs)
```

---

## 🚕 EXERCICE MENTAL VTC

**Imagine ces boucles pour tes courses :**

```python
# Calculer revenu total du jour
courses = [15.50, 23.00, 12.75, 18.20]
total = 0
for montant in courses:
    total += montant
# Ou : total = sum(courses)

# Trouver courses > 20€
importantes = [c for c in courses if c > 20]

# Vérifier si toutes payées
paiements = [True, True, True, False]
if all(paiements):
    print("Tout payé !")
else:
    print("Impayés !")

# Au moins une course en attente ?
statuts = ["ok", "ok", "attente", "ok"]
if any(s == "attente" for s in statuts):
    print("Courses en attente !")
```

**Pense à ces patterns pendant tes trajets ! 🧠**

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Cheatsheet boucles relu (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Code analysé (10 min)

**Total : 30 min ✅**

---

## 💡 ASTUCE DU JOUR

**Différencier if dans compréhensions :**

```python
# IF À LA FIN = Filtrage (garde ou enlève)
[x for x in liste if condition]

# IF AU DÉBUT = Transformation (change valeur)
[x if condition else y for x in liste]
```

**Mnémotech : "Fin = Filtre, Début = Décision" 🎯**

---

**Demain : Fiche Jour 4 (Sections 27-28) 📚**