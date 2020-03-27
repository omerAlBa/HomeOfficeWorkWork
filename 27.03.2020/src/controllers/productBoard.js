'use strict'

const buildBoard_EJS = require("../templates/liElement/productBoard.ejs")

function productBorad(nutrientBoard) {
    this.nutrientBoard = nutrientBoard
}

productBorad.prototype.init = function(){

}

productBorad.prototype.buildBoard = function(nutrients){
    const nutrientBoard_HTML = buildBoard_EJS({
        Kohlenhydrate: (Math.round(nutrients.caps*100)/100),
        Protein: (Math.round(nutrients.protein*100)/100), 
        Fett: (Math.round(nutrients.fat*100)/100)
    })
    this.nutrientBoard.innerHTML = nutrientBoard_HTML
}

module.exports = productBorad