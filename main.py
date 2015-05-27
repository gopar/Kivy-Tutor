from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


################################################################################
class KivyTutorRoot(BoxLayout):
    """Root of all widgets

    """
    def __init__(self, **kwargs):
        super(KivyTutorRoot, self).__init__(**kwargs)


################################################################################
class KivyTutorApp(App):
    """App object

    """
    def __init__(self, **kwargs):
        super(KivyTutorApp, self).__init__(**kwargs)

    def build(self):
        return KivyTutorRoot()

if __name__ == '__main__':
    KivyTutorApp().run()
