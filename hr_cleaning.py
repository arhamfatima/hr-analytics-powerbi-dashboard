import pandas as pd

# STEP 1 - LOAD DATA
print("=== STEP 1: LOADING DATA ===")

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")  # Load raw HR attrition data
print("Shape:", df.shape)
print("Data types:\n", df.dtypes)
print("First 5 rows:\n", df.head(5))

# STEP 2 - EXPLORE DATA
print("\n=== STEP 2: EXPLORE DATA ===")

print("Null counts per column:\n", df.isnull().sum())
print("\nNumeric summary:\n", df.describe())
print("\nAttrition value counts:\n", df["Attrition"].value_counts(dropna=False))
print("\nDepartment value counts:\n", df["Department"].value_counts(dropna=False))
print("\nJobRole value counts:\n", df["JobRole"].value_counts(dropna=False))
print("\nGender value counts:\n", df["Gender"].value_counts(dropna=False))

# STEP 3 - CLEAN DATA
print("\n=== STEP 3: CLEAN DATA ===")

shape_before = df.shape
print("Shape before cleaning:", shape_before)

# Drop constant or useless identifier columns that do not contribute to analysis
cols_to_drop = ["EmployeeCount", "EmployeeNumber", "Over18", "StandardHours"]
df = df.drop(columns=cols_to_drop, errors="ignore")

# Convert binary categorical columns to integer flags for modeling and summary
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0}).astype(int)
df["OverTime"] = df["OverTime"].map({"Yes": 1, "No": 0}).astype(int)

# Strip whitespace from all object/string columns to normalize text values
object_cols = df.select_dtypes(include="object").columns
for col in object_cols:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

shape_after = df.shape
print("Shape after cleaning:", shape_after)
print("Rows unchanged:", shape_before[0] == shape_after[0])

# STEP 4 - ENGINEER NEW FEATURES
print("\n=== STEP 4: ENGINEER NEW FEATURES ===")

# AgeGroup bins employee age into meaningful cohorts
age_bins = [17, 25, 35, 45, 55, 100]
age_labels = ["18-25", "26-35", "36-45", "46-55", "55+"]
df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels, right=True, include_lowest=True)

# TenureBand bins YearsAtCompany into progression stages
tenure_bins = [-1, 2, 5, 10, float("inf")]
tenure_labels = ["New (0-2)", "Developing (3-5)", "Experienced (6-10)", "Veteran (10+)"]
df["TenureBand"] = pd.cut(df["YearsAtCompany"], bins=tenure_bins, labels=tenure_labels, right=True)

# SalaryBand uses income quartiles to create four salary categories
salary_labels = ["Low", "Medium", "High", "Very High"]
df["SalaryBand"] = pd.qcut(df["MonthlyIncome"], q=4, labels=salary_labels, duplicates="drop")

# DistanceBand groups commuting distance into zones
distance_bins = [0, 5, 15, float("inf")]
distance_labels = ["Near (1-5)", "Medium (6-15)", "Far (16+)"]
df["DistanceBand"] = pd.cut(df["DistanceFromHome"], bins=distance_bins, labels=distance_labels, right=True)

# AttritionRisk score aggregates multiple risk factors into a 0-100 integer score
risk_score = pd.Series(0, index=df.index)
risk_score += df["Attrition"] * 40
risk_score += df["OverTime"] * 20
risk_score += (df["JobSatisfaction"] <= 2).astype(int) * 15
risk_score += (df["WorkLifeBalance"] <= 2).astype(int) * 15
risk_score += (df["YearsSinceLastPromotion"] >= 5).astype(int) * 10

# Cap risk score at 100 to keep values within range
risk_score = risk_score.clip(upper=100).astype(int)
df["AttritionRisk"] = risk_score

# STEP 5 - VALIDATE
print("\n=== STEP 5: VALIDATE ===")

print("AgeGroup value counts:\n", df["AgeGroup"].value_counts(dropna=False))
print("\nTenureBand value counts:\n", df["TenureBand"].value_counts(dropna=False))
print("\nSalaryBand value counts:\n", df["SalaryBand"].value_counts(dropna=False))
print("\nDistanceBand value counts:\n", df["DistanceBand"].value_counts(dropna=False))
print("\nAttritionRisk value counts:\n", df["AttritionRisk"].value_counts(dropna=False).sort_index())

print("\nAttritionRisk distribution:\n", df["AttritionRisk"].describe())
print("\nSample of engineered feature columns:\n", df[["AgeGroup", "TenureBand", "SalaryBand", "DistanceBand", "AttritionRisk"]].head(10))

# STEP 6 - EXPORT
print("\n=== STEP 6: EXPORT ===")

output_file = "HR_Analytics_Cleaned.csv"
df.to_csv(output_file, index=False)
print("Data cleaning complete! HR_Analytics_Cleaned.csv saved successfully.")
print("Final shape:", df.shape)
print("Columns:\n", df.columns.tolist())
