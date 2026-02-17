# Projet Docstring #1 : La Calculatrice

**Date :** 17 février 2026  
**Section :** 20 - Formation Docstring  
**Statut :** ✅ Complété  
**Score :** 99%

---

## 📋 Description

Premier projet officiel de la formation Docstring. Programme en ligne de commande qui additionne deux nombres saisis par l'utilisateur.

---

## 🎯 Consigne

1. Demander un premier nombre à l'utilisateur
2. Demander un deuxième nombre à l'utilisateur
3. Afficher : `"Le résultat de l'addition du nombre X avec le nombre Y est égal à Z"`

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

## ❌ Mon erreur initiale

```python
# Tout mélangé sur une ligne → ERREUR !
resultat = print(f"...{resultat}...")
# Problème 1 : resultat n'existe pas encore !
# Problème 2 : print() retourne None
```

---

## ✅ Ma solution finale

```python
a = int(input("Veuillez entrer un premier nombre : "))
b = int(input("Veuillez entrer un deuxième nombre : "))
resultat = a + b
print(f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {resultat}")
```

---

## ✅ Correction officielle Docstring

```python
a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxième nombre : ")
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
```

---

## 🔍 Comparaison

| Critère | Ma solution | Correction |
|---------|-------------|------------|
| Lisibilité | ✅ Plus lisible | Compact |
| Débogage | ✅ Plus facile | Moins facile |
| Validité | ✅ Correcte | ✅ Correcte |

**Règle retenue : Une ligne = Une responsabilité ! 🎯**

---

## 🚀 Améliorations futures

- **v2 (Section 21) :** Validation inputs avec conditions
- **v3 (Section 26) :** Boucle pour plusieurs calculs
- **v4 (Section 42) :** Fonctions pour chaque opération
- **v5 (Projet #2) :** Calculatrice complète (+, -, *, /)

---

## 🎓 Citation personnelle

> "Cette fois c'était beaucoup plus facile que la première fois où je paniquais complètement !"
> — Oualid, 17 février 2026
