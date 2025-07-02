from flask import Flask,render_template,request
import pandas as pd
import pickle
app = Flask(__name__)
car = pd.read_csv('cleaned car.csv')

model = pickle.load(open('LinearRegression.pkl','rb'))

@app.route('/')
def index():
    companies = sorted(car['company'].unique(),reverse=True)
    car_models = sorted(car['name'].unique(),reverse=True)
    year = sorted(car['year'].unique(),reverse=True)
    fuel_types = sorted(car['fuel_type'].unique(),reverse=True)
    
    
    return render_template('index.html',companies = companies, car_models = car_models , years = year , fuel_types = fuel_types)

@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year= int(request.form.get('year'))
    fuel_types = request.form.get('fuel_types')
    kms_driven = request.form.get('kilo_driven')
    print(company,car_model,year,fuel_types,kms_driven)
    
    return ""


if __name__ == "__main__":
    app.run(debug=True)