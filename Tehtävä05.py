
leiviskä = int(input("Anna leiviskä: "))
naula = int(input("Anna naula: "))
luoti = float(input("Anna luodit: "))

leiviskä = leiviskät = float(leiviskä * 20*32*13.3)
naulat = float(naula * 32 * 13.3)
luodit = float(luoti * 13.3)

grammat = float(luodit + naulat + leiviskät)
kilot = float(grammat / 1000)

kilo1 = int(kilot // 1)
gramma1 = round((kilot % 1) * 1000, 2)


print("Massa nykymittojen mukaan: \n")
print(kilo1, "kilogramma ja", gramma1, "gramma")
