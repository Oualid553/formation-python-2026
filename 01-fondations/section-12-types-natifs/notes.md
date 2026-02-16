# Section 12 - Les types natifs

**Date début :** 15 février 2026  
**Date fin :** 15 février 2026  
**Temps total :** ~1h30  
**Statut :** ✅ Validée

---

## 📚 Les 4 types natifs de base

### 1. **str** (string - chaîne de caractères)

Représente du texte.
```python
nom = "Oualid"
ville = 'Alger'
description = """Chauffeur VTC
en reconversion"""

print(type(nom))  # <class 'str'>
```

**Points clés :**
- Guillemets simples `'...'` ou doubles `"..."` (équivalents)
- Triple guillemets `"""..."""` pour texte multi-lignes
- Caractères échappés : `\'`, `\"`, `\n`

---

### 2. **int** (integer - nombre entier)

Représente un nombre entier (sans virgule).
```python
age = 36
annees_vtc = 5
temperature = -10

print(type(age))  # <class 'int'>
```

**Points clés :**
- Positif ou négatif
- Pas de limite de taille (Python gère automatiquement)
- Pas de virgule/point décimal

---

### 3. **float** (nombre décimal)

Représente un nombre à virgule flottante.
```python
prix_course = 45.50
distance_km = 12.8
pi = 3.14159

print(type(prix_course))  # <class 'float'>
```

**Points clés :**
- Utilise le point `.` (pas la virgule)
- Précision limitée (15-17 chiffres significatifs)
- Peut avoir notation scientifique : `1.5e3` = 1500.0

---

### 4. **bool** (boolean - booléen)

Représente une valeur de vérité : vrai ou faux.
```python
est_disponible = True
client_satisfait = False

print(type(est_disponible))  # <class 'bool'>
```

**Points clés :**
- Seulement 2 valeurs possibles : `True` et `False`
- **Majuscules obligatoires** (pas `true`/`false`)
- Résultat des comparaisons : `age > 18` → `True` ou `False`

---

## 🔧 Fonctions importantes

### Fonction `type()` - Vérifier le type
```python
variable = 42
print(type(variable))  # <class 'int'>

variable = "texte"
print(type(variable))  # <class 'str'>
```

**Utilité :** Savoir quel type de données on manipule

---

### Fonctions de conversion

**Convertir en chaîne :**
```python
age = 36
age_str = str(age)  # "36"
```

**Convertir en entier :**
```python
prix = "45"
prix_int = int(prix)  # 45
```

**Convertir en décimal :**
```python
distance = "12.5"
distance_float = float(distance)  # 12.5
```

**Convertir en booléen :**
```python
valeur = bool(1)  # True
valeur = bool(0)  # False
```

---

## 💡 Points importants à retenir

### Python compare les VALEURS, pas les TYPES
```python
a = 10      # int
b = 10.0    # float

print(a == b)  # True (même valeur)
print(type(a) == type(b))  # False (types différents)
```

### `input()` retourne TOUJOURS une chaîne
```python
age = input("Ton âge : ")  # age est un str !

# Pour faire des calculs :
age = int(input("Ton âge : "))  # Convertir en int
```

### Impossible de mélanger str + int
```python
"10" + 5  # ❌ ERREUR TypeError

# Solutions :
"10" + str(5)   # ✅ "105" (concaténation)
int("10") + 5   # ✅ 15 (addition)
```

---

## 🎯 Concepts clés maîtrisés

- ✅ Les 4 types natifs : str, int, float, bool
- ✅ Fonction `type()` pour identifier le type
- ✅ Conversions avec `int()`, `float()`, `str()`, `bool()`
- ✅ Différence entre int (entier) et float (décimal)
- ✅ Booléens en Python (True/False avec majuscules)
- ✅ Gestion guillemets/apostrophes dans les chaînes
- ✅ Python fortement typé (pas de conversion automatique)

---

## ✅ Exercices complétés

- [x] Exercice 1 : Créer des objets natifs (100%)
- [x] Exercice 2 : Corriger erreurs chaînes (100%)
- [x] Exercice 3 : Corriger variables (100%)

---

## 📊 Scores Quiz

**Udemy :**
- Quiz 3 (Chaînes) : 5/5 (100%)
- Quiz 4 (Booléens) : 3/3 (100%)
- Quiz 5 (Types natifs) : 7/7 (100%)
- **Total : 15/15 (100%)**

**Claude :**
- Score : 9.65/12 (80.4%)
- **Statut : Validée** ✅

---

## 🎓 Section validée le 15 février 2026

