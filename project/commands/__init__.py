import click
from flask.cli import with_appcontext

from project.commands.populate_initial import populate_initial
from project.commands.populate_random import populate_with_random


@click.command('populate_initial')
@with_appcontext
def populate_initial_command():
    populate_initial()


@click.command('populate_with_random')
@with_appcontext
def populate_with_random_command():
    populate_with_random()


command_list = [populate_initial_command, populate_with_random_command]
