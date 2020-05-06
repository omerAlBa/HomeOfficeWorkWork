
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep 
  
usr='de' 
pwd='' 

class MF():
    def __init__(this, user, password):
        this. user = user
        this.password = password
        this.driver = webdriver.Chrome('chromedriver')
        this.event_Elements = {}
        this.log_in()
        sleep(4)
        this.objekt = this.init_eventElements()
        
    def init_eventElements(this):
        JSInit_Elements = """
            const fn =function(){
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
            
            function Body(elements){
                this.elements = elements
            }

            Body.prototype.init = function(){
                for (element of this.elements.querySelectorAll(":scope > div") ){
                    if( element.innerHTML.contains('Erforderliche Information') ){
                        return this.basis(element)
                    }
                }
            }
            
            Body.prototype.basis = function(element){
                const obj = {}
                let basicData = Array.prototype.slice.call(element.querySelectorAll(":scope > div"));
                let bodyElements = basicData.find((element) => element.innerHTML.contains("Ort"))
                
                bodyElements = Array.prototype.slice.call(bodyElements.querySelectorAll(":scope > div"))

                obj["name"] = this.basisSpliter( bodyElements.find((element) => element.innerHTML.contains("Namen hinzu")),"Namen hinzu" )
                obj["ort"] = this.basisSpliter( bodyElements.find((element) => element.innerHTML.contains("Ort oder Adresse")), "Ort oder Adresse", 2)
                
                obj["beschreibung"] = this.basisSpliter( bodyElements.find((element) => element.innerHTML.contains("Beschreibe anderen")), "Beschreibe anderen")

                obj["kategorie"] = this.basisSpliter( bodyElements.find((element) => element.innerHTML.contains("Kategorie auswählen")), "Kategorie auswählen" )
                obj["zeit mangment"] = this.timeSpliter(this.basisSpliter( bodyElements.find((element) => element.innerHTML.contains("Beginn")), "Beginn",2))
                console.log(obj)
                return obj
            }
            
            Body.prototype.timeSpliter = function(elements){
                const beginn = this.basisSpliter(elements,"Beginn").querySelectorAll("input[type='text']")
                const ende = this.basisSpliter(elements,"Ende").querySelectorAll("input[type='text']")
                return {
                    "startDatum": beginn[0],
                    "startZeit": beginn[1],
                     "endeDatum": ende[0],
                     "endeZeit": ende[1],
                }
            }

            Body.prototype.basisSpliter = function(bodyElement,text,rounds=1){
                for (var i = 0; i < rounds; i++){
                    bodyElement = Array.prototype.slice.call(bodyElement.querySelectorAll(":scope > div"));
                    bodyElement = bodyElement.find((element) => element.innerHTML.contains(text))
                }
                return bodyElement
            }

            const getBodyEvent = function(body){
                for (element of body){
                    if(element.innerHTML.contains("Erforderliche Information")){
                        getBasisInfo(element)
                    }
                }
            }

            const getCloseEvent_action = function(footer){
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

    def createEvent(this):
        JScript = """
        const fn = function(text){
            document.querySelector('._4ixr').querySelector("span[class='_55pe']").innerText = String(text)
        }
        """
        this.objekt["event_body"]["name"].find_element_by_css_selector("input[type='text']").send_keys("Name und so")
        this.objekt["event_body"]["zeit mangment"]["startDatum"].send_keys(" 20.05.2020" + Keys.TAB)
        this.objekt["event_body"]["zeit mangment"]["startZeit"].send_keys("02:00")
        this.objekt["event_body"]["ort"].find_element_by_css_selector("input[type='text']").send_keys("Kiel")
        this.objekt["event_body"]["zeit mangment"]["endeDatum"].send_keys(" 22.05.2020" + Keys.TAB)
        this.objekt["event_body"]["zeit mangment"]["endeZeit"].send_keys("03:45")
        this.objekt["event_body"]['beschreibung'].find_element_by_css_selector("div[class='notranslate _5rpu']").send_keys("so das reicht jetzt")
        kategorie = "musik"
        this.driver.execute_script(JScript + "fn('" + kategorie + "')")
        # objekt["event_end"]["speichern/entwurf"].click() funktioniert!
        
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

    def wirte_Properties_4_event(this):
        JScript = """
        const listOfSpan = document.querySelectorAll('._55pe')
        for(element of listOfSpan){
            console.log(element)
            if(element.innerHTML.contains('Kategorie')){
                element.click()
                element.innerText = 'Theater'
                break
            }
        }
        """
        div_eventArea = this.driver.find_element_by_css_selector('._4t2a')
        # Name
        div_eventArea.find_elements_by_css_selector('input[class="_58al"]')[0].send_keys('Name der Vernastaltung')
        # Ort
        div_eventArea.find_elements_by_css_selector('input[class="_58al"]')[1].send_keys('Kiel')
        # Beschreibung
        div_eventArea.find_element_by_css_selector('._5yk2').send_keys("programmieren geschreibe macht spaß")
        # Categorie
        sleep(2)
        categorie = div_eventArea.find_element_by_css_selector('div[class="_mh- _4bl9"]')
        this.driver.execute_script(JScript)
        # Zeiten
        div_eventTime = div_eventArea.find_elements_by_css_selector('div[class="clearfix _ikh"]')
        # Beginn
        haveToStart = div_eventTime[0].find_elements_by_css_selector('input[type="text"]')
        print(haveToStart.__len__())
        sleep(2)
        haveToStart[0].send_keys(" 30.05.2020")
        #start time
        haveToStart[1].send_keys("12:00")
        # Ende
        haveToEnd = div_eventTime[1].find_elements_by_css_selector('input[type="text"]')
        sleep(1)
        haveToEnd[0].send_keys(" 01.06.2020")
        haveToEnd[1].send_keys("13:00")
    
    def tester(this):
        JScript = """
            const search = function({searchForText = ''}){
                const className = "_4ixr"
                const div_Wrapper = document.querySelectorAll(`.${className} > div`)
                for (const div_element of div_Wrapper) {
                    if (div_element.innerHTML.contains(searchForText)){
                        return getSingleElement(div_element)
                    }
                }
            };

            const getSingleElement = function(element){
                const childElements = element.querySelectorAll(":scope > div")
                for (childElement of childElements){
                    if(childElement.innerHTML.contains("Beschreibung")){
                        return collectElement(childElement.querySelectorAll(":scope > div"))
                    }
                }
            };

            const collectElement = function(listElements){
                console.log('listElements: ', listElements)
                console.log("collectElement wird ausgeführt")
                let index = 0
                let obj = {}
                const className = "_mh- _4bl9"
                for (listElement of listElements){
                    let element = listElement.innerHTML

                    if(element.contains('Name')){
                        console.log(listElement.querySelector(`div[class="${className}"]`))
                        obj['name'] = listElement.querySelector(`:scope div[class="${className}"]`)
                    } else if(element.contains('Ort')){
                        obj['ort'] = listElement.querySelector(`div[class="${className}"]`)
                    } else if(element.contains('Kategorie')){
                        obj['kategorie'] =  listElement.querySelector(`div[class="${className}"]`)
                    } else if(element.contains('Häufigkeit')){
                        obj['dateTime'] = getTime(listElement.querySelector(`div[class="${className}"]`))
                    } else if(element.contains('Beschreibung')){
                        obj['beschreibung'] = listElement.querySelector(`div[class="${className}"]`) || listElement.querySelector(`div[class="_3879 _4bl9"]`)
                    }

                }
                console.log("listElements: ",listElements)
                obj['eventBTN'] = getActionBTN(document.querySelector('div[class="_5lnf uiOverlayFooter _5a8u _67lr"]').querySelectorAll('button[type="submit"]'))
                return obj
            };

            const getTime = function(timeElement){
                const className = 'clearfix _ikh'
                const start = {}
                const ende = {}
                const timeElementList = timeElement.querySelectorAll(`div[class="${className}"]`)
                for(element of timeElementList){
                    if(element.innerHTML.contains("Beginn")){
                        beginnListe = element.querySelectorAll("input[class]")
                        start['datum'] = beginnListe[0]
                        start['uhrzeit'] = beginnListe[1]
                    } else if(element.innerHTML.contains("Ende")){
                        endeListe = element.querySelectorAll("input[class]")
                        ende['datum'] = endeListe[0]
                        ende['uhrzeit'] = endeListe[1]
                    }
                }
                return {start,ende}
            }

            const getActionBTN = function(elements){
                //element.querySelectorAll('button[type="submit"]')
                console.log("getActionBTN() wird ausgeführt")
                let obj = {}
                for(element of elements){
                    if(element.classList.contains('hidden_elem')){
                        continue
                    }
                    if(element.innerHTML.contains('Entwurf speichern')){
                        obj['entwurf'] = element
                    }else if(element.innerHTML.contains('Veröffentlichen')){
                        obj['speichern'] = element
                    }
                    console.log(element)
                }
                return obj
            }
        """
        objekt = this.driver.execute_script(JScript + 'return search({searchForText:"Erforderliche Information"})')
        # this.driver.execute_async_script("setTimeout(console.log('asynce is on!!!'), 2000)")
        # objekt["name"].find_element_by_css_selector('input[type="text"]').send_keys('Name der Vernastaltung')
        # this.driver.find_element_by_partial_link_text('Füge einen kurzen').send_keys("Kinder Garten")
        objekt['dateTime']['start']['datum'].send_keys(' 10.05.2020' + Keys.TAB)
        objekt['dateTime']['ende']['datum'].send_keys(' 10.05.2020' + Keys.TAB)
        # objekt["kategorie"].click()
        objekt["ort"].find_element_by_css_selector('input[type="text"]').send_keys('Kiel')
        objekt['dateTime']['start']['uhrzeit'].send_keys('12:00')
        objekt['dateTime']['ende']['uhrzeit'].send_keys('13:00')
        beschreibung = this.driver.find_element_by_partial_link_text('Beschreibe anderen')
        beschreibung.send_keys("kinder machen das halt so!")
        kategorie = this.driver.find_element_by_link_text('Kategorie auswählen')
        kategorie.send_keys(Keys.SPACE + Keys.NUMPAD3 + Keys.ENTER)
        # objekt['eventBTN']['entwurf'].click()

# driver.get('https://www.facebook.com/Mfv-104578101237033/?modal=admin_todo_tour')

x = MF(usr, pwd)
x.createEvent()
# x.facebook_mfSite()

x.close_mf()
