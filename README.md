# 🚗 Car Price Predictor

A machine learning web application built with Flask that predicts the selling price of a used car based on user input such as company, model, year, fuel type, and kilometers driven.

## 📂 Project Structure

```
car-price-predictor/
├── app.py                       # Flask application
├── cleaned car.csv             # Cleaned dataset used for training
├── LinearRegressionModel.pkl   # Trained Linear Regression model
├── quikr_car.csv               # Raw scraped dataset from Quikr
├── car-price-predictor.ipynb   # Jupyter notebook for preprocessing and model building
├── templates/
│   └── index.html              # HTML frontend form
├── static/
│   └── css/
│       └── style.css           # Styling for the webpage
└── README.md                   # Project documentation
```

## 📊 Dataset

- **Source**: Scraped from [Quikr.com](https://www.quikr.com/)
- **Raw Data**: `quikr_car.csv`
- **Cleaned Data**: `cleaned car.csv` contains structured columns:
  - `name`, `company`, `year`, `kms_driven`, `fuel_type`, `Price`

## 🧠 Model

- **Algorithm**: Linear Regression
- **Training**: Done in `car-price-predictor.ipynb`
- **Pipeline**: Includes preprocessing steps like:
  - Label encoding categorical values
  - Converting year and kms_driven to numeric
- **Saved Model**: Serialized using `pickle` (`LinearRegressionModel.pkl`)

## 🌐 Web Application

- **Framework**: Flask
- **Endpoints**:
  - `/` – Loads homepage with dropdowns for user input
  - `/predict` – Accepts POST requests and returns predicted price
- **Features**:
  - Dynamic dropdowns for car companies, models, fuel types, and years
  - Returns a predicted price on form submission

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install flask pandas numpy scikit-learn
```

### 3. Run the App
```bash
python app.py
```

### 4. Open in Browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📸 Screenshots

*(Add screenshots of the web UI here if available)*

## 🛠 Future Improvements

- Use more advanced models (e.g., XGBoost, Random Forest)
- Add input validation & error handling
- Show prediction on the HTML page instead of returning raw text
- Deploy on Render/Heroku

## 📄 License

This project is for educational purposes.

## 🙋‍♂️ Author

Parth Waradkar  
📧 your-email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)