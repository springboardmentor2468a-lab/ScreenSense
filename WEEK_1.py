import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Data/screentime.csv")

## Show structure

# (rows,columns)
print(df.shape)
#cloumn names and datatypes
df.info()
# visual structure
print(df.head())

## check data quality

# Check missing values
# --detect
missing = df.isnull().sum()
missing = missing[missing > 0]
print("Columns with missing values:\n", missing)
# --Percentage(decide)
missing_percent = (df.isnull().sum() / len(df)) * 100
print("\nMissing percentage:\n", missing_percent[missing_percent > 0])
# --Handle missing(fix)
df["Health_Impacts"].fillna(df["Health_Impacts"].mode()[0], inplace=True)
# --Verify
print("\nAfter cleaning:\n", df.isnull().sum())

# Check duplicate rows
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

## Statistical
print(df.describe())

## UNIVARIATE ANALYSIS

# Screen Time Distribution
plt.hist(df['Avg_Daily_Screen_Time_hr'])
plt.title("Distribution of Total Screen Hours")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.show()
# Device Usage
sns.countplot(x='Primary_Device', data=df)
plt.title("Device Usage")
plt.show()

## BIVARIATE ANALYSIS

# Screen Time by Gender
sns.boxplot(x='Gender', y='Avg_Daily_Screen_Time_hr', data=df)
plt.show()
# Screen Time by Age
sns.scatterplot(x='Age', y='Avg_Daily_Screen_Time_hr', data=df)
plt.show()
# Screen Time vs Urban/Rural
sns.boxplot(x='Urban_or_Rural', y='Avg_Daily_Screen_Time_hr', data=df)
plt.title("Urban vs Rural Screen Time")
plt.show()
# Screen Time vs Device
sns.boxplot(x='Primary_Device', y='Avg_Daily_Screen_Time_hr', data=df)
plt.title("Screen Time by Device")
plt.show()
# Screen Time vs Health Impact
sns.boxplot(x='Health_Impacts', y='Avg_Daily_Screen_Time_hr', data=df)
plt.title("Screen Time vs Health Impact")
plt.xticks(rotation=30)
plt.show()
# Screen Time vs Limit Exceeded
sns.boxplot(x='Exceeded_Recommended_Limit', y='Avg_Daily_Screen_Time_hr', data=df)
plt.title("Screen Time vs Recommended Limit")
plt.show()
# Device vs Location
sns.countplot(x='Primary_Device', hue='Urban_or_Rural', data=df)
plt.title("Device Preference by Location")
plt.xticks(rotation=30)
plt.show()

##MULTIVARIATE ANALYSIS

# Which device causes highest screen time in urban vs rural kids?
sns.boxplot(x='Primary_Device', y='Avg_Daily_Screen_Time_hr', hue='Urban_or_Rural', data=df)
plt.xticks(rotation=30)
plt.title("Screen Time by Device and Location")
plt.show()
# Teen boys using mobiles show highest screen exposure (INSIGHT EXTRACTION)
bins = [5, 8, 12, 16]
labels = ['Young Kids', 'Pre-Teens', 'Teenagers']

df['Age_Band'] = pd.cut(df['Age'], bins=bins, labels=labels)
sns.boxplot(x='Age_Band', y='Avg_Daily_Screen_Time_hr', hue='Gender', data=df)
plt.title("Screen Time by Age Group and Gender")
plt.show()

## OUTLIER DETECTION

sns.boxplot(y=df['Avg_Daily_Screen_Time_hr'])
plt.show()



