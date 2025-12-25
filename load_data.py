"""
Loan Data Analysis Project - Data Loader
Created by: Sheeza Nazeer

This script loads the loan dataset into a MySQL database.
"""

import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create database connection"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='loan_analysis_db',
            user='root',  # Change as per your MySQL configuration
            password=''   # Change as per your MySQL configuration
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def load_data_to_db(csv_file_path, connection):
    """Load CSV data into MySQL database"""
    try:
        # Read CSV file
        df = pd.read_csv(csv_file_path)
        
        # Clean data
        df = df.replace('', None)
        df = df.replace(' ', None)
        
        # Handle missing values
        df['Self_Employed'] = df['Self_Employed'].fillna('No')
        df['LoanAmount'] = pd.to_numeric(df['LoanAmount'], errors='coerce')
        df['Loan_Amount_Term'] = pd.to_numeric(df['Loan_Amount_Term'], errors='coerce')
        df['Credit_History'] = pd.to_numeric(df['Credit_History'], errors='coerce')
        df['Gender'] = df['Gender'].fillna('Male')
        df['Dependents'] = df['Dependents'].fillna('0')
        
        # Fill numeric missing values
        df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(360)
        df['Credit_History'] = df['Credit_History'].fillna(1)
        
        cursor = connection.cursor()
        
        # Clear existing data
        cursor.execute("DELETE FROM loan_applications")
        
        # Insert data
        insert_query = """
        INSERT INTO loan_applications 
        (Loan_ID, Gender, Married, Dependents, Education, Self_Employed,
         ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,
         Credit_History, Property_Area, Loan_Status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        for _, row in df.iterrows():
            values = (
                row['Loan_ID'],
                row['Gender'],
                row['Married'],
                row['Dependents'],
                row['Education'],
                row['Self_Employed'],
                float(row['ApplicantIncome']) if pd.notna(row['ApplicantIncome']) else None,
                float(row['CoapplicantIncome']) if pd.notna(row['CoapplicantIncome']) else None,
                float(row['LoanAmount']) if pd.notna(row['LoanAmount']) else None,
                int(row['Loan_Amount_Term']) if pd.notna(row['Loan_Amount_Term']) else None,
                int(row['Credit_History']) if pd.notna(row['Credit_History']) else None,
                row['Property_Area'],
                row['Loan_Status']
            )
            cursor.execute(insert_query, values)
        
        connection.commit()
        print(f"Successfully loaded {len(df)} records into database")
        
    except Error as e:
        print(f"Error loading data: {e}")
        connection.rollback()
    finally:
        if cursor:
            cursor.close()

def main():
    """Main function"""
    # Path to CSV file
    csv_file = 'loan_data_set.csv'
    
    # Create connection
    connection = create_connection()
    
    if connection:
        # Load data
        load_data_to_db(csv_file, connection)
        
        # Close connection
        connection.close()
        print("MySQL connection closed")

if __name__ == "__main__":
    main()

