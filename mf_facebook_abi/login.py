
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep 
  
usr='omera13@hotmail.de' 
pwd='Milkaka13' 

class MF():
    def __init__(this, user, password):
        this. user = user
        this.password = password
        this.driver = webdriver.Chrome('chromedriver')
        this.event_Elements = {}
        this.log_in()
        sleep(4)
        this.objekt = this.init_eventElements()
        for key in this.objekt.keys():
            print(key)
        
    def init_eventElements(this):
        JSInit_Elements = """
            
            const fn = function()
            {
                const obj = {}
                const className = "_4t2a"
                const body_className = "_4ixr"
                const footer_className = "uiOverlayFooter"

                const eventLayer = document.querySelector('div[class="_4t2a"]')

                const fn2 = new Body(eventLayer.querySelector(`.${body_className}`))
                obj['event_body'] = fn2.init()
                
                //speicher oder entwurf ist fertig, vlt kann man noch Planen mit einbringen!
                obj['event_end'] = getCloseEvent_action(eventLayer.querySelector(`.${footer_className}`))
                return obj
            }
            
            function Body(elements)
            {
                this.elements = elements
            }

            Body.prototype._ARRAY_ = function(element){
                return Array.prototype.slice.call(element)
            }

            Body.prototype.init = function()
            {
                obj = {}
                for (element of this.elements.querySelectorAll(":scope > div"))
                {
                    if( element.innerHTML.contains('Erforderliche Information') ){
                        obj['basis'] = this.basis(element)
                    } else if (element.innerHTML.contains('Weitere Gastgeber')){
                        obj['weitere gastgeber'] = this.hoster(element)
                    } else if (element.innerHTML.contains('Füge weitere Infos')){
                        obj['weitere details'] = this.extended_details(element)
                    } else if (element.innerHTML.contains('Eintritt')){
                        obj['eintritt'] = this.entry(element)
                    } else if (element.innerHTML.contains('Optionen')){
                        obj['optionen'] = this.option(element)
                    }
            
                }
                return obj
            }
            
            Body.prototype.option = function(element)
            {
                labelElements = this._ARRAY_(element.querySelectorAll(':nth-child(1) > label'))
                return{
                    "nachrichten erhalten" : labelElements.find(element => this.find('Messenger können Fragen')),
                    "gästeliste anzeigen" : labelElements.find(element => this.find('Gästeliste anzeigen'))
                }
            }

            Body.prototype.entry = function(element)
            {
                let spanElements = this._ARRAY_(element.querySelectorAll("span > div"))
                spanElements
                    .find(element => this.find(element,'Ticket-Link hinzufügen'))
                    .querySelector('button')
                    .click()
                spanElements
                    .find(element => this.find(element,'Bestätigung hinzufügen'))
                    .querySelector('button')
                    .click()

                // refresh "spanElements" new elements available
                spanElements = this._ARRAY_(element.querySelectorAll("span > div")) 
                
                return {
                    "ticket bestätigung": spanElements.find(element => this.find(element,'Bestätigung hinzufügen')).querySelector('button'),
                    "Ticket-Link hinzufügen": spanElements.find(span => this.find(element,'Ticket-URL')).querySelector('input[type="text"]')
                }
            }
            

            Body.prototype.extended_details = function(element)
            {
                const tableElement = this._ARRAY_(element.querySelectorAll('table'))
                return {
                    "kinder geeignet": tableElement.find(element => this.find(element,'Für Kinder')),
                    "ehrenamtliche tätigkeit": tableElement.find(element => this.find(element,'Ehrenamtlichen'))
                }
            }

            Body.prototype.hoster = function(element)
            {
                return element.querySelector('input[type="text"]')
            }

            Body.prototype.basis = function(element)
            {
                const obj = {}
                alert("basis wurde geklickt")
                let basicData = this._ARRAY_(element.querySelectorAll(":scope > div"));
                let bodyElements = basicData.find(element => element.innerHTML.contains("Ort"));
                bodyElements = this._ARRAY_(bodyElements.querySelectorAll(":scope > div"));
                
                obj["foto"] = bodyElements
                    .find(element => this.find(element,"Foto/Video"))
                    .querySelector('input[type="file"]')
                obj["name"] = bodyElements
                    .find(element => this.find(element,"Namen hinzu"))
                    .querySelector('input[type="text"]')
                obj["ort"] = bodyElements
                    .find(element => this.find(element,"Ort oder Adresse"))
                    .querySelector('input[type="text"]')
                obj["beschreibung"] = bodyElements
                    .find(element => this.find(element,"Beschreibe anderen"))
                    .querySelector('div[class="notranslate _5rpu"]')
                //obj["kategorie"] = bodyElements.find(element => this.find(element,"Beschreibe anderen"))

                obj["zeit mangment"] = this.timeSpliter(this.basisSpliter( bodyElements.find(element => this.find(element,"Beginn")), "Beginn",2))
                return obj
            }
            
            Body.prototype.find = function(element, getText)
            {
                console.log(`find(): [ element: ${element}, getText: ${getText} ]`)
                return element.innerHTML.contains(getText)
            }

            Body.prototype.finder = function(_element_, {getText = "", getElement="", actionNeeded=false}={})
            {
                _element_
                    .find(element => element.innerHTML.contains(getText))
                    .querySelector(getElement)
            }

            Body.prototype.timeSpliter = function(elements)
            {
                const beginn = this.basisSpliter(elements,"Beginn").querySelectorAll("input[type='text']")
                const ende = this.basisSpliter(elements,"Ende").querySelectorAll("input[type='text']")
                return {
                    "startDatum": beginn[0],
                    "startZeit": beginn[1],
                     "endeDatum": ende[0],
                     "endeZeit": ende[1],
                }
            }

            Body.prototype.basisSpliter = function(bodyElement,text,rounds=1)
            {
                for (var i = 0; i < rounds; i++){
                    bodyElement = this._ARRAY_(bodyElement.querySelectorAll(":scope > div"));
                    bodyElement = bodyElement.find((element) => element.innerHTML.contains(text))
                }
                return bodyElement
            }

            const getCloseEvent_action = function(footer)
            {
                return {
                    "speichern": document.evaluate('//button[text() = "Veröffentlichen" and not(contains(@class, "hidden_elem"))]', footer, null, XPathResult.ANY_TYPE, null ).iterateNext(),
                    "entwurf": document.evaluate('//button[text() = "Entwurf speichern"]', footer, null, XPathResult.ANY_TYPE, null ).iterateNext()
                }
            }
        """
        this.openEventLayer()
        sleep(3)
        return this.driver.execute_script(JSInit_Elements + " return fn() ")

    def openEventLayer(this):
        JScript = """
            const fn = function(){
                const event_start = document.evaluate('//span[text() = "Veranstaltung"]', document, null, XPathResult.ANY_TYPE, null )
                return event_start.iterateNext().click()
            }
        """
        this.driver.execute_script(JScript + " return fn() ")

    def createEvent(this,kategorie="theater"):
        JScript = """
        const fn = function(text)
            {
                document.querySelector('._4ixr').querySelector("span[class='_55pe']").innerText = text
            }
             """
        this.objekt["event_body"]['basis']["foto"].send_keys("C://Users/homer_000/Pictures/TERA_ScreenShots/img3.jpg")
        this.objekt["event_body"]['basis']["name"].send_keys("Bla und so")
        this.objekt["event_body"]['basis']["zeit mangment"]["startDatum"].send_keys(" 20.05.2020" + Keys.TAB)
        this.objekt["event_body"]['basis']["zeit mangment"]["startZeit"].send_keys("02:00")
        this.objekt["event_body"]['basis']["ort"].send_keys("Kiel")
        this.objekt["event_body"]['basis']["zeit mangment"]["endeDatum"].send_keys(" 22.05.2020" + Keys.TAB)
        this.objekt["event_body"]['basis']["zeit mangment"]["endeZeit"].send_keys("03:45")
        this.objekt["event_body"]['basis']['beschreibung'].send_keys("so das reicht jetzt")
        this.driver.execute_script(JScript + "fn('" + kategorie + "')")
        this.objekt["event_body"]["weitere details"]["kinder geeignet"].click()
        this.objekt["event_body"]["weitere gastgeber"].send_keys("Disco" + Keys.ENTER)
        this.objekt["event_body"]["optionen"]["gästeliste anzeigen"].click()
        this.objekt["event_end"]["entwurf"].click()
        
    def log_in(this):
        this.driver.get('https://www.facebook.com/')
        print ("Opened facebook")
        sleep(3)

        username_box = this.driver.find_element_by_id('email') 
        username_box.send_keys(usr) 
        print ("Email Id entered")

        password_box = this.driver.find_element_by_id('pass') 
        password_box.send_keys(pwd) 
        print ("Password entered") 

        login_box = this.driver.find_element_by_id('loginbutton') 
        login_box.click()
        sleep(3)
        this.driver.get('https://www.facebook.com/Mfv-104578101237033/?modal=admin_todo_tour')

    def feed_post(this,message):
        status_box = this.driver.find_element_by_xpath('.//*[@name="xhpc_message"]')
        status_box.send_keys(message)
        print('post writed')
        sleep(3)
        this.driver.execute_script("document.querySelector('._1mf7').click()")

    def close_mf(this):
        print("Script end")
        input('Press anything to quit') 
        this.driver.quit()



x = MF(usr, pwd)
x.createEvent()

x.close_mf()
