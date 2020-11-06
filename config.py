"""
    Description :- Configuration file for connection to the MySQL database server (LOCALLY)
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_ECHO = False

SQLALCHEMY_TRACK_MODIFICATIONS = True

# SQLALCHEMY_DATABASE_URI = mysql://username:password@server/db 
USERNAME = 'root'
PASSWORD = 'root'
SERVER = 'localhost'
DATABASE = 'iqubetestdata'

SQLALCHEMY_DATABASE_URI = f"mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}"