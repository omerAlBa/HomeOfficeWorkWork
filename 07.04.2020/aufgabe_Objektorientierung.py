class Cube():
    def __init__(self,length):
        self.length = length

    def surface(self):
        return (self.length ** 2) * 6

    def volume(self):
        return self.length ** 3

# Aufgabe 2. Kugel class
import math
class Kugel(Cube):
    def __init__(self,length):
        super().__init__(length)
    
    def surface(self):
        return (4 * math.pi) * (self.length **2)
    
    def volume(self):
        return (4/3) * math.pi * (self.length**3)

# danach erzeugen wir eine Instanz deiner Cube-Klasse 
#a = Cube(3)
a = Kugel(4)

# und testen die Methoden
print(a.surface())
print(a.volume())


#aufgabe 3 Modelliere ein Konto

class Account():
    def __init__(self,credits,pin):
        this = self
        this.credits = credits
        this.pin = pin
    
    def display(self):
        this = self
        return this.credits

    def pay_in(self,incoming):
        this = self
        this.credits += incoming
    
    def withdraw(self,outcoming,pin):
        this = self

        if pin == this.pin:    
            if outcoming > this.credits:
                return "maximale auszahlung ist " + str(this.credits) + "€"
            this.credits -= outcoming
            return
        return "Ha, nice try aber das passwort ist 1234 ;)"


Kunde111 = Account(500, "1234")
print(Kunde111.display())
print(Kunde111.pay_in(40))
print(Kunde111.display())
print(Kunde111.withdraw(25, "1234"))
print(Kunde111.display())
print(Kunde111.withdraw(600, "12345"))

print("--------Aufgabe 3----------")

class Train():
    def __init__(this,station,position):
        this.station = station
        this.position = position
    
    def show_station(this):
        return print(this.station[this.position])

    def move(this):
        if this.position < this.station.__len__()-1:
            this.position += 1
            return
        return print("Wir sind gerade in" + str(this.station[this.position]) + "weiter nachhinten gehts nicht!")
    
    def move_back(this):
        if this.position > 0 and this.position <= this.station.__len__()-1:
            this.position -= 1
            return
        return print("Wir sind gerade in" + this.station[this.position] + "weiter nachhinten gehts nicht!")

    def bypass_station(this,nameStation):
        this.station.remove(nameStation)
        print(nameStation + " wurde aus den Plan entfernt")
        this.position = 0
        return 

orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move_back()
orientexpress.show_station()
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()