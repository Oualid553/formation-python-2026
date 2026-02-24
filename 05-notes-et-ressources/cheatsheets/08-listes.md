# Cheatsheet : Les Listes

**Section 24 - Les Listes**
**Date :** 23 février 2026

---

## 📝 CRÉER UNE LISTE

```python
# Liste vide
ma_liste = []

# Liste avec éléments
nombres = [1, 2, 3, 4, 5]
langages = ["Python", "Java", "C++"]
mixte = [1, "deux", 3.0, True]

# Liste imbriquée
matrice = [[1, 2], [3, 4], [5, 6]]
```

---

## 🔍 ACCÉDER AUX ÉLÉMENTS

```python
ma_liste = ["A", "B", "C", "D", "E"]

# Par index positif (commence à 0)
ma_liste[0]    # "A" (premier)
ma_liste[1]    # "B" (deuxième)
ma_liste[4]    # "E" (cinquième)

# Par index négatif (depuis la fin)
ma_liste[-1]   # "E" (dernier)
ma_liste[-2]   # "D" (avant-dernier)

# Longueur
len(ma_liste)  # 5
```

---

## ✏️ MODIFIER UN ÉLÉMENT

```python
ma_liste = [1, 2, 3]

# Modifier par index
ma_liste[0] = 10
# Résultat : [10, 2, 3]
```

---

## ➕ AJOUTER DES ÉLÉMENTS

```python
ma_liste = [1, 2, 3]

# Ajouter à la FIN
ma_liste.append(4)
# Résultat : [1, 2, 3, 4]

# Ajouter à une POSITION précise
ma_liste.insert(0, 0)  # insert(index, element)
# Résultat : [0, 1, 2, 3, 4]

# Ajouter plusieurs éléments
ma_liste.extend([5, 6])
# Résultat : [0, 1, 2, 3, 4, 5, 6]
```

---

## ➖ ENLEVER DES ÉLÉMENTS

```python
ma_liste = ["A", "B", "C", "D"]

# Enlever par VALEUR (première occurrence)
ma_liste.remove("B")
# Résultat : ["A", "C", "D"]

# Enlever par INDEX et le retourner
element = ma_liste.pop(1)  # Enlève "C"
# element = "C"
# Résultat : ["A", "D"]

# Enlever le DERNIER élément
dernier = ma_liste.pop()
# dernier = "D"
# Résultat : ["A"]

# Vider complètement la liste
ma_liste.clear()
# Résultat : []
```

---

## 🔪 SLICES (Tranches)

### Syntaxe : `liste[début:fin:pas]`
- **début** : INCLUS
- **fin** : EXCLU
- **pas** : intervalle (optionnel)

```python
liste = [0, 1, 2, 3, 4, 5]

# Les 3 premiers
liste[:3]      # [0, 1, 2]

# Les 3 derniers
liste[-3:]     # [3, 4, 5]

# Du 2ème au 4ème
liste[1:4]     # [1, 2, 3]

# Tous sauf premier et dernier
liste[1:-1]    # [1, 2, 3, 4]

# Un élément sur deux
liste[::2]     # [0, 2, 4]

# Inverser
liste[::-1]    # [5, 4, 3, 2, 1, 0]

# Copier une liste
copie = liste[:]
```

---

## 🔄 AUTRES MÉTHODES UTILES

```python
ma_liste = [3, 1, 4, 1, 5]

# Trier (modifie la liste)
ma_liste.sort()
# Résultat : [1, 1, 3, 4, 5]

# Trier à l'envers
ma_liste.sort(reverse=True)
# Résultat : [5, 4, 3, 1, 1]

# Inverser l'ordre
ma_liste.reverse()
# Résultat : [1, 1, 3, 4, 5]

# Compter occurrences
ma_liste.count(1)  # 2

# Trouver l'index d'un élément
ma_liste.index(3)  # 2
```

---

## 🔗 LISTES ↔ STRINGS

```python
# String → Liste (split)
texte = "a,b,c"
liste = texte.split(",")
# Résultat : ["a", "b", "c"]

# Liste → String (join)
liste = ["a", "b", "c"]
texte = ",".join(liste)
# Résultat : "a,b,c"

# Attention : join() uniquement avec des strings !
nombres = [1, 2, 3]
# ",".join(nombres)  # ❌ ERREUR
",".join(str(n) for n in nombres)  # ✅ "1,2,3"
```

---

## ✅ OPÉRATEUR IN (Appartenance)

```python
ma_liste = [1, 2, 3, 4, 5]

# Vérifier présence
3 in ma_liste       # True
10 in ma_liste      # False

# Vérifier absence
10 not in ma_liste  # True
```

---

## 📦 LISTES IMBRIQUÉES

```python
matrice = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Accès niveau 1
matrice[0]      # [1, 2, 3]

# Accès niveau 2
matrice[0][1]   # 2

# Longueur
len(matrice)    # 3 (3 sous-listes)
len(matrice[0]) # 3 (3 éléments dans la 1ère sous-liste)

# IMPORTANT : Une sous-liste = 1 seul élément !
liste = [1, [2, 3], 4]
len(liste)      # 3 (pas 4 !)
```

---

## 🎯 TUPLES (Listes immuables)

```python
# Création
mon_tuple = (1, 2, 3)
singleton = (1,)  # Virgule obligatoire pour 1 élément

# Accès (comme les listes)
mon_tuple[0]    # 1

# MAIS : Impossible de modifier
# mon_tuple[0] = 10  # ❌ ERREUR TypeError

# Conversion
liste = list(mon_tuple)  # Tuple → Liste
tuple(liste)             # Liste → Tuple
```

---

## ⚠️ PIÈGES COURANTS

```python
# 1. append() retourne None !
ma_liste = [1, 2, 3]
nouvelle = ma_liste.append(4)  # ❌ nouvelle = None !
ma_liste.append(4)              # ✅ Modifie directement

# 2. remove() cherche la VALEUR, pas l'index
ma_liste = ["A", "B", "C"]
ma_liste.remove(1)   # ❌ Cherche le NOMBRE 1 (erreur)
ma_liste.remove("B") # ✅ Cherche la chaîne "B"

# 3. Slice [début:fin] → fin est EXCLU
liste = [0, 1, 2, 3, 4]
liste[0:3]   # [0, 1, 2] (pas 3 !)

# 4. Copie vs référence
a = [1, 2, 3]
b = a        # b pointe vers la même liste !
b[0] = 10    # a devient [10, 2, 3] aussi !
c = a[:]     # c est une COPIE indépendante ✅
```

---

## 📊 SCORES SECTION 24

**Quiz 19 :** 4/4 (100%) ✅  
**Quiz 20 :** 2/2 (100%) ✅  
**Quiz 21 :** 2/3 (67%) - Piège sous-liste = 1 élément  
**Exercice 19 :** 100% ✅  
**Exercice 20 :** 100% ✅
