//create the element

jest.mock("../api/product")
document.body.innerHTML = `
    <table>
        <tbody></tbody>
    </table>
`
import ProductList from "./productList"

let productList
const tbody = document.querySelector("tbody")

const fakeProduct = {
    description: "test-Product",
    product:{
        fdcId: "123456",
    },
    foodNutrients: []
}

beforeEach(()=>{
    productList = new ProductList(tbody)
});

describe("zustand ProductListe",()=>{
    beforeEach(()=>{
        productList = new ProductList(tbody)
    });

    test("productList länge ",()=>{
        expect(productList.products.length).toBe(0)
    })

})

describe("ProductListe wird getestet",()=>{
    beforeEach(()=>{
        productList = new ProductList(tbody)
    })
    test("übergabe eines Produktes",()=>{
        // productList.getProduct(8989898)
        // expect(productList.products).not.toBeNull()
        // expect(productList.products.length).toBe(1)
        // expect(productList.products[0].amount).toBe(100)
    });

    test("mit api und mok",(done)=>{
        productList.addFetchProduct = jest.fn()
        productList.getProduct("123456")
        .then(()=>{
            expect(productList.addFetchProduct).toBeCalled()
            done()
        })

    })
 
    test("wird getNutrientsValue aufgerufen?",(done)=>{
        productList.getNutrientsValue = jest.fn()
        
        expect(productList.products.length).toBe(0)
        return productList.getProduct("123456")
            .then(()=>{
                expect(document.querySelector("tbody").innerHTML != "").toBe(true)
                expect(productList.products.length).toBe(1)
                done()
            })
    })
})

describe("update Amount Tester first one",()=>{
    beforeEach(()=>{
        productList = new ProductList(tbody)
        productList.products = []
    })

    test("products die Liste sollte leer sein!",()=>{
        expect(productList.products.length === 0).toBe(true)
    })

})

describe("update Amount Tester",()=>{

       beforeEach(()=>{
            productList = new ProductList(tbody)
            productList.products = []
        })
    
    //brauchst ein element mit der id, also push
    test("productsList sollte nur ein Element enthalten",()=>{
        expect(productList.products.length).toBe(0)
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