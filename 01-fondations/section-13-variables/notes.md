# Section 13 - Les variables

**Date début :** 15 février 2026  
**Date fin :** 15 février 2026  
**Temps total :** ~2h  
**Statut :** ✅ Validée

---

## 📚 Qu'est-ce qu'une variable ?

### Définition

Une variable est un **nom** qui référence un **objet** en mémoire.

**En Python :**
- Les objets existent d'abord en mémoire
- Les variables sont des "étiquettes" sur ces objets
- Différent d'autres langages où la variable "contient" la valeur

### Exemple
```python
age = 36

# Ce qui se passe :
# 1. Python crée l'objet 36 en mémoire
# 2. Python crée le nom "age"
# 3. Python fait pointer "age" vers l'objet 36
```

---

## 🎯 Objets et noms (concept important)

### Plusieurs noms peuvent pointer vers le même objet
```python
a = 5
b = a  # b pointe vers le MÊME objet que a

# Mais si on réaffecte :
a = 10  # a pointe maintenant vers un NOUVEL objet
# b pointe toujours vers l'objet 5
```

### Affectation = copie de VALEUR, pas lien permanent
```python
a = 3
b = 6
a = b    # a prend la VALEUR de b (6)
b = 7    # b change, mais a reste à 6 !

print(a)  # 6
print(b)  # 7
```

---

## 🔤 Règles de nommage

### ✅ AUTORISÉ

- **Lettres** : `a-z`, `A-Z`
- **Chiffres** : `0-9` (SAUF au début)
- **Underscore** : `_`

**Exemples valides :**
```python
age = 36
prenom = "Oualid"
prix_total = 45.50
distance_km = 12.8
a1 = 10
_variable = 5  # Commence par underscore OK
variable_ = 5  # Finit par underscore OK
```

---

### ❌ INTERDIT

**Espaces :**
```python
nombre impair = 3  # ❌ ERREUR
```

**Commence par un chiffre :**
```python
3a = 15  # ❌ ERREUR
```

**Caractères spéciaux :**
```python
prix@total = 50     # ❌ ERREUR
%taux = 10          # ❌ ERREUR
prix-total = 50     # ❌ ERREUR (tiret interdit)
```

**Mots-clés Python réservés :**
```python
print = "Python"  # ❌ ERREUR (mot-clé)
if = 5            # ❌ ERREUR (mot-clé)
for = 10          # ❌ ERREUR (mot-clé)
class = "test"    # ❌ ERREUR (mot-clé)
```

---

## 📏 Conventions PEP 8 (bonnes pratiques)

### Variables en minuscules
```python
# ✅ BIEN
age = 36
prenom = "Oualid"

# ❌ À ÉVITER (mais valide)
Age = 36
PRENOM = "Oualid"
```

### Mots multiples avec underscore
```python
# ✅ BIEN (snake_case)
compte_en_banque = 1000
prix_total = 45.50
distance_km = 12.8

# ❌ À ÉVITER
compteEnBanque = 1000  # camelCase (pas Python)
PrixTotal = 45.50      # PascalCase (réservé aux classes)
```

### Noms explicites
```python
# ✅ BIEN
prix_course = 45.50
distance_parcourue = 12.8

# ❌ À ÉVITER
p = 45.50      # Trop court, pas clair
x = 12.8       # Pas explicite
```

**Exception :** Variables temporaires courtes OK dans boucles (`i`, `j`, `k`)

---

## 🔄 Types d'affectations

### Affectation simple
```python
age = 36
```

### Affectation parallèle (plusieurs variables en une ligne)
```python
a, b = 1, 2  # a vaut 1, b vaut 2
x, y, z = 10, 20, 30
```

### Affectation multiple (même valeur à plusieurs variables)
```python
a = b = c = 0  # Toutes valent 0
x = y = 100
```

---

## 💡 Points importants à retenir

### Python est sensible à la casse
```python
Age = 36
age = 30

# Ce sont 2 variables DIFFÉRENTES !
```

### Singleton et Small Integer Caching

**Concept avancé (juste pour info) :**
- Python réutilise certains objets (petits entiers -5 à 256, True, False, None)
- Optimisation mémoire
- N'affecte pas ton code au quotidien
```python
a = 10
b = 10
# a et b pointent vers le MÊME objet 10 en mémoire (cache)

x = 1000
y = 1000
# x et y pointent vers des objets DIFFÉRENTS (hors cache)
```

---

## 🎯 Concepts clés maîtrisés

- ✅ Variable = nom qui référence un objet
- ✅ Affectation copie la valeur (pas de lien permanent)
- ✅ Règles de nommage (lettres, chiffres, underscore)
- ✅ Conventions PEP 8 (minuscules, snake_case, noms explicites)
- ✅ Python sensible à la casse
- ✅ Mots-clés réservés interdits
- ✅ Affectations : simple, parallèle, multiple

---

## ✅ Exercices complétés

- [x] Exercice 4 : Déclarer variables (100%)
- [x] Exercice 5 : Corriger erreur guillemets (100%)
- [x] Exercice 6 : Variables valides uniquement (100%)
- [x] Exercice 7 : Valeur d'une variable (100%)

---

## 📊 Scores Quiz

**Udemy :**
- Quiz 6 (Introduction) : 5/7 (71%)
- Quiz 7 (Variables) : 6/7 (86%)
- **Total : 11/14 (79%)**

**Moyenne : 79%**

**Points à revoir :**
- Affectations multiples/parallèles
- Singleton et caching (concept avancé)

---

## 🎓 Section validée le 15 février 2026