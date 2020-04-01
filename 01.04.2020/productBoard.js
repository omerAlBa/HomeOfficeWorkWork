'use strict'

import buildBoard_EJS from "../templates/liElement/productBoard.ejs"



export default class productBorad {
    constructor(nutrientBoard){
        this.nutrientBoard = nutrientBoard
    }

    init(){}
    buildBoard(nutrients){
        const nutrientBoard_HTML = buildBoard_EJS({
            Kohlenhydrate: (Math.round(nutrients.caps*100)/100),
            Protein: (Math.round(nutrients.protein*100)/100), 
            Fett: (Math.round(nutrients.fat*100)/100)
        })
        this.nutrientBoard.innerHTML = nutrientBoard_HTML
    }
}