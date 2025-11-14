# Exploratory_Data_Analysis_Of_Titanic_Passengers_Dataset
"Exploratory Data Analysis (EDA) of Titanic passenger data to uncover key patterns and trends. Includes summary statistics, histograms, boxplots, pairplots, and correlation analysis using Pandas, Matplotlib, and Seaborn. Provides insights for further data cleaning and predictive modeling."
Overview
This repository contains the Exploratory Data Analysis (EDA) for the Titanic passenger dataset, completed as part of an internship curriculum task. The main objective is to understand the structure, relationships, and patterns within the data using descriptive statistics and visualizations.

Objectives
Generate summary statistics to understand data distribution

Visualize numerical features with histograms and boxplots

Examine feature relationships using pairplots and correlation heatmaps

Identify data patterns, trends, and anomalies

Draw basic inferences from visualizations for further ML tasks

Dataset
File: Final-Titanic-Dataset.csv

Description: Contains passenger demographics, class, fare, and survival-related attributes from the Titanic ship manifest.

Process Route
Data Loading: Loaded dataset using Pandas.

Statistical Summary: Generated numeric summary statistics (df.describe()).

Visualization:

Histogram of Age_Years to analyze age distribution.

Boxplot of Fare_Price to observe distribution and outliers.

Pairplot among numerical columns to identify feature relationships/possible clusters.

Correlation heatmap to quantify linear relationships between features.

Data Preparation: Converted categorical columns like Passenger_Class to numeric for analysis.

Analysis: Interpreted plots for trends and anomalies, such as the presence of outliers and correlations between fare/class.

Inputs and Outputs
Step	Input	Output
Data Loading	Final-Titanic-Dataset.csv	Pandas DataFrame
Statistical Summary	Numeric columns	Summary table (mean, std, min, max, etc.)
Histogram	Age_Years	Age distribution plot [Histogram]​
Boxplot	Fare_Price	Outlier/anomaly visualization [Boxplot]​
Pairplot	Numerical columns	Feature relationship plot [Pairplot]​
Correlation Matrix	Numerical columns	Correlation heatmap [Correlation]​
Key Visualizations
Histogram of Age
[Histogram-of-Age_Years.jpg]​

Boxplot of Fare
[Boxplot-of-Fair_Price.jpg]​

Correlation Matrix Heatmap
[Correlation-Matrix.jpg]​

Pairplot for Numeric Features
[Pairplot-for-Numeric-Values.jpg]​

Observations & Insights
Age distribution is approximately normal with some missing values and a concentration in young adults.

Fare price is skewed with several high-value outliers.

Passenger class is strongly negatively correlated with fare price, supporting ticket price as a proxy for socio-economic status.

Outliers and correlations are visually apparent and quantified by plots and statistics.

Tools Used
Python (Pandas, Matplotlib, Seaborn)

How to Run
Clone the repository

Ensure requirements are installed: pip install pandas matplotlib seaborn

Run Exploratory_Data_Analysis.py

Note on Visualization Tools
Although Plotly is a powerful library for creating interactive data visualizations, it was not used in this project for the following reasons:

The main visualizations required (histograms, boxplots, pairplots, and heatmaps) can be effectively created with Matplotlib and Seaborn, which are both easier to set up for static plots and widely used in academic and research settings.​

Plotly is specifically valuable for interactive charts and dashboard applications, but this task focused on static, explanatory analysis rather than web-based interactivity.​

Practical constraints existed in the development environment, such as difficulties installing Plotly due to missing pip or package manager support.

Matplotlib and Seaborn integrate seamlessly with Pandas and support highly customizable and publication-ready plots for EDA, meeting all the requirements for this internship assignment.

For future projects and advanced interactive dashboards, Plotly remains a recommended option.
