from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class NumberCardsApp(App):
    def build(self):
        self.title = 'Number Cards'

        # Create an outer BoxLayout to center everything
        outer_layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(1, 1))

        # Create a GridLayout with 4 columns for the number buttons
        layout = GridLayout(cols=4, padding=10, spacing=10, size_hint=(None, None), size=(400, 400))
        
        # Create buttons for numbers 0 to 9
        for i in range(10):
            button = Button(text=str(i), size_hint=(None, None), size=(80, 80), font_size=24)
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)

        # Create a BoxLayout to center the GridLayout vertically
        center_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=400)
        center_layout.add_widget(Label(size_hint_y=None, height=20))  # Spacer
        center_layout.add_widget(layout)
        center_layout.add_widget(Label(size_hint_y=None, height=20))  # Spacer

        # Add the centered layout to the outer layout
        outer_layout.add_widget(center_layout)

        # Add an instruction label below the buttons
        instruction_label = Label(text="Press a number:", size_hint=(1, None), height=30)
        outer_layout.add_widget(instruction_label)

        return outer_layout

    def on_button_press(self, instance):
        print(f'Button {instance.text} pressed!')

if __name__ == '__main__':
    NumberCardsApp().run()
