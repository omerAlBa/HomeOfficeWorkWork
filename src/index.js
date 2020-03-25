"use strict"
require("../scss/index.scss");
const ProductSearch = require("./controllers/productSearch");
const ProductList = require("./controllers/productList");

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
    productList.init()
    
    productList.getProduct(363938)

