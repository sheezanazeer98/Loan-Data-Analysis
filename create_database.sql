-- =====================================================
-- Loan Data Analysis Project - Database Setup
-- Created by: Sheeza Nazeer
-- =====================================================

-- Create Database
CREATE DATABASE IF NOT EXISTS loan_analysis_db;
USE loan_analysis_db;

-- Create Loan Applications Table
CREATE TABLE IF NOT EXISTS loan_applications (
    Loan_ID VARCHAR(20) PRIMARY KEY,
    Gender VARCHAR(10),
    Married VARCHAR(5),
    Dependents VARCHAR(5),
    Education VARCHAR(20),
    Self_Employed VARCHAR(5),
    ApplicantIncome DECIMAL(10, 2),
    CoapplicantIncome DECIMAL(10, 2),
    LoanAmount DECIMAL(10, 2),
    Loan_Amount_Term INT,
    Credit_History INT,
    Property_Area VARCHAR(20),
    Loan_Status VARCHAR(5)
);

-- Create Indexes for better query performance
CREATE INDEX idx_gender ON loan_applications(Gender);
CREATE INDEX idx_education ON loan_applications(Education);
CREATE INDEX idx_loan_status ON loan_applications(Loan_Status);
CREATE INDEX idx_property_area ON loan_applications(Property_Area);
CREATE INDEX idx_credit_history ON loan_applications(Credit_History);

