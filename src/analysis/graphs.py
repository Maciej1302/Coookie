import matplotlib.pyplot as plt
import pandas as pd

def bar_plot():
    users_frame = pd.read_csv('users.csv') # DataFrame z csvki
    print(users_frame.head())
    
    choosed_recipes = users_frame.loc[0,'ChoosedRecipes'] # wybranie ulubionych przepisow

    choosed_recipes_list = choosed_recipes.split() # zrobienie listy ulubionych przepisow

    print(choosed_recipes_list)
    print(type(choosed_recipes))
    recipes_frame = pd.read_csv('recipes.csv') # DataFrame z csvki z przepisami

    recipe_id = list(recipes_frame['id'])
    
    dict = {}

    for id in choosed_recipes_list:
        ing_list= recipes_frame.at[int(id)-1,'ingredients'].split()
        print(ing_list)

        for ing in ing_list:
            if ing in dict:
                dict[ing]+=1
            else:
                dict[ing] = 1
                
    ingredients = dict.keys()
    amount = dict.values()

    plt.bar(ingredients,amount)
    plt.xlabel("Ingredients")
    plt.ylabel("Amount")
    plt.title("Ingredients chart")
    plt.locator_params(axis='y', integer=True)
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.show()


    

    
    

    
    


    # choosed_recipes = users_frame['ChoosedRecipes']
    # print(choosed_recipes)    

bar_plot()


# print(df.head)
#     y = [1,2,3,4]
#     x = ["jajka","bulka","ser"]

#     x = {'jajka': 2,
#         'bułka': 3,
#         'ser':5}

#     os_x = list(x.keys())
#     os_y = list(x.values())
#     print(os_x)
#     print(os_y)
#     plt.bar(os_x,os_y)
#     plt.show()