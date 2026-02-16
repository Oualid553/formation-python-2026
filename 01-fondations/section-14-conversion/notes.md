# Section 14 - Conversion de types

**Date début :** 15 février 2026  
**Date fin :** 15 février 2026  
**Temps total :** ~1h  
**Statut :** ✅ Validée

---

## 📚 Python : dynamique et fortement typé

### Python est DYNAMIQUE

On ne déclare pas le type des variables, Python le déduit automatiquement.
```python
# Pas besoin de déclarer le type
a = 10       # Python sait que c'est un int
a = "texte"  # On peut changer le type (dynamique)
```

### Python est FORTEMENT TYPÉ

Pas de conversion automatique entre types incompatibles.
```python
# ❌ ERREUR : pas de conversion automatique
"10" + 5  # TypeError

# ✅ CORRECT : conversion explicite obligatoire
"10" + str(5)   # "105" (concaténation)
int("10") + 5   # 15 (addition)
```

---

## 🔧 Fonctions de conversion

### `str()` - Convertir en chaîne de caractères
```python
age = 36
age_str = str(age)  # "36"

prix = 45.50
prix_str = str(prix)  # "45.5"

actif = True
actif_str = str(actif)  # "True"
```

**Utilité :** Affichage, concaténation avec d'autres chaînes

---

### `int()` - Convertir en nombre entier
```python
# Depuis chaîne
prix_str = "45"
prix_int = int(prix_str)  # 45

# Depuis float (tronque, pas arrondit)
distance = 12.8
distance_int = int(distance)  # 12 (pas 13 !)

# Depuis bool
int(True)   # 1
int(False)  # 0
```

**⚠️ Attention :**
```python
int("45.5")  # ❌ ERREUR ValueError
int(float("45.5"))  # ✅ OK → 45
```

---

### `float()` - Convertir en nombre décimal
```python
# Depuis chaîne
distance = "12.5"
distance_float = float(distance)  # 12.5

# Depuis int
age = 36
age_float = float(age)  # 36.0

# Depuis bool
float(True)   # 1.0
float(False)  # 0.0
```

---

### `bool()` - Convertir en booléen
```python
# Valeurs "fausses" (False)
bool(0)       # False
bool(0.0)     # False
bool("")      # False (chaîne vide)
bool(None)    # False

# Toutes les autres valeurs (True)
bool(1)       # True
bool(-5)      # True
bool(42)      # True
bool("texte") # True
bool(" ")     # True (espace = pas vide)
```

---

## 🔗 Concaténation vs Addition

### Concaténation (texte)

Le `+` entre chaînes = coller bout à bout
```python
prenom = "Oualid"
nom = "Kassi"
nom_complet = prenom + " " + nom  # "Oualid Kassi"

# Les espaces ne sont PAS automatiques
"Hello" + "World"  # "HelloWorld"
"Hello" + " " + "World"  # "Hello World"
```

### Addition (nombres)

Le `+` entre nombres = calcul mathématique
```python
a = 10
b = 5
total = a + b  # 15
```

### ❌ Impossible de mélanger
```python
# ❌ ERREUR
"Prix: " + 45  # TypeError

# ✅ SOLUTIONS
"Prix: " + str(45)     # "Prix: 45" (tout en texte)
int("10") + 5          # 15 (tout en nombre)
```

---

## 📐 Ordre des opérations

Python calcule ce qui est entre parenthèses d'abord.
```python
# Calcul d'abord, puis conversion
resultat = "Total: " + str(10 + 5)
# 1. 10 + 5 = 15
# 2. str(15) = "15"
# 3. "Total: " + "15" = "Total: 15"

# Sans parenthèses
resultat = str(10) + str(5)  # "105" (pas 15 !)
```

---

## 🔍 Fonction `type()` - Rappel

Vérifier le type d'une variable :
```python
a = 10
print(type(a))  # <class 'int'>

a = str(a)
print(type(a))  # <class 'str'>
```

---

## 💡 Points importants à retenir

### Python = fortement typé
```python
# ❌ Pas de conversion automatique
"10" + 5  # ERREUR

# ✅ Conversion explicite obligatoire
"10" + str(5)  # OK
int("10") + 5  # OK
```

### Concaténation nécessite des chaînes
```python
nom = "Pierre"
age = 20

# ❌ ERREUR
message = "J'ai " + age + " ans"

# ✅ CORRECT
message = "J'ai " + str(age) + " ans"
# Ou mieux avec f-string (vu plus tard)
message = f"J'ai {age} ans"
```

### Conversions peuvent échouer
```python
int("abc")     # ❌ ValueError
int("45.5")    # ❌ ValueError
float("abc")   # ❌ ValueError

# ✅ Vérifier avant de convertir (vu plus tard)
```

---

## 🎯 Concepts clés maîtrisés

- ✅ Python dynamique (pas de déclaration de type)
- ✅ Python fortement typé (conversion explicite requise)
- ✅ Fonctions de conversion : `str()`, `int()`, `float()`, `bool()`
- ✅ Différence concaténation (texte) vs addition (nombres)
- ✅ Ordre des opérations avec parenthèses
- ✅ Impossibilité de mélanger str + int sans conversion

---

## ✅ Exercices complétés

- [x] Exercice 8 : Convertir variable (100%)
- [x] Exercice 9 : Concaténer variables (100%)
- [x] Exercice 1 : La concaténation (100%)

---

## 📊 Scores Quiz

**Udemy :**
- Quiz 8 : 5/5 (100%) ✅

**Exercices :** 3/3 (100%)

**Score global Section 14 : 100%**

---

## 🎓 Section validée le 15 février 2026