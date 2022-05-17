# @since: 2022-04-26
# @version: Alpha 2022-02-16-0.1.15
# @author: Sabri Salih
from flask import Flask
from flask import render_template

from Predict import Predict
from config import config
from flask_bootstrap import Bootstrap
from flask import request
from flask_sqlalchemy import SQLAlchemy
from CForm_upload import CForm_upload
from keras.models import model_from_json

# -----------------------------------
# App Specification
# ----------------------------------
app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config.from_object(config())

# LOAD TRAINED MODEL
json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("model.h5")

@app.route('/')
def index():
    form = CForm_upload()
    return render_template('index.html', form=form)


@app.route('/received_data', methods=['GET', 'POST'])
def received_data():
    from CUpload import CUpload

    # request is from the Function in the html @code: received_data in the html form.
    sUpload_path = app.config["UPLOAD_CONTENT"]
    data = CUpload(sUpload_path, request)
    img_path = data.upload_path
    prediction = Predict(img_path)

    return render_template('success.html', img_path=img_path, predict=prediction)


# Start the app.
if __name__ == '__main__':
    app.run(debug=True)

