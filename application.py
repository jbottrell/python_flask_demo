from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('')
def homepage():
    #Print("Is this thing on?")
    return "<h1>Hello World!</h1>"

@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()
#this is a comment