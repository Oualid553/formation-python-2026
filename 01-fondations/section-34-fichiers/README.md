# Section 34 : Les Fichiers

**Date :** 12 mars 2026  
**Statut :** ✅ Complété 100%  
**Temps total :** ~2h  
**Difficulté :** ⭐⭐⭐ Moyenne-Haute

---

## 🎯 Objectifs de la section

Apprendre à manipuler des fichiers en Python :
- Lire et écrire des fichiers texte
- Comprendre les modes d'ouverture (`r`, `w`, `a`)
- Gérer les chemins de fichiers
- Travailler avec le format JSON
- Sauvegarder et charger des données structurées

---

## 📚 Concepts appris

### Fichiers texte

**Lire un fichier :**
```python
# Mode lecture
with open("fichier.txt", "r", encoding='utf-8') as f:
    contenu = f.read()          # Tout le fichier
    # OU
    lignes = f.readlines()      # Liste de lignes
    # OU
    for ligne in f:             # Ligne par ligne
        print(ligne)
```

**Écrire dans un fichier :**
```python
# Mode écriture (écrase tout)
with open("fichier.txt", "w", encoding='utf-8') as f:
    f.write("Nouveau contenu")

# Mode ajout (ajoute à la fin)
with open("fichier.txt", "a", encoding='utf-8') as f:
    f.write("Ligne supplémentaire\n")
```

---

### Modes d'ouverture

| Mode | Action | Fichier existe ? | Contenu |
|------|--------|------------------|---------|
| `"r"` | Lecture | Obligatoire | Préservé |
| `"w"` | Écriture | Créé si absent | **Écrasé !** |
| `"a"` | Ajout | Créé si absent | Préservé + ajout |
| `"r+"` | Lecture + Écriture | Obligatoire | Modifiable |

---

### Encoding Windows

**Important sur Windows :**
```python
# TOUJOURS ajouter encoding='utf-8' sur Windows !
with open("fichier.txt", "r", encoding='utf-8') as f:
    contenu = f.read()
```

**Pourquoi ?**
- Windows utilise encodage différent par défaut
- Sans `encoding='utf-8'` → caractères français mal affichés
- É, è, à, ç, ê → remplacés par symboles bizarres

---

### Chemins de fichiers

**Chemin absolu (complet) :**
```python
chemin = r"C:\Users\ouali\OneDrive\Documents\fichier.txt"
```

**Chemin relatif (depuis script) :**
```python
chemin = "fichier.txt"  # Dans même dossier que script
```

**Module `os` pour chemins :**
```python
import os

# Dossier du script
dossier = os.path.dirname(__file__)

# Construire chemin
fichier = os.path.join(dossier, "fichier.txt")

# Vérifier existence
if os.path.exists(fichier):
    print("Fichier existe !")
```

---

### Format JSON

**JSON = Format universel pour sauvegarder données structurées**

**Différences Python ↔ JSON :**
- `True` / `False` → `true` / `false`
- `None` → `null`
- Guillemets simples → guillemets doubles

**Lire JSON :**
```python
import json

with open("data.json", "r", encoding='utf-8') as f:
    donnees = json.load(f)  # JSON → Python
    
print(donnees)  # Liste ou dictionnaire Python
```

**Écrire JSON :**
```python
import json

donnees = ["Pain", "Lait", "Œufs"]

with open("data.json", "w", encoding='utf-8') as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)
```

**Paramètres importants :**
- `indent=4` → formatage lisible
- `ensure_ascii=False` → caractères français préservés

---

## ✅ Compétences validées

- [x] Ouvrir fichiers avec `open()`
- [x] Modes `"r"`, `"w"`, `"a"`
- [x] Instruction `with` (fermeture automatique)
- [x] `encoding='utf-8'` sur Windows
- [x] Méthode `seek()` (curseur)
- [x] Module `json` (load, dump)
- [x] Conversions Python ↔ JSON
- [x] Chemins absolus vs relatifs
- [x] Module `os.path`

