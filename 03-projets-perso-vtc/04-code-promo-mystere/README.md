# Projet VTC #4 : Code Promo Mystère

**Date :** 10 mars 2026  
**Concepts :** Section 30 (Boucles, random, validation)  
**Statut :** ✅ Complété  
**Score :** 100%

---

## 🎯 Objectif

Jeu interactif où le client doit deviner un code promo mystère (0-100) en 5 essais maximum pour obtenir une réduction de 20% sur sa course VTC.

**Différenciation :** Adaptation du projet Section 30 (Nombre Mystère) au contexte métier VTC avec vocabulaire et thématique professionnels.

---

## 🚕 Fonctionnalités

1. ✅ Génération code promo aléatoire (0-100)
2. ✅ Limite de 5 essais pour le trouver
3. ✅ Validation entrée utilisateur (nombres uniquement)
4. ✅ Indices progressifs ("plus petit" / "plus grand")
5. ✅ Message victoire avec réduction appliquée
6. ✅ Message défaite avec révélation du code
7. ✅ Compteur essais restants
8. ✅ Thématique VTC complète (emojis, vocabulaire)

---

## 💻 Exemple d'utilisation

```
🚕🎫 CODE PROMO MYSTÈRE VTC 🎫🚕
--------------------------------------------------
Un code promo est disponible !
Trouvez-le en 5 essais pour -20% de réduction !
--------------------------------------------------

Code promo : 50
❌ Le code promo est plus petit que 50
Il vous reste 4 essai(s)

Code promo : 25
❌ Le code promo est plus grand que 25
Il vous reste 3 essai(s)

Code promo : 37
❌ Le code promo est plus petit que 37
Il vous reste 2 essai(s)

Code promo : 31
❌ Le code promo est plus grand que 31
Il vous reste 1 essai(s)

Code promo : 34
✅ CODE VALIDE ! Réduction de 20% appliquée !
Vous avez trouvé le code en 5 essai(s) !
Profitez de votre trajet à prix réduit ! 🎉
```

---

## 🛠️ Concepts Python utilisés

| Concept | Application |
|---------|-------------|
| `random.randint(0, 100)` | Génération code promo aléatoire |
| `while True` | Boucle de jeu principale |
| Validation input | `if not x.isdigit()` |
| `continue` | Redemander si input invalide |
| Conversion type | `int(saisie)` |
| Compteur décrémental | `TENTATIVES -= 1` |
| Conditions multiples | if/elif/else imbriqués |
| `break` | Sortie boucle victoire/défaite |
| F-strings | Affichage dynamique thématisé |
| Calcul inverse | `5 - TENTATIVES` (essais utilisés) |

---

## 🔄 Adaptation Nombre Mystère → Code Promo VTC

| Projet Docstring | Projet VTC #4 | Changement |
|------------------|---------------|------------|
| `NOMBRE_MYSTERE` | `CODE_PROMO` | Variable renommée |
| "nombre mystère" | "code promo" | Vocabulaire métier |
| "Bravo !" | "Code valide ! -20%" | Récompense contextualisée |
| "Le nombre était" | "Le code promo était" | Terminologie adaptée |
| 🎮 Emojis jeu | 🚕🎫 Emojis VTC | Thématique professionnelle |
| "Gagné en X essais" | "Trouvé en X essai(s)" | Formulation client |

**→ Même logique, vocabulaire professionnel VTC ! 💼**

---

## 💡 Différenciation Portfolio

**Ce projet démontre :**

### 1. Compréhension métier VTC ✅
- Vocabulaire adapté (code promo, réduction, trajet)
- Contexte réaliste (promotion client)
- Gamification expérience utilisateur

### 2. Capacité d'adaptation technique ✅
- Réutilisation intelligente du code
- Personnalisation messages et thème
- Adaptation sans modifier la logique

### 3. Pensée "use case réel" ✅
- Code promo = pratique VTC courante
- Engagement client ludique
- Application concrète des concepts

**→ Portfolio qui montre créativité ET compréhension terrain ! 🏆**

---

## 🐛 Bugs rencontrés et corrigés

