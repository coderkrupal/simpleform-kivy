from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('store.kv')

class PizzaBook(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    def Press(self):
        name = self.name.text
        pizza = self.pizza.text
        
        print(f"{name} {pizza}")
        
        self.name.text = ""
        self.pizza.text = ""
        

class MyStore(App):
    def build(self):
        return PizzaBook()
    
if __name__ == '__main__':
    MyStore().run()