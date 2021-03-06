from flask import Flask, render_template, request, jsonify,redirect, url_for
import  requests
import pickle

from sklearn.linear_model import LogisticRegression

app = Flask(__name__,template_folder='template')
model = pickle.load(open('loan_approval_prediction_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


lr = LogisticRegression
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Loan_Id=str(request.form.get('Loan_Id'))
        Applicant_income=str(request.form.get('Applicant_income'))
        Coapplicant_income=str(request.form.get('Coapplicant_income'))
        Loan_Amount=str(request.form.get('Loan_Amount'))
        Loan_Amount_Term=str(request.form.get('Loan_Amount_Term'))
        Credit_History=str(request.form.get('Credit_History'))
        Property_Area=str(request.form.get('Property_Area'))
        if(Property_Area=='Urban'):
          Property_Area=1
        else:       
          Property_Area=0
        Self_employed=str(request.form.get('self_employed'))
        if(Self_employed=='yes'):
           Self_employed=1
        else:
             Self_employed=0
        Dependents=str(request.form.get('Dependents'))
        if(Dependents=='0'):
           Dependents=0
        elif(Dependents=='1'):
            Dependents=1
        elif(Dependents=='2'):
            Dependents=2
        else:
            Dependents=3
        Education=str(request.form.get('Education'))
        if(Education=='Graduate'):
           Education=1
        else:
           Education=0
        Married=str(request.form.get('Married'))
        if(Married=='yes'):
           Married=1
        else:
            Married=0
        Gender=str(request.form.get('Gender'))
        if(Gender=='Male'):
           Gender=1
        else:
            Gender=0
        prediction=model.predict([[Applicant_income,Coapplicant_income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Area,Self_employed,Dependents,Education,Married,Gender,Loan_Id]])
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
