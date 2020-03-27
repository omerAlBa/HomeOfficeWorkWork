//create the element

jest.mock("../api/product")
document.body.innerHTML = `
    <table>
        <tbody></tbody>
    </table>
`
const ProductList = require("./productList")
let productList
const tbody = document.querySelector("tbody")

const fakeProduct = {
    description: "test-Product",
    product:{
        fdcId: "123456",
    },
    foodNutrients: []
}

afterEach(()=>{
    productList = null
})

describe("ProductListe wird getestet",()=>{
    beforeEach(()=>{
        productList = new ProductList(tbody)
    })

    test("wird getNutrientsValue aufgerufen?",()=>{
        expect(productList).not.toBeNull()
    })

    test("übergabe eines Produktes",()=>{
        productList.addFetchProduct(fakeProduct)
        expect(productList.products).not.toBeNull()
        expect(productList.products.length).toBe(1)
        expect(productList.products[0].amount).toBe(100)
    })

    test("mit api und mok",(done)=>{
        productList.addFetchProduct = jest.fn()
        productList.getProduct("123456")
        .then(()=>{
            expect(productList.addFetchProduct).toBeCalled()
            done()
        })

    })
 
    test("wird getNutrientsValue aufgerufen?",()=>{
        productList.getNutrientsValue = jest.fn()
        
        expect(productList.products.length).toBe(1)
        return productList.getProduct("123456")
            .then(()=>{
                expect(document.querySelector("tbody").innerHTML != "").toBe(true)
                expect(productList.products.length).toBe(2)
            })
        
    })
})

describe("update Amount Tester",()=>{
       beforeEach(()=>{
        productList = new ProductList(tbody)
    })
    
    //brauchst ein element mit der id, also push
    test("products ist gleich 2",()=>{
        expect(productList.products.length).toBe(2)
    })

    test("products ist gleich 2",()=>{
        expect(productList.products[1].amount).toBe(100)
    })

    //dann liste auslesen und vergleich
    test("products ist gleich 2",()=>{
        document.body.innerHTML = "<input data-fdcid='100' value='200'>200</input>"
        return productList.getProduct(100)
        .then(()=>{
            productList.updateAmount({x : "x", element: document.querySelector("input")})
            expect(productList.products.length).toBe(3)
            expect(productList.products[2].amount).toBe(200)

        })
    })

    test("wird das getNutrientsValue ausgelöst?",()=>{
        productList.getNutrientsValue = jest.fn()
        document.body.innerHTML = "<input data-fdcid='100' value='200'>200</input>"
        return productList.getProduct(100)
        .then(()=>{
            productList.updateAmount({x : "x", element: document.querySelector("input")})
            expect(productList.getNutrientsValue.mock.calls.length).toBe(2)
        })
    })

})