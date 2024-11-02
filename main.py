# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

# Set page configuration
st.set_page_config(layout='wide')
st.title("**Advanced Data Visualization Dashboard**")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type='csv')

# If file is uploaded
if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Display an overview of the dataset
    st.write("### Overview of the Dataset")
    st.write(data.head())

    # Display the shape of the dataset
    st.write("**Data Shape:**", data.shape)

    # Display basic statistics of the dataset
    st.write("### Basic Statistics")
    st.write(data.describe())

    # Sidebar for data visualization settings
    st.sidebar.subheader("Visualization Setup")

    # --- Pie Chart Section ---
    st.sidebar.subheader("Pie Chart")
    pie_column = st.sidebar.selectbox("Select Column for Pie Chart", data.columns)

    if st.sidebar.button("Generate Pie Chart"):
        st.write("### Pie Chart")
        fig, ax = plt.subplots()
        data[pie_column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax, startangle=90)
        ax.set_ylabel('')
        st.pyplot(fig)

    # --- Correlation Heatmap Section ---
    if st.sidebar.checkbox("Show Correlation Heatmap"):
        st.write("### Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # --- Bar Chart Section ---
    st.sidebar.subheader("Bar Chart")
    bar_column = st.sidebar.selectbox("Select Column for Bar Chart", data.columns)

    if st.sidebar.button("Generate Bar Chart"):
        st.write("### Bar Chart")
        fig, ax = plt.subplots()
        data[bar_column].value_counts().plot.bar(color="skyblue", ax=ax, edgecolor="black")
        ax.set_xlabel(bar_column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # --- Violin Plot Section ---
    st.sidebar.subheader("Violin Plot")
    violin_column = st.sidebar.selectbox("Select Column for Violin Plot", data.columns)

    if st.sidebar.button("Generate Violin Plot"):
        st.write("### Violin Plot")
        fig, ax = plt.subplots()
        sns.violinplot(x=data[violin_column], ax=ax)
        ax.set_xlabel(violin_column)
        st.pyplot(fig)

    # --- Histogram Section ---
    st.sidebar.subheader("Histogram")
    hist_column = st.sidebar.selectbox("Select Column for Histogram", data.columns)

    if st.sidebar.button("Generate Histogram"):
        st.write("### Histogram")
        fig, ax = plt.subplots()
        sns.histplot(data[hist_column], kde=True, color="purple", ax=ax)
        ax.set_xlabel(hist_column)
        st.pyplot(fig)

    # --- Box Plot Section ---
    st.sidebar.subheader("Box Plot")
    box_column = st.sidebar.selectbox("Select Column for Box Plot", data.columns)

    if st.sidebar.button("Generate Box Plot"):
        st.write("### Box Plot")
        fig, ax = plt.subplots()
        sns.boxplot(x=data[box_column], color="lightblue", ax=ax)
        ax.set_xlabel(box_column)
        st.pyplot(fig)

    # --- Line Plot Section ---
    st.sidebar.subheader("Line Plot")
    line_column = st.sidebar.selectbox("Select Column for Line Plot", data.columns)

    if st.sidebar.button("Generate Line Plot"):
        st.write("### Line Plot")
        fig, ax = plt.subplots()
        data[line_column].plot(kind='line', color="green", ax=ax)
        ax.set_xlabel("Index")
        ax.set_ylabel(line_column)
        st.pyplot(fig)

    # --- 3D Scatter Plot Section ---
    st.sidebar.subheader("3D Scatter Plot")
    scatter3d_x = st.sidebar.selectbox("3D Scatter X-axis", data.columns)
    scatter3d_y = st.sidebar.selectbox("3D Scatter Y-axis", data.columns)
    scatter3d_z = st.sidebar.selectbox("3D Scatter Z-axis", data.columns)

    if st.sidebar.button("Generate 3D Scatter Plot"):
        st.write("### 3D Scatter Plot")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[scatter3d_x], data[scatter3d_y], data[scatter3d_z], color='b', alpha=0.7)
        ax.set_xlabel(scatter3d_x)
        ax.set_ylabel(scatter3d_y)
        ax.set_zlabel(scatter3d_z)
        st.pyplot(fig)

else:
    st.write("Please upload a CSV file to proceed.")
