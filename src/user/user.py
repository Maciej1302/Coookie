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


def get_user_data(user_id):
    user_data = pd.read_csv('users.csv')
    personal_data = user_data[user_data['id'] == user_id][['email', 'name', 'surname', 'date_of_birth']].values
    if personal_data.size > 0:
        personal_data_tuple = tuple(personal_data[0])
    else:
        personal_data_tuple = ('', '', '', '')  # lub inna domyślna wartość
    print(personal_data_tuple)
    return personal_data_tuple

def change_password(user_id, current_passwd, new_passwd):
    
    df = pd.read_csv('users.csv')
    password = df[df['id'] == user_id]['password'].values
    
    if current_passwd == password:
        df.loc[df['id'] == user_id, 'password'] = new_passwd
        df.to_csv('users.csv', index=False)
        return True
    else:
        return False
    
def change_email(user_id,new_email):

    df = pd.read_csv('users.csv')

    df.loc[df['id'] == user_id, 'email'] = new_email
    df.to_csv('users.csv', index=False)
       
change_email(1,'gfgfdgfdigf')

        