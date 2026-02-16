# Section 17 - Manipuler les chaînes de caractères

**Date début :** 16 février 2026  
**Date fin :** 16 février 2026  
**Temps total :** ~2h  
**Statut :** ✅ Validée

---

## 📚 Vue d'ensemble

Section DENSE avec 15+ méthodes pour manipuler les strings.

**Vidéos :** 10 (99-107)  
**Quiz :** 1 (Quiz 9 - 7/8 = 87.5%)  
**Exercices :** 4 (10-13)

---

## 🎯 Concepts clés appris

### 1. Modification de la casse
- `upper()`, `lower()`, `title()`, `capitalize()`
- Cas d'usage pour chaque méthode

### 2. Remplacement
- `replace(old, new)` - Remplace toutes occurrences
- Possibilité d'enchaîner plusieurs replace

### 3. Nettoyer (Strip)
- `strip()`, `lstrip()`, `rstrip()`
- **Important :** Analyse caractère par caractère

### 4. Séparer et Joindre
- `split()` : STRING → LISTE
- `join()` : LISTE → STRING
- **Piège :** join() uniquement avec des strings

### 5. Remplir de zéros
- `zfill(width)` pour séquences numérotées

### 6. Validation
- Méthodes `is...` : `isdigit()`, `isalpha()`, etc.
- **Critique :** Valider avant conversion

### 7. Compter
- `count(sub)` compte CARACTÈRES, pas mots
- Ajouter espace pour compter mots

### 8. Trouver
- `find()` vs `index()` : -1 vs erreur
- `rfind()` pour chercher depuis la fin

### 9. Début/Fin
- `startswith()`, `endswith()`
- Utile pour extensions fichiers

---

## 💡 Points critiques à retenir

### Les méthodes NE modifient PAS l'original
```python
texte = "hello"
texte.upper()  # Inutile
nouveau = texte.upper()  # OK
```

### join() : syntaxe inversée
```python
# Séparateur D'ABORD
", ".join(['1', '2', '3'])  # OK
```

### strip() : caractère par caractère
```python
"  bonjour  ".strip(" ujor")  # "bon"
# Pas la chaîne " ujor" entière !
```

---

## ✅ Exercices complétés

- [x] Exercice 10 : Remplacer un mot
- [x] Exercice 11 : Compter occurrences
- [x] Exercice 12 : Compter phrases
- [x] Exercice 13 : Ordonner chaîne

---

## 📊 Scores

**Quiz 9 :** 7/8 (87.5%) ✅

**Erreur :** Syntaxe `join()` - Corrigée et comprise

---

## 🎓 Section validée le 16 février 2026

**Prêt pour Section 18 : Les opérateurs**