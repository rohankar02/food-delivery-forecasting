# 🍔 Food Delivery Demand Forecasting

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.7.2-orange.svg)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-Data_Manipulation-green.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

## 📌 Project Overview
This project aims to forecast the estimated delivery time (`Time_taken(min)`) for food orders based on temporal features. By leveraging machine learning techniques, we extract important patterns related to order times, days of the week, and weekend surges to help logistics teams optimize delivery operations.

## 🎯 Objective
To predict delivery times accurately using time-based features and to uncover the driving factors behind delivery delays. This analysis enables food delivery platforms to provide more precise delivery estimates to customers, minimizing churn and maximizing customer satisfaction.

## 🚀 Key Features & Approach
- **Data Engineering:** Parsed raw date and time strings to engineer robust temporal features (`hour`, `day`, `month`, `weekend`).
- **Data Cleaning:** Extracted continuous numerical targets from raw categorical text labels and handled missing values across the dataset.
- **Exploratory Data Analysis (EDA):** Visualized delivery patterns across hours of the day and weekdays using `Seaborn` to identify rush hours and peak operational blocks.
- **Predictive Modeling:** Developed a **Random Forest Regressor** (200 estimators, max depth 10) to capture nonlinear relationships in delivery behaviors.

## 📊 Results & Performance
The model successfully isolates peak hours as the primary driver of delivery time variability.
- **Mean Absolute Error (MAE):** 6.69 minutes
- **Mean Squared Error (MSE):** 69.78
- **R² Score:** 0.20

**Feature Importances:**
1. `Hour` (87.1%): The time of day dominates the delivery time impact.
2. `Day of Week` (6.2%): Mid-week vs. weekend variance.
3. `Month` (5.9%): Seasonal and monthly ordering trends.
4. `Weekend Indicator` (0.7%)

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (`RandomForestRegressor`)
* **Environment:** Jupyter Notebook

## 📂 Repository Structure
* `Data/orders.csv` : Raw dataset of delivery instances.
* `Data/cleaned_data.csv` : Processed and engineered dataset ready for modeling.
* `project2.ipynb` : Main Jupyter Notebook containing the full pipeline (EDA, preprocessing, model training, and evaluation).

## 💡 Future Work
- Incorporating geographical data (delivery location clustering) to introduce distance-based routing metrics.
- Partner and delivery-person profiling (e.g., vehicle type, historical ratings) to increase the model's predictive power.
- Experimenting with Gradient Boosting algorithms (XGBoost, LightGBM) to improve baseline accuracy.