const app = require("http")
const url = require("url")
const path = require("path")
const query = require("querystring")
const fs = require("fs")
const mime = require("mime")


app.createServer((request,response)=>{
    const pasedURL = url.parse(request.url)

    /** Functionen */
    function responseFile({ status = 200, ContentType = "text/html", write, pfad = false}) {       
        
        if (pfad) { //anfrage eines Dokument
            
            cleanedURL = path.normalize(pfad.pathname).replace(/^(\.\.[\/\/])+/,'')
            const getPath = path.join(__dirname, ".." ,"public", cleanedURL)
            
            fs.exists(getPath, (exists)=>{
                fs.readFile(getPath,(err,content)=>{
                    if (err) {
                        return responseFile({status: 404, ContentType:"text/plain", write:"File not found!"})
                    }
                    return responseFile({status: 200, ContentType:mime.getType(pfad.pathname), write:content})
                 });
            });
        } else {
            response.writeHead(status,{"Content-Type": ContentType })
            response.write(write)
            response.end()
        }

    }
    /** Ende der Functionen */
    
    const querys = query.parse(request.url)

    //hier wird gearbeitet
    if (pasedURL.pathname === "/") {
        return responseFile({ContentType:"text/plain", write:"<h1>Function ist am laufen</h1>"})
    }

    if (pasedURL.pathname === "/json") {
        const x = {"value": "scheue","m-Mann": "xxxX"}
        return responseFile({ContentType:"application/json",write:JSON.stringify(x)})
    }

    if (pasedURL.pathname === "/main.css") {
        return responseFile({ContentType:"text/css",write:"data", pfad:pasedURL})
    }

    if (pasedURL.pathname === "/home") {
        response.writeHead(302, { "Location": 'http://localhost:616/index.html' }); 
        return response.end()
    }

    if (pasedURL.pathname === "/index.html" || pasedURL.pathname.substring(0,6) === "/dist/") {
        const pasedURL = url.parse(request.url)
        return responseFile({ContentType:"text/html", write:"data", pfad:pasedURL})
    }

    return responseFile({ContentType:"text/plain", write:"404 Error, die anfrage konnte nicht bearbeitet werden!"})
    
}).listen(616)
console.log("Listen on port 616, http://localhost:616/");
