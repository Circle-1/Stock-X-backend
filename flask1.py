from flask import *  
from flask_cors import CORS
import csv
app = Flask(__name__) 
CORS(app)
 
@app.route('/')  
def home():  
    #return "Flask is active!"
    return redirect("http://localhost:3000/") 
 
@app.route('/predict', methods = ['POST']) 
def success():  
    if request.method == 'POST':  
        f = request.files['csvfile']  
        data=[]
        with open(f) as file:
            csvfile=csv.reader(file)

        f.save(f.filename)  
        return redirect("http://localhost:3000/predict")
  
if __name__ == '_main_':  
    app.run(host='0.0.0.0', debug = True)  
