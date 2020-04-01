const app = require("http")
const url = require("url")
const path = require("path")
const query = require("querystring")
const fs = require("fs")

app.createServer((request,response)=>{
    const querys = query.parse(request.url)
    console.log(request.url);
    if (request.url === "/") {
        response.writeHead(200,{
            "Content-Type": "text/html"
        })
        response.write("<h1>Willkommen zu '/'</h1>")
        response.end()
        return
    }
    if (request.url === "/json") {
        response.writeHead(200,{
            "Content-Type": "application/json"
        })
        const x = {
            "value": "scheue",
            "m-Mann": "xxxX"
        }
        response.write(JSON.stringify(x))
        response.end()
        return
    }
    if (request.url === "/main.css") {
        const pasedURL = url.parse(request.url)
        cleanedURL = path.normalize(pasedURL.pathname).replace(/^(\.\.[\/\/])+/,'')
        const getPath = path.join(__dirname, "public", cleanedURL)

        fs.readFile(getPath,(err,data)=>{
            response.writeHead(200,{"Content-Type":"text/css"})
            response.write(data)
            response.end()
            return
        })
    }

}).listen(666)