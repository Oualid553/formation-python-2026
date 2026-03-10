# Projet Docstring #4 : Le Nombre Mystère

**Date :** 10 mars 2026  
**Section :** 30 - Formation Docstring  
**Statut :** ✅ Complété  
**Score :** 95%

---

## 📋 Description

Quatrième projet officiel de la formation Docstring. Jeu de devinette où le joueur doit trouver un nombre mystère choisi aléatoirement par l'ordinateur, en 5 essais maximum.

---

## 🎯 Fonctionnalités

1. ✅ Génération nombre aléatoire (0-100)
2. ✅ Limite de 5 essais
3. ✅ Validation entrée utilisateur
4. ✅ Indices "Trop grand" / "Trop petit"
5. ✅ Message victoire avec nombre d'essais
6. ✅ Message défaite avec révélation du nombre
7. ✅ Compteur essais restants

---

## 💻 Exemple d'utilisation

```
🕹️🎮 Le jeu du nombre mystère 🎮🕹️
--------------------------------------------------
J'ai choisi un nombre entre 0 et 100. Devinez !
Vous avez 5 essais !
--------------------------------------------------
Devine le nombre : 50
📉 Trop grand !
Il te reste 4 essais

Devine le nombre : 25
📈 Trop petit !
Il te reste 3 essais

Devine le nombre : 37
📈 Trop petit !
Il te reste 2 essais

Devine le nombre : 43
📉 Trop grand !
Il te reste 1 essai(s)

Devine le nombre : 40
🎉 Gagné en 5 tentatives !
Fin du jeu.
```

---

## 🛠️ Concepts Python utilisés

| Concept | Application |
|---------|-------------|
| `random.randint()` | Génération nombre aléatoire |
| `while True` | Boucle de jeu principale |
| Validation input | `if not x.isdigit()` |
| `continue` | Redemander si input invalide |
| Conversion type | `int(input)` |
| Compteur décrémental | `TENTATIVES -= 1` |
| Conditions multiples | if/elif/else imbriqués |
| `break` | Sortie de boucle victoire/défaite |
| F-strings | Affichage dynamique |
| Calcul inverse | `5 - TENTATIVES` (essais utilisés) |

---

## 📊 Logique du jeu

### Structure principale

```python
import random

# Setup
nombre_mystere = random.randint(0, 100)
tentatives = 5

# Boucle de jeu
while True:
    # 1. Demander input
    # 2. Valider (isdigit)
    # 3. Convertir en int
    # 4. Décrémenter compteur
    # 5. Vérifier victoire
    # 6. Vérifier défaite
    # 7. Donner indices
```

### Ordre critique des vérifications

```python
# ✅ BON ORDRE
TENTATIVES -= 1

if saisie == NOMBRE_MYSTERE:  # Victoire d'abord
    break
elif TENTATIVES == 0:         # Défaite ensuite
    break
elif saisie > NOMBRE_MYSTERE: # Indices après
    # ...
```

**Pourquoi ?** Si on gagne au dernier essai, on doit afficher victoire, pas défaite !

---

## 🎓 Nouveaux concepts maîtrisés

### 1. Compteur décrémental
```python
# Compter à rebours
essais = 5
while True:
    essais -= 1  # Diminuer de 1
    
    if essais == 0:
        print("Plus d'essais !")
        break
```

### 2. Calcul inverse pour affichage
```python
# Afficher essais UTILISÉS, pas restants
tentatives_max = 5
tentatives_restantes = 2

utilisees = tentatives_max - tentatives_restantes
# utilisees = 5 - 2 = 3

print(f"Trouvé en {utilisees} essais")
```

### 3. Pattern jeu avec limite
```python
# Pattern universel jeu avec essais limités
essais = X

while True:
    # Input joueur
    # Validation
    essais -= 1
    
    if victoire:
        break
    
    if essais == 0:
        break
    
    # Donner indices
```

---

## 🐛 Bugs rencontrés et corrigés

