describe("Nutrient ausgabe im Dom",()=>{
    const ProductBoard = require("./productBoard")

    document.body.innerHTML = "<table><tbody></tbod></table>"
    const nutrients = {caps: 0, protein: 100.3333333333, fat: 0}
    const tbody = document.getElementsByTagName("tbody")
    const productBoard = new ProductBoard(document.querySelector("tbody"))
        


    test("ausgabe der Nutrients",()=>{
        productBoard.buildBoard(nutrients)
        const span = document.querySelectorAll("span")
        
        expect(span[1].textContent).toBe("100.33")
    })
})