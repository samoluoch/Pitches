import os

class Config:
    '''
    This is the general configuration parent class
    '''

    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:sam123@localhost/pitches'


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    This is the production configuration child class
    
    Args:
        Config: The parent configuration class with the general config settings
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:sam123@localhost/pitches_test'

class DevConfig(Config):
    '''
    Development configuration child class

    Arrgs:
        Config the parent configuration class with the general config settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:sam123@localhost/pitches'

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}
