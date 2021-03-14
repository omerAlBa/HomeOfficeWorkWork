// fertige Version

function EventListener(){
    this.events = {}

    // actionen werden hier gespeichert
     this.link = (eventName,action)=>{

        if (!(eventName in this.events)) {
            this.events[eventName] = []    
        }
        this.events[eventName].push(action)
        
    }
    // event wird gefeuert
    this.trigger = function(eventName,element){
        
        if (eventName in this.events) {
            this.events[eventName].forEach((function_) => {
              function_(element)
            });
        }
    }
}
