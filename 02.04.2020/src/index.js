"use strict"
require("../scss/index.scss");
import ProductSearch from "./controllers/productSearch"
import ProductList from "./controllers/productList";
import ProductBoard from "./controllers/productBoard";

const productSearch = new ProductSearch(
        document.querySelector("#productSearchButton"),
        document.querySelector("#productSearchInput"),
        document.querySelector("#productSearchResult")
    )
    productSearch.init()
    // productSearch.eventListener.link("click",()=>{  alert("kinder") })
    
    productSearch.events.on("ProductSelected",(result)=>{
        productList.getProduct(result)
    })
    
const productList = new ProductList(
        document.querySelector(".productList")
    )
    productList.getProduct(363938)
        .then(()=> productList.init())
    
    productList.events.on("nutrientsChanged",(result)=>{
        productBoard.buildBoard(result);
    })

const productBoard = new ProductBoard(
        document.querySelector(".product-amount-total")
    )
