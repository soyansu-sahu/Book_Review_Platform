class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_complex_and_secure_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:asdfghjkl@localhost:5431/postgres'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
