-- =====================================================
-- Loan Data Analysis Project - Data Analysis Queries
-- =====================================================

USE loan_analysis_db;

-- =====================================================
-- 1. BASIC STATISTICS
-- =====================================================

-- Total number of loan applications
SELECT COUNT(*) AS total_applications FROM loan_applications;

-- Loan approval rate
SELECT 
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loan_applications), 2) AS percentage
FROM loan_applications
GROUP BY Loan_Status;

-- =====================================================
-- 2. DEMOGRAPHIC ANALYSIS
-- =====================================================

-- Loan approval by Gender
SELECT 
    Gender,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Gender), 2) AS percentage
FROM loan_applications
WHERE Gender IS NOT NULL
GROUP BY Gender, Loan_Status
ORDER BY Gender, Loan_Status;

-- Loan approval by Marital Status
SELECT 
    Married,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Married), 2) AS percentage
FROM loan_applications
GROUP BY Married, Loan_Status
ORDER BY Married, Loan_Status;

-- Loan approval by Education
SELECT 
    Education,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Education), 2) AS percentage
FROM loan_applications
GROUP BY Education, Loan_Status
ORDER BY Education, Loan_Status;

-- Loan approval by Number of Dependents
SELECT 
    Dependents,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Dependents), 2) AS percentage
FROM loan_applications
GROUP BY Dependents, Loan_Status
ORDER BY Dependents, Loan_Status;

-- =====================================================
-- 3. INCOME ANALYSIS
-- =====================================================

-- Income statistics by loan status
SELECT 
    Loan_Status,
    COUNT(*) AS count,
    ROUND(AVG(ApplicantIncome), 2) AS avg_applicant_income,
    ROUND(AVG(CoapplicantIncome), 2) AS avg_coapplicant_income,
    ROUND(AVG(ApplicantIncome + CoapplicantIncome), 2) AS avg_total_income,
    ROUND(MIN(ApplicantIncome), 2) AS min_applicant_income,
    ROUND(MAX(ApplicantIncome), 2) AS max_applicant_income
FROM loan_applications
GROUP BY Loan_Status;

-- Loan approval by Self Employment status
SELECT 
    Self_Employed,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Self_Employed), 2) AS percentage
FROM loan_applications
GROUP BY Self_Employed, Loan_Status
ORDER BY Self_Employed, Loan_Status;

-- =====================================================
-- 4. LOAN AMOUNT ANALYSIS
-- =====================================================

-- Loan amount statistics
SELECT 
    Loan_Status,
    COUNT(*) AS count,
    ROUND(AVG(LoanAmount), 2) AS avg_loan_amount,
    ROUND(MIN(LoanAmount), 2) AS min_loan_amount,
    ROUND(MAX(LoanAmount), 2) AS max_loan_amount
FROM loan_applications
WHERE LoanAmount IS NOT NULL
GROUP BY Loan_Status;

-- =====================================================
-- 5. CREDIT HISTORY ANALYSIS
-- =====================================================

-- Credit history impact on loan approval
SELECT 
    Credit_History,
    CASE 
        WHEN Credit_History = 1 THEN 'Good Credit'
        WHEN Credit_History = 0 THEN 'Bad Credit'
        ELSE 'Unknown'
    END AS credit_status,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Credit_History), 2) AS percentage
FROM loan_applications
GROUP BY Credit_History, Loan_Status
ORDER BY Credit_History, Loan_Status;

-- =====================================================
-- 6. PROPERTY AREA ANALYSIS
-- =====================================================

-- Loan approval by Property Area
SELECT 
    Property_Area,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Property_Area), 2) AS percentage
FROM loan_applications
GROUP BY Property_Area, Loan_Status
ORDER BY Property_Area, Loan_Status;

-- =====================================================
-- 7. ADVANCED ANALYSIS
-- =====================================================

-- Income to Loan Ratio Analysis
SELECT 
    Loan_Status,
    COUNT(*) AS count,
    ROUND(AVG((ApplicantIncome + CoapplicantIncome) / NULLIF(LoanAmount, 0)), 2) AS avg_income_to_loan_ratio
FROM loan_applications
WHERE LoanAmount IS NOT NULL AND LoanAmount > 0
GROUP BY Loan_Status;

-- Loan Amount Categories
SELECT 
    CASE 
        WHEN LoanAmount <= 100 THEN 'Low (<=100)'
        WHEN LoanAmount <= 200 THEN 'Medium (101-200)'
        WHEN LoanAmount <= 300 THEN 'High (201-300)'
        ELSE 'Very High (>300)'
    END AS loan_amount_category,
    Loan_Status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY 
        CASE 
            WHEN LoanAmount <= 100 THEN 'Low (<=100)'
            WHEN LoanAmount <= 200 THEN 'Medium (101-200)'
            WHEN LoanAmount <= 300 THEN 'High (201-300)'
            ELSE 'Very High (>300)'
        END), 2) AS percentage
FROM loan_applications
WHERE LoanAmount IS NOT NULL
GROUP BY loan_amount_category, Loan_Status
ORDER BY loan_amount_category, Loan_Status;

