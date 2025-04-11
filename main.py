from kivy.app import App
from kivy.uix.label  import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = "name:"))
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text = "Branch:"))
        self.brnach = TextInput(multiline = False)
        self.add_widget(self.brnach)
        
        self.add_widget(Label(text = "En No:"))
        self.enno = TextInput(multiline = False)
        self.add_widget(self.enno)
        
        self.add_widget(Label(text = "year:"))
        self.year = TextInput(multiline = False)
        self.add_widget(self.year)
        
        
    
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()