### Bug 1 : Opérateur d'affectation vs décrémentation
```python
# ❌ ERREUR INITIALE
TENTATIVES = -1  # Affecte -1 au lieu de décrémenter

# ✅ CORRECTION
TENTATIVES -= 1  # Diminue de 1 à chaque essai
```

**Leçon :** 
- `=` affecte une valeur
- `-=` diminue la valeur existante

### Bug 2 : Révélation du code dans les indices
```python
# ❌ ERREUR INITIALE
print(f"Le code est plus petit que {CODE_PROMO}")
# → Révèle la réponse !

# ✅ CORRECTION
print(f"Le code est plus petit que {saisie}")
# → Indice correct basé sur la saisie
```

**Leçon :** Toujours référencer la **saisie utilisateur** dans les indices, jamais la réponse !

---

## 🎓 Ce que j'ai appris

### Compétences techniques renforcées
- ✅ Adaptation de code existant
- ✅ Thématisation professionnelle
- ✅ Débogage autonome (identification bugs)
- ✅ Opérateurs raccourcis (`-=` vs `=`)

### Compétences métier VTC
- ✅ Gamification expérience client
- ✅ Codes promo et promotions
- ✅ Engagement utilisateur ludique

### Bonnes pratiques
- ⚠️ Ne jamais révéler la réponse dans les indices
- ⚠️ Bien différencier `=` et `-=`
- ⚠️ Tester plusieurs scénarios (victoire, défaite, erreurs)

---

## 🚀 Améliorations futures possibles

### Court terme
1. Codes promo à thème (BIENVENUE20, ETE2026, etc.)
2. Niveaux de réduction (-10%, -20%, -30%)
3. Codes promo avec lettres (ex: VTC2026)

### Moyen terme
4. Historique codes promo utilisés
5. Codes promo à durée limitée
6. Statistiques réussites/échecs

### Long terme
7. Base de données codes promo
8. Génération codes uniques par client
9. Intégration système de réservation

---

## 🎯 Applications réelles VTC

**Ce jeu pourrait devenir :**

### Application marketing
- Newsletter avec code mystère
- Jeu sur réseau social
- Fidélisation client ludique

### Gamification app VTC
- Débloquer codes promo en jouant
- Challenges quotidiens
- Programme de fidélité gamifié

**→ Concept applicable en situation professionnelle ! 💼**

---

## 📊 Comparaison projets

| Aspect | Nombre Mystère | Code Promo VTC |
|--------|----------------|----------------|
| **Thème** | Jeu générique | Métier VTC |
| **Vocabulaire** | Neutre | Professionnel |
| **Contexte** | Divertissement | Service client |
| **Récompense** | "Bravo" | Réduction 20% |
| **Emojis** | 🎮🎯 | 🚕🎫 |
| **Public** | Joueur | Client VTC |

**→ Adaptation intelligente = valeur ajoutée portfolio ! 🎯**

---

## 📝 Notes de développement

**Temps passé :**
- Adaptation code : 10 min
- Correction bugs : 5 min
- Tests : 5 min
- Documentation : 10 min
- **Total : 30 min**

**Difficultés rencontrées :**
- Erreur `=` au lieu de `-=` (précipitation)
- Révélation code promo dans indices (logique)
- **Les deux rapidement corrigés ! ✅**

**Points forts :**
- Adaptation rapide du code existant
- Identification autonome du bug
- Thématisation cohérente

**Leçon principale :**
**Ne pas se précipiter ! Relire le code avant de tester ! 🎯**

---

## ✅ Projet validé le 10 mars 2026

**Prochains projets VTC :**
- **VTC #5** (après Section 37) : Gestion clients avec dictionnaires
- **VTC #6** (après Section 42) : Calculateur revenus avec fonctions
- **VTC #7** (après Section 55) : Système réservation POO

---

## 🔗 Liens

**Projet Docstring associé :** [Section 30 - Nombre Mystère](../../02-projets-docstring/projet-04-nombre-mystere/)

**Section du cours :** Section 30 - Le Nombre Mystère
