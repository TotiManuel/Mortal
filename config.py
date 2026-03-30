import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mortal-secret")

    SQLALCHEMY_DATABASE_URI = "sqlite:///tienda.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False