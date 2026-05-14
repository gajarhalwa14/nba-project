from dotenv import load_dotenv
import os

load_dotenv("config.env")

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG", False)
    SQLALCHEMY_TRACK_MODIFICATIONS = False