import os
from project.config import Config
from flask import Flask, render_template, redirect, flash, url_for
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    return app