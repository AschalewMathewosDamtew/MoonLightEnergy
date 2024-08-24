# scripts/data_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import plotly.express as px

# 1. Load the dataset
def load_data(filepath):
    return pd.read_csv(filepath, parse_dates=['Timestamp'])

# 2. Summary Statistics
def summary_statistics(df):
    return df.describe()

# 3. Data Quality Check
def data_quality_check(df):
    missing_values = df.isnull().sum()
    negative_values = df.select_dtypes(include=[np.number])[(df < 0).any(1)]
    return missing_values, negative_values

# 4. Time Series Analysis
def time_series_analysis(df):
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    df.set_index('Timestamp')['GHI'].plot(ax=axs[0, 0], title='GHI over Time')
    df.set_index('Timestamp')['DNI'].plot(ax=axs[0, 1], title='DNI over Time')
    df.set_index('Timestamp')['DHI'].plot(ax=axs[1, 0], title='DHI over Time')
    df.set_index('Timestamp')['Tamb'].plot(ax=axs[1, 1], title='Tamb over Time')
    plt.show()

# 5. Correlation Analysis
def correlation_analysis(df):
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.show()

# 6. Wind Analysis (Polar Plot)
def wind_analysis(df):
    fig = px.scatter_polar(df, r="WS", theta="WD", color="WSgust", 
                           title="Wind Speed and Direction")
    fig.show()

# 7. Temperature Analysis
def temperature_analysis(df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="RH", y="Tamb", ax=ax)
    ax.set_title('Temperature vs. Relative Humidity')
    plt.show()

# 8. Histograms
def plot_histograms(df):
    df[['GHI', 'DNI', 'DHI', 'WS', 'Tamb']].hist(bins=20, figsize=(10, 10))
    plt.show()

# 9. Z-Score Analysis
def z_score_analysis(df):
    z_scores = df.select_dtypes(include=[np.number]).apply(zscore)
    outliers = z_scores[(np.abs(z_scores) > 3).any(axis=1)]
    return outliers

# 10. Bubble Chart
def bubble_chart(df):
    fig = px.scatter(df, x='GHI', y='Tamb', size='WS', color='RH', 
                     title='GHI vs Tamb vs WS', hover_data=['BP'])
    fig.show()

# 11. Data Cleaning
def clean_data(df):
    # Example: Drop columns with all null values
    df_cleaned = df.dropna(axis=1, how='all')
    # Additional cleaning steps go here
    return df_cleaned
