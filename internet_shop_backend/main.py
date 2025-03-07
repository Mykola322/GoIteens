import os

from flask import Flask, jsonify
from flask_restful import Resource
from dotenv import load_dotenv

from src.database.base import db


load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")


with app.app_context():
    db.create_all()