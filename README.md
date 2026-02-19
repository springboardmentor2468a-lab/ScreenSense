# Week 1: Project Initialization and Dataset Setup

## Define Goals and Workflow
The goal of Week 1 was to understand the dataset and set a clear workflow for the project. The focus was on exploring the data before starting detailed analysis.

## Load the Dataset
The dataset was loaded using pandas in Jupyter Notebook. The CSV file was successfully imported for analysis.

## Explore Schema, Data Types, Size, and Null Values
- Checked the number of rows and columns using `df.shape`.
- Reviewed column names and data types using `df.info()`.
- Identified missing values using `df.isnull().sum()`.
- Observed that the `Health_Impacts` column contains missing values.

## Initial Notes on Data Quality and Assumptions
- Most columns are clean and properly structured.
- Some missing values are present in the dataset.
- Missing data was preserved during initial exploration to avoid bias.
- The dataset is suitable for further preprocessing and visualization in upcoming weeks.
