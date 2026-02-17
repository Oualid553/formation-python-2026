# Section 19 - Le Formatage des Chaînes de Caractères

**Date début :** 16 février 2026 (23h)
**Date fin :** 17 février 2026 (en cours)
**Statut :** 🔄 En cours (vidéo 120/124)

---

## 📚 Contenu

- Vidéo 118 : Introduction ✅
- Vidéo 119 : Concaténation et f-strings ✅
- Exercice 14 : F-string URL ✅ (100%)
- Vidéo 120 : Solution exercice 14 ✅
- Vidéo 121 : Méthode format ⏳
- Vidéo 122 : Dans quel cas utiliser format ⏳
- Vidéo 123 : Article pour aller plus loin ⏳
- Vidéo 124 : Fiche récapitulative ⏳

---

## 🔗 1. CONCATÉNATION vs F-STRINGS

### Concaténation (ancienne méthode)
```python
nom = "Pierre"
age = 25

# ❌ Lourd et peu lisible
message = "Bonjour " + nom + ", vous avez " + str(age) + " ans."
```

### F-strings (méthode moderne et recommandée)
```python
nom = "Pierre"
age = 25

# ✅ Simple et lisible
message = f"Bonjour {nom}, vous avez {age} ans."
```

### Avantages f-strings

- ✅ Plus lisible
- ✅ Pas besoin de convertir les types
- ✅ Peut contenir des expressions
- ✅ Méthode recommandée depuis Python 3.6+

### Expressions dans f-strings
```python
prix = 25.5
quantite = 3

# Expression directement dans la f-string
total = f"Total : {prix * quantite}€"  # "Total : 76.5€"
```

---

## 🎯 EXERCICE 14 : F-string URL (100% ✅)

### Consigne
Recréer l'URL : `https://www.docstring.fr/glossaire/`

### Code de base
```python
protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"

URL = f""
```

### Ma solution (identique à correction officielle)
```python
protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"

URL = f"{protocole}www.{nom_du_site}.{extension}/{page}/"
print(URL)
# https://www.docstring.fr/glossaire/ ✅
```

---

## ⏳ À COMPLÉTER (Vidéos 121-124)

- Méthode `.format()`
- Cas d'usage format vs f-strings
- Article complémentaire
- Fiche récapitulative

---

## 📊 Scores (partiel)

- **Exercice 14 :** 100% ✅
- **Quiz :** En attente

---

**Mise à jour :** 17 février 2026