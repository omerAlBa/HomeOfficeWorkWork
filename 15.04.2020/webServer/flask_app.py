from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/currency", methods=['GET', 'POST'])
def rechner():
    element = {}
    if request.args.__len__() > 0:
        element['währung1'] = request.args.get("währung1")
        element['währung2'] = request.args.get("währung2")
        element['wechselkurs'] = request.args.get("wechselkurs")
        
        table,table2 = {},{}

        for i in range(1,20):
            table[i] = round(i * float(element['wechselkurs']),2)
        element["table1"] = table

        for i in range(1,20):
            table2[i] = round(i / float(element['wechselkurs']),2)
        element["table2"] = table2

        print(element["table2"])

    return render_template('rechner.html',element=element)

if __name__ == "__main__":
    app.run()