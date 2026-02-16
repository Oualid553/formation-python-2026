# Section 12 - Les types natifs

**Date début :** 15 février 2026  
**Date fin :** 15 février 2026  
**Temps total :** ~1h30  
**Statut :** ✅ Validée

---

## 📚 Les 4 types de base en Python

### 1. str (string) - Chaîne de caractères

**Définition :** Texte, mot, phrase

**Exemples :**
```python
nom = "Oualid"
ville = 'Alger'
message = """Texte
sur plusieurs
lignes"""
```

**Points clés :**
- Guillemets simples `'...'` ou doubles `"..."`
- Triple guillemets `"""..."""` pour plusieurs lignes
- Échappement avec `\` : `'Je m\'appelle'`

---

### 2. int (integer) - Nombre entier

**Définition :** Nombre sans décimales

**Exemples :**
```python
age = 36
annees_vtc = 5
nombre_negatif = -10
```

**Points clés :**
- Pas de guillemets
- Peut être positif, négatif ou zéro
- Opérations : `+`, `-`, `*`, `/`, `//`, `%`, `**`

---

### 3. float - Nombre décimal

**Définition :** Nombre avec virgule (point en Python)

**Exemples :**
```python
prix = 45.50
distance = 12.8
pi = 3.14159
```

**Points clés :**
- Utilise le POINT `.` (pas la virgule)
- Plus précis que int pour les calculs
- Attention aux arrondis

---

### 4. bool (boolean) - Booléen

**Définition :** Vrai ou Faux uniquement

**Valeurs possibles :**
```python
True   # Vrai (avec majuscule !)
False  # Faux (avec majuscule !)
```

**Exemples :**
```python
est_majeur = True
client_satisfait = False
age_valide = age >= 18  # Retourne True ou False
```

**Points clés :**
- Seulement 2 valeurs : `True` et `False`
- ATTENTION aux majuscules (pas `true` ou `false`)
- Résultat des comparaisons : `>`, `<`, `==`, `!=`, `>=`, `<=`

---

## 🔧 Fonctions importantes

### Vérifier le type : `type()`
```python
age = 36
print(type(age))  # <class 'int'>

prix = 45.50
print(type(prix))  # <class 'float'>

nom = "Oualid"
print(type(nom))  # <class 'str'>

actif = True
print(type(actif))  # <class 'bool'>
```

---

### Convertir les types (constructeurs)

**int() - Convertir en entier**
```python
prix_texte = "45"
prix_nombre = int(prix_texte)  # "45" → 45
```

**float() - Convertir en décimal**
```python
distance_texte = "12.5"
distance_nombre = float(distance_texte)  # "12.5" → 12.5
```

**str() - Convertir en texte**
```python
age = 36
age_texte = str(age)  # 36 → "36"
```

**bool() - Convertir en booléen**
```python
valeur = bool(1)   # True
vide = bool(0)     # False
texte = bool("")   # False (chaîne vide)
```

---

## 💡 Points importants à retenir

### Comparaison de valeurs vs types
```python
a = 10       # int
b = 10.0     # float

print(a == b)           # True (valeurs identiques)
print(type(a) == type(b))  # False (types différents)
```

**→ Python compare les VALEURS, pas les TYPES**

---

### input() retourne TOUJOURS du texte
```python
age = input("Ton âge : ")  # age est un str !

# ❌ ERREUR
if age > 18:  # Impossible de comparer str et int

# ✅ CORRECT
age = int(input("Ton âge : "))  # Conversion en int
if age > 18:  # OK !
```

---

### Concaténation vs Addition
```python
# ❌ ERREUR - Types incompatibles
"Prix : " + 45  # str + int impossible

# ✅ Solution 1 : Tout en texte
"Prix : " + str(45)  # "Prix : 45"

# ✅ Solution 2 : f-string (plus propre)
prix = 45
f"Prix : {prix}"  # "Prix : 45"
```

---

### Guillemets et apostrophes
```python
# ❌ ERREUR
nom = 'Je m'appelle Pierre'  # L'apostrophe coupe la chaîne

# ✅ Solution 1 : Guillemets doubles
nom = "Je m'appelle Pierre"

# ✅ Solution 2 : Échappement
nom = 'Je m\'appelle Pierre'

# ✅ Solution 3 : Alterner
citation = 'Il a dit "Bonjour"'
```

---

## ✅ Exercices complétés

- [x] Exercice 1 : Créer des objets natifs (100%)
- [x] Exercice 2 : Corriger les erreurs chaînes (100%)
- [x] Exercice 3 : Corriger les variables (100%)

---

## 📊 Scores Quiz

**Udemy :**
- Quiz 3 (Chaînes) : 5/5 ✅
- Quiz 4 (Booléens) : 3/3 ✅
- Quiz 5 (Types natifs) : 7/7 ✅
- **Total : 15/15 (100%)**

**Quiz Claude :**
- Score : 9.65/12 (80.4%)
- **Statut : Validé** ✅

---

## 🎯 Points forts

- Types natifs maîtrisés
- Conversions comprises
- Gestion guillemets OK
- Détection d'erreurs

## 🔄 Points à revoir

- `input()` retourne toujours `str` (à retenir !)
- Optimisation code (petits détails)

---

## ✅ Section 12 VALIDÉE

**Prête pour Section 13 !**

