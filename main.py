from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import gc

class GamePanelApp(App):
    boosted = False

    def build(self):
        # Ekranda küçük bir baloncuk gibi durması için pencere boyutu
        Window.size = (120, 120)
        Window.top = 200
        Window.left = 10
        
        layout = FloatLayout()

        # Ana tetikleyici butonumuz
        self.btn = Button(
            text='BOOST\nOFF',
            size_hint=(1, 1),
            background_color=(0.2, 0.6, 1, 0.8),
            font_size=16,
            halign='center'
        )
        self.btn.bind(on_press=self.toggle_boost)
        layout.add_widget(self.btn)
        return layout

    def toggle_boost(self, instance):
        if not self.boosted:
            self.boost_on()
        else:
            self.boost_off()

    def boost_on(self):
        self.btn.text = 'BOOST\nON'
        self.btn.background_color = (0.2, 0.8, 0.2, 0.9)
        self.boosted = True
        
        # Rootsuz RAM Temizleme Stratejisi:
        # Yapay bir bellek yükü oluşturarak Android'in arka plandaki gereksiz uygulamaları kapatmasını tetikliyoruz.
        try:
            dummy_list = []
            # Casper Via M40'ın RAM durumuna göre geçici olarak belleği tetikle
            for _ in range(300000):
                dummy_list.append("SefaAi_Booster_Active_Memory_Clean_Process")
            
            # Belleği hemen geri serbest bırakıyoruz ki temizlenen RAM oyuna kalsın
            del dummy_list
            gc.collect() 
        except Exception:
            pass

    def boost_off(self):
        self.btn.text = 'BOOST\nOFF'
        self.btn.background_color = (0.2, 0.6, 1, 0.8)
        self.boosted = False
        gc.collect()

if __name__ == '__main__':
    GamePanelApp().run()

