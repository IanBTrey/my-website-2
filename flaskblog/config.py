import os


class Config:
    SECRET_KEY = '58c55421ddc3440d12ac4ac01e86cefb'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ianbriankibet006@gmail.com'
    MAIL_PASSWORD = 'sixthpinkrose'
