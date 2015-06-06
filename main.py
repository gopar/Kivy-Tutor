from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

import webbrowser

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


################################################################################
class KivyTutorRoot(BoxLayout):
    """Root of all widgets

    """
    def __init__(self, **kwargs):
        super(KivyTutorRoot, self).__init__(**kwargs)

    def changeScreen(self, next_screen):
        operations = "addition subtraction multiplication division".split()
        question = None

        if next_screen == "about this app":
            self.ids.kivy_screen_manager.current = "about_screen"


################################################################################
class KivyTutorApp(App):
    """App object

    """
    def __init__(self, **kwargs):
        super(KivyTutorApp, self).__init__(**kwargs)

    def build(self):
        return KivyTutorRoot()

    def getText(self):
        return ("Hey There!\nThis App was built using"
                "[b][ref=kivy]kivy[/ref][/b]\n"
                "Feel free to look at the source code "
                "[b][ref=source]here[/ref][/b].\n"
                "This app is under the [b][ref=mit]MIT License[/ref][/b]\n"
                "My site: [b][ref=website]PyGopar.com[/ref][/b]")

    def on_ref_press(self, instance, ref):
        _dict = {
            "source": "https://github.com/gopar/Kivy-Tutor",
            "website": "http://www.pygopar.com",
            "kivy": "http://kivy.org/#home",
            "mit": "https://github.com/gopar/Kivy-Tutor/blob/master/LICENSE"
        }

        webbrowser.open(_dict[ref])

if __name__ == '__main__':
    KivyTutorApp().run()
