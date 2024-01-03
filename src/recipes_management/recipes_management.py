import pandas as pd
import csv



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
    



def  find_favorite_choosed_recipe(login): #recipes management
    file='users.csv'
    favorite_recipe=""
    with open('users.csv', 'r') as plik_csv:
        csv_reader = csv.reader(plik_csv)
        for row in csv_reader:
            first_col = row[0]
            if first_col==login:
                print(row[4])
                favorite_recipe=row[4]
    return favorite_recipe

            
