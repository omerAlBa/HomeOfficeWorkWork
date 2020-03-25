//unfertig, funktioniert einfach nicht

function EventListener(){
    this.events = {}
    
    this.action = ()=>{
        let a = 1+1
        this.trigger("hub",a)
     }
    
     this.link = (eventName,action)=>{

        if (!(eventName in this.events)) {
            this.events[eventName] = []    
        }
        this.events[eventName].push(action)
        
    }

    this.trigger = function(eventName,element){
        console.log("hier ist trigger");
        
        if (eventName in this.events) {
            this.events[eventName].forEach((function_) => {
              function_(element)
            });
          }
    }
}


EventListener.link("hub",(a)=>{
    console.log("bin drinne", a);
});

EventListener.action()