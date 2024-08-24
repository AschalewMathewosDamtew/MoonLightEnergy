# app/main.py

import streamlit as st
import os
import sys
# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the scripts directory to the Python path
sys.path.append(os.path.join(current_dir, '../scripts'))
import data_analysis as da




st.title("Solar Radiation Data Analysis")

# Load data
df = da.load_data('../data/benin-malanville.csv')


# Sidebar
option = st.sidebar.selectbox("Select Analysis", ("Summary Statistics", "Time Series Analysis", 
                                                  "Correlation Analysis", "Create Wind Plot", 
                                                  "Temperature Analysis", "Histograms", 
                                                  "Z-Score Analysis", "Bubble Chart"))

# Display analysis
if option == "Summary Statistics":
    st.write(da.summary_statistics(df))
elif option == "Time Series Analysis":
    da.time_series_analysis(df)
elif option == "Correlation Analysis":
    da.correlation_analysis(df)
elif option == "Create Wind Analysis":
    da.create_polar_plot(df, 'Wind Direction')
elif option == "Temperature Analysis":
    da.temperature_analysis(df)
elif option == "Histograms":
    da.plot_histograms(df)
elif option == "Z-Score Analysis":
    st.write(da.z_score_analysis(df))
elif option == "Bubble Chart":
    da.bubble_chart(df)
