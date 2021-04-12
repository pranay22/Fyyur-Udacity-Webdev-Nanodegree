import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# Local DB URL
SQLALCHEMY_DATABASE_URI = 'postgresql://pranay:test123@localhost:5432/fyyurappdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False