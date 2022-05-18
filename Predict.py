## Author: Sabri Salih
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json


def Predict(upload_path):
    # LOAD TRAINED MODEL
    class_dict = {0: 'donuts', 1: 'falafel', 2: 'gebratener reis', 3: 'gnocchi', 4: 'hamburger',
                  5: 'eis', 6: 'nachos', 7: 'omlette', 8: 'pizza', 9: 'sushi',}
    json_file = open('modelv2.json', 'r')
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("modelv2.h5")
    image_path = upload_path
    predict_image = image.load_img(image_path, target_size=(240, 320, 3))
    predict = image.img_to_array(predict_image)
    predict = np.expand_dims(predict, axis=0)
    predicted_class = np.argmax(model.predict(predict), axis=1)[0]
    return str(class_dict[predicted_class])