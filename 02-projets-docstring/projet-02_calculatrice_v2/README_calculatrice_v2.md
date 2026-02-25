# Projet Docstring #2 : La Calculatrice v2 (avec gestion erreurs)

**Date :** 25 février 2026  
**Section :** 28 - Formation Docstring  
**Statut :** ✅ Complété  
**Score :** 95%

---

## 📋 Description

Deuxième projet officiel de la formation Docstring. Calculatrice en ligne de commande avec **gestion des erreurs** : redemande automatiquement si l'utilisateur entre autre chose que des nombres.

---

## 🎯 Consigne

1. Demander deux nombres à l'utilisateur
2. Afficher le résultat de l'addition
3. **Gérer les erreurs** : redemander si entrée invalide

---

## 💻 Exemple d'utilisation

### Cas normal
```
Entrez un premier nombre : 5
Entrez un deuxième nombre : 10
Le résultat de l'addition de 5 avec 10 est égal à 15
```

### Gestion erreur
```
Entrez un premier nombre : a
Entrez un deuxième nombre : sgoind
Veuillez entrer deux nombres valides
Entrez un premier nombre : 3
Entrez un deuxième nombre : 7
Le résultat de l'addition de 3 avec 7 est égal à 10
```

---

## 🛠️ Concepts Python utilisés

| Concept | Section | Application |
|---------|---------|-------------|
| Boucle `while` | 26 | Boucle infinie avec sortie conditionnelle |
| `input()` | 15 | Récupérer saisie utilisateur |
| `isdigit()` | 25 | Valider que l'entrée est un nombre |
| Opérateurs logiques `and` | 21 | Vérifier deux conditions |
| `if/else` | 21 | Structures conditionnelles |
| `break` | 26 | Sortir de la boucle |
| `int()` | 14 | Convertir str → int |
| f-strings | 19 | Formater l'affichage |

---

## 📊 Comparaison approches

### Ma solution (while True + break)

```python
while True:
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    if a.isdigit() and b.isdigit():
        resultat = int(a) + int(b)
        print(f"Le résultat de l'addition de {int(a)} avec {int(b)} est égal à {resultat}")
        break
    else:
        print("Veuillez entrer deux nombres valides")
```

**Avantages :**
- ✅ Logique claire et simple
- ✅ Tout dans la boucle
- ✅ Facile à comprendre pour débutants

**Amélioration possible :**
- ⚠️ Conversion `int()` répétée 3 fois

### Correction officielle (while not)

```python
a = b = ""
while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
```

**Avantages :**
- ✅ Condition directe dans `while`
- ✅ Conversion `int()` une seule fois
- ✅ Séparation validation/affichage

**Inconvénient :**
- ⚠️ Nécessite initialisation `a = b = ""`

---

## 🔧 Version optimisée (best of both)

```python
while True:
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)  # Conversion une seule fois
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {a + b}")
        break
    else:
        print("Veuillez entrer deux nombres valides")
```

---

## ⚠️ Limitations actuelles

**`isdigit()` ne gère PAS :**
- ❌ Nombres négatifs : `"-5".isdigit()` → `False`
- ❌ Nombres décimaux : `"3.14".isdigit()` → `False`

**Solution future :** `try/except` (vu plus tard dans formation)

---

## 🎓 Leçons retenues

### 1. `is True` est redondant
```python
if condition is True:  # ❌ Redondant
if condition:          # ✅ Suffit
```

### 2. Deux styles de boucles valides
```python
# Style 1 : while True + break
while True:
    if condition:
        break

# Style 2 : while not condition
while not condition:
    pass
```

### 3. `isdigit()` = validation basique
```python
"123".isdigit()    # True
"-5".isdigit()     # False
"3.14".isdigit()   # False
"abc".isdigit()    # False
```

---

## 📈 Évolution du projet

| Version | Section | Nouveauté |
|---------|---------|-----------|
| **v1** | 20 | Calculatrice basique (pas de gestion erreur) |
| **v2** | 28 | Gestion erreurs avec `isdigit()` + boucle |
| **v3** | ? | À venir : `try/except`, décimaux, autres opérations |

---

## 🚀 Améliorations futures possibles

1. Gérer nombres négatifs et décimaux
2. Ajouter autres opérations (-, *, /)
3. Permettre plusieurs calculs sans relancer
4. Historique des calculs
5. Interface graphique (tkinter)

---

## ✅ Projet validé le 25 février 2026

**Prêt pour Section 29 : Projet #3 - Liste de courses**