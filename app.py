from flask import Flask

#creating a object for Flask
app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def helloWorld():
    return "this is my first API"

@app.route("/intro")
def intro():
    return "hi this is avirath... "

if (__name__ == "__main__"):
    app.run( debug = True )
    #app.run(debug=True , port = 8000)
    