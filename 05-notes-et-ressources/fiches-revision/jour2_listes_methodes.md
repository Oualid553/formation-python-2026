# 📚 FICHE RÉVISION JOUR 2 - Vendredi 27 Février 2026

**Durée : 20-30 min**  
**Sections à réviser : 24-25 (Listes, Méthodes)**

---

## 🌅 MATIN (15 min) - Avant VTC

### Flashcards Anki (10 min)

**Créer/Réviser ces cartes :**

1. **Q:** Comment créer une liste vide ?  
   **R:** `ma_liste = []`

2. **Q:** Comment accéder au premier élément d'une liste ?  
   **R:** `ma_liste[0]`

3. **Q:** Comment accéder au dernier élément ?  
   **R:** `ma_liste[-1]`

4. **Q:** Différence entre `append()` et `insert()` ?  
   **R:** `append()` ajoute à la fin, `insert(index, valeur)` à une position

5. **Q:** Que retourne `ma_liste.sort()` ?  
   **R:** `None` (modifie la liste directement)

6. **Q:** Différence entre `sort()` et `sorted()` ?  
   **R:** `sort()` modifie, `sorted()` retourne nouvelle liste

7. **Q:** `liste[:3]` retourne quoi ?  
   **R:** Les 3 premiers éléments (indices 0, 1, 2)

8. **Q:** `liste[::-1]` fait quoi ?  
   **R:** Inverse la liste

9. **Q:** Comment transformer "a,b,c" en liste ?  
   **R:** `"a,b,c".split(",")`

10. **Q:** Différence méthode vs fonction ?  
    **R:** Méthode = `objet.methode()`, Fonction = `fonction(objet)`

### Lecture Cheatsheet (5 min)

**Relire :** `05-notes-et-ressources/cheatsheets/08-listes.md`

**Points clés à retenir :**
- Création et accès
- Slices [début:fin:pas]
- Méthodes principales (append, remove, pop)

---

## 🌙 SOIR (15 min) - Après VTC

### Quiz Mental (5 min) - Sans ordinateur !

**Réponds de tête :**

1. **Quel est le résultat de :**
   ```python
   liste = [1, 2, 3]
   liste.append(4)
   print(liste)
   ```
   <details><summary>Réponse</summary>[1, 2, 3, 4]</details>

2. **Que retourne `len([1, [2, 3], 4])` ?**
   <details><summary>Réponse</summary>3 (la sous-liste = 1 élément)</details>

3. **Que fait `liste[1:4]` sur `[0,1,2,3,4,5]` ?**
   <details><summary>Réponse</summary>[1, 2, 3] (indices 1, 2, 3 - pas 4)</details>

4. **Objets muables vs immuables : liste ?**
   <details><summary>Réponse</summary>Liste = muable (modifiable)</details>

5. **Comment inverser une liste ?**
   <details><summary>Réponse</summary>liste.reverse() ou liste[::-1]</details>

### Lecture Code (10 min)

**Relis ce code de ton Exercice 20 (Section 24) :**

```python
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]

trois_premiers = liste[:3]
trois_derniers = liste[-3:]
milieu = liste[1:-1]
premier_dernier = liste[::5]
```

**Questions à te poser :**
- ✅ Pourquoi `:3` et pas `[:2]` pour 3 éléments ?
- ✅ Que signifie `[-3:]` exactement ?
- ✅ Pourquoi `[1:-1]` exclut premier ET dernier ?
- ✅ Comment fonctionne le pas `::5` ?

---

## 📖 CONCEPTS CLÉS SECTIONS 24-25

### Section 24 : Listes

```python
# Création
ma_liste = [1, 2, 3]

# Accès
ma_liste[0]   # Premier
ma_liste[-1]  # Dernier
len(ma_liste) # Longueur

# Modification
ma_liste.append(4)      # Ajoute à la fin
ma_liste.insert(0, 0)   # Insère à position
ma_liste.remove(2)      # Enlève par valeur
ma_liste.pop(0)         # Enlève par index

# Slices [début:fin:pas]
liste[:3]      # 3 premiers
liste[3:]      # À partir du 4ème
liste[1:-1]    # Sans premier et dernier
liste[::-1]    # Inversé

# Opérateurs
3 in liste           # Vérifier présence
liste.index("Max")   # Position
liste.count(3)       # Nombre occurrences
```

### Section 25 : Méthodes vs Fonctions

```python
# MÉTHODE : objet.methode()
liste.append(x)
texte.upper()

# FONCTION : fonction(objet)
len(liste)
sorted(liste)

# MUABLE (modifiable)
liste[0] = 10  # ✅ OK
dictionnaire["a"] = 1  # ✅ OK

# IMMUABLE (non modifiable)
texte[0] = "B"  # ❌ TypeError
tuple[0] = 10   # ❌ TypeError
```

---

## 🚕 EXERCICE MENTAL VTC

**Imagine ce code pour tes courses VTC :**

```python
courses_jour = ["Paris-CDG", "CDG-Paris", "Paris-Versailles"]

# Comment ajouter une nouvelle course ?
courses_jour.append("Versailles-Paris")

# Comment compter combien de courses vers CDG ?
nombre_cdg = sum(1 for c in courses_jour if "CDG" in c)

# Comment afficher chaque course avec son numéro ?
for i, course in enumerate(courses_jour, start=1):
    print(f"Course {i}: {course}")
```

**Pense à ça pendant tes trajets ! 🧠**

---

## ✅ CHECKLIST FIN DE JOURNÉE

- [ ] Flashcards Anki révisées (10 min)
- [ ] Cheatsheet listes relu (5 min)
- [ ] Quiz mental fait (5 min)
- [ ] Code analysé (10 min)

**Total : 30 min ✅**

---

## 💡 ASTUCE DU JOUR

**Visualise les slices comme des "frontières" :**

```
    |  A  |  B  |  C  |  D  |
    ↑     ↑     ↑     ↑     ↑
    0     1     2     3     4

liste[:2]  # Coupe à frontière 2 → A, B
liste[1:3] # Frontières 1 à 3 → B, C
```

**Cette visualisation aide énormément ! 🎯**

---

**Demain : Fiche Jour 3 (Section 26 - Boucles) 📚**