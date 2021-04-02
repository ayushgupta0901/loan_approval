from flask import Flask, render_template, request
import jsonify
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('loan_approval_prediction_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Loan_Id=str(request.form['Loan_Id'])
        Applicant_income=int(request.form['Applicant_income'])
        Coapplicant_income=int(request.form['Coapplicant_income'])
        Loan_Amount=float(request.form['Loan_Amount'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
        Credit_History=float(request.form['Credit_History'])
        Property_Area=str(request.form['Property_Area'])
        if(Property_Area=='Urban'):
          Property_Area=2
        else:
          Property_Area=0
        Self_employed=str(request.form['self_employed'])
        if(Self_employed=='yes'):
           Self_employed=1
        else:
             Self_employed=0
        Dependents=int(request.form['Dependents'])
        if(Dependents=='0'):
           Dependents=0
        elif(Dependents=='1'):
            Dependents=1
        elif(Dependents=='2'):
            Dependents=2
        else:
            Dependents=3
        Education=str(request.form['Education'])
        if(Education=='Graduate'):
           Education=1
        else:
           Education=0
           Married=str(request.form['Married'])
        if(Married=='yes'):
           Married=1
        else:
            Married=0
        Gender=str(request.form['Gender'])
        if(Gender=='Male'):
           Gender=1
        else:
            Gender=0
        prediction=model.predict([[Applicant_income,Coapplicant_income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Area,Self_employed,Dependents,Education,Married,Gender,Loan_Id]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="main":
    app.run(debug=True)