---

## 📊 Évaluations

**Quiz 25 : Lire un fichier**
- Score : 4/4 (100%)
- Concepts : modes, seek(), différences w/a

**Quiz 26 : Les fichiers + JSON**
- Score : À compléter
- Concepts : JSON, format, sauvegarde

---

## 💡 Points clés à retenir

**1. TOUJOURS utiliser `with` :**
```python
# ✅ BON
with open("fichier.txt", "r") as f:
    contenu = f.read()
# Fichier fermé automatiquement

# ❌ MAUVAIS
f = open("fichier.txt", "r")
contenu = f.read()
f.close()  # Risque d'oubli !
```

**2. Windows = `encoding='utf-8'` OBLIGATOIRE**

**3. Mode `"w"` ÉCRASE tout le fichier !**

**4. JSON = 1 fichier = 1 structure (liste OU dict, pas les deux)**

**5. `json.load()` pour lire, `json.dump()` pour écrire**

---

## 🐛 Erreurs courantes rencontrées

### `FileNotFoundError`
**Cause :** Fichier n'existe pas  
**Solution :** Vérifier chemin ou utiliser mode `"w"` pour créer

### `JSONDecodeError`
**Cause :** Fichier JSON mal formaté  
**Solution :** Vérifier syntaxe avec JSONLint.com

### Caractères bizarres (�, Ã©, etc.)
**Cause :** Manque `encoding='utf-8'`  
**Solution :** Ajouter `encoding='utf-8'` partout !

---

## 🎯 Applications pratiques

**Exemples d'utilisation :**

**Sauvegarder configuration app :**
```python
import json

config = {
    "langue": "fr",
    "theme": "sombre",
    "notifications": True
}

with open("config.json", "w", encoding='utf-8') as f:
    json.dump(config, f, indent=4)
```

**Charger liste de clients :**
```python
import json

with open("clients.json", "r", encoding='utf-8') as f:
    clients = json.load(f)

for client in clients:
    print(f"{client['nom']} - {client['telephone']}")
```

**Logger activité app :**
```python
import datetime

with open("logs.txt", "a", encoding='utf-8') as f:
    timestamp = datetime.datetime.now()
    f.write(f"{timestamp} - Action utilisateur\n")
```

---

## 📝 Notes personnelles

**Ce qui était difficile :**
- Comprendre différence `json.load()` vs `json.dump()`
- Erreurs `JSONDecodeError` quand fichier mal formaté
- Se rappeler `encoding='utf-8'` systématiquement

**Ce qui était facile :**
- Instruction `with` (déjà vue)
- Logique modes `r`/`w`/`a`
- Similitude JSON ↔ dictionnaires Python

**Astuces découvertes :**
- `indent=4` rend JSON lisible
- `ensure_ascii=False` pour accents français
- `os.path.exists()` évite `FileNotFoundError`
- `__file__` donne chemin du script actuel

---

## 🔗 Ressources utiles

- [Documentation Python - open()](https://docs.python.org/3/library/functions.html#open)
- [Documentation Python - json](https://docs.python.org/3/library/json.html)
- [JSONLint](https://jsonlint.com/) - Validateur JSON en ligne
- Fiche Docstring JSON (document fourni)

---

## ✅ Validation finale

**Critères de validation :**
- [x] Toutes les vidéos visionnées (206-216)
- [x] Concepts compris (fichiers texte + JSON)
- [x] Quiz réussis (80%+)
- [x] Code testé et fonctionnel
- [x] Erreurs courantes identifiées

**Section validée :** ✅ OUI  
**Date validation :** 12 mars 2026  
**Prêt pour Section 35 :** ✅ OUI (Projet Liste Courses v2 avec JSON)

---

## ⏭️ Prochaine étape

**Section 35 : Projet Liste Courses v2**
- Application concepts Section 34
- Sauvegarde liste dans fichier JSON
- Chargement au démarrage
- Persistance des données

**→ Premier vrai programme avec mémoire ! 💾**
