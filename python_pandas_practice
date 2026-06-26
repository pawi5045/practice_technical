# ============================================================
# PANDAS — Interview Practice
# ============================================================
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "salary": [70000, 80000, 90000, 95000, 60000],
    "department": ["HR", "HR", "Engineering", "Engineering", "Marketing"]
}
df = pd.DataFrame(data)

# ----------------------------------------------------------
# BASICS
# ----------------------------------------------------------
# Q1: Show first 3 rows
df.head(3)

# Q2: Show shape
df.shape

# Q3: Select salary column
df["salary"]

# ----------------------------------------------------------
# FILTERING
# ----------------------------------------------------------
# Q4: Filter salary > 75000
df[df["salary"] > 75000]

# Q5: Filter Engineering department only
df[df["department"] == "Engineering"]

# Q6: Filter Eve's record only
df[df["name"] == "Eve"]

# ----------------------------------------------------------
# SORTING
# ----------------------------------------------------------
# Q7: Sort by salary highest to lowest
df.sort_values("salary", ascending=False)

# Q8: Sort by name A to Z
df.sort_values("name")

# ----------------------------------------------------------
# GROUPBY
# ----------------------------------------------------------
# Q9: Average salary per department
df.groupby("department")["salary"].mean()

# Q10: Maximum salary per department
df.groupby("department")["salary"].max()

# Q11: Count employees per department
df.groupby("department")["salary"].count()

# ----------------------------------------------------------
# ADDING/REMOVING COLUMNS
# ----------------------------------------------------------
# Q12: Add tax column = 20% of salary
df["tax"] = df["salary"] * 0.2

# Q13: Add net_salary = salary - tax
df["net_salary"] = df["salary"] - df["tax"]

# Q14: Remove tax column
df.drop(columns=["tax"])

# ----------------------------------------------------------
# MISSING VALUES
# ----------------------------------------------------------
# Q15: Count missing values per column
df.isnull().sum()

# Q16: Fill missing values with 0
df.fillna(0)

# Q17: Drop rows with missing values
df.dropna()

# ----------------------------------------------------------
# LAMBDA + APPLY
# ----------------------------------------------------------
# Q18: Add bonus column = 10% of salary using apply + lambda
df["bonus"] = df["salary"].apply(lambda x: x * 0.1)

# Q19: Add level column — "Senior" if salary >= 75000 else "Junior"
df["level"] = df["salary"].apply(lambda x: "Senior" if x >= 75000 else "Junior")

# ----------------------------------------------------------
# MERGING
# ----------------------------------------------------------
departments = pd.DataFrame({
    "department": ["HR", "Engineering", "Marketing"],
    "manager": ["Frank", "Grace", "Henry"]
})

# Q20: Inner join
df.merge(departments, on="department", how="inner")

# Q21: Left join
df.merge(departments, on="department", how="left")

# Q22: Outer join
df.merge(departments, on="department", how="outer")

