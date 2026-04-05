import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_charts():
    print("Loading data...")
    df = pd.read_csv('Data/cleaned_data.csv')
    
    os.makedirs('visualizations', exist_ok=True)

    # 1. Orders by Day
    print("Generating Orders by Day chart...")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='day', data=df, palette='viridis')
    plt.title('Orders by Day of Week (0 = Monday, 6 = Sunday)')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Orders')
    plt.savefig('visualizations/orders_by_day.png', bbox_inches='tight', dpi=300)
    plt.close()

    # 2. Delivery Time Analysis (by Hour)
    print("Generating Delivery Time Analysis chart...")
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='hour', y='Time_taken(min)', data=df, palette='coolwarm')
    plt.title('Delivery Time Analysis by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Time Taken (minutes)')
    plt.savefig('visualizations/delivery_time_analysis.png', bbox_inches='tight', dpi=300)
    plt.close()

    # 3. Correlation Heatmap
    print("Generating Heatmap...")
    plt.figure(figsize=(10, 8))
    # Select relevant numeric columns for correlation
    numeric_cols = ['Delivery_person_Age', 'Delivery_person_Ratings', 'Time_taken(min)', 'hour', 'day', 'month', 'weekend']
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt='.2f', square=True)
    plt.title('Feature Correlation Heatmap')
    plt.savefig('visualizations/heatmap.png', bbox_inches='tight', dpi=300)
    plt.close()
    print("Successfully saved all charts to the 'visualizations' folder.")

if __name__ == "__main__":
    create_charts()
