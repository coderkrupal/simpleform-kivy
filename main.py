from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('whatever.kv')



class MyGridLayout(Widget):
    
    name = ObjectProperty(None)
    id = ObjectProperty(None)
    
    

    def press(self):
        name = self.name.text
        rollno = self.rollno.text

        print(f"{name},{rollno}")

        self.name.text = " "
        self.rollno.text = " "

class ExApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    ExApp().run()
