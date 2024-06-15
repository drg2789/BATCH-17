import os
files=os.listdir(r'C:\Users\Admin\Desktop\student_data')
print(files)

all_csv_files=[]
for i in files:
    if i.endswith(".csv"):
        all_csv_files.append(i)
print(f"following are {all_csv_files} csv files")