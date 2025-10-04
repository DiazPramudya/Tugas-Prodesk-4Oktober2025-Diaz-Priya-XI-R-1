import matplotlib.pyplot as plt
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from io import BytesIO

class MatplotlibKivyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Tombol untuk pilih jenis grafik
        self.button_bar = Button(text="Tampilkan Grafik Bar", size_hint=(1, 0.15))
        self.button_scatter = Button(text="Tampilkan Scatter Plot", size_hint=(1, 0.15))
        self.button_log = Button(text="Tampilkan Grafik Logaritmik", size_hint=(1, 0.15))

        self.button_bar.bind(on_press=self.plot_bar)
        self.button_scatter.bind(on_press=self.plot_scatter)
        self.button_log.bind(on_press=self.plot_log)

        self.image = Image()

        # Tambahkan ke layout
        self.layout.add_widget(self.button_bar)
        self.layout.add_widget(self.button_scatter)
        self.layout.add_widget(self.button_log)
        self.layout.add_widget(self.image)

        return self.layout

    def show_plot(self, fig):
        """Helper untuk menampilkan plot matplotlib di Kivy"""
        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)

        core_image = CoreImage(buf, ext='png')
        self.image.texture = core_image.texture

    def plot_bar(self, instance):
        x = np.arange(1, 6)
        y = np.array([5, 7, 3, 8, 6])

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(x, y)
        ax.set_title("Grafik Bar")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        self.show_plot(fig)

    def plot_scatter(self, instance):
        x = np.random.rand(50)
        y = np.random.rand(50)

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.scatter(x, y, c='red', marker='o')
        ax.set_title("Scatter Plot")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")

        self.show_plot(fig)

    def plot_log(self, instance):
        x = np.linspace(1, 10, 100)
        y = np.exp(x)  # fungsi eksponensial biar jelas di log

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(x, y, marker='o')
        ax.set_yscale("log")
        ax.set_title("Grafik Skala Logaritmik")
        ax.set_xlabel("X")
        ax.set_ylabel("Y (log scale)")

        self.show_plot(fig)


if __name__ == '__main__':
    MatplotlibKivyApp().run()
