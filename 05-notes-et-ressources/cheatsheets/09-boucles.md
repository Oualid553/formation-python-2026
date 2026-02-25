# Cheatsheet : Les Boucles

**Section 26 - Les Boucles**
**Date :** 24 février 2026

---

## 🔄 BOUCLE WHILE

```python
# Syntaxe de base
while condition:
    # code à répéter

# Exemple
i = 0
while i < 5:
    print(i)
    i += 1  # IMPORTANT : incrémenter !

# Boucle infinie avec sortie
while True:
    reponse = input("Continuer ? (o/n) : ")
    if reponse == "n":
        break
```

**⚠️ Attention :** Toujours avoir une condition de sortie pour éviter boucle infinie !

---

## 🔄 BOUCLE FOR

```python
# Parcourir une liste
for element in liste:
    print(element)

# Parcourir une string
for caractere in "Python":
    print(caractere)

# Avec range()
for i in range(5):          # 0 à 4
    print(i)

for i in range(2, 8):       # 2 à 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (pas de 2)
    print(i)

for i in range(10, 0, -1):  # 10 à 1 (décroissant)
    print(i)
```

---

## 🛑 BREAK - Sortir de la boucle

```python
# Sort COMPLÈTEMENT de la boucle
for i in range(10):
    if i == 5:
        break  # Arrête tout
    print(i)
# Affiche : 0, 1, 2, 3, 4

# Chercher un élément
for element in liste:
    if element == recherche:
        print("Trouvé !")
        break
```

---

## ⏭️ CONTINUE - Passer à l'itération suivante

```python
# Saute juste cette itération, continue la boucle
for i in range(10):
    if i == 5:
        continue  # Saute 5
    print(i)
# Affiche : 0, 1, 2, 3, 4, 6, 7, 8, 9

# Ignorer les nombres pairs
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Affiche : 1, 3, 5, 7, 9
```

**Différence :**
- `break` → SORT de la boucle
- `continue` → SAUTE cette itération, continue

---

## 🔢 ENUMERATE() - Index + Valeur

```python
fruits = ["pomme", "banane", "orange"]

# Avec enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: pomme
# 1: banane
# 2: orange

# Commencer à 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: pomme
# 2: banane
# 3: orange
```

---

## ⚡ COMPRÉHENSIONS DE LISTE

**Syntaxe :** `[expression for element in iterable if condition]`

```python
# Sans condition
carres = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Avec condition (if)
pairs = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transformer des strings
mots = ["BONJOUR", "PYTHON"]
minuscules = [mot.lower() for mot in mots]
# ["bonjour", "python"]

# Filtrer et transformer
nombres = [1, 2, 3, 4, 5]
doubles_pairs = [x * 2 for x in nombres if x % 2 == 0]
# [4, 8]
```

**Équivalent classique :**
```python
# Compréhension
resultat = [x * 2 for x in range(5)]

# Classique
resultat = []
for x in range(5):
    resultat.append(x * 2)
```

---

## ✅ ANY() - Au moins un True

```python
# Retourne True si AU MOINS UN élément est True
any([False, False, True, False])  # True
any([False, False, False])        # False
any([])                           # False (liste vide)

# Avec condition
nombres = [1, 3, 5, 8, 11]
any(n % 2 == 0 for n in nombres)  # True (8 est pair)

# Vérifier si au moins un mot commence par "P"
mots = ["Chat", "Chien", "Python"]
any(mot.startswith("P") for mot in mots)  # True
```

---

## ✅ ALL() - Tous True

```python
# Retourne True si TOUS les éléments sont True
all([True, True, True])      # True
all([True, False, True])     # False
all([])                      # True (liste vide !)

# Avec condition
nombres = [2, 4, 6, 8]
all(n % 2 == 0 for n in nombres)  # True (tous pairs)

# Vérifier si tous les mots sont en majuscules
mots = ["PYTHON", "CODE", "TEST"]
all(mot.isupper() for mot in mots)  # True
```

---

## 🔁 BOUCLES IMBRIQUÉES

```python
# Boucle dans une boucle
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Table de multiplication
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# Parcourir matrice
matrice = [[1, 2], [3, 4], [5, 6]]
for ligne in matrice:
    for element in ligne:
        print(element)
```

---

## 🔚 ELSE AVEC BOUCLES

```python
# else s'exécute si la boucle se termine NORMALEMENT (sans break)

# Sans break → else s'exécute
for i in range(5):
    print(i)
else:
    print("Boucle terminée normalement")
# Affiche : 0, 1, 2, 3, 4, "Boucle terminée normalement"

# Avec break → else ne s'exécute PAS
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Boucle terminée normalement")  # Ne s'affiche pas
# Affiche : 0, 1, 2
```

**Usage pratique :** Chercher un élément
```python
nombres = [1, 3, 5, 7]
for n in nombres:
    if n == 4:
        print("Trouvé !")
        break
else:
    print("Pas trouvé")  # S'exécute car pas de break
```

---

## 📊 TABLEAU COMPARATIF

| Concept | Quand utiliser | Exemple |
|---------|----------------|---------|
| `while` | Nombre d'itérations inconnu | Attendre input utilisateur |
| `for` | Parcourir une séquence | Lire chaque élément d'une liste |
| `break` | Sortir immédiatement | Trouver un élément |
| `continue` | Ignorer une itération | Filtrer certains éléments |
| `enumerate()` | Besoin index + valeur | Afficher position et élément |
| `[... for ...]` | Créer nouvelle liste | Transformer/filtrer données |
| `any()` | Vérifier "au moins un" | Au moins une tâche terminée ? |
| `all()` | Vérifier "tous" | Tous les champs remplis ? |

---

## 🚕 EXEMPLES VTC

```python
# 1. Total revenus du jour
courses = [15.50, 23.00, 12.75, 18.20]
total = sum(courses)

# 2. Courses > 20€
importantes = [c for c in courses if c > 20]

# 3. Tous les paiements reçus ?
paiements = [True, True, False, True]
if all(paiements):
    print("Tout payé !")

# 4. Au moins une course en attente ?
statuts = ["ok", "ok", "attente", "ok"]
if any(s == "attente" for s in statuts):
    print("Courses en attente !")

# 5. Afficher courses avec numéro
for i, montant in enumerate(courses, start=1):
    print(f"Course {i}: {montant}€")
```

---

## 🎯 À RETENIR

1. **while** → condition vraie
2. **for** → parcourir séquence
3. **break** → SORTIR boucle
4. **continue** → SAUTER itération
5. **enumerate()** → index + valeur
6. **[x for x in ...]** → liste en 1 ligne
7. **any()** → AU MOINS UN
8. **all()** → TOUS

---

**Scores Section 26 :**
- Quiz 23 : 5/5 (100%) ✅
- Quiz 24 : 2/2 (100%) ✅
