# Exercice 1 : La concaténation (challenge)
# Section 14 - Formation Docstring
# Oualid - 15 février 2026

# ==========================================
# CODE DE DÉPART (AVEC ERREURS)
# ==========================================
# a = "J'ai une classe de " + 30 + " élèves"           # ❌ str + int
# b = 10 + " + " + "5" + " est égal à " + 15           # ❌ int + str
# c = 10 + "5"                                          # ❌ int + str
# d = "L'addition de 10 + 5 est égal à " + 10 + 5      # ❌ str + int

# ==========================================
# MA CORRECTION (100% identique à la correction officielle !)
# ==========================================
a = "J'ai une classe de " + str(30) + " élèves"
b = str(10) + " + " + "5" + " est égal à " + str(15)
c = 10 + int("5")
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)

print(a)  # J'ai une classe de 30 élèves
print(b)  # 10 + 5 est égal à 15
print(c)  # 15
print(d)  # L'addition de 10 + 5 est égal à 15

# Remarque : Ça commence à se compliquer !
#            Il faut bien réfléchir à chaque conversion.