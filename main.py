from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from CropModule import Cropimage



Builder.load_file('frontend.kv')
Window.size = (525, 525)

class FileChooser(BoxLayout):


    def select_min_neighbour(self):
        self.min_neighbours = self.ids.user_query.text

    def select_scale_factor(self):
        self.scale_factor = self.ids.user_query_1.text

    def select_size(self):
        self.sizee=self.ids.user_query_2.text

    def take_folder(self):
        self.take_path=self.ids.user_query_3.text
        #self.take_path=(filechooser.choose_dir())
        #print((self.take_path))
    def save_folder(self):
        self.save_path = self.ids.user_query_4.text
        if((self.take_path is not None) and (self.save_path is not None) ):
            crop = Cropimage(str(self.save_path), str(self.take_path))
        else:
            raise ValueError('You must give paths!')

        if (self.min_neighbours is not None):
            crop.set_min_neighbour(int(self.min_neighbours))
        if (self.scale_factor is not None):
            crop.set_scale_factor(float(self.scale_factor))
        if (self.sizee is not None):

            temp = eval(self.sizee)
            crop.set_size(temp)

        crop.crop()
class FileApp(App):

    def build(self):
        return FileChooser()




if __name__=="__main__":
    FileApp().run()