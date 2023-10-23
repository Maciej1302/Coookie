import csv

def  find_favorite_choosed_recipe(login):
    file='users.csv'
    with open('users.csv', 'r') as plik_csv:
        czytnik_csv = csv.reader(plik_csv)
        # Iteruj przez wiersze pliku CSV przy użyciu pętli for
        for wiersz in czytnik_csv:
            # Pierwsza kolumna to wiersz[0
            pierwsza_kolumna = wiersz[0]
            if pierwsza_kolumna==login:
                print(wiersz[4])
find_favorite_choosed_recipe("mail")