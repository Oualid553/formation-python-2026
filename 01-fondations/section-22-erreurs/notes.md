# Section 22 - Les Erreurs Que Vous Allez Rencontrer

**Date :** 17 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~30 min

---

## 📚 Contenu

- Vidéo 139 : Introduction
- Vidéo 140 : Les erreurs de syntaxe (4 min)
- Vidéo 141 : Les mots réservés par Python (1 min)
- Vidéo 142 : Les erreurs d'exécution (3 min)
- Vidéo 143 : Les erreurs sémantiques (1 min)

**Note :** Section théorique, pas de quiz ni d'exercices.

---

## ⚠️ 1. ERREURS DE SYNTAXE (SyntaxError)

**Définition :** Code mal écrit, Python ne peut pas l'interpréter.

**Exemples courants :**
```python
# Oubli des :
if age >= 18  # ❌ SyntaxError
if age >= 18: # ✅

# Mauvaise indentation
if age >= 18:
print("Majeur")  # ❌ IndentationError

# Parenthèses/crochets non fermés
liste = [1, 2, 3  # ❌ SyntaxError
```

**→ Python refuse de lancer le script !**

---

## 🔑 2. MOTS RÉSERVÉS

**Définition :** Mots interdits comme noms de variables (réservés par Python).

**Liste des mots réservés :**
```python
False, True, None, and, or, not, if, elif, else,
for, while, break, continue, def, class, return,
import, from, as, try, except, finally, raise, with
```

**Exemples d'erreurs :**
```python
if = 5      # ❌ SyntaxError
class = "A" # ❌ SyntaxError
for = 10    # ❌ SyntaxError
```

---

## 🔥 3. ERREURS D'EXÉCUTION (Runtime Errors)

**Définition :** Code syntaxiquement correct, mais plante pendant l'exécution.

**Exemples courants :**

### TypeError
```python
"10" + 5  # ❌ Impossible d'additionner str + int
```

### ValueError
```python
int("abc")  # ❌ "abc" n'est pas convertible en int
```

### NameError
```python
print(variable_inexistante)  # ❌ Variable non définie
```

### IndexError
```python
ma_liste = [1, 2, 3]
ma_liste[10]  # ❌ Index hors limite
```

### KeyError
```python
dico = {"a": 1}
dico["b"]  # ❌ Clé inexistante
```

### ZeroDivisionError
```python
10 / 0  # ❌ Division par zéro
```

---

## 🤔 4. ERREURS SÉMANTIQUES (Logic Errors)

**Définition :** Code fonctionne mais ne fait PAS ce qu'on veut (logique incorrecte).

**Exemples :**

```python
# Calculer la moyenne de 3 notes
note1, note2, note3 = 10, 12, 14

# ❌ ERREUR SÉMANTIQUE
moyenne = note1 + note2 + note3 / 3  # = 10 + 12 + 4.67 = 26.67 !!

# ✅ CORRECT
moyenne = (note1 + note2 + note3) / 3  # = 12
```

```python
# Vérifier si nombre pair
nombre = 10

# ❌ ERREUR SÉMANTIQUE
if nombre / 2:  # Teste si le résultat est "truthy", pas si c'est pair !
    print("Pair")

# ✅ CORRECT
if nombre % 2 == 0:
    print("Pair")
```

**→ Les plus difficiles à détecter car Python ne signale rien !**

---

## 📊 Résumé

| Type | Détection | Exemple |
|------|-----------|---------|
| **Syntaxe** | Avant exécution | `if age >= 18` (oubli :) |
| **Exécution** | Pendant exécution | `10 / 0` |
| **Sémantique** | Tests/Débogage | `(10+12+14) / 3` vs `10+12+14/3` |

---

## 💡 Conseils

1. **Lire le message d'erreur** → Python indique la ligne et le type
2. **Tester avec des print()** → Vérifier les valeurs intermédiaires
3. **Diviser le problème** → Tester chaque partie séparément
4. **Utiliser un débogueur** → VS Code debugger pour suivre l'exécution

---

## ✅ Section validée le 17 février 2026

**Prêt pour Section 23 : Modules et fonctions utiles**