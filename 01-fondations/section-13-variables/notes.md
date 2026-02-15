# Section 13 - Les variables

**Date début :** 15 février 2026  
**Date fin :** 15 février 2026  
**Temps total :** ~2h  
**Statut :** ✅ Validée

---

## 📚 Concepts clés

### Qu'est-ce qu'une variable ?

- Une variable est un **nom** qui référence un **objet** en mémoire
- En Python : les objets existent en mémoire, les variables sont des "étiquettes"
- Différent d'autres langages où la variable "contient" la valeur

### Objets et noms

- Python crée l'objet d'abord, puis lui associe un nom
- Plusieurs noms peuvent référencer le même objet
- Exemple : `a = 5` → crée l'objet `5` puis l'associe au nom `a`

### Affectations

**Simple :**
```python
age = 36
```

**Parallèle (multiple à gauche et à droite) :**
```python
a, b = 1, 2  # a vaut 1, b vaut 2
```

**Multiple (même valeur à plusieurs variables) :**
```python
a = b = c = 0  # Toutes valent 0
```

### Règles de nommage

**✅ AUTORISÉ :**
- Lettres (a-z, A-Z)
- Chiffres (SAUF au début)
- Underscores `_`
- Exemples : `age`, `prix_total`, `a1`, `_variable`

**❌ INTERDIT :**
- Espaces : `nombre impair` ❌
- Commence par chiffre : `3a` ❌
- Caractères spéciaux : `%taux`, `prix@`, `a$` ❌
- Mots-clés Python : `print`, `if`, `for`, `class` ❌

### Conventions PEP 8

- Variables en **minuscules** : `age`, `prenom`
- Mots multiples avec **underscore** : `compte_en_banque`, `prix_total`
- Noms **explicites** : `prix_course` plutôt que `p`
- Éviter noms d'une lettre sauf compteurs : `i`, `j`, `k`

---

## 💡 Points importants à retenir

- Affectation `a = b` → copie la VALEUR, pas de lien permanent
- Variables Python = étiquettes sur des objets
- Python sensible à la casse : `Age` ≠ `age`
- Singleton : Python réutilise certains objets (petits entiers, True, False, None)
- Small integer caching : nombres -5 à 256 partagés en mémoire

---

## ❓ Questions / Confusions

- Singleton et caching : concept avancé, à approfondir plus tard si besoin
- Affectations parallèles : pas encore pratiquées en exercices

---

## ✅ Exercices complétés

- [x] Exercice 4 : Créer des variables (100%)
- [x] Exercice 5 : Corriger erreur guillemets (100%)
- [x] Exercice 6 : Variables valides uniquement (100%)
- [x] Exercice 7 : Valeur d'une variable (100%)

---

## 📊 Scores Quiz

- Quiz 6 (Introduction) : 5/7 (71%)
- Quiz 7 (Variables) : 6/7 (86%)
- **Total : 11/14 (79%)**

**Points à revoir :** Affectations multiples/parallèles

---

## 🎯 Section validée ✅

**Prête pour Section 14 !**