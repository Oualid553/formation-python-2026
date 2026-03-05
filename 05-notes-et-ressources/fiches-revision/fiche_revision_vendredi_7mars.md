# 📚 FICHE RÉVISION - Vendredi 7 Mars 2026 (Jour VTC)

**Durée : 20-30 min maximum**  
**Sections à réviser : 21-23 (Conditions, Erreurs, Modules)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Syntaxe condition if/elif/else complète ?  
   **R:** `if condition: ... elif autre: ... else: ...`

2. **Q:** Opérateurs de comparaison Python ?  
   **R:** `==`, `!=`, `<`, `>`, `<=`, `>=`

3. **Q:** Opérateurs logiques Python ?  
   **R:** `and`, `or`, `not`

4. **Q:** Que fait `and` ? Exemple ?  
   **R:** Vrai si TOUTES conditions vraies. `age >= 18 and permis == True`

5. **Q:** Que fait `or` ? Exemple ?  
   **R:** Vrai si AU MOINS UNE vraie. `jour == "samedi" or jour == "dimanche"`

6. **Q:** Les 6 types d'erreurs Python courants ?  
   **R:** SyntaxError, IndentationError, TypeError, ValueError, NameError, ZeroDivisionError

7. **Q:** Comment importer le module random ?  
   **R:** `import random`

8. **Q:** Générer nombre aléatoire entre 1 et 10 ?  
   **R:** `random.randint(1, 10)`

9. **Q:** Comment importer sys et quitter ?  
   **R:** `import sys` puis `sys.exit()`

10. **Q:** Différence `==` vs `=` ?  
    **R:** `==` compare (égal?), `=` assigne (affecte valeur)

### Lecture Rapide (5 min)

**Relis mentalement :**

```python
# Conditions
if age >= 18:
    print("Majeur")
elif age >= 16:
    print("Adolescent")
else:
    print("Mineur")

# Modules
import random
nombre = random.randint(1, 100)
```

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Résultat de : `5 > 3 and 2 < 1` ?**
   <details><summary>Réponse</summary>False (car 2 < 1 est False)</details>

2. **Résultat de : `5 > 3 or 2 < 1` ?**
   <details><summary>Réponse</summary>True (car 5 > 3 est True)</details>

3. **Que fait ce code ?**
   ```python
   if tarif > 50:
       print("Cher")
   else:
       print("Ok")
   ```
   <details><summary>Réponse</summary>Affiche "Cher" si tarif > 50, sinon "Ok"</details>

4. **Quelle erreur : `int("abc")` ?**
   <details><summary>Réponse</summary>ValueError (valeur ne peut pas être convertie)</details>

5. **À quoi sert `random.choice([1,2,3])` ?**
   <details><summary>Réponse</summary>Retourne un élément aléatoire de la liste</details>

### Visualisation Code (10 min)

**Visualise ce code VTC :**

```python
import random

# Calculateur tarif avec supplément aléatoire
distance = 15
heure = 23

# Tarif de base
tarif = distance * 2

# Supplément nuit
if heure >= 22 or heure < 6:
    tarif = tarif * 1.15
    print("Supplément nuit appliqué")

# Pourboire aléatoire
if random.randint(1, 10) > 7:
    print("Client généreux !")
    tarif = tarif * 1.10

print(f"Tarif final : {tarif}€")
```

**Questions à te poser :**
- ✅ Quand le supplément nuit s'applique ?
- ✅ Quelle chance d'avoir pourboire ?
- ✅ Tarif si distance=15, heure=23, pas de pourboire ?

---

## 📖 CONCEPTS CLÉS SECTIONS 21-23

### Conditions (Section 21)

```python
# Simple
if condition:
    # code

# Avec else
if condition:
    # si vrai
else:
    # si faux

# Complète
if condition1:
    # cas 1
elif condition2:
    # cas 2
else:
    # autres cas

# Opérateurs comparaison
==  !=  <  >  <=  >=

# Opérateurs logiques
and  # ET (toutes vraies)
or   # OU (au moins une vraie)
not  # INVERSE
```

### Erreurs Courantes (Section 22)

```python
# SyntaxError - Syntaxe invalide
if x == 5  # ❌ Oubli :

# IndentationError - Mauvaise indentation
if x == 5:
print("Ok")  # ❌ Pas indenté

# TypeError - Type incompatible
"5" + 5  # ❌ str + int

# ValueError - Valeur inappropriée
int("abc")  # ❌ Pas un nombre

# NameError - Variable inexistante
print(variable_qui_nexiste_pas)

# ZeroDivisionError - Division par 0
10 / 0  # ❌
```

### Modules (Section 23)

```python
# Module random
import random

random.randint(1, 10)     # Nombre aléatoire 1-10
random.choice([1,2,3])    # Élément aléatoire liste
random.random()           # Nombre décimal 0-1

# Module sys
import sys
sys.exit()  # Quitter programme

# Module os
import os
os.getcwd()      # Répertoire actuel
os.listdir()     # Liste fichiers
```

---

## 🚕 CONNEXION VTC

**Pendant tes trajets, pense à :**

### Scénario 1 : Tarif selon distance
```
if distance < 5:
    tarif = 15  # Course courte
elif distance < 20:
    tarif = distance * 2
else:
    tarif = distance * 1.8  # Réduction longue distance
```

### Scénario 2 : Validation client
```
# Vérifier si client est premium
if client_type == "premium" and trajets > 10:
    reduction = 0.20
elif client_type == "premium":
    reduction = 0.10
else:
    reduction = 0
```

### Scénario 3 : Aléatoire embouteillages
```
import random

# Simulation embouteillage aléatoire
if random.randint(1, 10) > 7:
    print("Embouteillage ! +15 min")
    temps_trajet = temps_trajet + 15
```

**→ Connexion métier = meilleure mémorisation ! 🧠**

---

## 💡 ASTUCE DU JOUR

**Mémoriser opérateurs logiques :**

```
AND = ET = Strict (TOUT doit être vrai)
    True and True = True
    True and False = False ✅ UN False suffit !

OR = OU = Souple (au moins UN vrai)
    False or False = False
    False or True = True ✅ UN True suffit !

NOT = INVERSE
    not True = False
    not False = True
```

**Mnémotech VTC :**
- **AND** = Client ET carte bancaire (les 2 obligatoires)
- **OR** = Espèces OU carte (un des deux suffit)
- **NOT** = Inverse disponibilité (pas disponible = occupé)

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Opérateurs logiques compris (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Code VTC visualisé (10 min)

**Total : 30 min ✅**

---

## 🎯 POURQUOI CES SECTIONS ?

**Sections 21-23 = BASE de la logique de programmation !**

- ✅ Conditions = 90% des programmes
- ✅ Erreurs = comprendre bugs
- ✅ Modules = réutiliser du code

**→ Fondations critiques ! 💪**

---

## 🤲 RAMADAN

**Jour VTC 2/4 :**
- 30 min révision MAX
- Pas de pression
- Continuer doucement

**→ La régularité gagne ! 🌙**

---

## 💤 BONNE JOURNÉE DEMAIN !

**Ramadan Moubarak ! 🤲**

**Bon courage VTC ! 🚕**

**À samedi pour Fiche 3 ! 💪**
