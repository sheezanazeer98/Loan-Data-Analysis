"""
Loan Data Analysis Project - Python Data Analysis
Created by: Sheeza Nazeer

This script performs comprehensive data analysis on the loan dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data():
    """Load the loan dataset"""
    df = pd.read_csv('loan_data_set.csv')
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    return df

def data_cleaning(df):
    """Clean and preprocess the data"""
    print("\n" + "="*50)
    print("DATA CLEANING")
    print("="*50)
    
    # Check missing values
    print("\nMissing Values:")
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Percentage': missing_percent
    })
    print(missing_df[missing_df['Missing Count'] > 0])
    
    # Handle missing values
    df['Self_Employed'] = df['Self_Employed'].fillna('No')
    df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
    df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(360)
    df['Credit_History'] = df['Credit_History'].fillna(1)
    df['Gender'] = df['Gender'].fillna('Male')
    df['Dependents'] = df['Dependents'].fillna('0')
    
    print("\nData cleaning completed!")
    return df

def basic_statistics(df):
    """Perform basic statistical analysis"""
    print("\n" + "="*50)
    print("BASIC STATISTICS")
    print("="*50)
    
    print(f"\nTotal Applications: {len(df)}")
    print(f"\nLoan Status Distribution:")
    print(df['Loan_Status'].value_counts())
    print(f"\nApproval Rate: {(df['Loan_Status'] == 'Y').sum() / len(df) * 100:.2f}%")
    
    print("\n\nNumerical Statistics:")
    print(df[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']].describe())
    
    return df

def demographic_analysis(df):
    """Analyze demographic factors"""
    print("\n" + "="*50)
    print("DEMOGRAPHIC ANALYSIS")
    print("="*50)
    
    # Gender Analysis
    print("\n1. Loan Approval by Gender:")
    gender_analysis = pd.crosstab(df['Gender'], df['Loan_Status'], normalize='index') * 100
    print(gender_analysis)
    
    # Education Analysis
    print("\n2. Loan Approval by Education:")
    education_analysis = pd.crosstab(df['Education'], df['Loan_Status'], normalize='index') * 100
    print(education_analysis)
    
    # Marital Status Analysis
    print("\n3. Loan Approval by Marital Status:")
    married_analysis = pd.crosstab(df['Married'], df['Loan_Status'], normalize='index') * 100
    print(married_analysis)
    
    # Dependents Analysis
    print("\n4. Loan Approval by Dependents:")
    dependents_analysis = pd.crosstab(df['Dependents'], df['Loan_Status'], normalize='index') * 100
    print(dependents_analysis)
    
    return df

def income_analysis(df):
    """Analyze income factors"""
    print("\n" + "="*50)
    print("INCOME ANALYSIS")
    print("="*50)
    
    # Create total income column
    df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
    
    print("\nIncome Statistics by Loan Status:")
    income_stats = df.groupby('Loan_Status')[['ApplicantIncome', 'CoapplicantIncome', 'TotalIncome']].agg(['mean', 'median'])
    print(income_stats)
    
    # Self Employed Analysis
    print("\nLoan Approval by Self Employment:")
    self_emp_analysis = pd.crosstab(df['Self_Employed'], df['Loan_Status'], normalize='index') * 100
    print(self_emp_analysis)
    
    return df

def loan_amount_analysis(df):
    """Analyze loan amount factors"""
    print("\n" + "="*50)
    print("LOAN AMOUNT ANALYSIS")
    print("="*50)
    
    print("\nLoan Amount Statistics by Loan Status:")
    loan_stats = df.groupby('Loan_Status')['LoanAmount'].agg(['mean', 'median', 'min', 'max'])
    print(loan_stats)
    
    # Loan Amount Categories
    df['LoanAmount_Category'] = pd.cut(df['LoanAmount'], 
                                       bins=[0, 100, 200, 300, float('inf')],
                                       labels=['Low (<=100)', 'Medium (101-200)', 'High (201-300)', 'Very High (>300)'])
    
    print("\nLoan Approval by Loan Amount Category:")
    loan_cat_analysis = pd.crosstab(df['LoanAmount_Category'], df['Loan_Status'], normalize='index') * 100
    print(loan_cat_analysis)
    
    return df

def credit_history_analysis(df):
    """Analyze credit history impact"""
    print("\n" + "="*50)
    print("CREDIT HISTORY ANALYSIS")
    print("="*50)
    
    df['Credit_Status'] = df['Credit_History'].map({1: 'Good Credit', 0: 'Bad Credit'})
    
    print("\nLoan Approval by Credit History:")
    credit_analysis = pd.crosstab(df['Credit_Status'], df['Loan_Status'], normalize='index') * 100
    print(credit_analysis)
    
    return df

def property_area_analysis(df):
    """Analyze property area impact"""
    print("\n" + "="*50)
    print("PROPERTY AREA ANALYSIS")
    print("="*50)
    
    print("\nLoan Approval by Property Area:")
    property_analysis = pd.crosstab(df['Property_Area'], df['Loan_Status'], normalize='index') * 100
    print(property_analysis)
    
    return df

def create_visualizations(df):
    """Create visualizations"""
    print("\n" + "="*50)
    print("CREATING VISUALIZATIONS")
    print("="*50)
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Loan Data Analysis - Visualizations', fontsize=16, fontweight='bold')
    
    # 1. Loan Status Distribution
    df['Loan_Status'].value_counts().plot(kind='bar', ax=axes[0, 0], color=['green', 'red'])
    axes[0, 0].set_title('Loan Status Distribution')
    axes[0, 0].set_xlabel('Loan Status')
    axes[0, 0].set_ylabel('Count')
    
    # 2. Loan Approval by Gender
    pd.crosstab(df['Gender'], df['Loan_Status']).plot(kind='bar', ax=axes[0, 1], stacked=True)
    axes[0, 1].set_title('Loan Approval by Gender')
    axes[0, 1].set_xlabel('Gender')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].legend(title='Loan Status')
    
    # 3. Loan Approval by Education
    pd.crosstab(df['Education'], df['Loan_Status']).plot(kind='bar', ax=axes[0, 2], stacked=True)
    axes[0, 2].set_title('Loan Approval by Education')
    axes[0, 2].set_xlabel('Education')
    axes[0, 2].set_ylabel('Count')
    axes[0, 2].legend(title='Loan Status')
    
    # 4. Income Distribution
    df.boxplot(column=['ApplicantIncome', 'CoapplicantIncome'], ax=axes[1, 0])
    axes[1, 0].set_title('Income Distribution')
    axes[1, 0].set_ylabel('Income')
    
    # 5. Loan Amount Distribution
    df['LoanAmount'].hist(bins=30, ax=axes[1, 1], color='skyblue')
    axes[1, 1].set_title('Loan Amount Distribution')
    axes[1, 1].set_xlabel('Loan Amount')
    axes[1, 1].set_ylabel('Frequency')
    
    # 6. Credit History Impact
    pd.crosstab(df['Credit_History'], df['Loan_Status']).plot(kind='bar', ax=axes[1, 2], stacked=True)
    axes[1, 2].set_title('Loan Approval by Credit History')
    axes[1, 2].set_xlabel('Credit History (1=Good, 0=Bad)')
    axes[1, 2].set_ylabel('Count')
    axes[1, 2].legend(title='Loan Status')
    
    plt.tight_layout()
    plt.savefig('loan_analysis_visualizations.png', dpi=300, bbox_inches='tight')
    print("\nVisualizations saved as 'loan_analysis_visualizations.png'")
    plt.show()

def generate_report(df):
    """Generate summary report"""
    print("\n" + "="*50)
    print("SUMMARY REPORT")
    print("="*50)
    
    # Calculate statistics
    total_apps = len(df)
    approved = (df['Loan_Status'] == 'Y').sum()
    rejected = (df['Loan_Status'] == 'N').sum()
    approval_rate = (approved / total_apps * 100)
    
    # Gender statistics
    gender_crosstab = pd.crosstab(df['Gender'], df['Loan_Status'], normalize='index')
    male_approval = gender_crosstab.loc['Male', 'Y'] * 100 if 'Male' in gender_crosstab.index else 0
    female_approval = gender_crosstab.loc['Female', 'Y'] * 100 if 'Female' in gender_crosstab.index else 0
    
    # Education statistics
    edu_crosstab = pd.crosstab(df['Education'], df['Loan_Status'], normalize='index')
    grad_approval = edu_crosstab.loc['Graduate', 'Y'] * 100
    not_grad_approval = edu_crosstab.loc['Not Graduate', 'Y'] * 100
    
    # Credit history statistics
    credit_crosstab = pd.crosstab(df['Credit_History'], df['Loan_Status'], normalize='index')
    good_credit_approval = credit_crosstab.loc[1, 'Y'] * 100
    bad_credit_approval = credit_crosstab.loc[0, 'Y'] * 100
    
    # Loan amount statistics
    approved_loan_avg = df[df['Loan_Status'] == 'Y']['LoanAmount'].mean()
    rejected_loan_avg = df[df['Loan_Status'] == 'N']['LoanAmount'].mean()
    
    # Income statistics
    approved_income_avg = df[df['Loan_Status'] == 'Y']['TotalIncome'].mean()
    rejected_income_avg = df[df['Loan_Status'] == 'N']['TotalIncome'].mean()
    
    report = f"""
    LOAN DATA ANALYSIS REPORT
    ========================
    
    Dataset Overview:
    - Total Applications: {total_apps}
    - Approved Loans: {approved}
    - Rejected Loans: {rejected}
    - Approval Rate: {approval_rate:.2f}%
    
    Key Findings:
    1. Gender Impact:
       - Male Approval Rate: {male_approval:.2f}%
       - Female Approval Rate: {female_approval:.2f}%
    
    2. Education Impact:
       - Graduate Approval Rate: {grad_approval:.2f}%
       - Not Graduate Approval Rate: {not_grad_approval:.2f}%
    
    3. Credit History Impact:
       - Good Credit (1) Approval Rate: {good_credit_approval:.2f}%
       - Bad Credit (0) Approval Rate: {bad_credit_approval:.2f}%
    
    4. Average Loan Amount:
       - Approved: {approved_loan_avg:.2f}
       - Rejected: {rejected_loan_avg:.2f}
    
    5. Average Total Income:
       - Approved: {approved_income_avg:.2f}
       - Rejected: {rejected_income_avg:.2f}
    """
    
    print(report)
    
    # Save report to file
    with open('analysis_report.txt', 'w') as f:
        f.write(report)
    print("\nReport saved as 'analysis_report.txt'")

def main():
    """Main function"""
    print("="*50)
    print("LOAN DATA ANALYSIS PROJECT")
    print("Created by: Sheeza Nazeer")
    print("="*50)
    
    # Load data
    df = load_data()
    
    # Data cleaning
    df = data_cleaning(df)
    
    # Basic statistics
    df = basic_statistics(df)
    
    # Demographic analysis
    df = demographic_analysis(df)
    
    # Income analysis
    df = income_analysis(df)
    
    # Loan amount analysis
    df = loan_amount_analysis(df)
    
    # Credit history analysis
    df = credit_history_analysis(df)
    
    # Property area analysis
    df = property_area_analysis(df)
    
    # Create visualizations
    create_visualizations(df)
    
    # Generate report
    generate_report(df)
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETED SUCCESSFULLY!")
    print("="*50)

if __name__ == "__main__":
    main()