### Bug 1 : `break` manquant après victoire
```python
# ❌ AVANT
if saisie == NOMBRE_MYSTERE:
    print("Gagné !")
    # Pas de break → boucle continue !

# ✅ APRÈS
if saisie == NOMBRE_MYSTERE:
    print("Gagné !")
    break  # Sort de la boucle
```

### Bug 2 : Ordre victoire/défaite
```python
# ❌ MAUVAIS
if TENTATIVES == 0:  # Vérifie défaite d'abord
    print("Perdu")
    break
if saisie == NOMBRE_MYSTERE:  # Jamais atteint si gagné au dernier essai !
    break

# ✅ BON
if saisie == NOMBRE_MYSTERE:  # Victoire d'abord
    break
if TENTATIVES == 0:  # Défaite après
    break
```

---

## 💡 Améliorations futures possibles

### Court terme
1. Option "Rejouer" (nouvelle partie)
2. Meilleur score (nombre minimal d'essais)
3. Historique des tentatives

### Moyen terme
4. Niveaux de difficulté (facile/normal/difficile)
5. Chronomètre
6. Statistiques (% victoires, moyenne essais)

### Long terme
7. Mode 2 joueurs (tour par tour)
8. Sauvegarde scores dans fichier
9. Interface graphique (Tkinter)

---

## 🔄 Différences avec correction officielle

| Aspect | Mon code | Correction | Équivalent |
|--------|----------|------------|------------|
| Import | `import random` | `from random import randint` | ✅ Oui |
| Boucle | `while True` | `while tentatives > 0` | ✅ Oui |
| Décrémenter | Avant vérifications | Après vérifications | ✅ Oui |
| Messages | Dans la boucle | Après la boucle | ✅ Oui (styles différents) |
| Logique | Identique | Identique | ✅ 100% |

**→ Code fonctionnellement identique, juste style personnel ! 💪**

---

## ✅ Validation

**Critères de réussite :**
- [x] Génération aléatoire 0-100
- [x] Limite 5 essais
- [x] Validation input (isdigit)
- [x] Indices précis
- [x] Message victoire avec nb essais
- [x] Message défaite avec nombre révélé
- [x] Gestion break correcte
- [x] Code commenté
- [x] Tests complets

**Score final : 95/100**

**Pourquoi 95% ?**
- ✅ Logique parfaite
- ✅ Validation robuste
- ✅ Code clair et commenté
- ⚠️ 1 bug corrigé (break manquant)

---

## 🎯 Ce que j'ai appris

**Compétences renforcées :**
- ✅ Boucles while avec break
- ✅ Gestion compteurs (incrémenter/décrémenter)
- ✅ Validation entrées utilisateur
- ✅ Ordre logique des vérifications
- ✅ Module random (randint)
- ✅ Calculs inverses pour affichage

**Erreurs évitées à l'avenir :**
- ⚠️ Toujours break après victoire/défaite
- ⚠️ Vérifier victoire AVANT défaite
- ⚠️ Décrémenter au bon moment

---

## 🚀 Évolution du projet

| Version | Améliorations |
|---------|---------------|
| **v1 (actuelle)** | Jeu de base fonctionnel |
| **v2 (future)** | Option rejouer + meilleur score |
| **v3 (future)** | Niveaux difficulté + chrono |

---

## 📝 Notes personnelles

**Temps passé :**
- Code initial : 30 min
- Correction bugs : 5 min
- Tests : 10 min
- Documentation : 15 min
- **Total : 1h**

**Difficultés rencontrées :**
- Oubli du break après victoire (corrigé rapidement)
- Compréhension ordre vérifications (maîtrisé)

**Points forts :**
- Structure claire dès le départ
- Validation robuste
- Commentaires précis

---

## ✅ Projet validé le 10 mars 2026

**Prochains projets :**
- **Section 31** : Projet #5 - Jeu de Rôle
- **Section 32** : Fin Partie 1 Fondations
