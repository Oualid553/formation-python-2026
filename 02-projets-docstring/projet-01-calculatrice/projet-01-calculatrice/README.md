# Projet Docstring #1 : La Calculatrice

**Date :** 17 février 2026  
**Section :** 20 - Formation Docstring  
**Statut :** ✅ Complété  
**Score :** 99%

---

## 📋 Description

Premier projet officiel de la formation Docstring.

Programme en ligne de commande qui demande deux nombres à l'utilisateur et affiche le résultat de leur addition.

---

## 🎯 Consigne

Créer un script qui :
1. Demande un premier nombre à l'utilisateur
2. Demande un deuxième nombre à l'utilisateur
3. Affiche : `"Le résultat de l'addition du nombre X avec le nombre Y est égal à Z"`

---

## 💻 Exemple d'utilisation

```
Veuillez entrer un premier nombre : 5
Veuillez entrer un deuxième nombre : 10
Le résultat de l'addition du nombre 5 avec le nombre 10 est égal à 15
```

---

## 🛠️ Concepts Python utilisés

| Concept | Section | Application |
|---------|---------|-------------|
| `input()` | 15 | Récupérer saisie utilisateur |
| `int()` | 14 | Convertir str → int |
| f-strings | 19 | Formater l'affichage |
| Variables | 13 | Stocker les données |

---

## 📝 Ma Solution

```python
# Étape 1 : Demander premier nombre
a = int(input("Veuillez entrer un premier nombre : "))

# Étape 2 : Demander deuxième nombre
b = int(input("Veuillez entrer un deuxième nombre : "))

# Étape 3 : Calculer
resultat = a + b

# Étape 4 : Afficher
print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {resultat}")
```

---

## ✅ Correction Officielle Docstring

```python
a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxième nombre : ")
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
```

---

## 🔍 Comparaison Ma Solution vs Correction

| Critère | Ma Solution | Correction Officielle |
|---------|-------------|----------------------|
| Conversion | `int()` avant calcul | `int()` dans f-string |
| Variable résultat | ✅ Séparée | ❌ Pas de variable |
| Lisibilité | ✅ Plus lisible | Compact |
| Lignes de code | 4 lignes | 3 lignes |
| Validité | ✅ Correcte | ✅ Correcte |

**Les deux approches sont valides !**

**Ma solution :** Plus lisible, plus facile à déboguer, meilleure pratique pour projets complexes.

**Correction officielle :** Plus compacte, expression directe dans f-string, démontre la puissance des f-strings.

---

## 💡 Leçon importante retenue

### Erreur initiale

```python
# ❌ MAUVAIS : Tout mélangé sur une ligne
resultat = print(f"...{resultat}...")
# Problème 1 : resultat n'existe pas encore !
# Problème 2 : print() retourne None
```

### Bonne pratique

```python
# ✅ BON : Séparer calcul et affichage
resultat = a + b              # Calcul
print(f"...{resultat}...")    # Affichage
```

**Règle retenue : Une ligne = Une responsabilité ! 🎯**

---

## 🚀 Améliorations futures

**Version 2 (avec conditions - Section 21) :**
- [ ] Validation : vérifier que l'utilisateur entre bien un nombre
- [ ] Message d'erreur si saisie invalide

**Version 3 (avec boucles - Section 26) :**
- [ ] Effectuer plusieurs calculs d'affilée
- [ ] Menu pour choisir l'opération (+, -, *, /)

**Version 4 (avec fonctions - Section 42) :**
- [ ] Fonction `addition(a, b)`
- [ ] Fonction `calculer(a, b, operation)`

**Version 5 (projet Docstring #2 - Section 28) :**
- [ ] Calculatrice v2 avec toutes les opérations
- [ ] Gestion erreurs (division par zéro)

---

## 📊 Statistiques

**Lignes de code :** ~10  
**Temps de développement :** ~15 min  
**Blocage rencontré :** Confusion calcul/affichage → Résolu !  
**Tests réussis :** ✅ Tous

---

## 🎓 Progression personnelle

> "Cette fois c'était beaucoup plus facile que la première fois où je paniquais complètement.
> J'ai bien compris qu'il fallait utiliser input(), la conversion dans la variable et le f-string."
>
> — Oualid, 17 février 2026

**Preuve de progression : Section 20 maîtrisée avec confiance ! 🔥**

---

## 🔗 Fichiers

- `calculatrice.py` - Code source complet avec commentaires

---

**Premier projet Docstring réussi ! 🎉**
