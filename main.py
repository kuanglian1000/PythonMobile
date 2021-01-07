
import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from LoginScreen import LoginScreen

class MyApp(App):
  """
  docstring
  """
  def build(self):
    """
    docstring
    """
    # return Label(text='Hello World')
    return LoginScreen()

if __name__ == '__main__':
  MyApp().run()