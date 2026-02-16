# Cheatsheet : Méthodes Strings

**Section 17 - Manipuler les chaînes de caractères**  
**Date :** 16 février 2026  
**Mise à jour :** Après Quiz 9 (7/8 - 87.5%)

---

## 📚 TABLE DES MATIÈRES

1. [Casse (Majuscules/Minuscules)](#casse)
2. [Remplacement](#remplacement)
3. [Nettoyer (Strip)](#nettoyer)
4. [Séparer et Joindre](#separer-joindre)
5. [Remplir de zéros](#zeros)
6. [Validation (is...)](#validation)
7. [Compter](#compter)
8. [Trouver](#trouver)
9. [Début/Fin](#debut-fin)
10. [Règles importantes](#regles)

---

<a name="casse"></a>
## 🔤 1. CASSE (Majuscules/Minuscules)

### Méthodes disponibles

| Méthode | Action | Exemple | Résultat |
|---------|--------|---------|----------|
| `.upper()` | TOUT EN MAJUSCULES | `"bonjour".upper()` | `"BONJOUR"` |
| `.lower()` | tout en minuscules | `"BONJOUR".lower()` | `"bonjour"` |
| `.title()` | Première Lettre De Chaque Mot | `"bonjour tout le monde".title()` | `"Bonjour Tout Le Monde"` |
| `.capitalize()` | Première lettre uniquement | `"bonjour tout le monde".capitalize()` | `"Bonjour tout le monde"` |
| `.swapcase()` | Inverse la casse | `"Hello World".swapcase()` | `"hELLO wORLD"` |

### Cas d'usage

**upper() :**
- Affichage web (titres, boutons)
- Uniformiser pour comparaisons
- Formats de fichiers (extensions)

**lower() :**
- Recherche insensible à la casse
- Normaliser entrées utilisateur
- Comparaisons de chaînes

**title() :**
- Titres de livres, films
- Noms propres
- En-têtes

**capitalize() :**
- Début de phrase
- Formatage de texte

### Exemples pratiques
```python
# Normaliser nom client
nom = "PIERRE"
nom_propre = nom.title()  # "Pierre"

# Recherche insensible à la casse
recherche = "PYTHON"
texte = "J'apprends Python"
if recherche.lower() in texte.lower():
    print("Trouvé !")

# Uniformiser extension fichier
fichier = "IMAGE.PNG"
if fichier.lower().endswith(".png"):
    print("C'est un PNG")
```

---

<a name="remplacement"></a>
## 🔄 2. REMPLACEMENT

### Méthode replace()

| Syntaxe | Action | Exemple |
|---------|--------|---------|
| `.replace(old, new)` | Remplace TOUTES les occurrences | `"bonjour".replace("jour", "soir")` → `"bonsoir"` |
| `.replace(old, new, count)` | Remplace X fois | `"aaa".replace("a", "b", 2)` → `"bba"` |

### Points importants

**⚠️ Remplace TOUTES les occurrences par défaut**
```python
"bonjour bonjour".replace("jour", "soir")
# → "bonsoir bonsoir" (les DEUX occurrences)
```

**Peut enchaîner plusieurs replace :**
```python
"bonjour bonjour".replace(" ", "").replace("jour", "soir")
# → "bonsoirbonsoir"
```

**Pour enlever un caractère :**
```python
"a-b-c".replace("-", "")  # "abc"
```

### Exemples pratiques
```python
# Anonymiser données
telephone = "06 12 34 56 78"
masque = telephone.replace("12 34", "XX XX")  # "06 XX XX 56 78"

# Nettoyer données CSV
data = "Pierre, , Paris"
propre = data.replace(", ,", ",")  # "Pierre, Paris"

# Remplacer un nombre limité de fois
texte = "Python Python Python"
texte.replace("Python", "Java", 2)  # "Java Java Python"
```

---

<a name="nettoyer"></a>
## 🧹 3. NETTOYER (Strip)

### Méthodes disponibles

| Méthode | Action | Exemple |
|---------|--------|---------|
| `.strip()` | Enlève espaces début ET fin | `"  hello  ".strip()` → `"hello"` |
| `.strip(chars)` | Enlève caractères spécifiés | `"  bonjour  ".strip(" ujor")` → `"bon"` |
| `.rstrip()` | Enlève à DROITE uniquement | `"  hello  ".rstrip()` → `"  hello"` |
| `.lstrip()` | Enlève à GAUCHE uniquement | `"  hello  ".lstrip()` → `"hello  "` |

### ⚠️ IMPORTANT : Comment strip() fonctionne

**Strip analyse caractère par caractère, PAS la chaîne entière !**
```python
"  bonjour  ".strip(" ujor")

# Depuis GAUCHE :
# - Espace ? Oui, dans " ujor" → Enlève
# - Espace ? Oui, dans " ujor" → Enlève  
# - "b" ? Non, pas dans " ujor" → STOP

# Depuis DROITE :
# - Espace ? Oui → Enlève
# - Espace ? Oui → Enlève
# - "r" ? Oui, dans " ujor" → Enlève
# - "u" ? Oui, dans " ujor" → Enlève
# - "o" ? Oui, dans " ujor" → Enlève
# - "j" ? Oui, dans " ujor" → Enlève
# - "n" ? Non, pas dans " ujor" → STOP

# Résultat : "bon"
```

**L'ordre des caractères dans strip() n'a PAS d'importance !**
```python
"  hello  ".strip(" helo")  # ""
"  hello  ".strip(" oleh")  # "" (même résultat)
```

### Exemples pratiques
```python
# Nettoyer input utilisateur
nom = input("Nom : ")  # "  Pierre  "
nom_propre = nom.strip()  # "Pierre"

# Enlever ponctuation début/fin
phrase = "...Bonjour!!!..."
propre = phrase.strip(".!")  # "Bonjour"

# Nettoyer uniquement à droite
chemin = "/home/user/documents/"
sans_slash = chemin.rstrip("/")  # "/home/user/documents"
```

---

<a name="separer-joindre"></a>
## ✂️ 4. SÉPARER ET JOINDRE

### Split - Séparer

| Méthode | Action | Exemple |
|---------|--------|---------|
| `.split()` | Sépare sur espaces | `"a b c".split()` → `['a', 'b', 'c']` |
| `.split(sep)` | Sépare sur séparateur | `"a,b,c".split(",")` → `['a', 'b', 'c']` |

**💡 split() : STRING → LISTE**
```python
# Sans argument : sépare sur espaces
"hello world".split()  # ['hello', 'world']

# Avec séparateur
"16/02/2026".split("/")  # ['16', '02', '2026']
"a,b,c".split(",")  # ['a', 'b', 'c']
```

### Join - Joindre

| Syntaxe | Action | Exemple |
|---------|--------|---------|
| `sep.join(liste)` | Joint avec séparateur | `" ".join(['a', 'b'])` → `"a b"` |

**💡 join() : LISTE → STRING**

**⚠️ SYNTAXE : "séparateur".join(liste)**
```python
# Avec espace
" ".join(['a', 'b', 'c'])  # "a b c"

# Avec virgule
",".join(['a', 'b', 'c'])  # "a,b,c"

# Avec tiret
"-".join(['16', '02', '2026'])  # "16-02-2026"
```

### ⚠️ PIÈGES FRÉQUENTS

**1. Join fonctionne UNIQUEMENT avec des chaînes !**
```python
# ❌ ERREUR
"-".join([1, 2, 3])  # TypeError

# ✅ CORRECT
"-".join(['1', '2', '3'])  # "1-2-3"

# ✅ Convertir les nombres
"-".join([str(x) for x in [1, 2, 3]])  # "1-2-3"
```

**2. Syntaxe inversée (séparateur d'abord)**
```python
# ❌ Ce qu'on voudrait écrire
['a', 'b'].join(",")  # N'existe pas !

# ✅ La vraie syntaxe
",".join(['a', 'b'])  # "a,b"
```

### Combo Split + Join

**Remplacer un séparateur par un autre :**
```python
# Remplacer espaces par tirets
"a b c".split(" ")  # ['a', 'b', 'c']
"-".join("a b c".split(" "))  # "a-b-c"

# En une ligne
"-".join("a b c".split())  # "a-b-c"
```

### Exemples pratiques VTC
```python
# Parser données CSV
donnees = "Pierre,15.5,25,oui"
infos = donnees.split(",")
# ['Pierre', '15.5', '25', 'oui']

nom = infos[0]  # "Pierre"
distance = float(infos[1])  # 15.5
duree = int(infos[2])  # 25

# Créer une date depuis composants
jour, mois, annee = "16", "02", "2026"
date = "/".join([jour, mois, annee])  # "16/02/2026"

# Nettoyer et reformater
texte = "  bonjour   tout   le   monde  "
mots = texte.split()  # ['bonjour', 'tout', 'le', 'monde']
propre = " ".join(mots)  # "bonjour tout le monde"
```

---

<a name="zeros"></a>
## 0️⃣ 5. REMPLIR DE ZÉROS

### Méthode zfill()

| Syntaxe | Action | Exemple |
|---------|--------|---------|
| `.zfill(width)` | Remplit de 0 à gauche jusqu'à width caractères | `"42".zfill(5)` → `"00042"` |

### Comment ça marche
```python
"9".zfill(4)    # "0009" (ajoute 3 zéros)
"99".zfill(4)   # "0099" (ajoute 2 zéros)
"999".zfill(4)  # "0999" (ajoute 1 zéro)
"9999".zfill(4) # "9999" (ne fait rien, déjà 4)
```

### ⚠️ Fonctionne UNIQUEMENT sur des chaînes !
```python
# ❌ ERREUR
42.zfill(5)  # AttributeError

# ✅ CORRECT
str(42).zfill(5)  # "00042"
```

### Cas d'usage

**Séquences numérotées :**
```python
for i in range(100):
    fichier = f"image_{str(i).zfill(4)}.png"
    print(fichier)
# image_0000.png
# image_0001.png
# ...
# image_0099.png
```

**IDs, codes :**
```python
id_course = "42"
id_formate = id_course.zfill(6)  # "000042"
```

---

<a name="validation"></a>
## ✅ 6. VALIDATION (Méthodes is...)

### Méthodes disponibles

| Méthode | Vérifie | Exemple |
|---------|---------|---------|
| `.isdigit()` | Que des chiffres ? | `"123".isdigit()` → `True` |
| `.isalpha()` | Que des lettres ? | `"abc".isalpha()` → `True` |
| `.isalnum()` | Lettres OU chiffres ? | `"abc123".isalnum()` → `True` |
| `.isspace()` | Que des espaces ? | `"   ".isspace()` → `True` |
| `.isupper()` | Tout majuscules ? | `"HELLO".isupper()` → `True` |
| `.islower()` | Tout minuscules ? | `"hello".islower()` → `True` |
| `.istitle()` | Format titre ? | `"Hello World".istitle()` → `True` |

### Points importants

**Retournent True ou False**

**⚠️ UN SEUL caractère différent = False**
```python
"123".isdigit()    # True
"123a".isdigit()   # False (à cause du "a")

"abc".isalpha()    # True
"abc1".isalpha()   # False (à cause du "1")
```

### Cas d'usage CRITIQUE : Valider avant conversion
```python
# ❌ DANGEREUX (peut crasher)
age = int(input("Âge : "))  # Si user tape "abc" → ValueError

# ✅ SÛR
user_input = input("Âge : ")
if user_input.isdigit():
    age = int(user_input)
    print(f"Vous avez {age} ans")
else:
    print("Erreur : entrez un nombre")
```

### Exemples pratiques
```python
# Valider code postal
code = "75001"
if code.isdigit() and len(code) == 5:
    print("Code postal valide")

# Vérifier format titre
titre = "Bonjour Tout Le Monde"
if titre.istitle():
    print("Format titre OK")

# Valider username (lettres et chiffres uniquement)
username = "user123"
if username.isalnum():
    print("Username valide")
```

---

<a name="compter"></a>
## 🔢 7. COMPTER

### Méthode count()

| Syntaxe | Action | Exemple |
|---------|--------|---------|
| `.count(sub)` | Compte occurrences de sub | `"hello".count('l')` → `2` |
| `.count(sub, start, end)` | Compte dans une portion | `"hello".count('l', 0, 3)` → `1` |

### ⚠️ PIÈGE : Compte les CARACTÈRES, pas les MOTS !
```python
"bonjour le jour".count("jour")  # 2 (pas 1 !)

# Trouve "jour" dans :
# 1. "bonJOUR"
# 2. "le jour"
```

### Solution pour compter les MOTS
```python
# Ajouter un espace avant
"bonjour le jour".count(" jour")  # 1

# Ou utiliser split()
phrase = "bonjour le jour"
mots = phrase.split()
mots.count("jour")  # 1
```

### Exemples pratiques
```python
# Compter lettres dans phrase
phrase = "Bonjour tout le monde"
nb_o = phrase.count('o')  # 3

# Compter mots
texte = "Python Python Java Python"
nb_python = texte.split().count("Python")  # 3

# Vérifier répétitions
password = "password123"
if password.count('s') > 2:
    print("Trop de 's'")
```

---

<a name="trouver"></a>
## 🔍 8. TROUVER

### Méthodes disponibles

| Méthode | Action | Retour si pas trouvé | Exemple |
|---------|--------|---------------------|---------|
| `.find(sub)` | Position de sub | **-1** | `"hello".find('e')` → `1` |
| `.rfind(sub)` | Position depuis la FIN | **-1** | `"bonjour le jour".rfind("jour")` → `11` |
| `.index(sub)` | Position de sub | **ERREUR** | `"hello".index('e')` → `1` |

### Différence find() vs index()
```python
# find() : retourne -1 si pas trouvé (PAS d'erreur)
"hello".find("x")  # -1

# index() : lève une ERREUR si pas trouvé
"hello".index("x")  # ValueError: substring not found
```

**Quand utiliser quoi ?**

- **find()** : Si tu veux gérer toi-même le cas "pas trouvé"
- **index()** : Si tu veux qu'une erreur arrête le programme
```python
# Avec find()
position = texte.find("mot")
if position != -1:
    print(f"Trouvé à la position {position}")
else:
    print("Pas trouvé")

# Avec index() + try/except
try:
    position = texte.index("mot")
    print(f"Trouvé à {position}")
except ValueError:
    print("Pas trouvé")
```

### find() vs rfind()
```python
texte = "bonjour le jour"

# find() : cherche depuis le DÉBUT
texte.find("jour")   # 3 (dans "bonJOUR")

# rfind() : cherche depuis la FIN
texte.rfind("jour")  # 11 (dans "le jour")
```

### Exemples pratiques
```python
# Vérifier présence
email = "user@example.com"
if email.find("@") != -1:
    print("Email valide")

# Extraire extension fichier
fichier = "image.png"
position = fichier.rfind(".")
if position != -1:
    extension = fichier[position:]  # ".png"

# Position pour découpage
url = "https://example.com/page"
debut_path = url.find("/", 8)  # Cherche "/" après "https://"
```

---

<a name="debut-fin"></a>
## 📍 9. DÉBUT/FIN

### Méthodes disponibles

| Méthode | Vérifie | Exemple |
|---------|---------|---------|
| `.startswith(sub)` | Commence par sub ? | `"image.png".startswith("image")` → `True` |
| `.endswith(sub)` | Finit par sub ? | `"image.png".endswith(".png")` → `True` |

### Vérifier extensions de fichiers
```python
fichier = "image.png"

# Extension simple
if fichier.endswith(".png"):
    print("C'est un PNG")

# Plusieurs extensions possibles
if fichier.endswith((".jpg", ".jpeg", ".png", ".gif")):
    print("C'est une image")
```

### Vérifier préfixes
```python
url = "https://example.com"

if url.startswith("https://"):
    print("Connexion sécurisée")
elif url.startswith("http://"):
    print("Connexion non sécurisée")
```

### ⚠️ Attention orthographe
```python
# ✅ CORRECT (avec S)
"hello".startswith("he")
"hello".endswith("lo")

# ❌ ERREUR (sans S)
"hello".startwith("he")  # AttributeError
```

### Exemples pratiques
```python
# Filtrer fichiers
fichiers = ["doc.pdf", "image.png", "video.mp4", "data.csv"]
images = [f for f in fichiers if f.endswith((".png", ".jpg"))]

# Vérifier format téléphone
tel = "06 12 34 56 78"
if tel.startswith("06") or tel.startswith("07"):
    print("Numéro mobile")

# Catégoriser URLs
url = "https://api.example.com/users"
if url.startswith("https://api."):
    print("Appel API")
```

---

<a name="regles"></a>
## 🎯 RÈGLES IMPORTANTES

### 1. Les méthodes NE MODIFIENT PAS l'original !
```python
texte = "hello"
texte.upper()  # ❌ Inutile (résultat perdu)
print(texte)   # "hello" (pas changé)

# ✅ STOCKER le résultat
nouveau = texte.upper()
print(nouveau)  # "HELLO"

# ✅ OU écraser l'original
texte = texte.upper()
print(texte)  # "HELLO"
```

### 2. Toujours vérifier le type avant conversion
```python
# ❌ DANGEREUX
age = int(input("Âge : "))  # Crash si non-numérique

# ✅ SÛR
user_input = input("Âge : ")
if user_input.isdigit():
    age = int(user_input)
```

### 3. Attention aux espaces avec split/join
```python
# split() enlève les espaces multiples
"a    b    c".split()  # ['a', 'b', 'c']

# split(" ") les garde
"a    b    c".split(" ")  # ['a', '', '', '', 'b', '', '', '', 'c']
```

### 4. Strip analyse caractère par caractère
```python
# Pas une chaîne entière, mais chaque caractère !
"hello".strip("helo")  # "" (tous les caractères enlevés)
```

---

## ⚡ ANTISÈCHE ULTRA-RAPIDE
```
CASSE:        upper() lower() title() capitalize()
REMPLACER:    replace(old, new)
NETTOYER:     strip() lstrip() rstrip()
SÉPARER:      split(sep) → liste
JOINDRE:      sep.join(liste) → string
ZÉROS:        zfill(width)
VALIDER:      isdigit() isalpha() isupper() islower()
COMPTER:      count(sub)
TROUVER:      find(sub) rfind(sub) index(sub)
DÉBUT/FIN:    startswith(sub) endswith(sub)

⚠️ Ne modifient PAS l'original → toujours stocker !
⚠️ join() que des strings dans la liste
⚠️ count() compte CARACTÈRES, pas mots
⚠️ strip() analyse caractère par caractère
```

---

## 🎓 SCORE QUIZ 9 : 7/8 (87.5%)

**Erreur identifiée :** Syntaxe `join()` avec les crochets `[]`

**Correction :**
```python
# Pour obtenir "1, 2, 3,"
", ".join(['1', '2', '3']) + ","

# Pas l'inverse !
```

---

**Dernière mise à jour :** 16 février 2026  
**Statut :** ✅ Section 17 maîtrisée