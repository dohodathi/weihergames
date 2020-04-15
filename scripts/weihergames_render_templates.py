from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

env = Environment(
    loader=FileSystemLoader('../templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


template = env.get_template('playerprofile.html')

filename = os.path.join('builds', 'player_all.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        players = [
        {'name': 'THEEL', 'url': '/theel'},
        {'name': 'DOOMPY', 'url': '/doompy'},
        {'name': 'MAZL', 'url': '/mazl'}
        ]
    ))