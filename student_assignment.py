import os
import csv

Path=r'E:\New folder\Student_data'
def csv_files(path):

    try:
        files = os.listdir(path)
        all_csv_files = []
        for  i in files:
             j=Path +'\\' +i
             if j.endswith(".csv"):
                all_csv_files.append(j)
        return all_csv_files
    except Exception as e:
           print(f'erorr:{e}')
files=csv_files(Path)
def read_csv_file(csv_file_path):
        with open( csv_file_path,mode='r')as file1:
              csvfile=csv.reader(file1)
              header=next(csvfile)
              header.extend(['total','per'])
              data=[]
              for  file in  csvfile:
                   total=int(file[3])+int(file[4])+int(file[5])+int(file[6])+int(file[7])
                   per=total / 5
                   file.extend([total,per])
                   #data.append(total)
                   #data.append(per)
                   data.append(file)
                  #  print(file)
        print(data)
        return data,header


all_data=[]
for file_path in files:
     data,header=read_csv_file(file_path)
     all_data.extend(data)








