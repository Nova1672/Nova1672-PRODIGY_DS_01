import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure Matplotlib backend
import matplotlib
matplotlib.use('TkAgg')  # Adjust based on your environment

# Verify file existence
if not os.path.exists('gender_development.csv'):
    raise FileNotFoundError("The file 'gender_development.csv' was not found.")

# Load the data
df = pd.read_csv('gender_development.csv')

# Display basic info
print("Data Overview:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names in the dataset:")
print(df.columns.tolist())

# Clean data (handle multiple missing value representations)
df.replace(['..', '', 'NA', 'N/A'], pd.NA, inplace=True)

# Convert numeric columns from string to float
numeric_columns = ['Gender Development Index (GDI)', 'Human Development Index (Female)', 
                  'Human Development Index (Male)', 'Life Expectancy at Birth (Female)', 
                  'Life Expectancy at Birth (Male)', 'Expected Years of Education (Female)', 
                  'Expected Years of Education (Male)', 'Mean Years of Education (Female)', 
                  'Mean Years of Education (Male)', 'Estimated Gross National Income per Capita (Female)', 
                  'Estimated Gross National Income per Capita (Male)']

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Plot 1: Top 10 Countries by GDI
plt.figure(figsize=(8, 4))
top_gdi = df.dropna(subset=['Gender Development Index (GDI)']).nlargest(10, 'Gender Development Index (GDI)')
if not top_gdi.empty:
    sns.barplot(x='Gender Development Index (GDI)', y='Country', data=top_gdi, palette='tab10')
    plt.title('Top 10 Countries by Gender Development Index (GDI)')
    plt.xlabel('GDI Score')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()
else:
    print("No data available for GDI bar plot after dropping NA values.")

# Plot 2: Life Expectancy Comparison
plt.figure(figsize=(8, 4))
life_exp = df.dropna(subset=['Life Expectancy at Birth (Female)', 'Life Expectancy at Birth (Male)']).head(15)
if not life_exp.empty:
    life_exp.plot(x='Country', y=['Life Expectancy at Birth (Female)', 'Life Expectancy at Birth (Male)'], 
                  kind='bar', color=['#ff9999', '#66b3ff'])
    plt.title('Life Expectancy: Female vs Male (Top 15 Countries)')
    plt.ylabel('Years')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No data available for Life Expectancy plot after dropping NA values.")

# Plot 3: Education Comparison
plt.figure(figsize=(8, 4))
education = df.dropna(subset=['Expected Years of Education (Female)', 'Expected Years of Education (Male)']).head(15)
if not education.empty:
    education.plot(x='Country', y=['Expected Years of Education (Female)', 'Expected Years of Education (Male)'], 
                   kind='bar', color=['#ff9999', '#66b3ff'])
    plt.title('Expected Years of Education: Female vs Male (Top 15 Countries)')
    plt.ylabel('Years')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No data available for Education plot after dropping NA values.")

# Plot 4: Income Comparison Scatter Plot
plt.figure(figsize=(8, 4))
income = df.dropna(subset=['Estimated Gross National Income per Capita (Female)', 
                           'Estimated Gross National Income per Capita (Male)'])
if not income.empty:
    max_income = max(income['Estimated Gross National Income per Capita (Female)'].max(),
                     income['Estimated Gross National Income per Capita (Male)'].max()) * 1.1
    plt.scatter(income['Estimated Gross National Income per Capita (Female)'], 
                income['Estimated Gross National Income per Capita (Male)'], alpha=0.6)
    plt.plot([0, max_income], [0, max_income], 'r--')
    plt.title('Female vs Male Income per Capita')
    plt.xlabel('Female Income (USD)')
    plt.ylabel('Male Income (USD)')
    plt.xlim(0, max_income)
    plt.ylim(0, max_income)
    plt.grid(True)
    plt.show()
else:
    print("No data available for Income scatter plot after dropping NA values.")

# Plot 5: GDI Distribution Histogram
plt.figure(figsize=(8, 4))
gdi_data = df['Gender Development Index (GDI)'].dropna()
if not gdi_data.empty:
    sns.histplot(gdi_data, bins=min(20, len(gdi_data)//5), kde=True, color='purple')
    plt.title('Distribution of Gender Development Index (GDI)')
    plt.xlabel('GDI Score')
    plt.ylabel('Number of Countries')
    plt.show()
else:
    print("No data available for GDI histogram after dropping NA values.")