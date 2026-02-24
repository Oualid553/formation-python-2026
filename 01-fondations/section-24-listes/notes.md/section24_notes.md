# Section 24 - Les Listes

**Date :** 23 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~3h

---

## 📊 Scores

| Quiz/Exercice | Score |
|---------------|-------|
| Quiz 19 | 4/4 (100%) |
| Quiz 20 | 2/2 (100%) |
| Quiz 21 | 2/3 (67%) |
| Exercice 19 | 100% |
| Exercice 20 | 100% |
| Exercice 21 | 100% |
| Exercice 22 | 100% (avec aide) |
| Quiz final | 6/7 (86%) |
| **Moyenne** | **94%** |

---

## 🔑 CONCEPTS MAÎTRISÉS

### 1. Créer et accéder
- Créer listes, tuples
- Accès par index (positif/négatif)
- Modifier éléments

### 2. Ajouter/Enlever
- `append()`, `insert()`, `extend()`
- `remove()`, `pop()`, `clear()`, `del`

### 3. Slices ⭐
- `[début:fin:pas]`
- Début INCLUS, fin EXCLU
- Index négatifs

### 4. Méthodes utiles
- `index()`, `count()`
- `sort()`, `reverse()`
- `sorted()` (fonction)

### 5. Liste ↔ String
- `split()` : String → Liste
- `join()` : Liste → String

### 6. Opérateurs
- `in`, `not in`
- `+` (concaténation), `*` (répétition)

### 7. Listes imbriquées
- Accès multi-niveaux
- `liste[0][1][2]`

### 8. Fonctions pratiques
- `len()`, `min()`, `max()`, `sum()`
- `range()`

---

## ⚠️ ERREURS COURANTES (Vidéo 170)

```python
# ❌ Parenthèses au lieu de crochets
ma_liste = [1, 2, 3]
ma_liste(0)  # TypeError !
ma_liste[0]  # ✅

# ❌ remove() avec index
ma_liste.remove(0)  # Enlève le NOMBRE 0, pas l'index 0 !
ma_liste.pop(0)     # ✅ Enlève l'élément à l'index 0

# ❌ remove() n'enlève que la 1ère occurrence
ma_liste = [3, 1, 2, 3]
ma_liste.remove(3)  # → [1, 2, 3] (pas [1, 2] !)

# ❌ append() retourne None
ma_liste = ma_liste.append(4)  # ma_liste = None !
ma_liste.append(4)              # ✅
```

---

## 💡 CONSEIL STRUCTURES DE DONNÉES

**Quelle structure choisir ?**

1. Besoin d'associer clé → valeur ? → **Dictionnaire**
2. Pas besoin de modifier ? → **Tuple**
3. Pas besoin de garder l'ordre ? → **Set**
4. Tous les autres cas ? → **Liste** ✅

---

## 📝 POINTS DE RÉVISION

### ⚠️ À revoir
- **Listes imbriquées** (Exercice 22 difficile)
- Créer exercices perso sur multi-niveaux

### ✅ Bien maîtrisé
- Slices (explications claires comprises)
- Opérateurs `in`/`not in`
- Méthodes `append`, `remove`, `pop`

---

## 🎯 EXERCICES SUPPLÉMENTAIRES RECOMMANDÉS

```python
# Pratiquer listes imbriquées :
data = [
    [1, 2, [3, 4]],
    [[5], 6],
    [7, [8, [9, 10]]]
]
# Récupérer : 3, 5, 9, 10
```

---

## ✅ Section validée le 23 février 2026

**Prêt pour Section 25 : Méthodes et fonctions utiles sur les listes**