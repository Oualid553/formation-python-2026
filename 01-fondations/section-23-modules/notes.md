# Section 23 - Quelques Modules et Fonctions Utiles

**Date :** 17-22 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~2h

---

## 📚 Contenu

- Vidéo 144 : Sources
- Vidéo 145 : IMPORTANT - Quelques erreurs à éviter
- Vidéo 146 : Introduction
- Vidéo 147 : Le module random (5 min)
- Quiz 16 : 2/2 (100%) ✅
- Exercice 18 : Module random ✅
- Vidéo 148 : Solution exercice 18
- Vidéo 149 : Le module OS - obsolète ?
- Vidéo 150 : Le module os (7 min)
- Quiz 17 : 4/4 (100%) ✅
- Vidéo 151 : Aller chercher de l'aide avec dir et help (5 min)
- Quiz 18 : 2/2 (100%) ✅
- Vidéo 152 : Les objets callable

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

# Nombre entier avec pas
random.randrange(0, 101, 10) # 0, 10, 20, ..., 100
```

**Point critique :** `import random` obligatoire au début !

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

# Supprimer un dossier vide
os.rmdir("dossier")

# Vérifier existence
os.path.exists("fichier.txt")  # True ou False

# Joindre chemins (compatible tous OS)
os.path.join("dossier", "fichier.txt")

# Séparer chemin
os.path.split("dossier/fichier.txt")  # ('dossier', 'fichier.txt')
```

**Note :** `pathlib` est plus moderne (Section 36), mais `os` reste très utilisé.

---

## 🔍 FONCTIONS D'AIDE

```python
# dir() : Liste toutes les méthodes/attributs d'un objet
dir(str)           # Toutes les méthodes des strings
dir(random)        # Toutes les fonctions de random
dir(os)            # Toutes les fonctions de os

# help() : Documentation complète d'une fonction
help(str.upper)         # Explique upper()
help(random.randint)    # Explique randint()
help(os.getcwd)         # Explique getcwd()

# Utilisation pratique :
# Oublié une méthode ? → dir(objet)
# Pas sûr de comment utiliser ? → help(fonction)
```

---

## 📊 Scores

| Élément | Score |
|---------|-------|
| Quiz 16 (random) | 2/2 (100%) |
| Exercice 18 | 100% |
| Quiz 17 (os) | 4/4 (100%) |
| Quiz 18 (dir/help) | 2/2 (100%) |
| **Moyenne** | **100%** |

---

## 💡 Leçons retenues

**Exercice 18 :** Udemy attendait variables nommées `a` et `b`, pas `nombre_a` et `nombre_b`.
→ Toujours respecter les noms de variables demandés !

**Section difficile à retenir :** Normal ! Ce sont des fonctions de référence.
→ Créer une cheatsheet et utiliser `dir()` et `help()` quand on oublie.

---

## ✅ Section validée le 22 février 2026

**Prêt pour Section 24 : Les listes**