# Section 18 - Les Opérateurs

**Date :** 16 février 2026 (22h-23h)
**Temps :** ~1h
**Statut :** ✅ Validée

---

## 📚 Contenu

- Vidéo 112 : Introduction
- Vidéo 113 : Opérateurs mathématiques
- Vidéo 114 : Module math (avancé)
- Vidéo 115 : Opérateurs d'assignation
- Vidéo 116 : Opérateurs de comparaison
- Vidéo 117 : Différence is vs ==

---

## 🔢 1. OPÉRATEURS MATHÉMATIQUES

| Opérateur | Action | Exemple | Résultat |
|-----------|--------|---------|----------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (float) | `5 / 2` | `2.5` |
| `//` | Division entière | `5 // 2` | `2` |
| `%` | Modulo (reste) | `5 % 2` | `1` |
| `**` | Puissance | `5 ** 2` | `25` |

### Points importants
```python
# Division toujours retourne float
10 / 2  # 5.0 (pas 5 !)

# Division entière (arrondi vers le bas)
7 // 2  # 3 (pas 3.5)

# Modulo = reste de la division
10 % 3  # 1 (10 = 3*3 + 1)

# Puissance
2 ** 8  # 256
```

### Cas d'usage VTC
```python
# Calculer heures de travail
minutes_total = 485
heures = minutes_total // 60  # 8 heures
minutes_restantes = minutes_total % 60  # 5 minutes
print(f"{heures}h{minutes_restantes}min")  # 8h5min

# Calculer commission
tarif = 25.0
commission = tarif * 0.15  # 3.75€
```

---

## 🔬 2. MODULE MATH (Avancé)
```python
import math

math.sqrt(16)   # 4.0 (racine carrée)
math.pi         # 3.141592...
math.ceil(4.2)  # 5 (arrondi vers le haut)
math.floor(4.8) # 4 (arrondi vers le bas)
math.pow(2, 8)  # 256.0 (puissance)
math.abs(-5)    # 5 (valeur absolue)
```

---

## ➕ 3. OPÉRATEURS D'ASSIGNATION

| Opérateur | Équivalent | Exemple | Résultat |
|-----------|------------|---------|----------|
| `=` | Assignation | `x = 5` | `x = 5` |
| `+=` | x = x + n | `x += 3` | `x = 8` |
| `-=` | x = x - n | `x -= 3` | `x = 2` |
| `*=` | x = x * n | `x *= 3` | `x = 15` |
| `/=` | x = x / n | `x /= 2` | `x = 2.5` |
| `//=` | x = x // n | `x //= 2` | `x = 2` |
| `%=` | x = x % n | `x %= 3` | `x = 2` |
| `**=` | x = x ** n | `x **= 2` | `x = 25` |

### Exemple pratique
```python
# Compteur de courses
courses = 0
courses += 1  # courses = 1
courses += 1  # courses = 2

# Cumuler revenus
revenus = 0
revenus += 25.50  # Ajouter course
revenus += 18.00  # Ajouter course
print(f"Total : {revenus}€")  # 43.50€
```

---

## ⚖️ 4. OPÉRATEURS DE COMPARAISON

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `==` | Égal à | `5 == 5` | `True` |
| `!=` | Différent de | `5 != 3` | `True` |
| `>` | Supérieur à | `5 > 3` | `True` |
| `<` | Inférieur à | `5 < 3` | `False` |
| `>=` | Supérieur ou égal | `5 >= 5` | `True` |
| `<=` | Inférieur ou égal | `5 <= 3` | `False` |

### Retournent toujours True ou False
```python
age = 25
print(age >= 18)  # True
print(age == 30)  # False
```

---

## 🔍 5. DIFFÉRENCE is vs ==

### == : Compare les VALEURS
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (mêmes valeurs)
```

### is : Compare l'IDENTITÉ (même objet en mémoire)
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False (objets différents en mémoire)

# Exception : petits entiers et None
x = None
print(x is None)  # True (usage recommandé pour None)
```

### Règle pratique
```python
# ✅ Utiliser == pour comparer valeurs
if age == 18:
    print("Majeur")

# ✅ Utiliser is pour None
if resultat is None:
    print("Pas de résultat")

# ❌ Ne jamais utiliser is pour comparer valeurs
if age is 18:  # Mauvaise pratique !
    print("Majeur")
```

---

## 📊 Scores

- **Quiz 10 (Opérateurs math) :** 4/4 (100%) ✅
- **Quiz 11 (Assignation + Comparaison) :** 4/4 (100%) ✅
- **Moyenne : 100%** 🏆

---

## ✅ Section validée le 16 février 2026

**Prêt pour Section 19 : Formatage**