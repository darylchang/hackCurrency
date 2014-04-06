from flask import Flask, render_template
import util

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()

def makeAdjacencyMatrix(): 
  codeList = util.getCurrencyCodes()
  currAdjMatrix = {code: {code: None for code in codeList} for code in codeList}
  print currAdjMatrix

makeAdjacencyMatrix()
