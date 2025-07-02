from flask import Flask,render_template
import pandas as pd
app = Flask(__name__)
car = pd.read_csv('cleaned car.csv')


@app.route('/')
def index():
    companies = sorted(car['company'].unique(),reverse=True)
    car_models = sorted(car['name'].unique(),reverse=True)
    year = sorted(car['year'].unique(),reverse=True)
    fuel_types = sorted(car['fuel_type'].unique(),reverse=True)
    
    
    return render_template('index.html',companies = companies, car_models = car_models , years = year , fuel_types = fuel_types)

@app.route('predict',methods=['POST'])
def predict():
    return
if __name__ == "__main__":
    app.run(debug=True)