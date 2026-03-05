# 📚 FICHE RÉVISION - Jeudi 6 Mars 2026 (Jour VTC)

**Durée : 20-30 min maximum**  
**Section à réviser : 29 (Projet Liste de Courses)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Syntaxe menu interactif avec while ?  
   **R:** `while True: print(menu); choix = input(); if/elif/else`

2. **Q:** Comment valider un choix parmi ["1", "2", "3"] ?  
   **R:** `if choix not in ["1", "2", "3"]: print("Invalide"); continue`

3. **Q:** Syntaxe enumerate() avec start ?  
   **R:** `for index, item in enumerate(liste, start=1):`

4. **Q:** Différence append() vs remove() vs clear() ?  
   **R:** append = ajoute, remove = retire par valeur, clear = vide tout

5. **Q:** Comment vérifier si élément existe dans liste ?  
   **R:** `if element in liste:`

6. **Q:** Vérifier liste vide : deux méthodes ?  
   **R:** `if liste:` ou `if len(liste) == 0:`

7. **Q:** Quelle méthode plus pythonique pour liste vide ?  
   **R:** `if liste:` (plus simple et pythonique)

8. **Q:** Comment quitter programme proprement ?  
   **R:** `import sys` puis `sys.exit()`

9. **Q:** Différence `continue` vs `break` ?  
   **R:** continue = saute itération, break = sort de boucle

10. **Q:** Structure if/elif/else pour menu 5 choix ?  
    **R:** `if choix == "1": ... elif choix == "2": ... elif choix == "5": sys.exit()`

### Lecture Rapide (5 min)

**Relis mentalement la structure d'un menu interactif :**

```python
while True:
    # Afficher menu
    choix = input()
    # Valider
    if invalide:
        continue
    # Actions
    if choix == "1":
        # Faire action
    elif choix == "5":
        sys.exit()
```

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Comment ajouter "Pomme" à une liste ?**
   <details><summary>Réponse</summary>liste.append("Pomme")</details>

2. **Comment retirer "Pomme" d'une liste ?**
   <details><summary>Réponse</summary>liste.remove("Pomme")</details>

3. **Comment afficher liste avec numéros 1, 2, 3 ?**
   <details><summary>Réponse</summary>
   ```python
   for index, item in enumerate(liste, start=1):
       print(f"{index}. {item}")
   ```
   </details>

4. **Que fait `continue` dans une boucle while ?**
   <details><summary>Réponse</summary>Retourne au début de la boucle (recommence)</details>

5. **Comment vider complètement une liste ?**
   <details><summary>Réponse</summary>liste.clear()</details>

### Visualisation Code (10 min)

**Visualise mentalement ce programme :**

```python
# Menu VTC
COURSES = []

while True:
    print("1: Ajouter course")
    print("2: Afficher")
    print("3: Quitter")
    
    choix = input("Choix : ")
    
    if choix not in ["1", "2", "3"]:
        print("Invalide")
        continue
    
    if choix == "1":
        course = input("Trajet : ")
        COURSES.append(course)
        
        for i, c in enumerate(COURSES, start=1):
            print(f"{i}. {c}")
    
    elif choix == "2":
        if COURSES:
            for i, c in enumerate(COURSES, start=1):
                print(f"{i}. {c}")
        else:
            print("Vide")
    
    elif choix == "3":
        sys.exit()
```

**Questions à te poser :**
- ✅ Que fait chaque partie ?
- ✅ Pourquoi `continue` après validation ?
- ✅ Pourquoi `start=1` dans enumerate ?
- ✅ Que se passe si liste vide au choix 2 ?

---

## 📖 CONCEPTS CLÉS SECTION 29

### Menu Interactif
```python
while True:
    # Menu
    # Input
    # Validation
    # Actions selon choix
```

### Validation par Liste
```python
choix_valides = ["1", "2", "3", "4", "5"]
if choix not in choix_valides:
    print("Invalide")
    continue  # Recommence la boucle
```

### enumerate() - Numérotation Auto
```python
# Sans enumerate (compliqué)
for i in range(len(liste)):
    print(f"{i+1}. {liste[i]}")

# Avec enumerate (simple ✅)
for index, item in enumerate(liste, start=1):
    print(f"{index}. {item}")
```

### Gestion Liste
```python
# Ajouter
liste.append(element)

# Retirer par valeur
liste.remove(element)

# Vider
liste.clear()

# Vérifier existence
if element in liste:
    print("Existe")

# Vérifier vide (pythonique)
if liste:
    print("A des éléments")
else:
    print("Vide")
```

### Quitter Proprement
```python
import sys

# Dans le code
sys.exit()  # Arrête tout le programme
```

---

## 🚕 CONNEXION VTC - Pense à ça pendant tes trajets !

**Pendant que tu conduis, visualise mentalement :**

### Scénario 1 : Ajouter une course
```
Menu affiché
→ Choix 1
→ Input "Paris-CDG"
→ Ajout à la liste
→ Affichage avec enumerate
→ Retour au menu
```

### Scénario 2 : Validation erreur
```
Menu affiché
→ Choix "abc"
→ Validation échoue
→ Message "Invalide"
→ continue
→ Retour au menu
```

### Scénario 3 : Liste vide
```
Menu affiché
→ Choix 2 (Afficher)
→ Vérif : if COURSES
→ Liste vide → "Aucune course"
→ Retour au menu
```

**→ Révision active même sans ordinateur ! 🧠**

---

## 💡 ASTUCE DU JOUR

**Pattern UNIVERSEL des menus interactifs :**

```python
# 1. Données
DATA = []

# 2. Boucle infinie
while True:
    
    # 3. Menu
    print("Options...")
    
    # 4. Input
    choix = input()
    
    # 5. Validation
    if invalide:
        continue
    
    # 6. Actions
    if choix == "1":
        # Ajouter
    elif choix == "2":
        # Afficher
    elif choix == "fin":
        break
```

**Ce pattern fonctionne pour TOUT ! 🎯**

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Structure menu visualisée (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Code visualisé mentalement (10 min)

**Total : 30 min maximum ✅**

---

## 🎯 POURQUOI CETTE RÉVISION ?

**Section 29 est CRUCIALE car :**
- ✅ Base de tous les programmes interactifs
- ✅ Pattern réutilisé dans TOUS les projets futurs
- ✅ enumerate() utilisé constamment
- ✅ Validation = sécurité des programmes

**→ Bien ancrer ces concepts maintenant ! 💪**

---

## 🤲 ADAPTATION RAMADAN

**Aujourd'hui c'est un jour VTC :**
- ⏰ 20-30 min révision MAX
- 🚫 PAS de nouveau code
- ✅ Juste maintenir la continuité
- 💪 Santé et travail prioritaires

**→ Doucement mais sûrement ! 🌙**

---

## 🔄 DEMAIN (Vendredi 7 mars)

**Même routine :**
- Fiche révision Jour 2 (disponible demain)
- 20-30 min
- Flashcards + visualisation

**→ Continuer la régularité ! 💪**

---

## 💤 BON COURAGE POUR DEMAIN !

**Ramadan Moubarak ! 🤲**

**Bonne journée VTC ! 🚕💨**

**Ces 30 min de révision vont maintenir ton niveau ! 🔥**

---

**Prochaine session code : Lundi 9 mars (Section 30) 🚀**
