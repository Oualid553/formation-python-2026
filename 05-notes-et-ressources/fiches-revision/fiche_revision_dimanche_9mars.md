# 📚 FICHE RÉVISION - Dimanche 9 Mars 2026 (Jour VTC)

**Durée : 20-30 min maximum**  
**Sections à réviser : 26-28 (Boucles, Exercices, Calculatrice v2)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Syntaxe boucle while ?  
   **R:** `while condition: ... # Modifier condition !`

2. **Q:** Syntaxe boucle for ?  
   **R:** `for element in sequence: ...`

3. **Q:** Que fait `break` ?  
   **R:** Sort complètement de la boucle

4. **Q:** Que fait `continue` ?  
   **R:** Saute l'itération actuelle, continue la boucle

5. **Q:** `range(5)` génère quoi ?  
   **R:** 0, 1, 2, 3, 4

6. **Q:** `range(2, 7)` génère quoi ?  
   **R:** 2, 3, 4, 5, 6

7. **Q:** Syntaxe compréhension de liste simple ?  
   **R:** `[expression for element in liste]`

8. **Q:** Compréhension avec condition (filtrage) ?  
   **R:** `[x for x in liste if condition]`

9. **Q:** Opérateur ternaire dans compréhension ?  
   **R:** `[x if condition else y for x in liste]`

10. **Q:** Comment valider que input est un nombre ?  
    **R:** `if input_str.isdigit():`

### Lecture Rapide (5 min)

**Relis mentalement :**

