# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:08:14 2021

@author: Ahmed Heakl
"""

import pandas as pd

df = pd.read_csv('csv_saved/mydata.csv')

# get rid of jobs with no salary estimated
df = df[df['Salary Estimate'] != "-1"]

# Salary Parsing
minus_words = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

minus_kdn = minus_words.apply(lambda x: x.replace('K', '').replace('$', ''))

df['per_hour'] = minus_kdn.apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

minus_he = minus_kdn.apply(lambda x: x.lower().replace('per hour', '')\
                           .replace('employer provided salary', '').replace(':', ''))

df['min_salary'] = minus_he.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_he.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary'] + df['max_salary']) /2

# remove rating from company name
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 \
                             else x['Company Name'][:-3], axis = 1)
    
# taking only the two letter location
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df['job_state'].value_counts()

# new variable to check if the location is the same as the headquarters
df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0,axis = 1)

# get the age of the company
df['age'] = df['Founded'].apply(lambda x: x if x < 0 else 2021 - int(x))

# Description Parsing
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

# Drop the unnamed column
print(df.columns)
df = df.drop(['Unnamed: 0'], axis=1)

# Save the cleaned file
df.to_csv('./csv_saved/data_cleaned.csv', index = False)





