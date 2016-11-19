from flask import Flask, request
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/london") 
def name():         
	return "London is the capital and most populous city of England and the United Kingdom."
@app.route("/paris") 
def paris(): 
 return "Paris test"
	
@app.route("/japan") 
def japan(): 
 return " Japan test"
	
if __name__ == "__main__":     
	app.run()
