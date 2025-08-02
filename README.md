# Life-Expectancy-predictor
Predicting life expectancy using linear regression on WHO global health data. This project includes data preprocessing, exploratory data analysis, model training, and evaluation. Built using Python, pandas, scikit-learn, and visualized with seaborn and matplotlib.
# 🌍 Life Expectancy Prediction using Linear Regression

This project aims to predict life expectancy using a linear regression model trained on health and demographic data from the **World Health Organization (WHO)**. It demonstrates key data science workflows including data preprocessing, exploratory data analysis (EDA), model building, and performance evaluation.

## 📊 Dataset

- **Source**: WHO Global Health Observatory  
- **Features** include:
  - Adult Mortality  
  - Infant Deaths  
  - Alcohol Consumption  
  - BMI  
  - GDP  
  - Schooling  
  - Immunization Coverage  
  - Life Expectancy (Target)  

## 🛠️ Tools & Technologies

- **Python**
- **Pandas** & **NumPy** for data handling  
- **Seaborn** & **Matplotlib** for visualization  
- **Scikit-learn** for regression modeling  
- **Gradio** for web app deployment  

## 🔍 Project Workflow

1. **Data Preprocessing**
   - Handling missing values  
   - Encoding categorical variables  
   - Normalizing features  

2. **Exploratory Data Analysis (EDA)**
   - Visualizing correlations  
   - Understanding feature importance  

3. **Model Building**
   - Linear Regression using `scikit-learn`  
   - Train-test split  
   - Model evaluation using R² score and RMSE  

4. **Results**
   - Insights from the trained model  
   - Performance metrics visualization  

## 📈 Results

- Achieved reasonable accuracy in predicting life expectancy  
- Found strong correlations with schooling, income, and healthcare indicators  

## 💻 Web Application – Input Mechanism

You can interact with the **Life Expectancy Predictor** via a web interface built using **Gradio**. The application accepts health and demographic features through user-friendly sliders and provides an instant life expectancy prediction.

🔗 **Live Demo**: [Life Expectancy Predictor](https://14ec5fadd76a2ccddb.gradio.live)

### ✨ Features

- 📉 **BMI Slider**  
- 🍷 **Alcohol Consumption Slider**  
- 👶 **Infant Deaths Input**  
- 💰 **GDP Slider**  
- 🎓 **Schooling Slider**  
- 🧬 **HIV/AIDS Prevalence Input**

### 🧮 Output

Once you set the values and click **Submit**, the model instantly predicts the expected life expectancy, shown in the **"output"** box.

You can also:
- 🔁 Reset inputs using the **"Clear"** button  
- 🚩 Use the **"Flag"** button to report issues (if implemented)

### 🖼️ Sample UI Preview

![Gradio Life Expectancy Predictor](25f0f7b3-5461-44dd-8554-7995551b2e58.png)

## 📁 Folder Structure

