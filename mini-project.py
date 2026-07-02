import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset

df = pd.read_csv("students.csv")

# Display data

print("Dataset:\n", df) 

# Basic info

print("\nInfo:")

print(df.info())

# Statistical summary

print("\nSummary:")

print(df.describe())

# Add new column: Average marks

df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

df['Average'] = np.mean(df[['Math', 'Science', 'English']], axis=1)

# add grade column

def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

df['Grade']=df['Average'].apply(grade)

print("\nUpdated Dataset:\n",df)



# -------------------------------
# 📊 Visualization
# -------------------------------
# 1. Bar chart - Average marks
plt.figure()
plt.bar(df['Name'], df['Average'])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()


# 2. Pie chart - Grade distribution
plt.figure()
df['Grade'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Grade Distribution")
plt.ylabel('')
plt.show()


# 3. Line plot - Subject comparison
plt.figure()
plt.plot(df['Name'], df['Math'], label='Math')
plt.plot(df['Name'], df['Science'], label='Science')
plt.plot(df['Name'], df['English'], label='English')
plt.legend()
plt.title("Subject-wise Marks")
plt.xticks(rotation=45)
plt.show() 


