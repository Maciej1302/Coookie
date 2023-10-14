from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from projekt import szukarka 
from projekt import check_user_existence 
from projekt import add_user
from kivy.uix.image import Image
from datetime import datetime
import re

class MyPopup(Popup):

    pass



class FirstWindow(Screen):
    img =Image(source="kanapka_ze_schabem.png")
    pass

class GuestApp(Screen,Widget):
    def GuestPress(self, ingredients):
        return getRecipe(ingredients)*5

    pass


def open_pop_up(self):
    pops = MyPopup()
    pops.open()



def getRecipe(id):
    recipe=szukarka(id)
    final_recipe=""
    for item in recipe:
        final_recipe=final_recipe+item+"\n"+"\n"
    return final_recipe


class SecondWindow(Screen):
         def verification(self):
            login = self.ids.login.text
            password = self.ids.password.text
            #if check_user_existence(login):
            App.get_running_app().root.current='loggedapp'
            App.get_running_app().root.transition.direction = "up"
            #else:
               # App.get_running_app().root.current='second'
                #open_pop_up(self)
                


class ThirdWindow(Screen):
    def press(self):
        ingredients= self.ids.ingredients.text
        self.ids.recipe.text=getRecipe(ingredients)
    pass

class RegisterWindow(Screen):
    def verification(self,value,email,name,surname, passwd):
        name = self.ids.name.text
        surname = self.ids.surname.text
        passw = self.ids.register_passw.text
        email = self.ids.email.text
        no_valid = self.date_verification(value)
        email_check = self.email_verification(email)
        name_check = self.name_verification(name)
        surname_check = self.name_verification(surname)
        password_check = self.password_verification(passwd)
        if check_user_existence(email):
            App.get_running_app().root.current = 'second'
        elif name_check==False or surname_check == False or password_check == False or not no_valid or not email_check:
            open_pop_up(self)
        else:
            add_user(email, passw, name, surname)
            App.get_running_app().root.current = 'second'
    
    def date_verification(self, v1):
        input_date = v1.strip()
        if self.is_valid_date(input_date):
            return True

        else:
            
            return False

    def is_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:

            return False
    def email_verification(self, e1):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, e1) or e1==" ":
            return False
        else:
            return True
    def name_verification(self,data):
        if data== "":
            return False
        
        if not data[0].isupper() or data[1:].isupper():
            return False
        for char in data[1:]:
            if not char.isalpha() or char.isupper():
                return False
        
        return True
    
    def password_verification(self,password):
        if len(password) < 8 or password==" ":
            return False

        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]', password):
            return False

        return True
    pass

class WindowManager(ScreenManager):
    pass

class Widgets(Widget): 
    pass

class LoggedApp(Screen):
    def LoggedPress(self,ingredients):
        return getRecipe(ingredients)*5
    pass

class OptionWindow(Screen):
    pass



kv = Builder.load_file("proto.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()

#123
#321