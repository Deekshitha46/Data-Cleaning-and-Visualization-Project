import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("dataset.csv")

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["Salary"] >= lower) & (df["Salary"] <= upper)]

# Salary Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Salary"], bins=8)
plt.title("Salary Distribution")
plt.savefig("salary_distribution.png")
plt.show()

# Department Count
plt.figure(figsize=(6,5))
sns.countplot(x="Department", data=df)
plt.title("Employees in Each Department")
plt.savefig("department_count.png")
plt.show()

# Age vs Salary
plt.figure(figsize=(7,5))
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.savefig("age_salary.png")
plt.show()

# Salary Boxplot
plt.figure(figsize=(6,5))
sns.boxplot(y=df["Salary"])
plt.title("Salary Boxplot")
plt.savefig("salary_boxplot.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(5,4))
sns.heatmap(df[["Age","Salary"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

df.to_csv("cleaned_dataset.csv", index=False)

print("Project Completed Successfully")