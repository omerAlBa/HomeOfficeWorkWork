'use strict'
import EventEmitter from 'eventemitter3';
import {info} from "../api/product";

import createTrElement_EJS from "../templates/trElement/createTrElement.ejs"

import liveSelecter from "../utils/dom";

let products = []

export default class productList {
    constructor(tBody){
        this.tBody = tBody
        this.products = products
        this.events = new EventEmitter()
    }

    init(){
        liveSelecter(
            document.querySelector(".productList"),
            document.querySelector(".close"),
            "click",
            (result)=>{
                this.removeProduct(result);
            }
        )
        liveSelecter(
            document.querySelector(".productList"),
            document.querySelector(".product-amount"),
            "click",
            (result)=>{
                this.updateAmount(result);
            }
        )
    }

    removeProduct(result){
        let element = result.element
        const fdcId = element.getAttribute("data-fdcid")
        //remove from dom
        while (element) {              
            if(element.localName == "tr"){ element.remove() }
            element = element.parentNode
        }
        
        //remove from productListe
        const index = this.products
            .findIndex((element) => element.product["fdcId"] === parseInt(fdcId))
    
        index  === -1 ? "" : this.products.splice(index,1)
        this.getNutrientsValue()
        return
    }

    updateAmount(element){
        const index = this.products.findIndex((elementObj) => elementObj.product["fdcId"] === parseInt(element.element.getAttribute("data-fdcid")))
        index >= 0 ? this.products[index].amount = parseInt(element.element.value) : ""

        this.getNutrientsValue()
    }

    async getProduct(fdcId){
        const result = await info(fdcId)
        this.addFetchProduct(result)
    }

    addFetchProduct(result){
        const element = createTrElement_EJS({title: result.description, fdcid: result.fdcId})
        this.tBody.insertAdjacentHTML("beforeend", element) 
        this.products.push({
            amount: 100,
            foodNutrients: result.foodNutrients,
            product : result
        })
        this.getNutrientsValue()
    }

    sumTotalNutrient(){
        /* aufgabe: ermittelt die gesammten Nährwerte */
        
        let totalNutrientValue = { caps: 0, protein: 0, fat: 0}
        
        for (const product of this.products) {   
            const resultNutrient = this.getSingleNutrients(product)
                    
            totalNutrientValue.caps += resultNutrient.caps
            totalNutrientValue.protein += resultNutrient.protein
            totalNutrientValue.fat += resultNutrient.fat
            
        }
        return totalNutrientValue
    }

    getSingleNutrients(product){
        /* aufruf von der Function: sumTotalNutrient() */
        const giveBackNutrient = (foodNutrient, number)=>{
            return foodNutrient
                    .find((foodNutrients) => parseInt(foodNutrients.nutrient.number) === number).amount
        }
        
        let nutrientsValue = { 
            caps: (giveBackNutrient(product.foodNutrients,205) / 100 * product.amount), 
            protein: (giveBackNutrient(product.foodNutrients,203) / 100 * product.amount), 
            fat: (giveBackNutrient(product.foodNutrients,204) / 100 * product.amount)
        }

        return nutrientsValue
    }

    getNutrientsValue(){
        const nutrients = this.sumTotalNutrient()
        this.events.emit("nutrientsChanged", nutrients);
    }
}