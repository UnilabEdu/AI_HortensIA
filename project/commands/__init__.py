from flask_migrate import MigrateCommand
from flask_script import Manager

from project import create_app
from .populate_initial import PopulateInitial
from .populate_random import PopulateWithRandomCommand

manager = Manager(create_app())

manager.add_command('db', MigrateCommand)  # db commands prefix. available commands: db init, db migrate, db upgrade
manager.add_command('populate_initial', PopulateInitial)  # populate db with texts from files, emotions, admin user
manager.add_command('populate_with_random', PopulateWithRandomCommand)  # populate db with randomly filled tickets
