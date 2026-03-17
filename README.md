# Indian Kids Screen Time Analysis

## WEEK 1: Project Initialization and Dataset Setup

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
## Tools Used
- Python  
- Jupyter Notebook  
- GitHub
## Libraries Used
- pandas  
- numpy  
- matplotlib  
- seaborn
- plotly

## WEEK 2: Feature engineering and derived columns

## WEEK 3: Univariate and bivariate visual analysis

## WEEK 4: Device / Activity and Weekday–Weekend Analysis

## Objective
Analyze device usage patterns, digital activity balance, and screen time differences between weekdays and weekends to identify **peak usage cohorts** among children.
## Peak Usage Cohorts – Key Observations
- Teenagers emerge as the highest screen time users, with a majority falling under High and Very High screen time categories, indicating increased digital dependency with age.
- Smartphone users dominate peak usage cohorts, showing that small-screen, portable devices contribute most to extended screen exposure.
- Children categorized under “Mostly Recreational” usage spend significantly more time on screens compared to those with balanced digital habits.
- Screen time is noticeably higher during weekends, where entertainment and gaming activities increase, making weekends a key driver of peak usage.
- The “At Risk” group is largely concentrated among high screen time users, suggesting a strong link between excessive usage and unhealthy behavior patterns.
- Urban children form a larger portion of peak usage cohorts, likely due to better access to digital devices and internet connectivity.
- Higher screen time levels are associated with increased health severity, where children with moderate to severe impacts tend to belong to heavy usage groups.
- The most critical peak usage cohort identified is:
Teenagers using smartphones, primarily engaged in recreational activities during weekends, representing the highest risk and maximum engagement segment in the dataset.

## WEEK 5: Cohort and Segment Analysis

## WEEK 6: Seasonal/Calendar or Habit Patterns

## WEEK 7: Visual Report or Dashboard Preparation

## WEEK 8: Documentation and Final Presentation

