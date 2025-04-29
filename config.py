import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///political_party.db'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://padatabasefile_user:TMnKEQxct1LaWsDc84CYr8NXWJhbFCD2@dpg-d08lfseuk2gs73cg8lgg-a/padatabasefile'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
