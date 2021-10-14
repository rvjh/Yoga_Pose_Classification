
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class yoga:
    def __init__(self,filename):
        self.filename =filename


    def predictionyoga(self):
        # load model
        model = load_model('model_yoga_vgg19.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (300, 300))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        print(result[0])

        if result[0][0] == 1:
            prediction = 'downdog'
            print(prediction)
            return [{ "image" : prediction}]

        elif result[0][1] == 1:
            prediction = "goddess"
            print(prediction)
            return [{"image" : prediction}]
        elif result[0][2] == 1:
            prediction = "plank"
            print(prediction)
            return [{"image": prediction}]
        elif result[0][3] == 1:
            prediction = "tree"
            print(prediction)
            return [{"image": prediction}]
        else:
            prediction = 'warrior2'
            print(prediction)
            return [{ "image" : prediction}]






