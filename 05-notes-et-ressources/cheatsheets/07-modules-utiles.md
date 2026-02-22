# Cheatsheet : Modules Utiles

**Section 23 - Modules et Fonctions**
**Date :** 17 février 2026

---

## 🎲 MODULE RANDOM
```python
import random

# Nombre entier aléatoire (inclus)
random.randint(1, 10)        # ex: 7

# Nombre décimal entre 0 et 1
random.random()              # ex: 0.734

# Nombre décimal entre a et b
random.uniform(1.0, 10.0)    # ex: 4.73

# Choisir élément au hasard
random.choice([1, 2, 3])     # ex: 2

# Mélanger une liste
ma_liste = [1, 2, 3]
random.shuffle(ma_liste)     # Modifie la liste directement
```

---

## 📁 MODULE OS
```python
import os

# Dossier actuel
os.getcwd()                  # "C:/Users/ouali/Documents"

# Lister fichiers/dossiers
os.listdir()                 # ['fichier.py', 'dossier1']
os.listdir("chemin")         # Liste un dossier spécifique

# Créer un dossier
os.mkdir("nouveau_dossier")

# Supprimer un fichier
os.remove("fichier.txt")

# Vérifier existence
os.path.exists("fichier.txt")  # True ou False

# Joindre chemins (compatible tous OS)
os.path.join("dossier", "fichier.txt")
```

---

## 🔍 FONCTIONS D'AIDE
```python
# Lister toutes les méthodes d'un objet
dir(str)           # Toutes les méthodes des strings
dir(random)        # Toutes les fonctions de random
dir(os)            # Toutes les fonctions de os

# Documentation complète
help(str.upper)         # Explique upper()
help(random.randint)    # Explique randint()
help(os.getcwd)         # Explique getcwd()
```

---

## 💡 QUAND UTILISER QUOI ?

| Besoin | Module/Fonction |
|--------|----------------|
| Nombre aléatoire | `random.randint()` |
| Choisir au hasard | `random.choice()` |
| Dossier actuel | `os.getcwd()` |
| Créer dossier | `os.mkdir()` |
| Lister fichiers | `os.listdir()` |
| Oublié une méthode | `dir(objet)` |
| Comprendre fonction | `help(fonction)` |

---

**Scores Section 23 :**
- Quiz 16 (random) : 2/2 (100%) ✅
- Exercice 18 : 100% ✅
- Quiz 17 (os) : 4/4 (100%) ✅