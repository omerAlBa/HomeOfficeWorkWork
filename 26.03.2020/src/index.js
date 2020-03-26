/*
function Greeting(name){
    this.list = []
}
hallo Welt
Greeting.prototype.add = function(name){
    debugger
    if (this.list.includes(name)){
        return  
    } 
    console.log(this.list.includes(name));
    
    this.list.push(name)
}

module.exports = Greeting 

function resolveAsync(function_) {
    setTimeout(function() {
        function_("hallo Welt")
    },1000)
}

function resolvePromise() {
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("hallo Welt")
        },1000)
    })
}

module.exports.resolveAsync = resolveAsync
module.exports.resolvePromise = resolvePromise
 

 //testen von DOMElemente

 const button = document.getElementById("counter")
 let counter = parseInt(button.textContent)

 button.addEventListener("click",()=>{
    counter++
    button.textContent = counter 
 })
 */

 //

 function StudentModule() {
    this.students = []
  }
  
  StudentModule.prototype.addStudent = function(name) {
    if (this.students.indexOf(name) === -1) {
      this.students.push(name)
    }
  }
  
  StudentModule.prototype.removeStudent = function(name) {
    const pos = this.students.indexOf(name)
    if (pos !== -1) {
      this.students.splice(pos, 1)
    }
  }
  
  module.exports = StudentModule