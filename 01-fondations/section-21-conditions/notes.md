# Section 21 - Les Structures Conditionnelles

**Date :** 17 février 2026  
**Statut :** ✅ Validée  
**Temps :** ~2h

---

## 📚 Contenu

- Vidéo 126 : Introduction
- Vidéo 127 : Sources
- Vidéo 128 : Introduction aux conditions
- Vidéo 129 : Tester une condition avec if
- Quiz 12 : 5/5 (100%) ✅
- Vidéo 130 : Les blocs d'instructions
- Quiz 13 : 4/4 (100%) ✅
- Vidéo 131 : La guerre espaces/tabulations
- Exercice 15 : Structure simple ✅
- Exercice 16 : Structure simple ✅
- Vidéo 132 : Tester plusieurs conditions
- Vidéo 133 : Structure avec else
- Quiz 14 : 3/4 (75%) ⚠️
- Vidéo 134 : Opérateurs ternaires
- Vidéo 135 : Opérateurs logiques
- Quiz 15 : 3/3 (100%) ✅
- Exercice 17 : Structure avancée ✅
- Vidéo 136 : Solution exercice 17
- Vidéo 137 : Erreurs courantes
- Exercice 4 : Opérateurs logiques ✅
- Vidéo 138 : Fiche récapitulative

---

## 🔑 1. STRUCTURE IF SIMPLE

```python
age = 19

if age >= 18:
    print("Vous êtes majeur !")
# → "Vous êtes majeur !"
```

**Règles :**
- `:` obligatoire après la condition
- Indentation 4 espaces obligatoire
- Si condition False → rien ne s'affiche

---

## 🔑 2. IF / ELIF / ELSE

```python
note = 12

if note >= 18:
    print("Excellent")
elif note >= 14:
    print("Bien")
elif note >= 10:
    print("Moyen")
else:
    print("Insuffisant")
# → "Moyen"
```

**Règles :**
- Python teste dans l'ordre, s'arrête à la PREMIÈRE condition vraie
- `else` = si AUCUNE condition n'est vraie
- `else` appartient au `if` directement au-dessus de lui

---

## 🔑 3. OPÉRATEUR TERNAIRE

```python
# Format : valeur_si_vrai if condition else valeur_si_faux
statut = "Majeur" if age >= 18 else "Mineur"
tarif = 2.5 if heure < 22 else 3.0  # Exemple VTC nuit
```

**Utilisation :** Conditions simples sur une seule ligne

---

## 🔑 4. OPÉRATEURS LOGIQUES

```python
# AND : Les DEUX conditions doivent être vraies
if age >= 18 and permis == True:
    print("Peut conduire")

# OR : AU MOINS UNE condition vraie
if ville == "Paris" or ville == "Lyon":
    print("Grande ville")

# NOT : INVERSE la condition
if not en_service:
    print("Chauffeur disponible")
```

### Exercice 4 - Résultats (7/7 = 100% ✅)

```python
True or False                           # True
False and True                          # False
False and False and True                # False
True or True or False and True or False # True
True and False and False                # False
(True and False) or True                # True
True and (False or True)                # True
```

---

## ⚠️ 5. ERREURS COURANTES (Vidéo 137)

### Erreur 1 : = au lieu de ==
```python
if age = 18:    # ❌ SyntaxError !
if age == 18:   # ✅ Correct
```

### Erreur 2 : Plusieurs if au lieu de elif
```python
# ❌ MAUVAIS : 3 structures indépendantes
if note >= 14:
    print("Bien")
if note >= 10:
    print("Moyen")       # S'affiche même si "Bien" affiché !
if note < 10:
    print("Insuffisant")

# ✅ CORRECT : Une seule structure
if note >= 14:
    print("Bien")
elif note >= 10:
    print("Moyen")       # Ne s'affiche que si note < 14
else:
    print("Insuffisant")
```

### Erreur 3 : else appartient au mauvais if
```python
# ❌ PIÈGE : else appartient au dernier if, pas au premier
if note < 10:
    print("Insuffisant")
if note >= 10 and note < 14:
    print("Moyen")
if note >= 14:
    print("Bien")
else:
    print("Vous êtes le meilleur !")  # ← S'affiche si note < 14 !!
```

---

## 💡 6. LEÇON CLÉ - ORDRE DES ELIF

```python
# Python s'arrête à la PREMIÈRE condition vraie !
# → Pas besoin de "and" dans la plupart des cas
# → "and" uniquement si deux plages se chevauchent

# EXEMPLE : note >= 18 attrape aussi le 20 !
elif note >= 18 and note < 20:  # "and" NÉCESSAIRE ici
    commentaire = "Excellent !!"
elif note == 20:
    commentaire = "C'est un sans faute !"
```

---

## 🚕 APPLICATION VTC

```python
distance = 15.5
heure = 23

tarif = distance * 2.0

# Supplément nuit
if heure >= 22 or heure <= 6:
    tarif *= 1.15

# Tarif final
print(f"Tarif : {tarif:.2f} €")
```

---

## 📊 Scores

| Élément | Score | Statut |
|---------|-------|--------|
| Quiz 12 | 5/5 (100%) | ✅ |
| Quiz 13 | 4/4 (100%) | ✅ |
| Quiz 14 | 3/4 (75%) | ⚠️ |
| Quiz 15 | 3/3 (100%) | ✅ |
| Exercice 15 | 100% | ✅ |
| Exercice 16 | 100% | ✅ |
| Exercice 17 | Compris avec aide | ✅ |
| Exercice 4 | 7/7 (100%) | ✅ |
| **Moyenne** | **96%** | ✅ |

### Erreur Quiz 14
- Question : Variable `a` déclarée mais `age` utilisée
- Leçon : Toujours vérifier que les variables utilisées sont bien déclarées !

### Difficultés Exercice 17
- Erreur 1 : Modifié les conditions avec `and` (interdit par consigne)
- Erreur 2 : Double `print()` mal placé
- Erreur 3 : `sys.argv` mal compris → besoin terminal pas bouton Play
- Leçon : Lire la consigne entièrement avant de coder !

---

## ✅ Section validée le 17 février 2026

**Prêt pour Section 22 : Les erreurs que vous allez rencontrer**