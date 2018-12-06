import os


class Config:
    SECRET_KEY = '6086dbce01e4a17787cf07135787e954'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FLASKBLOG_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('FLASKBLOG_EMAIL_PASS')
