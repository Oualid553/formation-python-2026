# Section 16 - Résolution de problèmes

**Date début :** 16 février 2026  
**Date fin :** 16 février 2026  
**Temps total :** ~15 min  
**Statut :** ✅ Validée

---

## 🧠 MÉTHODOLOGIE : Décomposer un problème

### ❌ ERREUR CLASSIQUE DES DÉBUTANTS

**Partir directement dans le code sans réfléchir**

**Conséquences :**
- Mélange de syntaxe et de logique
- Code désordonné
- Découragement rapide
- Impression de "ne pas avoir de logique"

---

## ✅ LA BONNE MÉTHODE

### 1. DÉCRIRE LE PROBLÈME EN FRANÇAIS

**Avant d'écrire une seule ligne de code :**

- Utiliser des **commentaires** (`#`)
- Décrire **chaque étape** en français
- Écrire un **cahier des charges** simple

**Pourquoi ?**
- Sépare la logique de la syntaxe
- Évite de s'emmêler les pinceaux
- Permet de voir le déroulé complet

---

### 2. EXEMPLE CONCRET : Calculatrice addition

#### Étape 1 : Décrire en français (commentaires)
```python
# 1. Demander un premier nombre à l'utilisateur
# 2. Demander un deuxième nombre à l'utilisateur
# 3. Additionner les deux nombres ensemble
# 4. Afficher le résultat à l'utilisateur
```

#### Étape 2 : Traduire en code Python
```python
# 1. Demander un premier nombre à l'utilisateur
a = int(input("Premier nombre : "))

# 2. Demander un deuxième nombre à l'utilisateur
b = int(input("Deuxième nombre : "))

# 3. Additionner les deux nombres ensemble
resultat = a + b

# 4. Afficher le résultat à l'utilisateur
print(f"Résultat : {resultat}")
```

---

### 3. TRADUCTION FRANÇAIS → PYTHON

**Python est presque de la traduction littérale :**

| Français | Python |
|----------|--------|
| Afficher | `print()` |
| Demander | `input()` |
| Additionner | `+` |
| Si... | `if` |
| Stocker | Variable |

**Chaque action en français = ~1 ligne de code Python**

---

## 📝 OUTILS DE RÉFLEXION

### Option 1 : Commentaires dans le code
```python
# Étape par étape avec #
```

### Option 2 : Papier + stylo (RECOMMANDÉ)

**Avantages :**
- Plus organique, plus malléable
- Facile de raturer, dessiner, refaire
- Libère la créativité
- Pas de distraction écran

**Utiliser :**
- Schémas
- Dessins
- Listes d'étapes
- Organigrammes

---

## 🎯 PROCESSUS ITÉRATIF

**Normal que le premier jet ne soit pas parfait !**

1. Écrire le plan en français
2. Identifier ce qui manque
3. Ajuster le plan
4. Traduire en code
5. Tester
6. Corriger si besoin

---

## ⚠️ MÊME POUR LES EXPERTS

**Même avec de l'expérience :**
- Toujours utile de planifier en français
- Évite d'oublier des éléments
- Évite de réécrire du code inutile
- Bonne pratique professionnelle

---

## 📚 UTILISER LA DOCUMENTATION

### Documentation officielle Python (en français !)

**URL :** https://docs.python.org

**Choisir :**
- Langue : **French** (en haut à gauche)
- Version : **3.12** (ou ta version actuelle)

### Contenu disponible

- **Tutoriels** (f-strings, listes, etc.)
- **Référence des méthodes** (append, extend, etc.)
- **Exemples de code**

### Comment chercher

**Barre de recherche** (en haut à droite) :
- Taper mot-clé : `list`, `dict`, `string`, etc.
- Ne pas forcément cliquer sur le premier résultat
- Chercher "Structures de données" ou "Tutoriel"

**Exemple :** Chercher `list` → Section "Structures de données" → Méthodes des listes

---

## 🔍 AUTRES RESSOURCES

### Glossaire Docstring

- Révision des notions vues en formation
- Exemples de code concrets
- Aide pour trouver des idées

### Communauté

- **Google** (recherches ciblées)
- **Discord Docstring** (entraide)
- **Communautés Python francophones**
- **Stack Overflow** (en anglais, mais solutions universelles)

---

## 💡 PHILOSOPHIE IMPORTANTE

**Ne pas rester bloqué seul !**

- Utiliser la documentation
- Chercher des exemples
- Demander de l'aide à la communauté
- Apprendre avec les autres, pas tout seul

---

## 🎯 MÉTHODOLOGIE RÉSUMÉE

### Pour CHAQUE problème/exercice :

**1. COMPRENDRE** le problème (lire l'énoncé)

**2. DÉCOMPOSER** en étapes simples (français/papier)

**3. PLANIFIER** le déroulé (commentaires)

**4. TRADUIRE** en code Python (ligne par ligne)

**5. TESTER** et corriger

**6. AMÉLIORER** si besoin

---

## 🚗 APPLICATION AU PROJET VTC

**Projet : Calculateur de tarif VTC**

### Étape 1 : Décomposer (sur papier)
```
1. Demander le nom du client
2. Demander la distance en km
3. Demander la durée en minutes
4. Demander si pourboire (oui/non)
5. Calculer tarif de base (distance × 2€)
6. Ajouter pourboire si oui (5€)
7. Afficher récapitulatif formaté
```

### Étape 2 : Traduire en code

Chaque ligne française devient du code Python !

---

## 🎓 Concepts clés maîtrisés

- ✅ Méthodologie de résolution de problèmes
- ✅ Décomposition en français AVANT le code
- ✅ Traduction français → Python
- ✅ Utilisation documentation officielle
- ✅ Recherche efficace d'informations
- ✅ Approche itérative (normal de refaire)
- ✅ Utilisation papier/stylo pour réfléchir

---

## 📊 Section sans exercices de code

**Type :** Méthodologie + Culture développeur

**Podcasts (95-97) :** Culture générale (optionnels)

---

## 🎓 Section validée le 16 février 2026