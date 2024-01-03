import matplotlib.pyplot as plt
import pandas as pd

def bar_plot(id):
    

    

    users_frame = pd.read_csv('user_recipes.csv') # DataFrame z csvki
    print(users_frame.head())
    index = users_frame.index[users_frame['user_id'] == id]
    choosed_recipes = users_frame.loc[index,'choosed_recipes'].iloc[0] # wybranie ulubionych przepisow
    
    
    choosed_recipes = str(choosed_recipes)
    print("wybrane przepisy to" + choosed_recipes + 'grdgf')
    choosed_recipes_list = choosed_recipes.split() # zrobienie listy ulubionych przepisow

    print("lista wybranych przepisów to" + str(choosed_recipes_list))
    
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
    
    
    fig, ax = plt.subplots()  # Utwórz figurę i osie
    ax.bar(ingredients, amount)
    ax.set_xlabel("Ingredients")
    ax.set_ylabel("Amount")
    ax.set_title("Ingredients chart")
    ax.locator_params(axis='y', integer=True)
    ax.set_xticklabels(ingredients, rotation=45, ha='right', rotation_mode='anchor')
    fig.tight_layout()
    plt.subplots_adjust(bottom=0.2)
    
    return fig  # Zwróć figurę zamiast wywoływania plt.show()






    
    

    
    


  