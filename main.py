from flask import Flask, render_template
from pygraph.classes.graph import graph
import util

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()