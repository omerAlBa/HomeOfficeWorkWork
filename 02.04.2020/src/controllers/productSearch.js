import EventEmitter from "eventemitter3"
import {search} from "../api/product"

import lifeSelector from '../utils/dom'

export default function productSearch(buttonElement,searchElement,resultElement) {
    this.buttonElement = buttonElement
    this.searchElement = searchElement
    this.resultElement = resultElement

    this.events = new EventEmitter()
}

productSearch.prototype.init = function (event) {
    this.buttonElement.addEventListener("click", (event)=>{    
        event.preventDefault()
        this.getResult(this.searchElement.value)
    });
    const this_ = this
    lifeSelector(
        document.querySelector(".list-product-search-result"),
        document.querySelector(".list-group-item-result"),
        "click",
        function (result){
            result.origanalEvent.preventDefault();
            const fdcid = result.element.getAttribute("data-fcid");
            this_.events.emit("ProductSelected",fdcid);
        }
    );
}

productSearch.prototype.getResult = function (toSearchFor,resultElement) {

    search(toSearchFor)
    .then((results)=>{
         this.resultElement.innerHTML = "";
         for (let i = 0; i < results.length; i++) {
             const element = results[i];
             this.resultElement.innerHTML += `
             <a href="#" 
                class="list-group-item list-group-item-action list-group-item-result" 
                data-fcid="${element.fdcId}">
                    ${element.description}
                </a>
             `
         }
         
        // return results
    })
}