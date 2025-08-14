import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

DB_ENGINE = os.getenv("DB_ENGINE", "mysql")
DB_NAME = os.getenv("DB_NAME", "invoicesap")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USERNAME = os.getenv("DB_USERNAME", "root")
DB_PASS = quote_plus(os.getenv("DB_PASS", ""))  # encode nếu có ký tự đặc biệt

SQLALCHEMY_DATABASE_URI = (
    f"{DB_ENGINE}+pymysql://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False