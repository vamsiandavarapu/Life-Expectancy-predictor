import pandas as pd
import gradio as gr
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("Life Expectancy Data.csv")

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Selected features
features = [
    ' BMI ',
    'Alcohol',
    'infant deaths',
    'GDP',
    'Schooling',
    ' HIV/AIDS'
]

target = 'Life expectancy '

X = df[features]
y = df[target]

# Train model
model = LinearRegression()
model.fit(X, y)


def predict_life_expectancy(
    bmi, alcohol, infant_deaths,
    gdp, schooling, hiv
):
    input_df = pd.DataFrame([[
        bmi,
        alcohol,
        infant_deaths,
        gdp,
        schooling,
        hiv
    ]], columns=features)

    prediction = model.predict(input_df)[0]

    return f"{prediction:.2f} years"


demo = gr.Interface(
    fn=predict_life_expectancy,
    inputs=[
        gr.Slider(10, 50, label="BMI"),
        gr.Slider(0, 15, label="Alcohol"),
        gr.Slider(0, 100, label="Infant Deaths"),
        gr.Slider(0, 100000, label="GDP"),
        gr.Slider(0, 20, label="Schooling"),
        gr.Slider(0, 30, label="HIV/AIDS")
    ],
    outputs="text",
    title="🌍 Life Expectancy Predictor",
    description="Enter health and economic factors to predict average life expectancy."
)
import os

port = int(os.environ.get("PORT", 7860))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)
