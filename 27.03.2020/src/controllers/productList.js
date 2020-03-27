'use strict'
const EventEmitter = require("eventemitter3")
const Api = require("../api/product")
const apiIdRequest = Api.info
const createTrElement_EJS = require("../templates/trElement/createTrElement.ejs")
const liveSelecter = require("../utils/dom")

let products = []

function productList(tBody) {
    this.tBody = tBody
    this.products = products

    this.events = new EventEmitter()
}


productList.prototype.init = function(){
    liveSelecter.on(
        document.querySelector(".productList"),
        document.querySelector(".close"),
        "click",
        (result)=>{
            this.removeProduct(result);
        }
    )
    liveSelecter.on(
        document.querySelector(".productList"),
        document.querySelector(".product-amount"),
        "click",
        (result)=>{
            this.updateAmount(result);
        }
    )    
}


productList.prototype.removeProduct = function(result){
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


productList.prototype.updateAmount = function(element){
    
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

productList.prototype.getProduct = function(fdcId){
    return apiIdRequest(fdcId)
    .then((result)=>{
       this.addFetchProduct(result)
    })
}

productList.prototype.addFetchProduct = function(result){
    const element = createTrElement_EJS({title: result.description, fdcid: result.fdcId})
        this.tBody.insertAdjacentHTML("beforeend", element) 
        this.products.push({
            amount: 100,
            foodNutrients: result.foodNutrients,
            product : result
        })
        this.getNutrientsValue()
}


productList.prototype.sumTotalNutrient = function(){
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


productList.prototype.getSingleNutrients = function(product){
    /**
     * aufruf von der Function: sumTotalNutrient()
     */
    let nutrientsValue = { caps: 0, protein: 0, fat: 0}

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

productList.prototype.getNutrientsValue = function(){
    const nutrients = this.sumTotalNutrient()
    this.events.emit("nutrientsChanged", nutrients);
}

module.exports = productList