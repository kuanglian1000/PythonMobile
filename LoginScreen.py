from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
  """
  Login Screen
  """
  def __init__(self , **kwargs):
    """
    docstring
    """
    super(LoginScreen , self).__init__(**kwargs)
    self.cols = 2
    self.add_widget(Label(text='User Name'))
    self.username = TextInput(multiline=False)
    self.add_widget(self.username)
    self.add_widget(Label(text='Password'))
    self.password = TextInput(password=True,multiline=False)
    self.add_widget(self.password)
