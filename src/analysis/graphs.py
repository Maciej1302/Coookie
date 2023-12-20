import matplotlib.pyplot as plt
import pandas as pd

def bar_plot(id):
    
    users_frame = pd.read_csv('users.csv') # DataFrame z csvki
    print(users_frame.head())
    
    choosed_recipes = users_frame.loc[id,'ChoosedRecipes'] # wybranie ulubionych przepisow
    print("wybrane przepisy to" + choosed_recipes)

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


    

    
    

    
    


  