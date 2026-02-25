# 📚 FICHE RÉVISION JOUR 1 - Jeudi 26 Février 2026

**Durée : 20-30 min**  
**Sections à réviser : 21-23 (Conditions, Erreurs, Modules)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Quelle est la syntaxe d'une condition if/elif/else ?  
   **R:** `if condition: ... elif autre_condition: ... else: ...`

2. **Q:** Différence entre `==` et `=` ?  
   **R:** `==` compare, `=` assigne

3. **Q:** Qu'est-ce qu'une SyntaxError ?  
   **R:** Erreur de syntaxe (oubli `:`, mauvaise indentation)

4. **Q:** Qu'est-ce qu'une TypeError ?  
   **R:** Opération sur type incompatible (ex: `"5" + 5`)

5. **Q:** Comment importer le module random ?  
   **R:** `import random`

6. **Q:** `random.randint(1, 10)` fait quoi ?  
   **R:** Retourne nombre aléatoire entre 1 et 10 (inclus)

7. **Q:** Comment obtenir l'aide sur une fonction ?  
   **R:** `help(fonction)` ou `dir(objet)`

8. **Q:** Opérateurs de comparaison Python ?  
   **R:** `==`, `!=`, `<`, `>`, `<=`, `>=`

9. **Q:** Opérateurs logiques Python ?  
   **R:** `and`, `or`, `not`

10. **Q:** `os.getcwd()` fait quoi ?  
    **R:** Retourne le répertoire de travail actuel

### Lecture Cheatsheet (5 min)

**Relire :** `05-notes-et-ressources/cheatsheets/06-conditions.md`

**Points clés à retenir :**
- Structure if/elif/else
- Opérateurs de comparaison
- Opérateurs logiques (and, or, not)

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Quel est le résultat de :** `5 > 3 and 2 < 1` ?  
   <details><summary>Réponse</summary>False (car 2 < 1 est False)</details>

2. **Que fait ce code ?**
   ```python
   if age >= 18:
       print("Majeur")
   else:
       print("Mineur")
   ```
   <details><summary>Réponse</summary>Affiche "Majeur" si age ≥ 18, sinon "Mineur"</details>

3. **Quelle différence entre ValueError et NameError ?**
   <details><summary>Réponse</summary>ValueError = valeur inappropriée, NameError = variable inexistante</details>

4. **Comment générer un nombre aléatoire entre 1 et 100 ?**
   <details><summary>Réponse</summary>random.randint(1, 100)</details>

5. **Que fait `os.listdir()` ?**
   <details><summary>Réponse</summary>Liste les fichiers du répertoire</details>

### Lecture Code (10 min)

**Relis ce code de ton Exercice 17 (Section 21) :**

```python
nombre_a = int(input("Entrez le nombre a : "))
nombre_b = int(input("Entrez le nombre b : "))

if nombre_a > nombre_b:
    print(f"{nombre_a} est supérieur à {nombre_b}")
elif nombre_a < nombre_b:
    print(f"{nombre_a} est inférieur à {nombre_b}")
else:
    print(f"{nombre_a} est égal à {nombre_b}")
```

**Questions à te poser :**
- ✅ Pourquoi `int()` autour de `input()` ?
- ✅ Que se passe si nombre_a == nombre_b ?
- ✅ Quel ordre : if, elif, else ?

---

## 📖 CONCEPTS CLÉS SECTIONS 21-23

### Section 21 : Conditions
```python
if condition:
    # code si vrai
elif autre_condition:
    # code si vrai
else:
    # code sinon

# Opérateurs
==  !=  <  >  <=  >=
and  or  not
```

### Section 22 : Erreurs
```python
# Types d'erreurs
SyntaxError      # Syntaxe invalide
IndentationError # Mauvaise indentation
TypeError        # Type incompatible
ValueError       # Valeur inappropriée
NameError        # Variable inexistante
ZeroDivisionError # Division par 0
```

### Section 23 : Modules
```python
import random
random.randint(1, 10)  # 1 à 10
random.choice([1,2,3]) # Élément aléatoire

import os
os.getcwd()      # Répertoire actuel
os.listdir()     # Liste fichiers
```

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Cheatsheet conditions relu (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Code analysé (10 min)

**Total : 30 min ✅**

---

## 💡 ASTUCE DU JOUR

**Pendant tes trajets VTC, pense mentalement à :**
- Comment tu ferais un `if` pour vérifier si un client est à l'heure
- Quel module tu utiliserais pour générer un code course aléatoire
- Comment tu gères les erreurs si un client entre une adresse invalide

**→ Connexion formation/métier = meilleure mémorisation ! 🧠**

---

**Demain : Fiche Jour 2 (Sections 24-25) 📚**