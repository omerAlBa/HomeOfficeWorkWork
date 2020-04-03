# gebe alle Kontinete nacheinader aus
continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for continent in continents:
    print(continent)

print("\n")
# gebe alle Kontinete aus die bewohnt sind <Antarktis> überspringen
for bewohnteContinente in continents:
    if bewohnteContinente == "Antarktis":
        continue
    print(bewohnteContinente)

print("\n")


#vergleiche Liste und gebe überschneidungen aus aufagbe 1.d & e
anzahlDerKontinente = []
stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]
for continent1 in stuff:
    for continent2 in continents:
        if continent1 == continent2:
            anzahlDerKontinente.append(continent1)
            print(continent1)

print("anzahl der Continente in der liste 'stuff': " + str(len(anzahlDerKontinente)))
print("\n")

#Aufgabe 2
price = 50

if price <= 20:
    price = price * 0.8
elif price <= 50:
    price = price * 0.6
else:
    price = price * 0.4

print(price)
print("\n")

#aufgabe 2.b  
# Berechne nun für jeden der alten Preise aus der Liste
# prices die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices. 
# Gib diese Liste schließlich aus.

prices = [2, 50, 70, 30]
new_prices =[]

for price in prices:
    if price <= 20:
        price = price * 0.8
    elif price <= 50:
        price = price * 0.6
    elif price > 50:
        price = price * 0.4
    new_prices.append(price)
print(new_prices) 
print("\n")

#augfabe 2.c

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for element in chaos:
    if "old" in element:
        element = element.split(": ")
        element[1] = int(element[1])
        if element[1] <= 20:
            element[1] = element[1] * 0.8
        elif element[1] <= 50:
            element[1] = element[1] * 0.6
        elif element[1] > 50:
            element[1] = element[1] * 0.4
        order.append(element[1])
    else:
        element = element.split(": ")
        element[1] = int(element[1])
        order.append(element[1])

print(order)
