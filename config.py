import os

SECRET_KEY = 'youtan'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='',
        servidor='localhost',
        database='youtan_jr'
    )


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
WTF_CSRF_CHECK_DEFAULT = False





























