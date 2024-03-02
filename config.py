import os

class Config:
    # Secret key for protecting against CSRF attacks and other security-related features
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Database connection URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/db_name'

    # Prevent SQLAlchemy from tracking modifications (can improve performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False