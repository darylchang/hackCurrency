from flask import Flask, render_template
import util

app = Flask(__name__)

@app.route("/")
def home():
	results = util.findCycles() #[("USD", 1.1)]
	return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run()
