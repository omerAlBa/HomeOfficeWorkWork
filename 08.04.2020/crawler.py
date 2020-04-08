import requests
from bs4 import BeautifulSoup as bS
from urllib.parse import urljoin
import time
import csv

class Article(object):
    def __init__(this,headerText,emoji,textCard,img,site):
        this.headerText = headerText
        this.emoji = emoji
        this.textCard = textCard
        this.img = img
        this.site = site
# End of <Article> Class

class fetchArticle():
    def __init__(this,url):
        this. url = url

    def fetch(this):

        artciles = []
        while this.url != False:
            
            response = requests.get(this.url)
            data = bS(response.text, "html.parser")
            cards = data.select(".card")
            
            for card in cards:
                emoji = card.select_one(".emoji").text
                textCard = card.select_one(".card-text").text
                headerText = card.select("span")[1].text
                img = urljoin(this.url,card.select_one("img").attrs['src'])
                site = this.url

                newArticle = Article(headerText,emoji,textCard,img,site)
                artciles.append(newArticle)
            # End for card in cards
            
            nextSiteExists = data.select_one(".navigation a")
            if nextSiteExists != None:
                nextPage = urljoin(this.url,nextSiteExists.attrs['href'])
                this.url = nextPage
            else:
                this.url = False
    
        return artciles
# End of <fetchArticle> Class

class writeIntoCsvFile():
    def __init__(this, content):
        this.content = content

    def createCsvFile(this):
        with open("csvFile.csv","w",encoding="utf-8") as file:
            spamwriter = csv.writer(file, delimiter=';', quotechar='"')
            for line in this.content:
                # headerText,emoji,textCard,img,site
                spamwriter.writerow([line.headerText,line.emoji,line.textCard,line.img,line.site])
# End of <writeIntoCsvFile> class

url = "http://python.beispiel.programmierenlernen.io/index.php"

zeit = fetchArticle(url).fetch()
# print(zeit[0].headerText)
writeIntoCsvFile(zeit).createCsvFile()



# versuch nächste Seite zu bekommen Omer
# nextSiteExsits = True

# counter = 1
# while nextSiteExsits:
#     try:
#         if nextSiteExsits == True:
#             url = url.replace("index.php","index.php?page=1")
#         else:
#             url = url.replace("index.php?page="+str(counter),nextSiteExsits)
#             counter += 1

#         zeit = fetchArticle(url).fetch()

#         response = requests.get(url)
#         data = bS(response.text, "html.parser")
#         nextSiteExsits = data.select_one(".navigation a").attrs["href"]

#         print(url)
#     except Exception:
#         break
# print("Super! Das war's!")
# print(zeit.__len__())
# print(zeit[zeit.__len__()-1].img)