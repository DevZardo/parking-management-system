import os

class Config:
    DEBUG = os.getenv('DEBUG', False)
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///parking.db')
