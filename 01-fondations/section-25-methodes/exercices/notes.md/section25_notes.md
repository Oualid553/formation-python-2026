# Section 25 - Les Méthodes et Fonctions Utiles sur les Listes

**Date :** 23-24 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~2h

---

## 📚 Contenu

- Vidéo 172 : La différence entre méthodes et fonctions (3 min)
- Vidéo 173 : Les objets muables et immuables (2 min)
- Vidéo 174 : Quelques fonctions supplémentaires (3 min)
- Vidéo 175 : La fonction range avec Python 3 (1 min)
- Quiz 22 : Les méthodes et fonctions
- Exercice 5 : Vérifier la validité d'un mot de passe ✅

---

## 🔑 1. MÉTHODES vs FONCTIONS (Vidéo 172)

### Méthode
**Syntaxe :** `objet.methode()`  
**Exemple :**
```python
ma_liste = [1, 2, 3]
ma_liste.append(4)  # Méthode sur l'objet liste

texte = "bonjour"
texte.upper()       # Méthode sur l'objet string
```

**→ Appartient à un objet spécifique**

### Fonction
**Syntaxe :** `fonction(objet)`  
**Exemple :**
```python
ma_liste = [1, 2, 3]
len(ma_liste)       # Fonction qui prend la liste en argument

sorted(ma_liste)    # Fonction qui prend la liste en argument
```

**→ Indépendante, prend des arguments**

---

## 🔄 2. OBJETS MUABLES vs IMMUABLES (Vidéo 173)

### Objets MUABLES (Modifiables)
**Peuvent être modifiés après création**

```python
# LISTES - Muables ✅
ma_liste = [1, 2, 3]
ma_liste[0] = 10      # ✅ Possible
ma_liste.append(4)    # ✅ Possible
# Résultat : [10, 2, 3, 4]

# DICTIONNAIRES - Muables ✅
mon_dico = {"a": 1}
mon_dico["a"] = 2     # ✅ Possible
```

### Objets IMMUABLES (Non modifiables)
**Ne peuvent PAS être modifiés après création**

```python
# STRINGS - Immuables ❌
texte = "bonjour"
texte[0] = "B"        # ❌ TypeError !
# Solution : Créer une nouvelle string
texte = "B" + texte[1:]  # "Bonjour"

# TUPLES - Immuables ❌
mon_tuple = (1, 2, 3)
mon_tuple[0] = 10     # ❌ TypeError !

# NOMBRES - Immuables ❌
nombre = 5
nombre += 1           # Crée un NOUVEAU nombre, pas modification
```

**→ Modification = Création d'un nouvel objet !**

---

## 🛠️ 3. FONCTIONS SUPPLÉMENTAIRES (Vidéo 174)

### len() - Longueur
```python
len([1, 2, 3])        # 3
len("bonjour")        # 7
len({"a": 1, "b": 2}) # 2
```

### min() / max() - Minimum / Maximum
```python
min([3, 1, 4, 2])     # 1
max([3, 1, 4, 2])     # 4

min("bonjour")        # "b" (ordre alphabétique)
max("bonjour")        # "u"
```

### sum() - Somme (uniquement nombres)
```python
sum([1, 2, 3, 4])     # 10
sum([1.5, 2.5, 3])    # 7.0
```

### round() - Arrondir
```python
round(3.7)            # 4
round(3.14159, 2)     # 3.14 (2 décimales)
```

### sorted() - Trier (retourne nouvelle liste)
```python
liste = [3, 1, 4, 2]
sorted(liste)         # [1, 2, 3, 4]
# liste reste [3, 1, 4, 2] (inchangée)

sorted(liste, reverse=True)  # [4, 3, 2, 1]
```

---

## 🔢 4. FONCTION range() (Vidéo 175)

### Syntaxe
```python
range(stop)           # De 0 à stop-1
range(start, stop)    # De start à stop-1
range(start, stop, step)  # Avec un pas
```

### Exemples
```python
range(5)              # 0, 1, 2, 3, 4
range(2, 7)           # 2, 3, 4, 5, 6
range(0, 10, 2)       # 0, 2, 4, 6, 8
range(10, 0, -1)      # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### ⚠️ Python 3 : range() retourne un objet, pas une liste
```python
# Python 3
interval = range(10)
print(interval)       # range(0, 10) (pas une liste !)
print(type(interval)) # <class 'range'>

# Attributs accessibles
interval.start        # 0
interval.stop         # 10
interval.step         # 1

# Convertir en liste
liste = list(range(10))
print(liste)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**→ Utilisé principalement avec les boucles `for` (Section 26) !**

---

## 📊 Scores

| Élément | Score |
|---------|-------|
| Quiz 22 | ? |
| Exercice 5 | 100% ✅ |

---

## 💡 Concepts clés maîtrisés

### Exercice 5 - Validation mot de passe
**Compétences démontrées :**
- ✅ Structures conditionnelles (`if/elif/else`)
- ✅ Fonction `len()`
- ✅ Méthodes de casse (`.upper()`, `.title()`, `.capitalize()`)
- ✅ Méthode `.isdigit()`
- ✅ Ordre logique des conditions (cas spécifique d'abord)
- ✅ Analyse sur papier avant de coder

**Différence retenue :**
```python
# title() - Chaque Mot
"bonjour tout le monde".title()
# "Bonjour Tout Le Monde"

# capitalize() - Seulement première lettre
"bonjour tout le monde".capitalize()
# "Bonjour tout le monde"
```

---

## 📋 Résumé

| Concept | Type | Exemple |
|---------|------|---------|
| **Méthode** | `objet.methode()` | `liste.append(x)` |
| **Fonction** | `fonction(objet)` | `len(liste)` |
| **Muable** | Modifiable | Liste, Dictionnaire |
| **Immuable** | Non modifiable | String, Tuple, Nombre |

---

## ✅ Section validée le 24 février 2026

**Prêt pour Section 26 : Les boucles ⭐ SECTION CRITIQUE**