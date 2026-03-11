# Projet Docstring #5 : Jeu de Rôle Terminal

**Date :** 11 mars 2026  
**Section :** 31 - Formation Docstring  
**Statut :** ✅ Complété  
**Score :** 95%

---

## 📋 Description

Cinquième projet officiel de la formation Docstring. Jeu de combat textuel dans le terminal où le joueur affronte un ennemi en tour par tour, avec possibilité d'attaquer ou d'utiliser des potions de soin.

**Complexité :** Plus avancé que les projets précédents, nécessite de gérer plusieurs états simultanés (PV joueur, PV ennemi, stock potions, ordre des actions).

---

## 🎯 Fonctionnalités

1. ✅ Combat tour par tour (joueur vs ennemi)
2. ✅ 2 actions possibles : Attaquer ou Boire une potion
3. ✅ Système de points de vie (50 PV chacun au départ)
4. ✅ Dégâts aléatoires (joueur : 5-10, ennemi : 5-15)
5. ✅ 3 potions de soin (récupération : 15-50 PV aléatoire)
6. ✅ Validation entrée utilisateur (choix 1 ou 2 uniquement)
7. ✅ Gestion stock potions (décrément + vérification)
8. ✅ Mécanisme "passer le tour" après potion
9. ✅ Vérification victoire/défaite après chaque action
10. ✅ Affichage PV restants en temps réel

---

## 💻 Exemple d'utilisation

```
🎮 JEU DE RÔLE - COMBAT TERMINAL 🎮
==================================================
Vous : 50 PV ❤️ | 3 Potions 🧪
Ennemi : 50 PV ❤️
Que la bataille commence !
==================================================

Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? 1
Vous avez infligé 8 points de dégâts à l'ennemi ⚔
L'ennemi vous a infligé 12 points de dégâts ⚔
Il vous reste 38 points de vie.
Il reste 42 points de vie à l'ennemi.
------------------------------------------------------------

Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? 2
Vous récupérez 35 points de vie ❤ (2 🧪 restantes)
Vous passez votre tour !
L'ennemi vous a infligé 10 points de dégâts ⚔
Il vous reste 63 points de vie.
Il reste 42 points de vie à l'ennemi.
------------------------------------------------------------

... (combat continue)

Tu as gagné 💪
Fin du jeu.
```

---

## 🛠️ Concepts Python utilisés

| Concept | Application |
|---------|-------------|
| `random.randint()` | Dégâts et soins aléatoires |
| `while` | Boucle principale du jeu |
| Validation input | `if choix not in ["1", "2"]` |
| `continue` | Recommencer tour si invalide |
| Conditions multiples | if/elif pour attaque vs potion |
| `break` | Sortie si victoire/défaite |
| Variables compteurs | Décrémenter PV et potions |
| Opérateurs composés | `PV -= degats` |
| F-strings dynamiques | Affichage en temps réel |
| Logique conditionnelle | Ordre critique vérifications |

---

## 🔄 Comparaison avec correction officielle

| Aspect | Mon code | Correction |
|--------|----------|------------|
| Boucle | `while PV > 0 and PV_ENNEMI > 0` | `while True` + breaks |
| Validation | `if not in: continue` | `while not in: input()` |
| "Passer tour" | Message immédiat | Variable `SKIP_TURN` |

**Mon approche :**
- ✅ Condition `while` plus explicite ("tant que les deux vivants")
- ✅ Logique identique, style personnel
- ✅ Code fonctionnel et clair

---

## 🎓 Ce que j'ai appris

**Compétences renforcées :**
- ✅ Gestion états multiples (PV, potions, tours)
- ✅ Logique conditionnelle complexe
- ✅ Ordre critique des vérifications
- ✅ Variables temporaires pour clarté
- ✅ Validation robuste entrées

**Leçon principale :**
**Pseudo-code en français AVANT de coder = gain de temps énorme !**

---

## 📝 Notes de développement

**Temps passé :** 1h30
- Pseudo-code : 20 min
- Code : 30 min
- Tests : 15 min
- Corrections : 5 min
- Documentation : 20 min

**Points forts :**
- Pseudo-code détaillé d'abord
- Structure claire
- Tests systématiques

---

## ✅ Projet validé le 11 mars 2026

**Score : 95/100**

**Prochaine étape :** Section 32 - Fin Partie 1 ! 🚀
