# 📚 FICHE RÉVISION - Samedi 8 Mars 2026 (Jour VTC)

**Durée : 20-30 min maximum**  
**Sections à réviser : 24-25 (Listes, Méthodes)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Comment créer une liste vide ?  
   **R:** `ma_liste = []`

2. **Q:** Accéder au 1er élément ? Au dernier ?  
   **R:** `liste[0]` pour 1er, `liste[-1]` pour dernier

3. **Q:** Slice pour 3 premiers éléments ?  
   **R:** `liste[:3]`

4. **Q:** Slice pour tout sauf premier et dernier ?  
   **R:** `liste[1:-1]`

5. **Q:** Comment inverser une liste ?  
   **R:** `liste[::-1]` ou `liste.reverse()`

6. **Q:** Différence append() vs insert() ?  
   **R:** append ajoute à la fin, insert à une position spécifique

7. **Q:** Différence remove() vs pop() ?  
   **R:** remove enlève par valeur, pop par index

8. **Q:** Différence sort() vs sorted() ?  
   **R:** sort modifie la liste, sorted retourne nouvelle liste

9. **Q:** Différence méthode vs fonction ?  
   **R:** Méthode = `objet.methode()`, Fonction = `fonction(objet)`

10. **Q:** Objets muables vs immuables : liste ?  
    **R:** Liste = muable (modifiable)

### Lecture Rapide (5 min)

**Relis mentalement :**

```python
# Listes
courses = ["Paris-CDG", "CDG-Paris"]
courses.append("Boulogne-Neuilly")
courses.remove("CDG-Paris")
courses[0]  # "Paris-CDG"
courses[-1]  # "Boulogne-Neuilly"
```

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Résultat de `len([1, [2, 3], 4])` ?**
   <details><summary>Réponse</summary>3 (la sous-liste = 1 élément)</details>

2. **Que fait `liste[1:4]` sur `[0,1,2,3,4,5]` ?**
   <details><summary>Réponse</summary>[1, 2, 3] (indices 1, 2, 3 - pas 4)</details>

3. **Différence entre ces deux ?**
   ```python
   liste.append(4)
   liste.insert(0, 4)
   ```
   <details><summary>Réponse</summary>append ajoute à la fin, insert au début (index 0)</details>

4. **Que retourne `"a,b,c".split(",")` ?**
   <details><summary>Réponse</summary>['a', 'b', 'c']</details>

5. **Comment compter combien de fois "Paris" apparaît ?**
   <details><summary>Réponse</summary>liste.count("Paris")</details>

### Visualisation Code (10 min)

**Visualise ce code VTC :**

```python
# Gestion courses journée
courses = []

# Ajouter courses matin
courses.append("Paris-CDG")
courses.append("CDG-Paris")
courses.append("Paris-Versailles")

# Client annule 2e course
courses.remove("CDG-Paris")

# Insérer course urgente au début
courses.insert(0, "URGENT-Hôpital")

# Afficher toutes les courses
for course in courses:
    print(course)

# Combien de courses Paris-XXX ?
paris_courses = [c for c in courses if "Paris" in c]
print(f"Courses Paris : {len(paris_courses)}")

# Dernière course du jour
print(f"Dernière : {courses[-1]}")
```

**Questions à te poser :**
- ✅ Ordre final des courses ?
- ✅ Combien de courses au total ?
- ✅ Quelle est la première course ?
- ✅ Combien contiennent "Paris" ?

---

## 📖 CONCEPTS CLÉS SECTIONS 24-25

### Listes (Section 24)

