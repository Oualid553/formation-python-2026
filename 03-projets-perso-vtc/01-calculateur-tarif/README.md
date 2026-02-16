# Projet VTC #1 : Calculateur de Tarif

**Date :** 16 février 2026  
**Sections utilisées :** 12-16  
**Temps de développement :** ~1h30  
**Statut :** ✅ Version 1 complète

---

## 📋 Description

Programme qui calcule le prix d'une course VTC en fonction de :
- Distance parcourue (km)
- Durée du trajet (minutes)
- Pourboire éventuel (5€)

**Tarif :** 2€ par kilomètre

---

## ✨ Fonctionnalités

- ✅ Input utilisateur (nom, distance, durée, pourboire)
- ✅ Calcul automatique du tarif (2€/km)
- ✅ Gestion du pourboire optionnel (5€)
- ✅ Affichage récapitulatif formaté

---

## 🛠️ Concepts Python utilisés

**Sections appliquées :**
- **Types natifs** (str, int, float, bool)
- **Variables** (nommage clair et explicite)
- **Conversion de types** (int(), float())
- **Input utilisateur** (input())
- **Structures conditionnelles** (if)
- **Constantes** (TARIF_KM, POURBOIRE_STANDARD)
- **Formatage** (f-strings)

---

## 💻 Exemple d'utilisation
```
=== CALCULATEUR DE TARIF VTC ===

Quel est votre nom ? Pierre
Quelle est la distance de votre trajet (km) ? 15.5
Quelle est la durée du trajet (min) ? 25
Pourboire (oui/non) : oui

--- RÉCAPITULATIF COURSE ---
Client : Pierre
Distance : 15.5 km
Durée : 25 minutes
Tarif de base : 31.0 €
Pourboire : 5.0 €
TOTAL : 36.0 €

Merci et bonne journée !
```

---

## 🚀 Améliorations futures (v2, v3...)

**Version 2 (avec conditions) :**
- [ ] Tarif jour/nuit différent
- [ ] Supplément aéroport
- [ ] Réduction client régulier

**Version 3 (avec boucles) :**
- [ ] Calculer plusieurs courses d'affilée
- [ ] Historique des courses du jour

**Version 4 (avec fichiers) :**
- [ ] Sauvegarder les courses dans un fichier
- [ ] Lire l'historique

**Version 5 (avec POO) :**
- [ ] Classe Course
- [ ] Classe Client
- [ ] Classe Tarif

**Version 6 (avec Django) :**
- [ ] Interface web
- [ ] Base de données
- [ ] Tableau de bord

---

## 📊 Statistiques

**Lignes de code :** ~40  
**Temps développement :** ~1h30  
**Tests réussis :** ✅ Tous

---

## 🎓 Compétences démontrées

- ✅ Décomposition d'un problème en étapes
- ✅ Application de la méthodologie (Section 16)
- ✅ Conversion et validation des données
- ✅ Logique conditionnelle
- ✅ Code propre et commenté
- ✅ Projet fonctionnel de bout en bout

---

**Premier projet VTC réussi ! 🎉**