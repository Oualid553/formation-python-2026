# Cheatsheet : Opérateurs

**Section 18 - Les Opérateurs**
**Date :** 16 février 2026

---

## 🔢 Opérateurs Mathématiques

| Opérateur | Action | Exemple | Résultat |
|-----------|--------|---------|----------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Soustraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (float) | `5 / 2` | `2.5` |
| `//` | Division entière | `5 // 2` | `2` |
| `%` | Modulo (reste) | `5 % 2` | `1` |
| `**` | Puissance | `5 ** 2` | `25` |
```python
10 / 2   # 5.0 (toujours float)
7 // 2   # 3 (arrondi vers le bas)
10 % 3   # 1 (reste)
2 ** 8   # 256
```

---

## ➕ Opérateurs d'Assignation

| Opérateur | Équivalent |
|-----------|------------|
| `x += n` | `x = x + n` |
| `x -= n` | `x = x - n` |
| `x *= n` | `x = x * n` |
| `x /= n` | `x = x / n` |
| `x //= n` | `x = x // n` |
| `x %= n` | `x = x % n` |
| `x **= n` | `x = x ** n` |

---

## ⚖️ Opérateurs de Comparaison

| Opérateur | Signification |
|-----------|---------------|
| `==` | Égal à |
| `!=` | Différent de |
| `>` | Supérieur à |
| `<` | Inférieur à |
| `>=` | Supérieur ou égal |
| `<=` | Inférieur ou égal |

**→ Retournent True ou False**

---

## 🔍 is vs ==
```python
# == : Compare les VALEURS
[1,2] == [1,2]  # True

# is : Compare l'IDENTITÉ (même objet mémoire)
[1,2] is [1,2]  # False

# Règle : is uniquement pour None
if resultat is None:
    print("Vide")
```

---

## 🔬 Module Math
```python
import math

math.sqrt(16)   # 4.0
math.pi         # 3.14159...
math.ceil(4.2)  # 5
math.floor(4.8) # 4
math.pow(2, 8)  # 256.0
```

---

**Score Quiz 10 :** 4/4 (100%) ✅
**Score Quiz 11 :** 4/4 (100%) ✅