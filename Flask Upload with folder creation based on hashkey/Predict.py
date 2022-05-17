## Author: Sabri Salih
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json


def Predict(upload_path):
    # LOAD TRAINED MODEL
    class_dict = {0: 'daisy', 1: 'dandelion', 2: 'rose', 3: 'sunflower', 4: 'tulip'}
    json_file = open('model.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("model.h5")
    image_path = upload_path
    predict_image = image.load_img(image_path, target_size=(240, 320, 3))
    predict = image.img_to_array(predict_image)
    predict = np.expand_dims(predict, axis=0)
    predicted_class = np.argmax(model.predict(predict), axis=1)[0]
    return str(class_dict[predicted_class])