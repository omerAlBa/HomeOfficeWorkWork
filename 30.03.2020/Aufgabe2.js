"use strict"

let products = [
  {title: "Banane", carbs: 23, fat: 0.3, protein: 1},
  {title: "Kastanie", carbs: 28, fat: 1.4, protein: 2},
  {title: "Avocado", carbs: 9, fat: 15, protein: 2},
  {title: "Macadamia", carbs: 14, fat: 76, protein: 8},
  {title: "Zwiebel", carbs: 9, fat: 0.1, protein: 1.1},
]

// Aufgabe 1
//
// Gegeben ist eine Liste Nährwertangaben zu Produkten (pro 100g). 
// Diese sollst du per JavaScript auswerten und ein paar Fragen
// beantworten :) 
// 
// 1a) Ergänze über ein .map() zu jedem Produkt die `kcal`-Eigenschaft.
//     Du kannst hier von folgenden Werten ausgehen:
//      - 1g Fett: 9kcal
//      - 1g Protein: 4kcal
//      - 1g Kohlenhydrate: 4kcal

const determineKcal = (obj)=>{
  obj.kcal = ((obj.carbs / 100) + (obj.fat / 100) + (obj.protein / 100)) *100
  return obj
}
/** lösung 1a. */
products = products
  .map(determineKcal)// ausgelagerte Version, soll "schöner sein"

/* ausgeschrieben
let x = products.map((obj)=>{
  let {carbs,fat,protein,kcal} = obj;
  kcal = ((carbs / 100) + (fat / 100) + (protein / 100)) *100 
  obj.kcal = kcal
  return obj
})
*/


//     Hinweis: .map() erstellt ein neues Array. Du kannst dieses aber
//     zurück in die Variable schreiben lassen:
//     products = products.map(...)

// 1b) Schreibe ein Programm, welches prüft, ob es ein Produkt
//     mit mehr als 50g Fett gibt. Wenn ja, dann soll "true"
//     ausgegeben werden, wenn nicht, "false".

/** lösung 1b. */
const y = products.some(({fat})=> fat >= 50)
console.log(y);


//     Hinweis: Verwende hierzu keine for-Schleife, sondern eine der 
//              neuen Funktionen (aber nicht die .reduce()-Funktion)!

// 1c) Kannst du 1b) auch mit einem .reduce() lösen? Wenn ja, wie?

/** lösung 1c. */

const y2 = products.reduce((pre, cur)=> { 
  if (pre){
    return true 
  } else {
    return cur.fat > 50
  }
 },false)

 //kurze schreibweise
const y3 = products.reduce((pre,current) => pre || current.fat > 50,false)
console.log(y3);


// 1d) Finde das Produkt, welches am meisten Fett enthält. 
//     Tipp: Hier gibt es mehrere Lösungen. 
// 
//     Möglichkeit 1: 
//       - Du holst dir die Eigenschaft `fat` von allen Produkten
//       - Anschließend ermittelst du, wie viel Fett das fettreichste
//         Produkt enthält
//       - Anschließend kannst du das Produkt über ein .find() suchen
 /** lösung 1d. Möglichkeit 1 */
 const maxFat = products.map(value => value.fat)
 const maxFat2 = Math.max(...maxFat)
 const productsMaxFat = products.find(value => value.fat === maxFat2) 
 console.log(productsMaxFat);
 
 

//     Möglichkeit 2 (effizienter, Bonus, optional, komplizierter):
//       - Du löst das gesamte Problem über ein .reduce(). Beachte hierbei
//         dass der initiale Wert / der Parameter `prev` sowie der
//         Rückgabewert des Callbacks nicht zwingend eine Zahl sein muss -
//         es darf auch ein Object sein:
// 
debugger
const x2 = products.reduce((prev, cur) => {
  if (prev.fat > cur.fat) {
    return prev
  } else {
    return cur
  }
}, {fat: 0})

console.log(x2);


// 
//         Was für einen initialien Wert würde hier statt dem {key: "value"} 
//         sinn machen? 

