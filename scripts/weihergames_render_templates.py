from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, '../templates')
env = Environment(
    loader=FileSystemLoader(templates_dir),
    autoescape=select_autoescape(['html', 'xml'])
)


template = env.get_template('playerprofile.html')

filename = os.path.join(root, 'builds', 'player_all.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        players = [
        {'name': 'THEEL', 'image': 'images/vectorstock_21106731.png'},
        {'name': 'DOOMPY', 'image': 'images/vectorstock_21320352.png'},
        {'name': 'MAZL', 'image': '/mazl'}
        ]
    ))