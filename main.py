from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from plyer import vibrator


class TestAndroidApp(MDApp):
    boxlayout = None
    vib_statis = False

    def build(self):
        print("build")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.boxlayout = MDBoxLayout(orientation="vertical")
        try:
            self.vib_status = (True if vibrator.exists() else False)
            print("True")
        except NotImplementedError:
            self.vib_status = False
        label = MDLabel(text=str(self.vib_status))
        button = MDRaisedButton(text="Vibrate", on_press=self.mytrigger)
        self.boxlayout.add_widget(label)
        self.boxlayout.add_widget(button)
        return self.boxlayout

    def mytrigger(self, a):
        if self.vib_status:
            vibrator.vibrate(time=2)


if __name__ == '__main__':
    TestAndroidApp().run()
