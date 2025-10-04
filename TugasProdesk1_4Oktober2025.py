from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from PIL import Image as PILImage
import os

Window.size = (600, 400)

class ImageConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.choose_btn = Button(text="Pilih Gambar JPG", size_hint=(1, 0.1))
        self.choose_btn.bind(on_release=self.open_filechooser)
        self.add_widget(self.choose_btn)

        self.img_preview = Image(size_hint=(1, 0.8))
        self.add_widget(self.img_preview)

    def open_filechooser(self, instance):
        content = FileChooserIconView(filters=["*.jpg", "*.jpeg"])
        popup = Popup(title="Pilih Gambar JPG",
                      content=content,
                      size_hint=(0.9, 0.9))

        content.bind(on_submit=lambda chooser, selection, touch: self.convert_image(selection, popup))
        popup.open()

    def convert_image(self, selection, popup):
        if not selection:
            return
        jpg_path = selection[0]
        self.img_preview.source = jpg_path

        # Resize dan convert ke PNG
        img = PILImage.open(jpg_path)
        img_resized = img.resize((300, 300))  # ubah ukuran ke 300x300 px
        png_path = os.path.splitext(jpg_path)[0] + "_converted.png"
        img_resized.save(png_path, "PNG")

        print(f"Gambar berhasil disimpan sebagai {png_path}")
        popup.dismiss()


class ImageConverterApp(App):
    def build(self):
        return ImageConverter()


if __name__ == "__main__":
    ImageConverterApp().run()
