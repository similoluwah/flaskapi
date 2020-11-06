"""
    Description :- This script is used for managing reversible changes to the database Schema
"""

# Importing required packages
from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from Model import db 

from app import create_app 

app = create_app("config")

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()



"""
    TO RUN in your terminal -> Ensure migrate.py is in your current working directory
    >> python migrate.py db init
    >> python migrate.py db migrate
    >> python migrate.py db upgrade
"""