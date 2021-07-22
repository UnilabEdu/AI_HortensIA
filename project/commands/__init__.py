from project import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from .populate_initial import PopulateInitial
from .populate_random import PopulateWithRandomCommand

manager = Manager(create_app())

manager.add_command('db', MigrateCommand)
manager.add_command('populate_initial', PopulateInitial)
manager.add_command('populate_with_random', PopulateWithRandomCommand)
# manager.add_command('populate_streaks', )
