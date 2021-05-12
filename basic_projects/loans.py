# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = 'object')
numerical_var = bank.select_dtypes(include = 'number')

#=======================================================
# print(bank.head())

bank.drop(columns=['Loan_ID'],inplace=True)
banks = bank.copy()
# print(banks.isnull().sum())
bank_mode = banks.mode()
# val = bank_mode.to_dict()
# vall = {'Gender': { 'Male'}, 'Married': { 'Yes'}, 'Dependents': { '0'}, 'Education': { 'Graduate'}, 'Self_Employed': { 'No'}, 'ApplicantIncome': { 2500}, 'CoapplicantIncome': { 0.0}, 'LoanAmount': { 120.0}, 'Loan_Amount_Term': { 360.0}, 'Credit_History': { 1.0}, 'Property_Area': { 'Semiurban'}, 'Loan_Status': { 'Y'}}
# print(val)
# print(type(bank_mode))
# print(banks.isnull().sum())
# print("="*50)
# # banks.fillna(value=bank_mode,inplace=True)
# # banks.apply(lambda x: x.fillna(x.mean()),axis=0)
# banks.fillna(banks.mode(),inplace=True)
banks['Gender'].fillna(banks['Gender'].mode()[0], inplace=True)
banks['Married'].fillna(banks['Married'].mode()[0], inplace=True)
banks['Dependents'].fillna(banks['Dependents'].mode()[0], inplace=True)
banks['Self_Employed'].fillna(banks['Self_Employed'].mode()[0], inplace=True)
banks['Credit_History'].fillna(banks['Credit_History'].mode()[0], inplace=True)
banks['Loan_Amount_Term'].fillna(banks['Loan_Amount_Term'].mode()[0], inplace=True)
banks['LoanAmount'].fillna(banks['LoanAmount'].median(), inplace=True)
# print(banks.isnull().sum().values.sum())
#===============================================================================
avg_loan_amount = pd.pivot_table(banks,values='LoanAmount',index=['Gender', 'Married', 'Self_Employed'],aggfunc=np.mean)
# print(avg_loan_amount)
#===============================================================================
# loan_approved_se = banks[banks['Self_Employed'=='Yes' and'Loan_Status'=='Y'] ]
loan_approved_se = banks.query('Self_Employed=="Yes" & Loan_Status=="Y"')
loan_approved_se = len(loan_approved_se.index)
loan_approved_nse = banks.query('Self_Employed=="No" & Loan_Status=="Y"')
loan_approved_nse = len(loan_approved_nse.index)
percentage_se = round((loan_approved_se * 100 / 614),2)
percentage_nse =round((loan_approved_nse * 100 / 614),2)

# print(percentage_se,percentage_nse)


#===============================================================================
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
# print(type(loan_term))
big_loan_term = loan_term[ loan_term>=25 ]

# print(len(big_loan_term))
#===============================================================================
loan_groupby = banks.groupby('Loan_Status')
# print(loan_groupby.head())
loan_groupby  = loan_groupby [['ApplicantIncome', 'Credit_History']]
# print(loan_groupby.head(10))
mean_values = loan_groupby.mean()
print(mean_values)
#===============================================================================




