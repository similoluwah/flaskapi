"""
    Description :- This script creates the table 'data' and the Schema for serializing and deserializing data records.
"""

# Importing required packages
from flask import Flask 
from flask_marshmallow import Marshmallow 
from flask_sqlalchemy import SQLAlchemy 

from marshmallow import Schema, fields, validate, ValidationError

# Instantiating the Marshmallow and SQLAlchemy class
ma = Marshmallow()
db = SQLAlchemy()

# Creating the data schema
class Data(db.Model):

    __tablename__ = 'data'

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    phone_number = db.Column(
        db.BigInteger,
        nullable = False
    )

    run_time = db.Column(
        db.DateTime,
        index = False,
        unique = False,
        nullable = False
    )

    created_at = db.Column(
        db.DateTime, 
        index = False,
        unique = False,
        nullable = False
    )

    def __init__(self, phone_number, run_time, created_at):
        self.phone_number = phone_number
        self.run_time = run_time
        self.created_at = created_at

    def __repr__(self):
        return f"User :- {self.phone_number}"


# Defining the Schema for serialization and deserialization of responses

class DataSchema(ma.Schema):

    id = fields.Integer(
        dump_only = True
    )

    phone_number = fields.Integer(
        required = True
    )

    run_time = fields.DateTime(
        required = True 
    )

    created_at = fields.DateTime(
        required = True
    )