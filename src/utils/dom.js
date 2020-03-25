/** 
 * live Selektor
 * Fragen: an das ganze Dom oder bedingt? 2.) was passiert mit mehreren on's?
 * Antwort: bedingt ist mir lieber. 2.) weis ich nicht
 * @who classname
 */

 // erstelle eine function
 //parameter (event, wonachAusSchauHalten, woHalteIchAusschau, wasSollGemachtWerden)
 module.exports.on = function on(whereToTrigger, who, event, action){
    whereToTrigger.addEventListener(event,function(event){
        //suche auch in eltern!
        let clickedElement = event.target
        while(whereToTrigger.contains(clickedElement)){
            if (clickedElement.className === who.className) {
                return action({
                    element: clickedElement,
                    origanalEvent: event
                })
            }
            clickedElement = clickedElement.parentNode
        }
        
        return event.target   
    });
 }