# subject_name_email_csv
*********************************************************************
   Parses 'Subject', 'From: (Name)', 'From: (email)' from CSV-file
*********************************************************************
Example how to use:
  python3.exe subject_name_email_csv Midrange-L.CSV
    or
  (For Windows)
  subject_name_email_csv.exe Midrange-L.CSV

*********************************************************************
You can to compile python script file into executable file like this:

1) Install compiler for building exe-file:
    pip install pyinstaller  

2) Build executable file: 
    pyinstaller --onefile pythonScriptName.py
     or
    pyinstaller -F test.py  # build exe-file
*********************************************************************
