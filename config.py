import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///political_party.db'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://u6stgvkaog777g:pd2c6d566e18ed1c6ce7478753e1e1cd12511a9bb381c3f6c0334722473ac348c@c952v5ogavqpah.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dfgmmtcun2thfr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
