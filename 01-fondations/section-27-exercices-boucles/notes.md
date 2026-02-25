# Section 27 - Exercices sur les Boucles

**Date :** 25 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~3h

---

## 📊 Scores

| Exercice | Score | Statut |
|----------|-------|--------|
| Exercice 6 | 100% | ✅ |
| Exercice 7 | 90% | ✅ |
| Exercice 23 | 100% | ✅ |
| Exercice 24 | 100% | ✅ |
| Exercice 25 | 95% | ✅ |
| Exercice 8 | 100% | ✅ |
| Exercice 9 | 95% | ✅ |
| Exercice 26 | 100% | ✅ |
| **Moyenne** | **97.5%** | ✅ |

---

## 💪 Points forts

- ✅ Compréhensions de liste maîtrisées
- ✅ Modulo (%) pour pairs/impairs
- ✅ range() avec len()
- ✅ break avec conditions
- ✅ f-strings avec calculs
- ✅ Autonomie (recherches internet quand bloqué)

---

## ⚠️ Points à consolider

- ⚠️ `reversed()` : Compris après aide
- ⚠️ Opérateur ternaire dans compréhensions (cherché sur internet)
- ⚠️ `pass` : Hésitation à supprimer

---

## 🔑 Nouvelles compétences acquises

### 1. Opérateur ternaire dans compréhensions

```python
# SANS else - Filtrage simple
pairs = [x for x in liste if x % 2 == 0]

# AVEC else - Transformation conditionnelle
inverses = [x if x % 2 == 0 else -x for x in liste]
#          ↑ valeur si vrai    ↑ valeur si faux
```

**Structure :** `valeur_si_vrai if condition else valeur_si_faux for x in liste`

### 2. `reversed()` pour inverser une séquence

```python
# Méthode 1 : reversed()
for lettre in reversed("Python"):
    print(lettre)  # n, o, h, t, y, P

# Méthode 2 : Slice [::-1]
for lettre in "Python"[::-1]:
    print(lettre)  # n, o, h, t, y, P
```

**Les deux sont équivalentes !**

### 3. `pass` - Instruction vide

```python
while condition:
    pass  # Ne fait rien, placeholder temporaire
```

**Usage :** Code à compléter plus tard, éviter erreur syntaxe

---

## 📝 Résumé exercices

### Exercice 6 - Afficher 10 utilisateurs
**Objectif :** Afficher "Utilisateur 1" à "Utilisateur 10"

**Solution :**
```python
for i in range(1, 11):
    print(f"Utilisateur {i}")
```

**Alternative :**
```python
for i in range(10):
    print(f"Utilisateur {i + 1}")
```

---

### Exercice 7 - Mot à l'envers
**Objectif :** Afficher lettres de "Python" inversées

**Solution :**
```python
mot = "Python"
for lettre in reversed(mot):
    print(lettre)
```

**Alternative avec slice :**
```python
for lettre in mot[::-1]:
    print(lettre)
```

**Blocage initial :** Confusion avec `reversed`  
**Leçon :** `reversed()` retourne un itérateur inversé

---

### Exercice 23 - Fixer erreur range()
**Objectif :** Afficher index de chaque lettre de "Python"

**Code bugué :**
```python
for i in range(mot):  # ❌ range() attend un nombre !
    print(i)
```

**Solution :**
```python
mot = "Python"
for i in range(len(mot)):  # ✅ len() retourne 6
    print(i)  # 0, 1, 2, 3, 4, 5
```

**Leçon :** `range()` nécessite un nombre, utiliser `len()` pour obtenir longueur

---

### Exercice 24 - Table de multiplication
**Objectif :** Afficher table du 7 (0×7 à 10×7)

**Solution :**
```python
nombre = 7
for i in range(11):  # 0 à 10
    print(f"{i} x {nombre} = {i * nombre}")
```

**Leçon :** Calculs possibles directement dans f-strings

---

### Exercice 25 - Sortir boucle infinie
**Objectif :** Corriger boucle while infinie

**Code bugué :**
```python
i = 0
while i < 10:
    pass  # ❌ i jamais incrémenté → boucle infinie !
```

**Solution :**
```python
i = 0
while i < 10:
    i += 1  # ✅ Incrémenter pour sortir
resultat = "Exercice réussi !"
```

**Leçon :** Toujours prévoir condition de sortie avec `while`

---

### Exercice 8 - Sortir avec input
**Objectif :** Permettre à l'utilisateur de sortir de la boucle

**Solution 1 (la mienne) :**
```python
continuer = "o"
while continuer == "o":
    print("On continue !")
    response = input("Voulez-vous continuer ? o/n ")
    if response == "n":
        break
```

**Solution 2 (correction) :**
```python
continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")
```

**Différence :** Solution 2 réassigne `continuer`, pas besoin de `break`

---

### Exercice 9 - Compréhensions de liste
**Objectif :** Remplacer boucles classiques par compréhensions

**Exemple 1 : Filtrer pairs**
```python
# Classique
nombres_pairs = []
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)

# Compréhension ✅
nombres_pairs = [i for i in nombres if i % 2 == 0]
```

**Exemple 2 : Filtrer positifs**
```python
# Compréhension
nombres_positifs = [i for i in nombres if i >= 0]
```

**Exemple 3 : Doubler valeurs**
```python
# Compréhension
nombres_doubles = [i * 2 for i in range(5)]
```

**Exemple 4 : Transformation conditionnelle** ⭐
```python
# Pairs inchangés, impairs inversés
nombres_inverses = [i if i % 2 == 0 else -i for i in range(10)]
```

**Leçon :** Opérateur ternaire dans compréhensions = transformation conditionnelle

---

### Exercice 26 - Nombres pairs avec modulo
**Objectif :** Extraire nombres pairs de 0 à 50

**Solution compréhension :**
```python
nombres = range(51)
nombres_pairs = [i for i in nombres if i % 2 == 0]
```

**Solution classique :**
```python
nombres_pairs = []
for i in range(51):
    if i % 2 == 0:
        nombres_pairs.append(i)
```

**Leçon :** Modulo `%` parfait pour tester parité

---

## 🎯 Concepts clés consolidés

| Concept | Maîtrisé | Application |
|---------|----------|-------------|
| `range()` avec `len()` | ✅ | Parcourir indices |
| `reversed()` | ✅ | Inverser séquence |
| Compréhensions simples | ✅ | `[x for x in liste if ...]` |
| Compréhensions ternaires | ✅ | `[x if ... else y for x in liste]` |
| Modulo `%` | ✅ | Tester pairs/impairs |
| `break` avec `input()` | ✅ | Sortie interactive |
| `pass` | ✅ | Placeholder vide |

---

## 📚 Références

### Opérateur ternaire
```python
# Dans une variable
resultat = "pair" if x % 2 == 0 else "impair"

# Dans une compréhension
liste = [x if x > 0 else 0 for x in nombres]
```

### Inverser une séquence
```python
reversed(iterable)  # Fonction
sequence[::-1]      # Slice
```

### Modulo
```python
10 % 2   # 0 (pair)
11 % 2   # 1 (impair)
```

---

## ✅ Section validée le 25 février 2026

**Prêt pour Section 28 : Projet Docstring #2 - Calculatrice v2**