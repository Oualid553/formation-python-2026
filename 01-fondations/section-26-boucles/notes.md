# Section 26 - Les Boucles

**Date :** 24 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~2h

---

## 📊 Scores

| Quiz | Score |
|------|-------|
| Quiz 23 | 5/5 (100%) ✅ |
| Quiz 24 | 2/2 (100%) ✅ |
| **Moyenne** | **100%** |

---

## 🔑 1. BOUCLE WHILE

**Syntaxe :** Répète tant qu'une condition est vraie

```python
# Boucle while simple
i = 0
while i < 5:
    print(i)
    i += 1
# Affiche : 0, 1, 2, 3, 4

# Boucle infinie (attention !)
while True:
    reponse = input("Continuer ? (o/n) : ")
    if reponse == "n":
        break  # Sort de la boucle
```

**⚠️ Danger :** Toujours avoir une condition de sortie !

---

## 🔑 2. BOUCLE FOR

**Syntaxe :** Répète pour chaque élément d'une séquence

```python
# Parcourir une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Parcourir une string
for lettre in "Python":
    print(lettre)

# Avec range()
for i in range(5):
    print(i)
# Affiche : 0, 1, 2, 3, 4

for i in range(2, 8):
    print(i)
# Affiche : 2, 3, 4, 5, 6, 7

for i in range(0, 10, 2):
    print(i)
# Affiche : 0, 2, 4, 6, 8
```

---

## 🔑 3. BREAK - Sortir d'une boucle

**Utilisation :** Arrête la boucle immédiatement

```python
# Chercher un élément
nombres = [1, 5, 8, 3, 9, 2]
for nombre in nombres:
    if nombre == 8:
        print("Trouvé !")
        break  # Sort de la boucle
    print(f"Recherche... {nombre}")
# Affiche :
# Recherche... 1
# Recherche... 5
# Trouvé !
```

---

## 🔑 4. CONTINUE - Passer à l'itération suivante

**Utilisation :** Saute le reste du code et passe à la prochaine itération

```python
# Afficher que les nombres impairs
for i in range(10):
    if i % 2 == 0:
        continue  # Saute les pairs
    print(i)
# Affiche : 1, 3, 5, 7, 9
```

**Différence break vs continue :**
```python
# BREAK : Sort complètement de la boucle
for i in range(5):
    if i == 3:
        break
    print(i)
# Affiche : 0, 1, 2

# CONTINUE : Saute juste cette itération
for i in range(5):
    if i == 3:
        continue
    print(i)
# Affiche : 0, 1, 2, 4
```

---

## 🔑 5. ENUMERATE() - Index + Valeur

**Syntaxe :** `enumerate(liste)` retourne (index, valeur)

```python
fruits = ["pomme", "banane", "orange"]

# Sans enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Avec enumerate ✅ Plus pythonique
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Commencer à 1 au lieu de 0
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: pomme
# 2: banane
# 3: orange
```

---

## 🔑 6. COMPRÉHENSIONS DE LISTE ⭐

**Syntaxe :** Créer une liste en une seule ligne

```python
# Sans compréhension (méthode classique)
carres = []
for i in range(5):
    carres.append(i ** 2)
# carres = [0, 1, 4, 9, 16]

# Avec compréhension ✅
carres = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]

# Avec condition
pairs = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]

# Transformer des strings
mots = ["BONJOUR", "PYTHON", "CODE"]
minuscules = [mot.lower() for mot in mots]
# ["bonjour", "python", "code"]
```

**Structure :**
```python
[expression for element in iterable if condition]
```

---

## 🔑 7. ANY() et ALL()

### any() - Au moins un True
```python
nombres = [0, 0, 5, 0]
any(nombres)  # True (5 est "truthy")

any([False, False, False])  # False
any([False, True, False])   # True

# Vérifier si au moins un nombre > 10
nombres = [5, 8, 12, 3]
any(n > 10 for n in nombres)  # True (12 > 10)
```

### all() - Tous True
```python
nombres = [5, 10, 15]
all(nombres)  # True (tous "truthy")

all([True, True, True])   # True
all([True, False, True])  # False

# Vérifier si tous les nombres sont pairs
nombres = [2, 4, 6, 8]
all(n % 2 == 0 for n in nombres)  # True
```

---

## 🔑 8. BOUCLES IMBRIQUÉES

**Syntaxe :** Boucle dans une boucle

```python
# Table de multiplication
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Parcourir liste imbriquée
matrice = [[1, 2], [3, 4], [5, 6]]
for ligne in matrice:
    for element in ligne:
        print(element)
# Affiche : 1, 2, 3, 4, 5, 6
```

---

## 🔑 9. ELSE AVEC BOUCLES

**Utilisation :** Exécuté si la boucle se termine NORMALEMENT (sans break)

```python
# Chercher un élément
nombres = [1, 3, 5, 7]
for n in nombres:
    if n == 4:
        print("Trouvé !")
        break
else:
    print("Pas trouvé")  # S'exécute car pas de break
# Affiche : "Pas trouvé"

# Avec break
nombres = [1, 3, 4, 5]
for n in nombres:
    if n == 4:
        print("Trouvé !")
        break
else:
    print("Pas trouvé")  # Ne s'exécute PAS
# Affiche : "Trouvé !"
```

---

## 🚕 EXEMPLES VTC

```python
# 1. Calculer revenu journalier
courses = [15.50, 23.00, 12.75, 18.20, 9.50]
total = 0
for montant in courses:
    total += montant
print(f"Revenu du jour : {total}€")

# Ou avec sum()
total = sum(courses)

# 2. Trouver courses > 20€
courses_importantes = [montant for montant in courses if montant > 20]

# 3. Vérifier si toutes les courses sont payées
courses_payees = [True, True, True, False, True]
if all(courses_payees):
    print("Tout est payé !")
else:
    print("Il reste des impayés")

# 4. Vérifier si au moins une course en attente
statuts = ["terminée", "terminée", "en attente", "terminée"]
if any(s == "en attente" for s in statuts):
    print("Courses en attente !")
```

---

## ⚠️ POINTS À REVOIR (Auto-évaluation)

- ⚠️ **Compréhensions de liste** : À pratiquer davantage
- ⚠️ **any() et all()** : Comprendre l'utilisation
- ⚠️ **continue et break** : Bien différencier

**→ Section 27 (Exercices boucles) pour pratiquer ! 🎯**

---

## 📋 Résumé

| Concept | Utilisation | Exemple |
|---------|-------------|---------|
| `while` | Répète tant que condition vraie | `while i < 10:` |
| `for` | Parcourt une séquence | `for x in liste:` |
| `break` | Sort de la boucle | Chercher élément |
| `continue` | Passe à l'itération suivante | Ignorer pairs |
| `enumerate()` | Index + valeur | `for i, v in enumerate(liste):` |
| `[... for ...]` | Compréhension liste | `[x*2 for x in range(5)]` |
| `any()` | Au moins un True | `any([False, True])` |
| `all()` | Tous True | `all([True, True])` |

---

## ✅ Section validée le 24 février 2026

**Prêt pour Section 27 : Exercices sur les boucles**
