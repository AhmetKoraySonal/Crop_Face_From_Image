import cv2
import glob


class Cropimage:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def __init__(self, path_save, path_take, size=(72, 72),scaleFactor=1.001,minNeighbours=11,minSize=(30,30)):
        self.minSize = minSize
        self.minNeighbours = minNeighbours
        self.scaleFactor = scaleFactor
        self.size = size
        self.path_take = path_take
        self.path_save = path_save
        self.path = glob.glob(self.path_take + "\\*.*")

    def crop(self):
        count = 0
        for filename in self.path:
            img = cv2.imread(filename)

            # img = cv2.flip(img, -1) # flip video image vertically
            imgg = cv2.resize(img, self.size, interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=self.scaleFactor, minNeighbors=self.minNeighbours, minSize=self.minSize)
            rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
            for (x, y, w, h) in faces:
                # cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite(str(self.path_save) + '\\'+'.' + str(count) + ".png", rgb[y:y + h, x:x + w])


    def set_scale_factor(self,value):
        self.scaleFactor=value

    def set_min_neighbour(self,value):
        self.minNeighbours=value

    def set_size(self,size):
        self.size=size

