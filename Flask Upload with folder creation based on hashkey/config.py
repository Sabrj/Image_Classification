# App.
# @since: 2022-01-01
# @version: Alpha 2022-01-11-0.1.11
# @development time: 67h (stage: 2022-02-02 14:00)
# @author: Dr. Benjamin M. Abdel-Karim
# @source: https://hackersandslackers.com/configure-flask-applications/
# SHA 256: https://emn178.github.io/online-tools/sha256.html
class config(object):

    SECRET_KEY = '860db5535f297d6e338c6e50fb5be215dd9c06bc16cc5520a98eb84dd06a9387!'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_DATABASE_NAME = 'database.db'
    UPLOAD_CONTENT = 'static/'

    # @source: https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 12345678910
    sSerializerKey = '63640264849a87c90356129d99ea165e37aa5fabc1fea46906df1a7ca50db492'

    # E-Mail address