```python
# Création
ma_liste = [1, 2, 3]
vide = []

# Accès
liste[0]      # Premier (index 0)
liste[-1]     # Dernier
liste[1]      # Deuxième
len(liste)    # Longueur

# Slices [début:fin:pas]
liste[:3]     # 3 premiers
liste[3:]     # À partir du 4e
liste[1:-1]   # Sans premier et dernier
liste[::-1]   # Inversé
liste[::2]    # Un sur deux

# Modification
liste.append(4)       # Ajoute à la fin
liste.insert(0, 0)    # Insère à index
liste.remove(2)       # Enlève par valeur
liste.pop(0)          # Enlève par index et retourne
liste.clear()         # Vide tout
liste.reverse()       # Inverse sur place
liste.sort()          # Trie sur place

# Opérations
3 in liste           # Vérifier présence
liste.index("Max")   # Position
liste.count(3)       # Nombre occurrences
sorted(liste)        # Trie (nouvelle liste)

# Transformer
"a,b,c".split(",")   # String → Liste
",".join(liste)      # Liste → String
```

### Méthodes vs Fonctions (Section 25)

```python
# MÉTHODE (avec point)
liste.append(x)      # Modifie liste
texte.upper()        # Retourne nouveau texte

# FONCTION (sans point)
len(liste)           # Compte éléments
sorted(liste)        # Retourne nouvelle liste
sum(liste)           # Somme
min(liste), max(liste)  # Min et max

# MUABLE (modifiable)
liste = [1, 2, 3]
liste[0] = 10        # ✅ OK
dictionnaire["a"] = 1  # ✅ OK

# IMMUABLE (non modifiable)
texte = "hello"
texte[0] = "H"       # ❌ TypeError
nombre = 5
nombre[0] = 1        # ❌ TypeError
```

---

## 🚕 CONNEXION VTC

**Pendant tes trajets, visualise :**

### Scénario 1 : Trajets fréquents
```python
trajets = ["CDG", "Orly", "CDG", "Versailles", "CDG"]

# Compter CDG
nb_cdg = trajets.count("CDG")  # 3

# Trajets uniques
uniques = list(set(trajets))  # ['CDG', 'Orly', 'Versailles']
```

### Scénario 2 : Organisation courses
```python
courses = []

# Matin
courses.append("8h - Paris-CDG")
courses.append("10h - CDG-Paris")

# Midi - Course urgente en premier
courses.insert(0, "12h - URGENT Hôpital")

# Soir
courses.append("18h - Gare-Domicile")

# Dernière course
print(courses[-1])  # "18h - Gare-Domicile"
```

### Scénario 3 : Filtrer par zone
```python
courses = [
    "Paris-Neuilly",
    "Versailles-Paris", 
    "Paris-Boulogne",
    "Orly-Paris"
]

# Courses vers Paris
vers_paris = [c for c in courses if "Paris" in c.split("-")[1]]
# ['Versailles-Paris', 'Orly-Paris']
```

**→ Applications concrètes VTC ! 🚕**

---

## 💡 ASTUCE DU JOUR

**Visualiser les SLICES comme des frontières :**

```
Frontières :  |  A  |  B  |  C  |  D  |
Index :       0     1     2     3     4

liste[:2]     → Frontière 0 à 2 → A, B
liste[1:3]    → Frontière 1 à 3 → B, C
liste[2:]     → Frontière 2 à fin → C, D
liste[:-1]    → Début à avant-dernière frontière → A, B, C
```

**Mnémotech :** 
- `:3` = "jusqu'à la frontière 3" (pas "3 éléments")
- `1:` = "à partir de la frontière 1"

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Slices comprises (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Code VTC visualisé (10 min)

**Total : 30 min ✅**

---

## 🎯 POURQUOI CES SECTIONS ?

**Listes = structure de données #1 en Python !**

- ✅ 80% des programmes utilisent des listes
- ✅ Base pour dictionnaires, tuples, sets
- ✅ Indispensable pour tout projet

**→ Maîtriser maintenant = gagner du temps après ! 💪**

---

## 🤲 RAMADAN

**Jour VTC 3/4 :**
- 30 min révision
- Presque fini !
- Dernier effort demain

**→ Tu assures ! 🌙**

---

## 💤 BONNE JOURNÉE DEMAIN !

**Ramadan Moubarak ! 🤲**

**Courage VTC ! 🚕**

**Dernière fiche demain ! 💪**
