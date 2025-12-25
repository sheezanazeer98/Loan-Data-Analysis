# Loan Data Analysis Project

## Project Overview

This project provides a comprehensive analysis of loan application data using both SQL and Python. The analysis includes data cleaning, exploratory data analysis, statistical insights, and visualizations to understand factors affecting loan approval decisions.

## Dataset Description

The dataset contains loan application information with the following features:

- **Loan_ID**: Unique loan application ID
- **Gender**: Applicant's gender (Male/Female)
- **Married**: Marital status (Yes/No)
- **Dependents**: Number of dependents (0, 1, 2, 3+)
- **Education**: Education level (Graduate/Not Graduate)
- **Self_Employed**: Self employment status (Yes/No)
- **ApplicantIncome**: Applicant's income
- **CoapplicantIncome**: Co-applicant's income
- **LoanAmount**: Loan amount requested
- **Loan_Amount_Term**: Loan term in days
- **Credit_History**: Credit history status (1=Good, 0=Bad)
- **Property_Area**: Property area type (Urban/Rural/Semiurban)
- **Loan_Status**: Loan approval status (Y=Approved, N=Rejected)

## Project Structure

```
Project/
│
├── loan_data_set.csv          # Dataset file
├── create_database.sql         # SQL script to create database and table
├── data_analysis.sql           # SQL queries for data analysis
├── load_data.py               # Python script to load data into MySQL
├── data_analysis.py           # Python script for comprehensive analysis
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Prerequisites

### Software Requirements

1. **Python 3.7+**
2. **MySQL Server** (for SQL analysis)
3. **MySQL Connector** (for Python-MySQL integration)

### Python Libraries

Install required Python libraries using:

```bash
pip install -r requirements.txt
```

Required libraries:
- pandas
- numpy
- matplotlib
- seaborn
- mysql-connector-python

## Installation & Setup

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: MySQL Database Setup

1. Start your MySQL server
2. Open MySQL command line or MySQL Workbench
3. Run the database creation script:

```bash
mysql -u root -p < create_database.sql
```

Or execute the SQL file in MySQL Workbench.

### Step 3: Load Data into MySQL (Optional)

If you want to use SQL analysis, load the data using:

```bash
python load_data.py
```

**Note:** Update the MySQL connection details in `load_data.py`:
- `host`: Your MySQL host (default: 'localhost')
- `user`: Your MySQL username (default: 'root')
- `password`: Your MySQL password

## Usage

### Python Analysis

Run the comprehensive Python analysis:

```bash
python data_analysis.py
```

This script will:
1. Load and clean the data
2. Perform statistical analysis
3. Analyze demographic factors
4. Analyze income and loan amount factors
5. Create visualizations
6. Generate a summary report

**Output Files:**
- `loan_analysis_visualizations.png` - Visualization charts
- `analysis_report.txt` - Summary report

## Expected Output

When you run `python data_analysis.py`, you will see the following output in your console and generated files:

### Console Output

The script will display comprehensive analysis results in the following sections:

#### 1. **Project Header**
```
==================================================
LOAN DATA ANALYSIS PROJECT
Created by: Sheeza Nazeer
==================================================
```

#### 2. **Data Loading**
- Dataset loaded successfully message
- Dataset shape (rows, columns)

#### 3. **Data Cleaning Section**
```
==================================================
DATA CLEANING
==================================================

Missing Values:
[Shows missing value counts and percentages for each column]

Data cleaning completed!
```

#### 4. **Basic Statistics Section**
```
==================================================
BASIC STATISTICS
==================================================

Total Applications: [number]

Loan Status Distribution:
Y    [count]
N    [count]

Approval Rate: [percentage]%

Numerical Statistics:
[Shows descriptive statistics for ApplicantIncome, CoapplicantIncome, LoanAmount]
```

#### 5. **Demographic Analysis Section**
```
==================================================
DEMOGRAPHIC ANALYSIS
==================================================

1. Loan Approval by Gender:
[Shows percentage breakdown by gender and loan status]

2. Loan Approval by Education:
[Shows percentage breakdown by education level and loan status]

3. Loan Approval by Marital Status:
[Shows percentage breakdown by marital status and loan status]

4. Loan Approval by Dependents:
[Shows percentage breakdown by number of dependents and loan status]
```

#### 6. **Income Analysis Section**
```
==================================================
INCOME ANALYSIS
==================================================

Income Statistics by Loan Status:
[Shows mean and median income statistics grouped by loan status]

Loan Approval by Self Employment:
[Shows percentage breakdown by self-employment status]
```

#### 7. **Loan Amount Analysis Section**
```
==================================================
LOAN AMOUNT ANALYSIS
==================================================

Loan Amount Statistics by Loan Status:
[Shows mean, median, min, max loan amounts]

Loan Approval by Loan Amount Category:
[Shows percentage breakdown by loan amount categories]
```

#### 8. **Credit History Analysis Section**
```
==================================================
CREDIT HISTORY ANALYSIS
==================================================

Loan Approval by Credit History:
[Shows percentage breakdown by credit history status]
```

#### 9. **Property Area Analysis Section**
```
==================================================
PROPERTY AREA ANALYSIS
==================================================

Loan Approval by Property Area:
[Shows percentage breakdown by property area type]
```

#### 10. **Visualizations Section**
```
==================================================
CREATING VISUALIZATIONS
==================================================

