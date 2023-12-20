import pandas as pd
import csv
from datetime import datetime

def check_user_existence(mail): #user
    df = pd.read_csv('users.csv')
    for index, row in df.iterrows():
        csv_mail=row['email']
        if mail == csv_mail:
            return True
    return False



def add_user(email,password,name,surname,date_of_birth): #user
    
    with open("users.csv","a+",newline='') as csv_user_file: 

        csv_user_file.seek(0)   
        
        reader = csv.reader(csv_user_file)

        existing_data = list(reader)
        
        last_index = len(existing_data) 

        date = datetime.now()
        
        date_of_registration = date.date()
        
        data=[[last_index,email,password,name,surname,date_of_birth,date_of_registration]]
        writer=csv.writer(csv_user_file)
        
        writer.writerows(data)

def get_user_id(email):
    users_frame = pd.read_csv('users.csv')
    user_id = users_frame[users_frame['email'] ==email]['id'].values
    print(user_id[0])
    return user_id[0]





get_user_id("przykladowy@gmail.com")
        