from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from datetime import datetime
import re
from src.recipes_management import recipes_management as rm
from src.user import user as user
from src.verification import verification as verification 
from src.analysis import graphs as graph
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy, FigureCanvasKivyAgg
class MyPopup(Popup):
    pass



class FirstWindow(Screen):
    
    pass


class GuestApp(Screen,Widget):
    def GuestPress(self, ingredients):
        return getRecipe(ingredients)*5
    
    pass

def open_pop_up(self):
    pops = MyPopup()
    pops.open()
    

def getRecipe(id): 
    recipe=rm.recipe_searcher(id)
    final_recipe=""
    for item in recipe:
        final_recipe=final_recipe+item+"\n"+"\n"
    return final_recipe    

class SecondWindow(Screen):
         def verification(self):
            login = self.ids.login.text
            global user_login
            user_login=login
            password = self.ids.password.text
            if user.check_user_existence(login):
                App.get_running_app().root.current='loggedapp'
                App.get_running_app().root.transition.direction = "up"
            else:
                App.get_running_app().root.current='second'
                open_pop_up(self)
            


class MyAccount(Screen):
    pass    


class ThirdWindow(Screen):
    def press(self):
        ingredients= self.ids.ingredients.text
        self.ids.recipe.text= getRecipe(ingredients)
    pass


class RegisterWindow(Screen):
    def verification(self, date_of_birth, email, name, surname, passwd):
        name = self.ids.name.text
        surname = self.ids.surname.text
        passw = self.ids.register_passw.text
        email = self.ids.email.text
        no_valid = verification.date_verification(date_of_birth)
        email_check = verification.email_verification(email)
        name_check = verification.name_verification(name)
        surname_check = verification.name_verification(surname)
        password_check = verification.password_verification(passwd)


        if user.check_user_existence(email):
            App.get_running_app().root.current = 'second'
        elif name_check==False or surname_check == False or password_check == False or not no_valid or not email_check:
            open_pop_up(self)
        else:
            user.add_user(email, passw, name, surname,date_of_birth)
            App.get_running_app().root.current = 'second'
    
    pass

class WindowManager(ScreenManager):
    pass



class Widgets(Widget): 
    pass


class LoggedApp(Screen):
    def LoggedPress(self,ingredients):
        return getRecipe(ingredients)*5
    pass

    def AddFavorite(self):
        print(user_login)
        recipe_A=self.ids.favorite_id_recipe.text
        recipe_B = self.ids.choosed_id_recipe.text
        rm.add_favorite_choosed_recipe(recipe_A,user_login,7)
        rm.add_favorite_choosed_recipe(recipe_B,user_login,8)
        

class OptionWindow(Screen):
    pass

class SavedRecipes(Screen):
    def SavedPress(self):
        self.ids.your_saved_recipes.text=rm.find_favorite_choosed_recipe(user_login)
    pass

class Analysis(Screen):
    pass

class FoodAnalysis(Screen):
    def generate_analysis(self):

        return graph.bar_plot()
    pass

class FoodAnalysisScreen(Screen):
    pass

kv = Builder.load_file("proto.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()

#1233212