# Journal d'Apprentissage Python

## Semaine 1 - Février 2026

### Jour 1 - Samedi 15 Février 2026

**Sections étudiées :** 12
**Temps codé :** 4h  
**Commits :** 4

**Ce que j'ai appris :**
- **Setup technique :**
- Configuration complète de GitHub (premier repository professionnel)
- Workflow Git : add, commit, push (maîtrisé)
- Structure de projet professionnelle (arborescence claire)
- Conventions de messages de commit

**Python - Section 12 (Types natifs) :**
- Les 4 types de base : `str`, `int`, `float`, `bool`
- Fonction `type()` pour vérifier le type d'une variable
- Conversions de types : `int()`, `float()`, `str()`, `bool()`
- Différence entre `int` (entier) et `float` (décimal)
- Booléens : `True` et `False` (avec majuscules obligatoires)
- Gestion des guillemets et apostrophes dans les chaînes
- Échappement avec `\` (exemple : `'Je m\'appelle'`)
- Alternance guillemets simples/doubles selon le contexte

**Concepts importants :**
- Python compare les VALEURS, pas les TYPES (`10 == 10.0` → `True`)
- `input()` retourne TOUJOURS une chaîne de caractères (`str`)
- Impossible d'additionner `str` + `int` sans conversion
- f-strings pour formater facilement : `f"Total : {prix} €"`

**Difficultés rencontrées :**
- **Technique :**
- Configuration initiale Git (email privé sur GitHub → résolu)
- Comprendre la différence entre sauvegarder localement vs pousser sur GitHub
- Se rappeler de convertir `input()` en `int` ou `float` pour faire des calculs

**Concepts Python :**
- Petite confusion sur l'orthographe exacte des types (`flo` au lieu de `float`, `bol` au lieu de `bool`)
- Pas évident au début : `print(type(age))` affiche le type, pas la valeur
- Différence entre comparaison de valeurs (`==`) et comparaison de types (`type(a) == type(b)`)
- Optimisation du code (utiliser directement `pourboire = 5` au lieu de `int("5")`)

**Organisation :**
- Trouver le bon rythme entre apprendre et commiter sur Git
- Résister à la tentation d'aller trop vite (bien comprendre avant d'avancer)


**Victoires du jour :**
- ✅ Setup GitHub complet et professionnel
- ✅ Workflow Git maîtrisé (4 commits réussis)
- ✅ Section 12 terminée (vidéos + exercices + quiz)
- ✅ Score Udemy : 15/15 (100% sur les 3 quiz)
- ✅ Score quiz Claude : 9.65/12 (80.4%) → Section validée !
- ✅ Premiers fichiers Python codés et documentés
- ✅ Honnêteté sur ce que je ne savais pas (meilleur apprentissage)
- ✅ Rigueur dans les commits (GitHub se remplit progressivement)

**Score quiz :** __%
**Udemy :**
- Quiz 3 (Chaînes de caractères) : 5/5 ✅
- Quiz 4 (Booléens) : 3/3 ✅
- Quiz 5 (Types natifs) : 7/7 ✅
- **Total : 15/15 (100%)**

**Quiz Claude :**
- Score : 9.65/12 (80.4%)
- Seuil validation : 10/12 (83%)
- **Statut : Validé** (très proche du seuil + concepts clés maîtrisés)

**Points forts :** Types natifs, conversions, guillemets, détection d'erreurs  
**À renforcer :** `input()` toujours `str`, optimisation code, f-strings

**État d'esprit :** 😃 / 😐 / 😓
😃 **Motivé et fier !**

Premier jour intense mais productif. Content d'avoir un vrai portfolio GitHub qui commence à se remplir. Les exercices Docstring sont bien faits, et le fait de coder EN MÊME TEMPS que la vidéo aide vraiment à retenir. 

Petite fatigue en fin de journée (setup + apprentissage = beaucoup), mais satisfaction d'avoir tout compris et validé la section.

Hâte de continuer demain avec les variables !

**Objectifs demain :**
**Matin :**
- Réviser `input()` et f-strings (10 min)
- Section 13 : Variables
- Section 14 : Conversion de types

**Après-midi :**
- Section 15 : Interagir avec l'utilisateur
- Mini-projet VTC appliquant sections 12-15
- Commit + mise à jour métriques

**Cible :** 3-4 sections validées (12-15)

---

#### 💭 RÉFLEXIONS

**Ce qui marche bien :**
- Coder EN MÊME TEMPS que la vidéo (pas juste regarder)
- Faire les exercices SEUL avant de regarder la solution
- Commiter régulièrement sur GitHub (rigueur)
- Demander à Claude quand je bloque (gain de temps)

**À améliorer demain :**
- Relire mes notes de la veille avant de démarrer (5 min)
- Tester mes propres variantes des exemples (créativité)
- Ajouter plus de commentaires dans mon code (documentation)


---


---

### Jour 1 (suite) / Jour 2 - Samedi 15 Février 2026 (soir)

**Sections étudiées :** Section 13 - Les variables  
**Temps codé :** ~2h  
**Commits :** 2

---

#### 📚 CE QUE J'AI APPRIS

**Section 13 - Les variables :**
- Définition d'une variable : un nom qui référence un objet
- Concept Python : objets et noms (différent d'autres langages)
- Affectations simples : `a = 5`
- Affectations parallèles : `a, b = 1, 2` (pas encore pratiqué)
- Affectations multiples : `a = b = c = 0` (pas encore pratiqué)

**Règles de nommage :**
- ✅ Lettres (a-z, A-Z)
- ✅ Chiffres (mais pas au début)
- ✅ Underscores `_`
- ❌ Espaces interdits
- ❌ Caractères spéciaux (@, %, $, etc.)
- ❌ Mots-clés Python (`print`, `if`, `for`, etc.)

**Conventions (PEP 8) :**
- Variables en minuscules : `age`, `prenom`
- Mots multiples avec underscore : `compte_en_banque`
- Noms explicites : `prix_total` plutôt que `p`

**Concepts importants :**
- Quand on fait `a = b`, on copie la VALEUR (pas de lien permanent)
- Python : objets dans la mémoire, variables = étiquettes sur ces objets
- Singleton et small integer caching (concept avancé, à creuser)

---

#### 😓 DIFFICULTÉS RENCONTRÉES

**Concepts :**
- Quiz 6 : 5/7 (71%) - 2 erreurs (probablement affectations multiples/parallèles)
- Quiz 7 : 6/7 (86%) - 1 erreur (concept non identifié)
- Singleton et caching : pas totalement compris (normal, concept avancé)

**Pratique :**
- Exercice 6 : Hésitation sur `_a` et `a_` (en fait valides, mais j'ai choisi de supprimer)

---

#### 🎉 VICTOIRES DU JOUR

- ✅ Section 13 terminée en 2h
- ✅ Tous les exercices réussis (4/4 - 100%)
- ✅ Bonne compréhension des règles de nommage
- ✅ Concept "copie de valeur" bien compris (exercice 7 parfait)
- ✅ Rigueur : code de base + correction dans chaque exercice
- ✅ 2 sections validées en 1 journée (12 + 13)

---

#### 📊 SCORES QUIZ

**Section 13 :**
- Quiz 6 (Introduction variables) : 5/7 (71%)
- Quiz 7 (Variables) : 6/7 (86%)
- **Total : 11/14 (79%)**

**Exercices :**
- Exercice 4 : Déclarer variables ✅
- Exercice 5 : Corriger erreur ✅
- Exercice 6 : Syntaxe ✅
- Exercice 7 : Valeur variable ✅
- **Total : 4/4 (100%)**

---

#### 😊 ÉTAT D'ESPRIT

😃 **Satisfait et motivé !**

Pause d'une heure au milieu qui m'a permis de recharger les batteries. La Section 13 était plus facile que la 12 (concepts déjà vus ailleurs). Content de voir que je progresse vite quand je suis concentré.

Petite frustration sur les quiz (79% vs 100% en Section 12), mais les exercices parfaits montrent que je comprends bien en pratique.

Envie de continuer sur ma lancée !

---

#### 🎯 OBJECTIFS PROCHAINE SESSION

**Si je continue ce soir :**
- Section 14 : Conversion de types
- Section 15 : Input utilisateur

**Sinon demain matin :**
- Révision rapide sections 12-13 (10 min)
- Sections 14-15-16
- Premier mini-projet VTC

---

#### 💭 RÉFLEXIONS

**Ce qui marche bien :**
- Pause au milieu = meilleure concentration après
- Format code de base + correction dans exercices (bon pour révision)
- Rigueur sur les commits (portfolio se construit)

**À améliorer :**
- Revoir les points flous des quiz (affectations multiples/parallèles)
- Peut-être ralentir sur les concepts avancés (singleton, caching)

---

---

---

### Section 14 - Samedi 15 Février 2026 (soir ~21h)

**Section étudiée :** Section 14 - Conversion de types  
**Temps codé :** ~1h  
**Commits :** 1

**Ce que j'ai appris :**
- Fonctions de conversion : `str()`, `int()`, `float()`, `bool()`
- Python fortement typé : pas de conversion automatique str + int
- Concaténation de chaînes avec `+`
- Ordre des opérations : calcul d'abord, puis conversion
- Différence entre addition (`10 + 5`) et concaténation (`"10" + "5"`)

**Difficultés rencontrées :**
- Exercice 9 : Comprendre que les `" + "` sont du texte (5 min de réflexion)
- Exercice 1 ligne d : Comprendre `str(10 + 5)` → calcul d'abord, puis conversion

**Victoires du jour :**
- ✅ **3 sections validées en 1 jour !** (12, 13, 14)
- ✅ Score parfait Section 14 (100% quiz + 100% exercices)
- ✅ Exercice challenge réussi du premier coup
- ✅ Code identique à la correction officielle

**Scores quiz :**
- Quiz 8 : 5/5 (100%) ✅

**Exercices :**
- Exercice 8 : Convertir variable ✅
- Exercice 9 : Concaténer variables ✅
- Exercice 1 : La concaténation ✅

**État d'esprit :** 😃 **Très motivé mais fatigué !**

Grosse journée productive. Content d'avoir continué ce soir malgré la fatigue. La Section 14 était plus facile que prévu (concepts déjà vus en Section 12). Satisfaction d'avoir 3 sections validées en 1 jour !

**Objectifs demain :** Sections 15-17 + Premier projet VTC

---

**Session terminée :** ~21h30  
**Prochaine session :** Demain 9h00
---
---

### Jour 2 - Dimanche 16 Février 2026

**Sections étudiées :** Section 15 (Input), Section 16 (Résolution problèmes), Section 17 (Strings)  
**Temps codé :** ~7-8h  
**Commits :** 10+

---

#### 📚 CE QUE J'AI APPRIS

**Section 15 - Input utilisateur :**
- Fonction `input()` retourne TOUJOURS une chaîne (str)
- Conversion obligatoire pour calculs : `int(input(...))`, `float(input(...))`
- Messages clairs pour l'utilisateur
- Application immédiate dans projet VTC

**Section 16 - Résolution de problèmes :**
- **Méthodologie CRUCIALE** : Décrire en français AVANT de coder
- Ne jamais partir directement dans le code
- Décomposer le problème en étapes simples
- Utiliser papier/stylo pour réfléchir
- Documentation Python officielle (en français)
- Processus itératif normal

**Section 17 - Manipuler les chaînes (DENSE !) :**
- **Casse :** `upper()`, `lower()`, `title()`, `capitalize()`
- **Remplacement :** `replace(old, new)` - Remplace TOUTES occurrences
- **Nettoyer :** `strip()`, `lstrip()`, `rstrip()` - Analyse caractère par caractère
- **Séparer/Joindre :** `split()` (STRING→LISTE), `join()` (LISTE→STRING)
- **Zéros :** `zfill(width)` pour séquences numérotées
- **Validation :** `isdigit()`, `isalpha()`, `isalnum()` - Critique avant conversion
- **Compter :** `count(sub)` - Compte CARACTÈRES, pas mots
- **Trouver :** `find()` (retourne -1), `index()` (fait erreur)
- **Début/Fin :** `startswith()`, `endswith()` - Extensions fichiers

**Point CRITIQUE retenu :**
- Les méthodes strings NE MODIFIENT PAS l'original !
- Toujours STOCKER le résultat : `nouveau = texte.upper()`

---

#### 😓 DIFFICULTÉS RENCONTRÉES

**Section 15 :**
- Aucune difficulté majeure (concepts déjà vus en Section 14)

**Section 16 :**
- Section théorique/méthodologique (pas de code)
- Vidéos 95-97 = podcasts culturels (optionnels)

**Section 17 (LA PLUS DENSE) :**
- 15+ méthodes d'un coup = Beaucoup d'informations
- **Quiz 9 :** Erreur sur syntaxe `join()` avec les crochets
- **Exercice 11 :** Oublié `.lower()` pour insensibilité à la casse
- **Exercice 13 :** Petit blocage sur stockage résultat `join()`
- Confusion `strip()` : analyse caractère par caractère, pas chaîne entière

**Concepts qui demandent attention :**
- `join()` : Syntaxe inversée `"sep".join(liste)` (pas intuitif)
- `strip()` : Chaque caractère individuellement, pas la chaîne
- `count()` : Compte caractères, pas mots (ajouter espace pour mots)
- `find()` vs `index()` : -1 vs erreur

---

#### 🎉 VICTOIRES DU JOUR

**Projet VTC :**
- ✅ **Premier projet perso créé !** Calculateur de tarif VTC v1
- ✅ Code fonctionnel à 96%
- ✅ Méthodologie Section 16 appliquée (décomposition en français)
- ✅ Application concrète des sections 12-16

**Apprentissage :**
- ✅ **Section 17 maîtrisée** malgré la densité (96% moyenne)
- ✅ Entraînement split/join réussi (100%)
- ✅ Autonomie : Cherché dans la documentation quand bloqué
- ✅ **Cheatsheet complète** créée pour référence permanente

**Progression :**
- ✅ 3 sections validées en 1 jour
- ✅ Méthodologie professionnelle acquise
- ✅ Portfolio GitHub s'enrichit

---

#### 📊 SCORES QUIZ & EXERCICES

**Section 15 :**
- Exercice 2 : 100% ✅

**Section 16 :**
- Pas d'exercices (méthodologie)

**Section 17 :**
- Quiz 9 : 7/8 (87.5%) ✅
- Exercice 10 : 100% ✅
- Exercice 11 : 95% ⚠️ (oublié `.lower()`)
- Exercice 12 : 100% ✅
- Exercice 13 : 100% ✅
- **Moyenne globale : 96%**

---

#### 😊 ÉTAT D'ESPRIT

😃 **Surmotivé et fier !**

Grosse journée productive mais intense. La Section 17 était vraiment dense (15+ méthodes), j'ai dû créer une cheatsheet complète pour tout retenir. Très content d'avoir appliqué la méthodologie de la Section 16 pour mon projet VTC.

**Citation du jour :** "Ça change vraiment de travailler avec Claude comme mentor, ça m'aide énormément ! Et ça me surmotive !"

Premier vrai projet personnel créé et fonctionnel. Satisfaction de voir le code marcher et de comprendre chaque ligne.

Petite fatigue en fin de journée après 7-8h de travail concentré, mais satisfaction immense d'avoir maîtrisé une section difficile.

---

#### 🎯 OBJECTIFS JOUR 3

**Sections prévues :**
- Section 18 : Opérateurs
- Section 19 : Formatage
- Section 20 : PROJET #1 - Calculatrice (Docstring)

**Ou révision si besoin :**
- Revoir sections 12-17
- Améliorer projet VTC v1
- Créer cheatsheets manquantes

---

#### 💭 RÉFLEXIONS

**Ce qui marche bien :**
- Créer cheatsheet pendant section dense (référence immédiate)
- Entraînement ciblé sur points difficiles (split/join)
- Chercher dans documentation = compétence pro
- Appliquer immédiatement dans projet perso

**À améliorer :**
- Penser `.lower()` pour comparaisons insensibles à la casse
- Utiliser variables fournies (pas valeurs en dur)
- Toujours vérifier stockage résultat des méthodes

**Leçon importante :**
- Section dense ≠ impossible
- Cheatsheet + pratique = maîtrise
- Erreurs comprises = apprentissage solide

---

**Heures totales Jour 2 :** 7-8h  
**Sections totales :** 5/80 (6.25%)  
**Projets créés :** 1 (VTC Calculateur v1)

---

**Session terminée :** ~18h00  
**Prochaine session :** Mardi 17 février, 11h00 