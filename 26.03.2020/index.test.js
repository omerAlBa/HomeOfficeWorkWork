/*
const Greeting = require("./src/index")
test("testen wir dich einmal",(done)=>{
   const greeting = new Greeting()
    greeting.add("hallo")
    greeting.add("hallo")
    greeting.add("was machen sachen")
    
    expect(greeting.list.length === 2).toBe(true)
    done()
})


 const {resolveAsync,resolvePromise} = require("./src/index")

 test("teste async functionen und promise",(done)=>{
     resolveAsync((message)=>{
        expect(message).toBe("hallo Welt")
        done()
     })
 })

 test("teste async functionen und promise",()=>{
    return resolvePromise().then((message)=>{
        expect(message).toBe("hallo Welt")
    })
})


 beforeEach(()=>{
     document.body.innerHTML = `<button id="counter">0</button>`
 })

 test("test mein Dom action",()=>{
    const x = document.getElementById("counter")

    expect(x.textContent === "0").toBe(true)

    
    require("./src/index")
    x.click();

    expect(x.textContent === "1").toBe(true)
 })

  */

  describe("studentsModule",()=>{
      test("einbauen von den KonstruktorFunction",()=>{
          const X = require("./src/index")
          const x = new X()
          expect(x.addStudent).not.toBeNull()
      })

      test("user hinzufügen",()=>{
        const X = require("./src/index")
        const x = new X()
        expect(x.students.length === 0).toBe(true)
        x.addStudent("Omer Ali")
        expect(x.students.length === 1).toBe(true)
    })

    test("keine zwei user hinzufügen",()=>{
        const X = require("./src/index")
        const x = new X()
        expect(x.students.length === 0).toBe(true)
        x.addStudent("Omer Ali")
        x.addStudent("Omer Ali")
        expect(x.students.length === 1).toBe(true)
    })

    test("user löschen",()=>{
        const X = require("./src/index")
        const x = new X()
        
        x.addStudent("Omer Ali")
        x.addStudent("Ali")
        x.addStudent("Negga")

        x.removeStudent("Ali")
        expect(x.students.includes("Ali") === -1).toBe(true)
    })
  })
 