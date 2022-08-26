# Moduuli2, Syöte- ja muuttujaesimerkkejä
import math
import random

username = "Kalle"
# int value
age = 6
age = age + 1
# float value
wallet_balance = 15.40
fullname = "Kalle Kontio"
# merkkijonojen liittäminen
user = username + " (" + fullname + ")"
print("Käyttäjä " + user + " on " + str(age) + " vuotta")
print("Hänellä on lompakossa", wallet_balance, "euroa.")
ticket_price = input(username + " osti bussilipun, hinta?")
wallet_balance = wallet_balance - float(ticket_price)
print(f"Hänellä on lompakossa {wallet_balance:.2f} euroa.")