Visualizations saved as 'loan_analysis_visualizations.png'
[A matplotlib window will open showing 6 charts]
```

#### 11. **Summary Report Section**
```
==================================================
SUMMARY REPORT
==================================================

LOAN DATA ANALYSIS REPORT
========================

Dataset Overview:
- Total Applications: [number]
- Approved Loans: [number]
- Rejected Loans: [number]
- Approval Rate: [percentage]%

Key Findings:
1. Gender Impact:
   - Male Approval Rate: [percentage]%
   - Female Approval Rate: [percentage]%

2. Education Impact:
   - Graduate Approval Rate: [percentage]%
   - Not Graduate Approval Rate: [percentage]%

3. Credit History Impact:
   - Good Credit (1) Approval Rate: [percentage]%
   - Bad Credit (0) Approval Rate: [percentage]%

4. Average Loan Amount:
   - Approved: [amount]
   - Rejected: [amount]

5. Average Total Income:
   - Approved: [amount]
   - Rejected: [amount]

Report saved as 'analysis_report.txt'
```

#### 12. **Completion Message**
```
==================================================
ANALYSIS COMPLETED SUCCESSFULLY!
==================================================
```

### Generated Files

After running the script, two files will be created in your project directory:

#### 1. **loan_analysis_visualizations.png**
A high-resolution PNG image (300 DPI) containing 6 visualization charts arranged in a 2x3 grid:

- **Top Row:**
  - Chart 1: Loan Status Distribution (Bar chart showing Y vs N counts)
  - Chart 2: Loan Approval by Gender (Stacked bar chart)
  - Chart 3: Loan Approval by Education (Stacked bar chart)

- **Bottom Row:**
  - Chart 4: Income Distribution (Box plot for ApplicantIncome and CoapplicantIncome)
  - Chart 5: Loan Amount Distribution (Histogram)
  - Chart 6: Loan Approval by Credit History (Stacked bar chart)

#### 2. **analysis_report.txt**
A text file containing:
- Dataset overview statistics
- Key findings summary
- Approval rates by different factors
- Average loan amounts and incomes by loan status

### Sample Output Values

Based on typical loan datasets, you can expect:

- **Total Applications**: ~600 records
- **Approval Rate**: Approximately 68-70%
- **Gender Impact**: Males typically show slightly higher approval rates
- **Education Impact**: Graduates show 5-10% higher approval rates
- **Credit History Impact**: Good credit history shows 40-50% higher approval rates
- **Average Loan Amount**: Approved loans typically range from 140-150, rejected loans from 150-160

### Visual Output

The script will also open a matplotlib window displaying the visualizations. You can:
- View the charts interactively
- Zoom and pan if needed
- Close the window to continue (the PNG file is already saved)

### SQL Analysis

Run SQL queries for analysis:

```bash
mysql -u root -p loan_analysis_db < data_analysis.sql
```

Or execute queries directly in MySQL Workbench.

## Analysis Features

### 1. Basic Statistics
- Total number of applications
- Loan approval rate
- Descriptive statistics for numerical variables

### 2. Demographic Analysis
- Loan approval by gender
- Loan approval by marital status
- Loan approval by education level
- Loan approval by number of dependents

### 3. Income Analysis
- Average income by loan status
- Income distribution analysis
- Self-employment impact on loan approval

### 4. Loan Amount Analysis
- Loan amount statistics
- Loan amount categories and approval rates
- Income to loan ratio analysis

### 5. Credit History Analysis
- Impact of credit history on loan approval
- Credit history distribution

### 6. Property Area Analysis
- Loan approval rates by property area type

### 7. Visualizations
- Loan status distribution
- Demographic factor comparisons
- Income distributions
- Loan amount distributions
- Credit history impact

## Key Insights

The analysis reveals several important factors affecting loan approval:

1. **Credit History**: Applicants with good credit history have significantly higher approval rates
2. **Education**: Graduates tend to have higher approval rates
3. **Income**: Higher total income (applicant + co-applicant) correlates with loan approval
4. **Property Area**: Urban areas show different approval patterns compared to rural/semiurban
5. **Loan Amount**: Smaller loan amounts have higher approval rates

## Results

After running the analysis, you will get:

1. **Statistical Summary**: Detailed statistics for all variables
2. **Visualizations**: Multiple charts showing relationships between variables
3. **Analysis Report**: Text file with key findings and insights

## Troubleshooting

### Common Issues

1. **MySQL Connection Error**
   - Ensure MySQL server is running
   - Check connection credentials in `load_data.py`
   - Verify database exists

2. **Missing Dependencies**
   - Run `pip install -r requirements.txt`
   - Ensure Python 3.7+ is installed

3. **File Not Found Error**
   - Ensure `loan_data_set.csv` is in the same directory
   - Check file path in scripts

## Future Enhancements

Potential improvements for the project:

1. Machine learning models for loan prediction
2. Interactive dashboards using Plotly/Dash
3. Automated report generation
4. Data validation and quality checks
5. Advanced statistical modeling

## Author

**Sheeza Nazeer**

## License

This project is for educational and analysis purposes.

## Contact

For questions or suggestions, please contact the project author.

---

**Note:** This project demonstrates data analysis techniques using both SQL and Python. Choose the approach that best fits your needs - Python for comprehensive analysis with visualizations, or SQL for database-focused analysis.

