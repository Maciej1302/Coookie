import pandas as pd
import csv


def check_user_existence(mail): #user
    df = pd.read_csv('users.csv')
    for index, row in df.iterrows():
        csv_mail=row['email']
        if mail == csv_mail:
            return True
    return False



def add_user(email,password,name,surname): #user
   data=[[email,password,name,surname]]
   file=open("users.csv","a",newline='')
   writer=csv.writer(file)

   writer.writerows(data)
   file.close()