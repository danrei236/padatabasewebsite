import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///political_party.db'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://uuvjjka53mnm:p719f9bf82e75f3d4a06bb715bdea05f80308926d56487255b5dabb2ef74a280f@c9uss87s9bdb8n.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d6nl21rb2ui94b'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
