import pandas as pd
import csv
import sqlite3



def recipe_searcher(ing): #recipes management 
    x=[]
    ing =ing.lower().split() 
    
    df = pd.read_csv('recipes.csv')
    for index, row in df.iterrows():
        ingredients_list = row['ingredients'].lower().split() 
        
        if any(ingredient in ingredients_list for ingredient in ing) and all(ingredient in ing for ingredient in ingredients_list):
            
            x.append(row['description'])

    if len(x) == 0:
        text = ['Unfortunately, we have not matched any of the recipes to the given ingredients']
        
        return text
    
    return x





def  add_favorite_choosed_recipe(recipe_id,user_id,col): #recipes management 

    df = pd.read_csv("user_recipes.csv")
    df[col] = df[col].astype('object')
    
    user_id = int(user_id)
    existing_users_id = list(df['user_id'])
    
    if user_id in existing_users_id:

        index = df.index[df['user_id'] == user_id]
        print(type(recipe_id))
        print(recipe_id)
        existing_data = df.loc[index,col]
        
    
        if pd.isna(existing_data).any():
            df.loc[index, col] = recipe_id
        else:
            current_data = str(existing_data.iloc[0])
            if recipe_id not in current_data:
                df.loc[index, col] = current_data + " " + recipe_id
        
       
    
    else:
        new_data = {'user_id': user_id, col: recipe_id}
        
        df = df._append(new_data, ignore_index=True)


    
    
   
    df.to_csv('user_recipes.csv', index=False)
    



def find_favorite_choosed_recipe(user_id): #recipes management

    df_user_recipes = pd.read_csv("user_recipes.csv")
    fav_recipes_str = df_user_recipes[df_user_recipes['user_id'] == user_id]['favourite_recipes'].iloc[0]
    fav_recipes_list = fav_recipes_str.split(' ')

    print(fav_recipes_list)

    data_csv = 'recipes.csv'
    df = pd.read_csv(data_csv)
    conn = sqlite3.connect('recipes.db')
    df.to_sql('recipe_table', conn, if_exists='replace', index=False)
    conn.close()
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()

    placeholders = ','.join('?' for _ in fav_recipes_list)  # Tworzenie placeholderów
    zapytanie = f'SELECT description FROM recipe_table WHERE id IN ({placeholders})'

    c = conn.cursor()
    c.execute(zapytanie, fav_recipes_list)
    wyniki = c.fetchall()

    final_result = ' ' 

    for output in wyniki:
        final_result += output[0] + '\n'

    print(final_result)
    return final_result

    
    


find_favorite_choosed_recipe(3)
