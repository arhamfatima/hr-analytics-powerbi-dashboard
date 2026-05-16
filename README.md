# 🏢 AI-Powered HR Analytics & Workforce Intelligence Dashboard

## 📊 Project Overview
An end-to-end HR analytics dashboard built in Power BI analysing 
workforce composition, attrition risk, and employee retention patterns 
across 1,470 employees using AI-augmented development.

## 🔍 Key Insights Uncovered
- Overall attrition rate: **16.1%** across the organisation
- **Sales Representatives** have highest attrition at **39.8%**
- Employees who left earned **$2,040/month less** than those who stayed
- **Frequent travellers** leave at **24.9%** vs 8% for non-travellers
- Poor work-life balance (score 1) drives **31.3% attrition rate**
- **160 high-risk employees** identified with AttritionRisk score ≥ 60
- Age group **18-25** has highest attrition at **64.1%**

## 🛠️ Tools & Technologies
- **Power BI Desktop** — 3-page interactive dashboard
- **DAX** — Custom measures for attrition rate, risk scoring, 
  income comparison
- **Python (Pandas)** — Data cleaning and feature engineering
- **Star Schema** — Fact_Employees + 4 dimension tables
- **Claude AI** — DAX generation, data profiling, 
  narrative summaries
- **GitHub** — Portfolio hosting and documentation

## 📐 Data Model
Star schema with Fact_Employees connected to:
- Dim_Department
- Dim_JobRole
- Dim_Education
- Dim_Demographics

![Data Model](screenshots/Data_Model.png)

## 📈 Dashboard Pages

### Page 1 — Workforce Overview
- Total employees, attrition rate, avg income, avg tenure KPIs
- Headcount by department, gender split, age distribution
- Salary band breakdown and department slicer

![Page 1](screenshots/Workforce_Overview.png)

### Page 2 — Attrition Analysis
- Attrition rate by department, age group, salary band
- Attrition risk distribution
- Overtime and department slicers

![Page 2](screenshots/Attrition_Analysis.png)

### Page 3 — Attrition Deep Dive & Risk Analysis
- 160 high-risk employees identified
- Income gap: $4.79K (left) vs $6.83K (stayed)
- Attrition by job role, tenure, business travel, work-life balance
- TenureBand and department slicers

![Page 3](screenshots/Recruitment_Funnel.png)

## 🤖 AI Usage in This Project
- **Claude** generated Python cleaning script and DAX measures
- **AI-assisted feature engineering** — AttritionRisk score, 
  AgeGroup, TenureBand, SalaryBand, DistanceBand
- **AI narrative summaries** embedded on each dashboard page
- **LLM-assisted documentation** — README and code comments

## 📁 Repository Structure
hr-analytics-powerbi-dashboard/
│
├── screenshots/
│   ├── Workforce_Overview.png
│   ├── Attrition_Analysis.png
│   ├── Recruitment_Funnel.png
│   └── Data_Model.png
│
├── hr_cleaning.py
├── HR_Analytics_Cleaned.csv
├── HrAnalyticsDashboard.pbix
├── ibm-hr-analytics-employee-attrition-performance.csv
└── README.md

## 📊 Dataset
IBM HR Analytics Employee Attrition Dataset
- 1,470 employees
- 35 original features
- 5 engineered features added
- Source: Kaggle
