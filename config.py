# IMPORTS 
import os

# CLASSES
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'