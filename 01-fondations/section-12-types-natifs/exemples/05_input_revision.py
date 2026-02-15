# RÉVISION : input() retourne TOUJOURS du texte

# ❌ ERREUR fréquente
age = input("Ton âge : ")
# age est un str (texte), pas un int !

# ✅ CORRECT
age = int(input("Ton âge : "))
# Maintenant age est un int (nombre)

# ✅ CORRECT aussi
prix = float(input("Prix : "))
# prix est un float (décimal)

#-----------------------------------------------------------------------#

# RÉVISION : f-strings

nom = "Oualid"
age = 36

# ❌ Lourd (concaténation)
print("Je m'appelle " + nom + " et j'ai " + str(age) + " ans")

# ✅ Mieux (f-string)
print(f"Je m'appelle {nom} et j'ai {age} ans")