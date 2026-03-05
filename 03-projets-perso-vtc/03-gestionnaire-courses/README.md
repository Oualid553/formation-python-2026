# Projet VTC #3 : Gestionnaire de Courses Journalières

**Date :** 5 mars 2026  
**Concepts :** Section 29 (Menu interactif, Listes, enumerate)  
**Statut :** ✅ Complété  
**Score :** 100%

---

## 🎯 Objectif

Gérer les courses VTC de la journée avec un menu interactif : ajouter, retirer, afficher, vider et quitter.

**Différenciation :** Adaptation du projet Docstring #3 au contexte métier VTC.

---

## 🚕 Fonctionnalités

1. ✅ Ajouter une course (trajet)
2. ✅ Retirer une course (annulation)
3. ✅ Afficher les courses du jour
4. ✅ Vider la journée (fin de service)
5. ✅ Quitter l'application

---

## 💻 Exemple d'utilisation

```
=== GESTIONNAIRE COURSES VTC ===

Choisissez parmi les 5 options suivantes :
1: Ajouter une course
2: Retirer une course
3: Afficher les courses du jour
4: Vider la journée
5: Quitter
👉 Votre choix : 1

Entrez le trajet de la course (ex: Paris-CDG) : Paris-CDG
✅ Course Paris-CDG ajoutée.

📋 Courses du jour :
1. Paris-CDG
--------------------------------------------------

👉 Votre choix : 1
Entrez le trajet de la course (ex: Paris-CDG) : CDG-Paris
✅ Course CDG-Paris ajoutée.

📋 Courses du jour :
1. Paris-CDG
2. CDG-Paris
--------------------------------------------------

👉 Votre choix : 3
📋 Courses du jour :
1. Paris-CDG
2. CDG-Paris
--------------------------------------------------

👉 Votre choix : 2
Entrez le trajet de la course à annuler : Paris-CDG
❌ Course Paris-CDG annulée.
--------------------------------------------------

👉 Votre choix : 4
🏁 Journée terminée. Toutes les courses ont été effacées.
--------------------------------------------------

👉 Votre choix : 3
📭 Aucune course pour aujourd'hui.
--------------------------------------------------

👉 Votre choix : 5
👋 Bonne route !
```

---

## 🛠️ Concepts Python utilisés

| Concept | Application |
|---------|-------------|
| `while True` | Boucle principale de l'application |
| Liste dynamique | `COURSES_JOUR = []` |
| Validation | `if choix not in ["1", "2", "3", "4", "5"]` |
| `enumerate(liste, start=1)` | Numérotation automatique des courses |
| `append()` | Ajouter une course |
| `remove()` | Annuler une course |
| `clear()` | Vider la journée |
| `in` opérateur | Vérifier si course existe |
| `sys.exit()` | Quitter proprement |
| Emojis | UX améliorée |

---

## 🔄 Adaptation Docstring → VTC

| Projet Docstring #3 | Projet VTC #3 |
|---------------------|---------------|
| Liste de courses | Courses journalières VTC |
| `article` | `trajet` |
| "Pomme", "Pain" | "Paris-CDG", "CDG-Paris" |
| "liste vidée" | "journée terminée" |
| "Au revoir !" | "Bonne route !" |

**→ Même logique, vocabulaire adapté au métier ! 🎯**

---

## 🚕 Exemples de trajets réels

**Trajets courants Paris/Île-de-France :**
- Paris-CDG (45€)
- CDG-Paris (45€)
- Paris-Orly (35€)
- Boulogne-Neuilly (15€)
- Paris-Versailles (35€)
- Neuilly-La Défense (12€)
- Gare du Nord-Gare de Lyon (20€)

---

## 💡 Différenciation portfolio

**Ce projet démontre :**

### 1. Compréhension métier VTC ✅
- Vocabulaire adapté (trajet, course, annulation)
- Contexte journée de travail
- Cas d'usage réalistes

### 2. Capacité d'adaptation ✅
- Code générique → application métier
- Réutilisation intelligente des concepts
- Personnalisation UX (emojis, messages)

### 3. Pensée pratique ✅
- Gestion quotidienne des courses
- Annulations (réalité du métier)
- Fin de journée (remise à zéro)

**→ Portfolio qui se démarque des autres étudiants Docstring ! 🏆**

---

## 📈 Évolution du projet

| Version | Fonctionnalité |
|---------|----------------|
| **v1 (actuelle)** | Gestion trajets uniquement |
| **v2 (future)** | Trajets + tarifs + calcul revenu |
| **v3 (future)** | Sauvegarde journée dans fichier |
| **v4 (future)** | Statistiques mensuelles |

---

## 🚀 Améliorations futures possibles

### Court terme (concepts déjà vus)
1. Afficher nombre total de courses
2. Compteur courses par trajet
3. Rechercher une course spécifique

### Moyen terme (après Section 37 - Dictionnaires)
4. Ajouter tarif par course
5. Calculer revenu total journée
6. Statistiques par type de trajet

### Long terme (après Section 58 - BDD)
7. Sauvegarder dans fichier/base de données
8. Historique des journées
9. Statistiques mensuelles/annuelles
10. Export Excel pour comptabilité

---

## 🎓 Leçons retenues

### 1. Réutilisation de code
**Ne pas tout recoder à zéro !**
- Copier projet Docstring
- Adapter vocabulaire
- Personnaliser UX
- → Gain de temps énorme ! ⏱️

### 2. Thématisation
**Appliquer concepts à son domaine**
- Rend l'apprentissage plus concret
- Portfolio différenciant
- Démontre compréhension métier

### 3. Itération progressive
**Version basique d'abord, améliorations ensuite**
- v1 : Juste les trajets ✅
- v2 : Ajouter tarifs (plus tard)
- v3 : Ajouter BDD (plus tard)

---

## ✅ Projet validé le 5 mars 2026

**Prochains projets VTC :**
- **VTC #4** (après Section 37) : Registre chauffeurs avec dictionnaires
- **VTC #5** (après Section 42) : Simulateur revenus avec fonctions
- **VTC #6** (après Section 53) : Gestionnaire courses POO
