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



def  add_favorite_choosed_recipe(recipe_id,login,col): #recipes management 
    file='users.csv'
    row_num=0
    col_num=col
    counter=0
   
    new_value = recipe_id
    with open('users.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        
        for row in csv_reader:
            # Pierwsza kolumna to wiersz[0]
            first_col = row[1]
            if first_col==login:
                print(counter)
                row_num=counter
            counter+=1


    with open(file, 'r', newline='') as csv_file:
        scanner = csv.reader(csv_file)
        data = list(scanner)

    if row_num < len(data) and col_num < len(data[row_num]):
        data[row_num][col_num] = data[row_num][col_num]+" " +new_value

        # Zapisz zmienione dane z powrotem do pliku CSV
        with open(file, 'w', newline='') as csv_file:
            save_file = csv.writer(csv_file)
            save_file.writerows(data)
    else:
        print('fail')




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

            
