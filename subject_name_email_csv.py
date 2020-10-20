# Parses 'Subject', 'From: (Name)', 'From: (email)' from CSV-file
# Example how to use:
# subject_name_email_csv Midrange-L.CSV

import sys
import pandas as pd
import re
import os.path
from os import path
  
num_arg = len(sys.argv)

if num_arg > 2:
    print("ERROR! There is too much parameters.")
    sys.exit()
    
if num_arg == 1:    
    print("Please enter the file you want to parse!")
    sys.exit()

filename = sys.argv[1]

if (path.exists(filename) == False):
    print("File not exists!!!")
    sys.exit()
    
df = pd.read_csv(filename, sep = ',')

new_df = pd.DataFrame(df[['Body']])

def find_subject(text):
    res_array = re.findall('\r\nsubject: (.*)\r\n\r\n', text)
    if (res_array):
        return res_array[0]
    else:
        return float("NaN")

def find_name(text):
    res_array = re.findall('\r\nfrom: (.*) <(\w+@\w+\.\w+)>\r\nsubject', text)
    if (res_array):
        return res_array[0][0]
    else:
        return float("NaN")

def find_email(text):
    res_array = re.findall('\r\nfrom: (.*) <(\w+@\w+\.\w+)>\r\nsubject', text)
    if (res_array):                
        return res_array[0][1]
    else:
        return float("NaN")

new_df['Subject'] = new_df['Body'].apply(lambda text: find_subject(text))
new_df['From: (Name)'] = new_df['Body'].apply(lambda text: find_name(text))
new_df['From: (email)'] = new_df['Body'].apply(lambda text: find_email(text))

del new_df['Body']

new_df.dropna(how='any',inplace=True)

print(new_df)
new_df.to_csv('subject_name_email.csv', index=False)
print("File 'subject_name_email.csv' is succesfully created.")
