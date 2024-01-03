from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from datetime import datetime
import re
from src.recipes_management import recipes_management as rm
from src.user import user as user
from src.verification import verification as verification 
from src.analysis import graphs as graph
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy, FigureCanvasKivyAgg
from kivy.garden.matplotlib.backend_kivyagg import NavigationToolbar2Kivy
from kivy.metrics import dp
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
            global user_id
            login = self.ids.login.text
            global user_login
            user_login=login
            password = self.ids.password.text
            if user.check_user_existence(login):
                user_id = user.get_user_id(login)
                print(user_id)
                App.get_running_app().root.current='loggedapp'
                App.get_running_app().root.transition.direction = "up"
            else:
                App.get_running_app().root.current='second'
                open_pop_up(self)
            





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
        
        recipe_A=self.ids.favorite_id_recipe.text
        recipe_B = self.ids.choosed_id_recipe.text
        
        rm.add_favorite_choosed_recipe(recipe_A,user_id,'favourite_recipes')
        rm.add_favorite_choosed_recipe(recipe_B,user_id,'choosed_recipes')
        

class OptionWindow(Screen):
    def go_to_my_account(self):
        if 'my_account' in self.manager.screen_names:
            self.manager.current = 'my_account'
        else:
            app = App.get_running_app()
            app.build_my_acc()  
            self.manager.current = 'my_account'


class SavedRecipes(Screen):
    def SavedPress(self):
        self.ids.your_saved_recipes.text=rm.find_favorite_choosed_recipe(user_login)
    pass

class Analysis(Screen):
    pass

class KivyMatplotlibCanvas(FigureCanvasKivyAgg):
    def __init__(self, fig, **kwargs):
        super(KivyMatplotlibCanvas, self).__init__(fig, **kwargs)
        self._touches = []
        self._last_touch_pos = None
        self.fig = fig
        self.ax = self.fig.axes[0]

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            return False
        self._touches.append(touch)
        return True

    def on_touch_move(self, touch):
        if touch in self._touches:
            if len(self._touches) == 1:
                self.translate(touch)
            elif len(self._touches) == 2:
                self.zoom(touch)
        return True

    def on_touch_up(self, touch):
        if touch in self._touches:
            self._touches.remove(touch)
        return True

    def translate(self, touch):
        if self._last_touch_pos:
            dx = (touch.x - self._last_touch_pos[0]) / dp(100)
            dy = (touch.y - self._last_touch_pos[1]) / dp(100)
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.ax.set_xlim([xlim[0] - dx, xlim[1] - dx])
            self.ax.set_ylim([ylim[0] + dy, ylim[1] + dy])
            self.draw_idle()
        self._last_touch_pos = touch.pos

    def zoom(self, touch):
        if self._last_touch_pos:
            touch1, touch2 = self._touches
            old_distance = ((touch1.px - touch2.px) ** 2 + (touch1.py - touch2.py) ** 2) ** 0.5
            new_distance = ((touch1.x - touch2.x) ** 2 + (touch1.y - touch2.y) ** 2) ** 0.5
            zoom_factor = old_distance / new_distance
            self.handle_zoom(zoom_factor)
        self._last_touch_pos = touch.pos

    def handle_zoom(self, zoom_factor):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        self.ax.set_xlim([x * zoom_factor for x in xlim])
        self.ax.set_ylim([y * zoom_factor for y in ylim])
        self.draw_idle()


class FoodAnalysis(Screen):

    def generate_analysis(self):
        fig = graph.bar_plot(user_id)  
        canvas = KivyMatplotlibCanvas(fig)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(canvas)

        close_button = Button(text='Close', size_hint=(1, 0.1))
        close_button.bind(on_press=self.dismiss_popup)

        layout.add_widget(close_button)

        self.popup = Popup(title="Ingredients Chart", content=layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def dismiss_popup(self, instance):
        self.popup.dismiss()


class FoodAnalysisScreen(Screen):
    pass

class MyAccount(Screen):
    unique_id = StringProperty('')
    email = StringProperty('')
    name = StringProperty('')
    surname = StringProperty('')
    date_of_birth = StringProperty('')
    
    def on_pre_enter(self, *args):
        
        self.load_user_data()

    def on_leave(self, *args):
        # Resetowanie danych użytkownika po opuszczeniu ekranu
        self.reset_data()

    def reset_data(self):
        # Resetowanie wartości właściwości do wartości domyślnych
        self.unique_id = ''
        self.email = ''
        self.name = ''
        self.surname = ''
        self.date_of_birth = ''

    def load_user_data(self):
        # Załaduj dane użytkownika i przypisz je do właściwości ekranu
        
        print('dziala??')
        user_data = user.get_user_data(user_id)  # Załóżmy, że ta funkcja zwraca wszystkie potrzebne dane
        print("dane to: ")
        print(user_data)
        self.email, self.name, self.surname, self.date_of_birth = user_data
        self.unique_id = str(user_id)
            

        

        


    def change_password(self,current_password,new_password):
        if verification.password_verification(new_password):
            user.change_password(user_id,current_password, new_password)
            return create_popup('The password has been successfully changed')
        
        else:
            return create_popup('The current password is incorrect or \n the new password does not meet the requirements')
            
    
    def change_email(self,new_email):
        if verification.email_verification(new_email) and user.check_user_existence(new_email) == False:
            user.change_email(user_id, new_email)
            create_popup("The email address change was successful \n reopen 'My Account' to see the changes")
        
        else:
            create_popup("The email address provided is incorrect or belongs to another user")


def create_popup(message):
    popup = Popup(title='Information',
                  content=Label(text=message),
                  size_hint=(None, None), size=(400, 400))
    popup.open()


kv = Builder.load_file("proto.kv")



class MyMainApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(FirstWindow(name='first'))
        self.sm.add_widget(SecondWindow(name='second'))
        self.sm.add_widget(ThirdWindow(name='third'))
        self.sm.add_widget(RegisterWindow(name='register_window'))
        self.sm.add_widget(OptionWindow(name='option'))
        self.sm.add_widget(SavedRecipes(name='savedrecipes'))
        self.sm.add_widget(GuestApp(name='guestapp'))
        self.sm.add_widget(Analysis(name='analysis'))
        self.sm.add_widget(LoggedApp(name='loggedapp'))
        self.sm.add_widget(MyAccount(name='my_account'))
        return self.sm
        
    def build_my_acc(self):
        if 'my_account' not in self.sm.screen_names:
            self.sm.add_widget(MyAccount(name='my_account'))
    
if __name__ == "__main__":
    MyMainApp().run()

#1233212