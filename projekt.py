import pandas as pd
import csv


 
ing="salata pomidor ogorek chleb jajka bułka ser"

def szukarka(ing): 
    x=[]
    ing =ing.lower().split() 
    df = pd.read_csv('przepisy.csv')
    for index, row in df.iterrows():
        ingredients_list = row['ingredients'].lower().split() 
        if any(ingredient in ingredients_list for ingredient in ing) and all(ingredient in ing for ingredient in ingredients_list):
            x.append(row['description'])
    return x 

def check_user_existence(mail):
    df = pd.read_csv('users.csv')
    for index, row in df.iterrows():
        csv_mail=row['email']
        if mail == csv_mail:
            return True
    return False

def  add_favorite_choosed_recipe(recipe_id,login,col):
    file='users.csv'
    nr_wiersz=0
    kolumna=col
    licznik=0
   
    nowa_wartosc = recipe_id
    with open('users.csv', 'r') as plik_csv:
        czytnik_csv = csv.reader(plik_csv)

        # Iteruj przez wiersze pliku CSV przy użyciu pętli for
        for wiersz in czytnik_csv:
            # Pierwsza kolumna to wiersz[0]
            pierwsza_kolumna = wiersz[0]
            if pierwsza_kolumna==login:
                print(licznik)
                nr_wiersz=licznik
            licznik+=1


    # Wczytaj istniejące dane z pliku CSV
    with open(file, 'r', newline='') as plik_csv:
        czytnik = csv.reader(plik_csv)
        dane = list(czytnik)

    # Sprawdź, czy wiersz i kolumna istnieją w pliku CSV
    if nr_wiersz < len(dane) and kolumna < len(dane[nr_wiersz]):
        # Zaktualizuj wartość w określonym wierszu i kolumnie
        dane[nr_wiersz][kolumna] = dane[nr_wiersz][kolumna]+" " +nowa_wartosc

        # Zapisz zmienione dane z powrotem do pliku CSV
        with open(file, 'w', newline='') as plik_csv:
            zapisywacz = csv.writer(plik_csv)
            zapisywacz.writerows(dane)
    else:
        print('Nieprawidłowy wiersz lub kolumna.')


def  find_favorite_choosed_recipe(login):
    file='users.csv'
    favorite_recipe=""
    with open('users.csv', 'r') as plik_csv:
        czytnik_csv = csv.reader(plik_csv)
        for wiersz in czytnik_csv:
            pierwsza_kolumna = wiersz[0]
            if pierwsza_kolumna==login:
                print(wiersz[4])
                favorite_recipe=wiersz[4]
    return favorite_recipe



def add_user(email,password,name,surname):
   data=[[email,password,name,surname]]
   file=open("users.csv","a",newline='')
   writer=csv.writer(file)

   writer.writerows(data)
   file.close()