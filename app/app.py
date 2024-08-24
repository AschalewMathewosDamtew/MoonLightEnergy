import streamlit as st
from data_processing import load_data, clean_and_prepare_data
from utils import data_quality_check
from plots import plot_time_series, plot_area, create_scatter_plot, create_correlation_analysis
import pandas as pd

# Load datasets
datasets = load_data()

# Streamlit UI
st.title("Solar Radiation Data Analysis")

# Sidebar for dataset selection
dataset_name = st.sidebar.selectbox("Select Dataset", ("Benin", "Togo", "Sierra Leone"))
df = datasets[dataset_name]

# Display the dataset summary
st.write(f"### {dataset_name} Dataset Summary")
st.write(df.describe())

# Sidebar: Want to Clean Section
clean_data = st.sidebar.checkbox("Want to Clean Data")

if clean_data:
    # Data Quality Check Before Cleaning
    quality_results_before = data_quality_check(df)
    st.write("#### Data Quality Check Results (Before Cleaning)")
    st.write(pd.DataFrame(quality_results_before).T)

    # Clean Data
    df_cleaned = clean_and_prepare_data(df)

    # Data Quality Check After Cleaning
    quality_results_after = data_quality_check(df_cleaned)
    st.write("#### Data Quality Check Results (After Cleaning)")
    st.write(pd.DataFrame(quality_results_after).T)

    # Display cleaned data
    st.write(f"### {dataset_name} Cleaned Data")
    st.write(df_cleaned.head())

# Sidebar: Analysis Selection
st.sidebar.write("### Which to Analyze?")
analyze_uncleaned = st.sidebar.checkbox("Analyze Uncleaned Data")
analyze_cleaned = st.sidebar.checkbox("Analyze Cleaned Data")

# Determine which dataset to analyze
df_to_analyze = None
data_label = ""

if analyze_uncleaned:
    df_to_analyze = df
    data_label = "Uncleaned Data"
elif analyze_cleaned and clean_data:
    df_to_analyze = df_cleaned
    data_label = "Cleaned Data"

# Display analysis options if either checkbox is selected
if analyze_uncleaned or (analyze_cleaned and clean_data):
    st.sidebar.write(f"### Analysis Options for {data_label}")
    plot_area_selected = st.sidebar.checkbox("Area Plot")
    plot_time_series_selected = st.sidebar.checkbox("Time Series Plot")
    plot_scatter_selected = st.sidebar.checkbox("Scatter Plot")
    plot_correlation_selected = st.sidebar.checkbox("Correlation Analysis")

    # Perform selected analyses
    if plot_correlation_selected and df_to_analyze is not None:
        create_correlation_analysis(df_to_analyze, dataset_name)

    if plot_area_selected and df_to_analyze is not None:
        plot_area(df_to_analyze, dataset_name)

    if plot_scatter_selected and df_to_analyze is not None:
        create_scatter_plot(df_to_analyze)

    if plot_time_series_selected and df_to_analyze is not None:
        plot_time_series(df_to_analyze, dataset_name)
else:
    st.warning("Please select either 'Analyze Uncleaned Data' or 'Analyze Cleaned Data'.")
