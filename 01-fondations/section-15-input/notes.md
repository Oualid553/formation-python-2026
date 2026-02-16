# Section 15 - Interagir avec l'utilisateur (input)

**Date début :** 16 février 2026  
**Date fin :** 16 février 2026  
**Temps total :** ~30 min  
**Statut :** ✅ Validée

---

## 📚 La fonction `input()`

### Définition

`input()` permet de demander une saisie à l'utilisateur et récupérer sa réponse.

### Syntaxe
```python
variable = input("Question à poser : ")
```

**Important :** L'espace après le `:` dans la question améliore la lisibilité.

---

## 💻 Utilisation de base

### Exemple simple
```python
prenom = input("Quel est votre prénom ? ")
print(f"Bonjour {prenom} !")
```

**Exécution :**
```
Quel est votre prénom ? Oualid
Bonjour Oualid !
```

### Plusieurs inputs
```python
prenom = input("Prénom : ")
ville = input("Ville : ")
age = input("Âge : ")

print(prenom)
print(ville)
print(age)
```

---

## ⚠️ POINT CRITIQUE : input() retourne TOUJOURS une chaîne (str)

### Le piège classique
```python
age = input("Ton âge : ")  # Utilisateur tape 25
print(type(age))  # <class 'str'> → "25" pas 25 !

# ❌ ERREUR si on veut calculer
dans_10_ans = age + 10  # TypeError: can't add str + int
```

### Solution : Convertir en nombre
```python
# ✅ CORRECT
age = int(input("Ton âge : "))
dans_10_ans = age + 10
print(f"Dans 10 ans : {dans_10_ans}")
```

---

## 🔢 Conversion selon le besoin

### Pour un nombre entier
```python
age = int(input("Âge : "))
nb_courses = int(input("Nombre de courses : "))
```

### Pour un nombre décimal
```python
distance = float(input("Distance (km) : "))
prix = float(input("Prix : "))
```

### Pour du texte (par défaut)
```python
nom = input("Nom : ")
ville = input("Ville : ")
# Pas besoin de str(), c'est déjà une chaîne !
```

---

## 💡 Quand convertir ?

### ❌ PAS BESOIN de conversion si :

- Tu affiches juste la valeur
- Tu concatènes avec d'autres textes
- Pas de calcul mathématique
```python
age = input("Âge : ")
print(f"Tu as {age} ans")  # OK même si str
```

### ✅ CONVERSION OBLIGATOIRE si :

- Calculs mathématiques
- Comparaisons numériques
```python
age = int(input("Âge : "))
if age >= 18:
    print("Majeur")
```

---

## 🎯 Bonnes pratiques

### 1. Messages clairs et explicites
```python
# ✅ BIEN
prenom = input("Entrez votre prénom : ")

# ❌ PAS CLAIR
x = input("? ")
```

### 2. Ajouter un espace après la question
```python
# ✅ BIEN (espace avant ")
input("Nom : ")
# Nom : Oualid
#       ↑ espace naturel

# ❌ SANS ESPACE
input("Nom:")
# Nom:Oualid
#     ↑ collé
```

### 3. Convertir au bon moment
```python
# ✅ BIEN : conversion immédiate
age = int(input("Âge : "))

# ✅ BIEN AUSSI : conversion plus tard si besoin
age_str = input("Âge : ")
# ... du code ...
age = int(age_str)  # Conversion quand nécessaire
```

---

## 📋 Exemple complet
```python
# Calculateur d'âge dans X années

nom = input("Quel est votre nom ? ")
age = int(input("Quel est votre âge ? "))
annees = int(input("Dans combien d'années ? "))

age_futur = age + annees

print(f"{nom}, vous aurez {age_futur} ans dans {annees} ans.")
```

**Exécution :**
```
Quel est votre nom ? Oualid
Quel est votre âge ? 36
Dans combien d'années ? 10
Oualid, vous aurez 46 ans dans 10 ans.
```

---

## 🎓 Concepts clés maîtrisés

- ✅ Fonction `input()` pour récupérer saisie utilisateur
- ✅ `input()` retourne TOUJOURS une chaîne (str)
- ✅ Conversion nécessaire pour calculs : `int()`, `float()`
- ✅ Messages clairs et explicites
- ✅ Différence entre affichage (pas besoin conversion) et calcul (conversion obligatoire)

---

## ✅ Exercices complétés

- [x] Exercice 2 : Récupérer saisie utilisateur (100%)

---

## 📊 Résultat

**Exercice :** 1/1 (100%) ✅

**Code fonctionnel et propre**

---

## 💭 Réflexion personnelle

> "Petite panique au début pendant 10 secondes puis rappel avec assurance. Relativement simple au final."

**Excellente progression !** La réactivité s'améliore. 💪

---

## 🎓 Section validée le 16 février 2026