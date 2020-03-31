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

    removeProduct(){
        let element = result.element
        const fdcId = element.getAttribute("data-fdcid")
        //remove from dom
        while (element) {              
            if(element.localName == "tr"){
                element.remove()
            }
            element = element.parentNode
        }
        //remove from productListe
        for (let index = 0; index < this.products.length; index++) {
            const element = this.products[index].product;
            if (element["fdcId"] === parseInt(fdcId)) { 
                this.products.splice(index,1)   
                this.getNutrientsValue()
                return      
            }
        }
    }

    updateAmount(element){
        for (let index = 0; index < this.products.length; index++) {
            const elementObj = this.products[index];
            //result übergibt immer einen objekt aus den angeklicken und den gewünschten element,
            //die zwei namen! element.element!
            
            if(elementObj.product["fdcId"] === parseInt(element.element.getAttribute("data-fdcid"))){
                elementObj.amount = parseInt(element.element.value) 
            }
        }
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
        /**
        * aufgabe: ermittelt die gesammten Nährwerte
        */
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
        /**
        * aufruf von der Function: sumTotalNutrient()
        */
        let nutrientsValue = { 
            caps: product.foodNutrients.find((foodNutrients) => parseInt(foodNutrients.nutrient.number) === 205).amount, 
            protein: product.foodNutrients.find((foodNutrients) => parseInt(foodNutrients.nutrient.number) === 203).amount, 
            fat: product.foodNutrients.find((foodNutrients) => parseInt(foodNutrients.nutrient.number) === 204).amount
        } 
     
        for (const nutrient of product.foodNutrients) {        
            
            if (parseInt(nutrient.nutrient.number) === 205) {
                nutrientsValue.caps += (nutrient.amount / 100) * product.amount
            } else if(parseInt(nutrient.nutrient.number) === 203){
                nutrientsValue.protein += (nutrient.amount / 100) * product.amount
            } else if(parseInt(nutrient.nutrient.number) === 204){
                nutrientsValue.fat += (nutrient.amount / 100) * product.amount
            }
            
        }
        return nutrientsValue
    }

    getNutrientsValue(){
        const nutrients = this.sumTotalNutrient()
        this.events.emit("nutrientsChanged", nutrients);
    }
}
