try:
    file = open("nicht_oeffnen.txt", "r")
    print(file)
except FileNotFoundError:
    print("File konnte nicht gefunden werden")


articles = ["Unsichtbare Tastatur", "Holographisches Display", "Endlosschleifenschneider"]

prices = {"Unsichtbare Tastatur": 150, "Holographisches Display": 1150}

def print_prices():
    for article in articles:
        print(prices[article])

try:
    print_prices()
except KeyError:
    print("error kleines")

#aufgabe 1.d)
try:
    if len(d) == 0:
        print("Hier soll jetzt ein Fehler ausgelöst werden")
except:
    print("noch ein Fehler")