from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget



class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = 'lr-tb'
        for i in range(100):
            # size = dp(100 + i * 10)
            size = dp(100)
            self.add_widget(Button(text=str(i+1), size_hint=(None, None), size=(size, size)))
# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     b3 = Button(text='C')
    #     self.orientation = 'vertical'  # 'horizontal' is default operation
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


if __name__ == '__main__':
    TheLabApp().run()