```python
# Boucle while
i = 0
while i < 5:
    print(i)
    i += 1  # Important !

# Boucle for avec range
for i in range(3):
    print(i)  # 0, 1, 2
```

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Que fait ce code ?**
   ```python
   for i in range(5):
       if i == 3:
           break
       print(i)
   ```
   <details><summary>Réponse</summary>Affiche 0, 1, 2 (s'arrête à 3)</details>

2. **Et celui-ci ?**
   ```python
   for i in range(5):
       if i == 3:
           continue
       print(i)
   ```
   <details><summary>Réponse</summary>Affiche 0, 1, 2, 4 (saute 3)</details>

3. **Résultat de `[x*2 for x in range(3)]` ?**
   <details><summary>Réponse</summary>[0, 2, 4]</details>

4. **Résultat de `[x for x in range(10) if x%2==0]` ?**
   <details><summary>Réponse</summary>[0, 2, 4, 6, 8]</details>

5. **Pattern validation input nombre ?**
   <details><summary>Réponse</summary>
   ```python
   while True:
       x = input()
       if x.isdigit():
           x = int(x)
           break
   ```
   </details>

### Visualisation Code (10 min)

**Visualise ce code VTC :**

```python
# Calculateur revenus journée
courses_tarifs = []

while True:
    print("\n1: Ajouter course")
    print("2: Total journée")
    print("3: Quitter")
    
    choix = input("Choix : ")
    
    if choix == "1":
        tarif = input("Tarif course : ")
        
        # Validation
        while not tarif.isdigit():
            print("Entrez un nombre !")
            tarif = input("Tarif : ")
        
        courses_tarifs.append(int(tarif))
        print(f"✅ Course de {tarif}€ ajoutée")
    
    elif choix == "2":
        if courses_tarifs:
            # Compréhension de liste
            total = sum(courses_tarifs)
            nb_courses = len(courses_tarifs)
            moyenne = total / nb_courses
            
            print(f"\n📊 BILAN JOURNÉE")
            print(f"Courses : {nb_courses}")
            print(f"Total : {total}€")
            print(f"Moyenne : {moyenne:.2f}€")
            
            # Afficher détails
            for i, tarif in enumerate(courses_tarifs, start=1):
                print(f"  {i}. {tarif}€")
        else:
            print("Aucune course")
    
    elif choix == "3":
        print("Bonne route !")
        break
```

**Questions à te poser :**
- ✅ Combien de boucles while ?
- ✅ Où est utilisé enumerate ?
- ✅ Comment la validation fonctionne ?
- ✅ Que fait sum(courses_tarifs) ?

---

## 📖 CONCEPTS CLÉS SECTIONS 26-28

### Boucles (Section 26)

```python
# While - Tant que condition vraie
i = 0
while i < 5:
    print(i)
    i += 1  # ← CRUCIAL (sinon infini)

# For - Pour chaque élément
for fruit in fruits:
    print(fruit)

for i in range(10):
    print(i)  # 0 à 9

# break - SORTIR de boucle
for i in range(10):
    if i == 5:
        break  # Stop à 5

# continue - SAUTER itération
for i in range(10):
    if i == 5:
        continue  # Saute 5, continue

# enumerate - Index + valeur
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Compréhensions de liste
# Simple
[x*2 for x in range(5)]

# Filtrage (if à la fin)
[x for x in range(10) if x%2==0]

# Transformation (if...else au début)
[x if x>0 else 0 for x in liste]
```

### Validation Entrées (Section 28)

```python
# Pattern UNIVERSEL validation
while True:
    entree = input("Valeur : ")
    
    # Validation
    if entree.isdigit():
        entree = int(entree)  # ← Convertir !
        break
    else:
        print("Erreur, recommencez")

# Maintenant entree est un int ✅

# Validation avec plage
while True:
    choix = input("1-5 : ")
    
    if choix.isdigit() and 1 <= int(choix) <= 5:
        choix = int(choix)
        break
    else:
        print("Invalide")
```

---

## 🚕 CONNEXION VTC

**Synthèse 4 jours - Imagine ton app VTC complète :**

```python
import sys

# Données
COURSES = []
TARIFS = []

# Menu principal
while True:
    print("\n=== APP VTC ===")
    print("1: Ajouter course")
    print("2: Annuler course")
    print("3: Bilan journée")
    print("4: Fin de journée")
    print("5: Quitter")
    
    choix = input("Choix : ")
    
    # Validation (Section 21)
    if choix not in ["1","2","3","4","5"]:
        print("Invalide")
        continue
    
    # Ajouter (Sections 24-25)
    if choix == "1":
        course = input("Trajet : ")
        tarif = input("Tarif : ")
        
        # Validation (Section 28)
        while not tarif.isdigit():
            tarif = input("Tarif (nombre) : ")
        
        COURSES.append(course)
        TARIFS.append(int(tarif))
        
        # Afficher (Section 29)
        print("\nCourses du jour :")
        for i, c in enumerate(COURSES, start=1):
            print(f"{i}. {c} - {TARIFS[i-1]}€")
    
    # Bilan (Section 26)
    elif choix == "3":
        if COURSES:  # Vérifier vide (Section 25)
            total = sum(TARIFS)
            nb = len(COURSES)
            
            print(f"\n📊 BILAN")
            print(f"Courses : {nb}")
            print(f"Revenus : {total}€")
            
            # Meilleure course (Section 26)
            max_tarif = max(TARIFS)
            index_max = TARIFS.index(max_tarif)
            print(f"Meilleure : {COURSES[index_max]} ({max_tarif}€)")
    
    # Quitter (Section 23)
    elif choix == "5":
        sys.exit()
```

**→ TOUT ce que tu as appris en 1 seul programme ! 🎯**

---

## 💡 ASTUCE DU JOUR

**Différencier les boucles :**

```
WHILE = "TANT QUE"
→ Utilise quand tu ne sais pas combien d'itérations
→ Exemple : validation input (until correct)

FOR = "POUR CHAQUE"
→ Utilise quand tu connais la séquence
→ Exemple : parcourir liste, range connu
```

**Mnémotech VTC :**
- **WHILE** = Attendre client (tant qu'il n'arrive pas)
- **FOR** = Liste de courses (pour chaque course)

---

## 🎯 SYNTHÈSE 4 JOURS

**Tu as révisé TOUTES les bases Python ! 🏆**

| Jour | Sections | Concepts |
|------|----------|----------|
| Jeu 6 | 29 | Menu, enumerate, validation liste |
| Ven 7 | 21-23 | Conditions, erreurs, modules |
| Sam 8 | 24-25 | Listes, méthodes, muable/immuable |
| **Dim 9** | **26-28** | **Boucles, compréhensions, validation** |

**→ Fondations COMPLÈTES ! 💪**

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Boucles comprises (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] App VTC complète visualisée (10 min)

**Total : 30 min ✅**

---

## 🎊 BRAVO POUR CES 4 JOURS !

**Tu as maintenu ta continuité pendant le VTC ! 💪**

**4 jours × 30 min = 2h de révision**

**→ Pas de régression, concepts ancrés ! 🔥**

---

## 🚀 DEMAIN = RETOUR AU CODE !

**Lundi 9 mars - Prochaine session :**
- Section 30 : Projet Nombre Mystère
- 3-4h de code
- Nouveau projet VTC

**→ Tu vas reprendre en force ! 💪**

---

## 🤲 RAMADAN MOUBARAK !

**Dernier jour VTC de ce cycle ! 🚕**

**Félicitations pour ta régularité ! 🏆**

**Profite de ta journée ! 🌙**

**À demain pour coder ! 🚀**

---

**4/4 JOURS RÉVISÉS ! TU AS ASSURÉ ! 🎉💪🔥**
