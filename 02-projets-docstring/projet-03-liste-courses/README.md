# Projet Docstring #3 : Liste de Courses

**Date :** 5 mars 2026  
**Section :** 29 - Formation Docstring  
**Statut :** ✅ Complété  
**Score :** 95% (quasi identique correction officielle)

---

## 📋 Description

Troisième projet officiel de la formation Docstring. Application en ligne de commande pour gérer une liste de courses avec menu interactif et 5 fonctionnalités.

---

## 🎯 Fonctionnalités

1. ✅ Ajouter un élément à la liste
2. ✅ Retirer un élément de la liste
3. ✅ Afficher la liste complète
4. ✅ Vider toute la liste
5. ✅ Quitter l'application

---

## 💻 Exemple d'utilisation

```
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : 1

Entrez le nom d'un élément à ajouter : Pomme
L'élément Pomme a bien été ajouté à la liste.

Voici le contenu de votre liste :
1. Pomme

👉 Votre choix : 1
Entrez le nom d'un élément à ajouter : Pain
L'élément Pain a bien été ajouté à la liste.

Voici le contenu de votre liste :
1. Pomme
2. Pain

👉 Votre choix : 3
Voici le contenu de votre liste :
1. Pomme
2. Pain

👉 Votre choix : 2
Entrez le nom d'un élément à retirer : Pomme
L'élément Pomme a bien été retiré de la liste.

👉 Votre choix : 5
Au revoir !
```

---

## 🛠️ Concepts Python utilisés

| Concept | Application |
|---------|-------------|
| `while True` | Boucle infinie avec sortie conditionnelle |
| Liste vide | `LISTE = []` |
| Validation choix | `if choix not in ["1", "2", "3", "4", "5"]` |
| `continue` | Retourne au début de la boucle |
| `enumerate(liste, start=1)` | Numérotation automatique des éléments |
| `append()` | Ajouter élément en fin de liste |
| `remove()` | Retirer élément par valeur |
| `clear()` | Vider toute la liste |
| `in` opérateur | Vérifier existence dans liste |
| `sys.exit()` | Quitter le programme |
| `if/elif/else` | Structure conditionnelle complète |

---

## 📊 Comparaison avec correction officielle

### Similarités (95%) ✅
- ✅ Logique identique
- ✅ Validation par liste de choix
- ✅ Gestion des cas d'erreur
- ✅ Utilisation de `enumerate()`
- ✅ Messages clairs

### Différences mineures
| Mon code | Correction | Impact |
|----------|------------|--------|
| `liste_course` | `LISTE` | Aucun (fonctionnel) |
| Plusieurs `print()` menu | Variable `MENU` | Aucun (style) |
| `if len(liste) == 0:` | `if LISTE:` | Aucun (les 2 valides) |

**→ Code validé à 95% ! 🏆**

---

## 🎓 Nouveaux concepts maîtrisés

### 1. Menu interactif avec boucle
```python
while True:
    print("Menu...")
    choix = input()
    
    if choix not in ["1", "2", "3"]:
        continue
    
    if choix == "1":
        # Action
```

### 2. enumerate() pour numéroter
```python
# Au lieu de :
for i in range(len(liste)):
    print(f"{i+1}. {liste[i]}")

# On utilise :
for index, item in enumerate(liste, start=1):
    print(f"{index}. {item}")
```

### 3. Validation avec liste de choix
```python
# Plus propre que isdigit() + plage
choix_valides = ["1", "2", "3", "4", "5"]
if choix not in choix_valides:
    print("Invalide")
```

### 4. Vérifier liste vide
```python
# Pythonique
if ma_liste:
    print("Liste a des éléments")
else:
    print("Liste vide")
```

---

## 🚀 Évolution du projet

| Version | Section | Nouveauté |
|---------|---------|-----------|
| **v1** | 29 | Liste en mémoire (cette version) |
| **v2** | 35 | Sauvegarde dans fichier (à venir) |
| **v3** | ? | Base de données (à venir) |

---

## 💡 Améliorations futures possibles

1. Sauvegarder la liste dans un fichier
2. Catégories de produits (fruits, légumes, etc.)
3. Quantités par article
4. Budget total estimé
5. Suggestions auto-complétion
6. Export PDF ou email

---

## ✅ Projet validé le 5 mars 2026

**Prochains projets :**
- **Section 30** : Projet #4 - Le Nombre Mystère
- **Section 31** : Projet #5 - Jeu de Rôle
