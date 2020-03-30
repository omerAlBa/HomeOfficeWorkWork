"use strict"

// Aufgabe 1:
// 
// Schreibe eine Funktion `average`, die den Durschschnitt aller
// ihr übergebenen Funktionsparameter berechnet.

function average(...values) {
  let start = null
  for (let index = 0; index < values.length; index++) {
    const element = values[index];
    start += element
  }
  return start / values.length
} 

console.log(average(5)) // Ausgabe: 5
console.log(average(1, 2, 3)) // Ausgabe: 2
console.log(average(20, 15, 45, 20)) // Ausgabe: 25

// Aufgabe 2
//
// Schreibe ein Programm für NodeJS, welches Informationen zum aktuellen 
// Computersystem ausgibt. Diese Informationen werden dir über das "os"-
// Modul zur Verfügung gestellt.
// 
// Du findest den Beispielcode in der Funktion `getOsInfo`. 
// 
// Schreibe die Funktion so um, dass JavaScript Template-Strings verwendet
// werden - dadurch können wir uns die "+"-Operationen sparen, und diese
// durch die ${}-Schreibeweise ersetzen!

const os = require("os")

function getOsInfo() {
  // os.cpus() gibt ein Array zurück, mit einem Eintrag pro (virtuellem) 
  // Prozessor(kern) im System. 
  // 
  // Hinweis: Bei Hyperthreading kann die Zahl der virtuellen 
  // Prozessorkerne höher sein als die der "echten" Kerne.
  // 
  // Ich habe z.B. nur einen Quad-Core, aber für's Betriebssystem sieht es
  // so aus, als hätte ich 8 Kerne. 
  // 
  // => https://en.wikipedia.org/wiki/Hyper-threading
  const cpuModel = os.cpus()[0]['model']
  const message = [
    `
    Betriebssystem:  ${os.arch()} ,  ${os.type()},
    CPU: ${cpuModel} , ${os.cpus().length} Prozessorkerne,
    Angeschaltet seit: ${os.uptime()} Sekunden`
  ].join("\n")
  return message
}
console.log(getOsInfo())


// Aufgabe 3, Einleitung:
// 
// Damit eine Banküberweisung ausgeführt werden kann, müssen
// der Funktion "makeTransfer" ein paar Parameter übergeben werden:

function makeTransfer(iban, bic, accountHolder) {
  // Hier stünde jetzt Code der mit einer Bank kommunizieren würde
  console.log("makeTransfer, iban: ", iban)
  console.log("makeTransfer, bic: ", bic)
  console.log("makeTransfer, accountHolder: ", accountHolder)
}

// Jetzt stellt sich aber heraus, dass der Parameter `bic` automatisch
// aus der IBAN berechnet werden kann (zumindest für Konten in Deutschland).
//
// Da der Parameter `accountHolder` aber nicht optional sein darf, wäre folgende
// Funktionsdefinition ausgesprochen unschön - für `bic` muss jetzt weiterhin
// immer ein Wert mit übergeben werden, den können wir ja nicht einfach weglassen:

function makeTransfer2(iban, bic = "", accountHolder) {
  console.log("makeTransfer2, iban: ", iban)
  console.log("makeTransfer2, bic: ", bic)
  console.log("makeTransfer2, accountHolder: ", accountHolder)
}
// makeTransfer3("DE12345", "", "Max Mustermann")

// Das hier geht nicht, hier würde die `bic` auf "Max Mustermann" gesetzt, und der 
// `accountHolder` auf undefined (weil kein 3. Parameter angegeben ist): 
// makeTransfer3("DE12345", "Max Mustermann")

// Aufgabe 3a)
// 
// Schreibe eine Funktion `makeTransfer3`, bei der die Parameter als Objekt
// übergeben werden. Verwende dazu die {}-Schreibweise im Funktionsparameter!

function makeTransfer3({iban, bic="nega",accountHolder}={}) {
  // Kommentiere diesen Code zum Testen ein:
  // console.log("makeTransfer3, iban: ", iban)
  // console.log("makeTransfer3, bic: ", bic)
  // console.log("makeTransfer3, accountHolder: ", accountHolder)
}
makeTransfer3({iban: "DE12345", accountHolder: "Max Mustermann"})

// Aufgabe 3b)
// 
// Schreibe eine Funktion `makeTransfer3`, bei der die Parameter als Objekt
// übergeben werden. Verwende dazu *NICHT* die {}-Schreibweise im Funktionsparameter!

function makeTransfer4(obj) {
  const {iban,bic,accountHolder} = obj
  // Kommentiere diesen Code zum Testen ein:
  console.log("makeTransfer4, iban: ", iban)
  console.log("makeTransfer4, bic: ", bic)
  console.log("makeTransfer4, accountHolder: ", accountHolder)
}
makeTransfer4({iban: "DE12345", accountHolder: "Max Mustermann"})
