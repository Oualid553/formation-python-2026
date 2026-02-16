# Section 14 - Conversion de types

**Date début :** 15 février 2026  
**Date fin :** 15 février 2026  
**Temps total :** ~1h  
**Statut :** ✅ Validée

---

## 📚 Concepts clés

### Python : dynamique et fortement typé

**Dynamique :**
- Pas besoin de déclarer le type d'une variable
- Le type peut changer pendant l'exécution
```python
a = 10       # a est un int
a = "texte"  # a devient un str (OK en Python)
```

**Fortement typé :**
- Python ne fait PAS de conversion automatique
- Impossible de mélanger les types sans conversion explicite
```python
# ❌ ERREUR
"Prix : " + 45  # TypeError: can't concatenate str and int

# ✅ SOLUTION
"Prix : " + str(45)  # Conversion explicite
```

---

## 🔧 Fonctions de conversion

### str() - Convertir en chaîne de caractères

**Usage :** Transformer n'importe quoi en texte
```python
age = 36
age_texte = str(age)  # 36 → "36"

prix = 45.50
prix_texte = str(prix)  # 45.5 → "45.5"

actif = True
actif_texte = str(actif)  # True → "True"
```

**Quand l'utiliser :**
- Pour concaténer avec du texte
- Pour afficher des nombres dans une phrase
- Pour enregistrer dans un fichier texte

---

### int() - Convertir en entier

**Usage :** Transformer en nombre entier
```python
prix_texte = "45"
prix_nombre = int(prix_texte)  # "45" → 45

# Conversion avec perte de décimales
decimal = 45.99
entier = int(decimal)  # 45.99 → 45 (troncature)
```

**Attention :**
```python
# ✅ OK
int("42")      # 42
int("  42  ")  # 42 (espaces supprimés)

# ❌ ERREUR
int("42.5")    # ValueError (pas de décimales)
int("quarante-deux")  # ValueError
```

---

### float() - Convertir en décimal

**Usage :** Transformer en nombre à virgule
```python
distance_texte = "12.5"
distance = float(distance_texte)  # "12.5" → 12.5

entier = 10
decimal = float(entier)  # 10 → 10.0
```

---

### bool() - Convertir en booléen

**Valeurs "fausses" (False) :**
- `0` (zéro)
- `""` (chaîne vide)
- `[]` (liste vide)
- `None`

**Valeurs "vraies" (True) :**
- Tout le reste !
```python
bool(1)      # True
bool(0)      # False
bool("Oui")  # True
bool("")     # False
```

---

## 💡 Concaténation vs Addition

### Addition (nombres)
```python
10 + 5  # 15 (calcul mathématique)
```

### Concaténation (texte)
```python
"10" + "5"  # "105" (coller bout à bout)
```

### Erreur courante
```python
# ❌ ERREUR
"Le résultat est " + 15  # Types incompatibles

# ✅ Solution 1 : Conversion
"Le résultat est " + str(15)  # "Le résultat est 15"

# ✅ Solution 2 : f-string (recommandé)
resultat = 15
f"Le résultat est {resultat}"  # "Le résultat est 15"
```

---

## 🎯 Exemples pratiques

### Exemple 1 : Concaténer avec conversion
```python
nombre = 15
resultat = "Le nombre est " + str(nombre)
print(resultat)  # "Le nombre est 15"
```

---

### Exemple 2 : Créer une chaîne formatée
```python
a = 2
b = 6
c = 3
resultat = str(a) + " + " + str(b) + " + " + str(c)
print(resultat)  # "2 + 6 + 3"
```

**Explication :**
- `str(a)` → convertit 2 en "2"
- `" + "` → texte littéral " + "
- `+` entre les éléments → opérateur de concaténation

---

### Exemple 3 : Mélanger texte et calculs
```python
# Ligne complexe
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)
print(d)  # "L'addition de 10 + 5 est égal à 15"
```

**Ordre des opérations :**
1. `10 + 5` → calcul d'abord → `15`
2. `str(15)` → conversion → `"15"`
3. Concaténation finale → `"L'addition... 15"`

---

## 📊 Fonction type()

**Vérifier le type d'une variable :**
```python
a = 42
print(type(a))  # <class 'int'>

b = "42"
print(type(b))  # <class 'str'>

c = 42.0
print(type(c))  # <class 'float'>
```

---

## 💡 Points importants à retenir

### 1. Python = fortement typé

- Pas de conversion automatique
- `str + int` → ERREUR
- Conversion explicite OBLIGATOIRE

### 2. Les " + " dans les chaînes
```python
str(a) + " + " + str(b)
#        ^^^^^ 
#        Ceci est du TEXTE (chaîne)
#        Pas l'opérateur mathématique
```

### 3. Ordre des opérations
```python
str(10 + 5)  # Calcul d'abord (15), puis conversion ("15")
```

### 4. f-strings (alternative moderne)
```python
# Au lieu de :
"Prix : " + str(45) + " €"

# Utilise :
f"Prix : {45} €"  # Plus lisible !
```

---

## ✅ Exercices complétés

- [x] Exercice 8 : Convertir variable (100%)
- [x] Exercice 9 : Concaténer variables (100%)
- [x] Exercice 1 : La concaténation (100%)

---

## 📊 Scores Quiz

- Quiz 8 : 5/5 (100%) ✅

---

## 🎯 Points forts

- Conversions maîtrisées
- Logique de concaténation comprise
- Code identique à correction officielle

## 🔄 Difficultés rencontrées

- Exercice 9 : Comprendre que `" + "` est du texte (5 min)
- Exercice 1 ligne d : `str(10 + 5)` → ordre des opérations

---

## ✅ Section 14 VALIDÉE - Score parfait 100% !

**Prête pour Section 15 !**