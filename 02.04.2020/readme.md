# Wie startest du das Projekt?

1. npm install
2. npm run start:dev
3. Irgendwo in der Ausgabe wird ausgegeben: Project is running at http://localhost:8081/.
   Den Link im Browser öffnen, ggf. in den "public"-Ordner navigieren! Der Port ist aber
   ggf. unterschiedlich!
4. `npm run build` baut die Dateien im `production`-Modus!

# Wie wurde das Projekt erstellt?

- npm install --save-dev @webpack-cli/init ejs

- npx webpack-cli init
  - SASS benutzen: JA
  - Sass ermöglichst uns CSS komfortabler zu schreiben
  - Sass wird in normales CSS umgewandelt

- SASS aktivieren:
  - In der index.js-Datei können wir jetzt eine .scss-Datei per require()
    einbinden
  - Diese wird dann von Webpack automatisch mit Hilfe von SCSS nach CSS 
    umgewandelt
  - Der CSS-Code landet aber standardmäßig mit in unserer .js-Datei
  - Daher brauchen wir noch ein Webpack-Plugin: 
    https://github.com/webpack-contrib/mini-css-extract-plugin
  - npm install --save-dev mini-css-extract-plugin
  - Und müssen den "style-loader" aus unserer Webpack-Konfiguration entfernen
    https://github.com/webpack-contrib/mini-css-extract-plugin/issues/173

- Webpack-Dev-Server wurde eingerichtet
  - npm install --save-dev webpack-dev-server
  - => https://webpack.js.org/configuration/dev-server/
  - Kann über `npm run start:dev` gestartet werden

- ejs-Loader wurde eingerichtet
  - Wenn wir jetzt per require() eine .ejs-Datei einbinden, wird diese automatisch
    in eine JavaScript-Funktion umgewandelt!
  - => https://www.npmjs.com/package/ejs-loader