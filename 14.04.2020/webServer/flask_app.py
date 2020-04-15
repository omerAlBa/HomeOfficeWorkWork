from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/rechner", methods=['GET', 'POST'])
def rechner():
    if request.method == 'POST':
        print(request.form.get('betrag'))
    return render_template('rechner.html')

if __name__ == "__main__":
    app.run()