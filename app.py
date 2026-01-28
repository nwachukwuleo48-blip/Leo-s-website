from flask import Flask render-template
app=Flask(__name__)

@app.route("/")
def hello_leo():
    return render-template("home.html")
if __name__=='__main__':
    app.run(debug=True)
