import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///political_party.db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://u93rujlo0fek1b:pc0748f040f84ae539830f559bb6dd10316316f817ca627b2cf5bb21898288d00@c952v5ogavqpah.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d57ucann7r8e8q'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
