import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_time_series(df, dataset_name):
    fig, ax = plt.subplots(figsize=(14, 8))
    df[['GHI', 'DNI', 'DHI', 'Tamb']].plot(ax=ax)
    plt.title(f'Time Series Analysis of GHI, DNI, DHI, and Tamb in {dataset_name}')
    st.pyplot(fig)

import matplotlib.pyplot as plt
import streamlit as st

def plot_area(df, title, columns):
    try:
        # Check if any column contains both positive and negative values
        for col in columns:
            if df[col].min() < 0 and df[col].max() > 0:
                raise ValueError(f"Column '{col}' contains both positive and negative values, which is not allowed in an area plot.")

        # Create area plot
        fig, ax = plt.subplots()
        df[columns].plot(kind='area', ax=ax, alpha=0.5)
        ax.set_title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    
    except ValueError as e:
        # Handle the ValueError and provide an appropriate message
        st.error(f"Error in plotting area chart: {e}")

def create_scatter_plot(df):
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='RH', y='Tamb', ax=ax)
    plt.title("Scatter Plot: Temperature (Tamb) vs Relative Humidity (RH)")
    st.pyplot(fig)

def create_correlation_analysis(df, dataset_name):
    correlation = df[['RH', 'Tamb', 'TModA', 'TModB']].corr()
    st.write(f"### Correlation Analysis - {dataset_name}")
    st.write(correlation)
