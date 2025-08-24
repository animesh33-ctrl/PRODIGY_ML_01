# 🏠 House Price Prediction (Linear Regression)

This project provides a simple **web app** for predicting house prices using a **Linear Regression model** trained on the [Ames Housing Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

The app is built with **Gradio**, so you can interact with it via a clean UI in your browser.

---

## 🚀 Features

- Trains or loads a saved `LinearRegression` model
- Uses the following features:
  - `FullBath`
  - `HalfBath`
  - `BedroomAbvGr`
  - `LotArea`
- Predicts the target:
  - `SalePrice`
- Provides an easy-to-use browser interface

---

## 📂 Project Structure

```bash

PRODIGY_ML_01/
│── 01_House Pricing/ # Dataset & preprocessing files (if any)
│ ├── 01_House_Pricing.ipynb # Jupyter Notebook (EDA + Training)
│ ├── 01_House_Pricing_UI.py # Gradio UI for predictions
│ ├── house_lr.joblib # Saved ML model
│
│── README.md # Project documentation
```

---

## ⚙️ Installation

Clone the repo and install required dependencies:

```bash
git clone https://github.com/animesh33-ctrl/PRODIGY_ML_01
cd PRODIGY_ML_01
pip install -r requirements.txt
```

🚀 Usage

```bash
1️⃣ Train the Model (Optional)

If you want to retrain:

jupyter notebook 01_House_Pricing.ipynb


This will create/update the file house_lr.joblib.

2️⃣ Run the Gradio UI

Run the following:

python 01_House_Pricing_UI.py


This will start a Gradio web app in your browser where you can enter input values (e.g., area, number of bedrooms, location, etc.) and get predicted house price instantly.
```
