from flask import Flask, render_template, request
import pickle

app = Flask(__name__,template_folder='template')

model= pickle.load(open('heartdisease.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html')

@app.route('/predict', methods =['POST', 'GET'])
def predict():
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    cp = float(request.form['cp'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    fbs = float(request.form['fbs'])
    restecg = float(request.form['restecg'])
    thalach = float(request.form['thalach'])
    ca = float(request.form['ca'])
    thal= float(request.form['thal'])
    
    result = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,ca,thal]])[0]
    return render_template('index.html')


           
if __name__== '__main__':
    app.run(debug=True)
