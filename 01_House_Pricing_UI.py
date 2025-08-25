import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
import gradio as gr

TRAIN_CSV = r"C:\Programming\Prodigy Infotech\PRODIGY_ML_01\01_House Pricing\train.csv"
MODEL_PATH = "house_lr.joblib"
FEATURES = ['FullBath','HalfBath','BedroomAbvGr','LotArea']
TARGET = 'SalePrice'

def fit_or_load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    df = pd.read_csv(TRAIN_CSV)
    X = df[FEATURES]
    y = df[TARGET]
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

model = fit_or_load_model()

def predict_price(full_bath, half_bath, bedroom_abv_gr, lot_area):
    X = [[full_bath, half_bath, bedroom_abv_gr, lot_area]]
    pred = float(model.predict(X)[0])
    return f"{pred:,.2f}"

demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="FullBath", precision=0, value=2),
        gr.Number(label="HalfBath", precision=0, value=1),
        gr.Number(label="BedroomAbvGr", precision=0, value=3),
        gr.Number(label="LotArea (sq ft)", value=8000),
    ],
    outputs=gr.Textbox(label="Predicted SalePrice"),
    title="House Price Prediction (Linear Regression)",
    description="Trained exactly like your notebook on: FullBath, HalfBath, BedroomAbvGr, LotArea."
)

if __name__ == "__main__":
    demo.launch()
