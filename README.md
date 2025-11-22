# ev-population-analysis-end-to-end
End-to-end Electric Vehicle (EV) Population Analysis project using Python, MySQL, and Power BI. Includes full ETL pipeline, data cleaning, categorization, MySQL loading, and interactive Power BI dashboards analyzing EV trends, prices, battery capacity, range, counties, CAFV eligibility, and vehicle categories.

## Project Overview  
This project is an **end-to-end data analytics pipeline** built using:

- **Python** → Data cleaning, transformation, and categorization  
- **MySQL** → Structured storage & query layer for BI tools  
- **Power BI** → Interactive dashboard (EV Adoption, Range, Price, Battery Categories)  
- **GitHub** → Version control & portfolio showcase  

The dataset used is the **Electric Vehicle Population Dataset** (from Washington State), containing **150K+ vehicle records** with fields like make, model, range, MSRP, battery capacity, county, year, CAFV eligibility, etc.


## Objectives

1. Clean & transform raw EV data into a usable analytics dataset  
2. Categorize vehicles into **High / Medium / Low** buckets based on:
   - Range  
   - Price  
   - Battery capacity  
3. Load cleaned data into **MySQL** for BI querying  
4. Build an **interactive Power BI dashboard** with slicers, KPIs & drill-downs  
5. Present insights about EV adoption trends, manufacturers, ranges & pricing  



## Problem Statement
EV growth has accelerated, but stakeholders need clarity on:  
- Which counties lead EV adoption?  
- Which manufacturers dominate?  
- Are consumers buying high-range / high-price EVs or economical ones?  
- What are the top 3 EV models in:  
  - High-end category  
  - Mid-range category  
  - Budget category  
- What is the average price, range, and age of EVs by model/make?



##  Solution Approach

###  Step 1 — Data Ingestion  
Load raw CSV using **pandas**.

### Step 2 — Cleaning & Preprocessing  
- Fix missing values  
- Clean column names  
- Standardize datatypes  
- Extract battery kWh

###  Step 3 — Categorization
Range / Price / Battery Category (High / Medium / Low)

###  Step 4 — Save Cleaned Data  
Output → `ev_cleaned.csv`

###  Step 5 — Load into MySQL  
Using `data_pipeline.py`.

###  Step 6 — Power BI Dashboard  
Three pages: Home, Details, Summary.

##  Dashboard Pages
(Home, Details, Summary – full descriptions included earlier)

##  Installation & Setup

### Install dependencies
```
pip install -r requirements.txt
```

### Create DB
```
python db_setup.py
```

### Run ETL
```
python data_pipeline.py
```

##  SQL Queries & DAX Measures  
(As described in the README above)

##  GitHub Deployment
```
git init
git add .
git commit -m "Initial commit"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

##  Conclusion
End-to-end EV Data Analytics Project.
End-to-end EV Data Analytics Project.

