
"""
OUTPUT SPECIFICATION
<data> = {
    'player': <playerdata>,
    'matches': [<matchdata>],
}

<playerdata> = {
    'name': <string>,
    'elo': <float>,
    'rank': <int>,
    'img': <string>,
    'sumOffSeasonWon': <int>,
    'sumOffSeasonTie': <int>,
    'sumOffSeasonLose': <int>,
    'sumSeasonWon': <int>,
    'sumSeasonTie': <int>,
    'sumSeasonLose': <int>,
    'sumWon': <int>,
    'sumTie': <int>,
    'sumLose': <int>,
}


<matchdata> = {
    'game': <gamedata>,
    'participants': [<playerdata>],
    'result': [<integer>], # same order as participants
    'elo_delta': [<float>], # same order as participants
    'elo_total': [<float>], # same order as participants
    'winner': <playerdata>,
    'datetime': <datetime>,
    'tie': <boolean>,
}

<gamedata> = {
    'name': <string>,
    'img': <string,
    'field_of_play': <string>,
    'field_of_play_icon': <string>,
    'pointrules': [<string>] # example: "lowerwins",
    'specific_leveling_value' = <integer>,
}
"""

import os
import logging
import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from operator import itemgetter



logging.basicConfig(level=logging.DEBUG)

_ROOT_FILE = os.path.dirname(os.path.abspath(__file__))
JSON_DATABASE = os.path.join(_ROOT_FILE, '../data2012.json')


""" ELO CALC PARAMTER """
ELO_START_VALUE = 10000.0


class PlayerData():
    def __init__(self, name):
        self.name = name
        self.elo = 0.0
        self.rank = 0
        self.img = ''
        self.sumWon = 0
        self.sumTie = 0
        self.sumLose = 0
        self.sumSeasonWon = 0
        self.sumSeasonTie = 0
        self.sumSeasonLose = 0
        self.sumOffSeasonWon = 0
        self.sumOffSeasonTie = 0
        self.sumOffSeasonLose = 0
    def __str__(self):
        return 'PlayerData for {0}'.format(self.name)

class GameData():
    def __init__(self, name):
        self.name = name
        self.img = ''
        self.field_of_play = ''
        self.field_of_play_icon = ''
        self.pointrules = []
        self.specific_leveling_value = 0
    def __str__(self):
        return 'GameData for {0}'.format(self.name)


class MatchData():
    def __init__(self, game):
        self.game = game
        self.participants= []
        self.result = []
        self.winner = None
        self.datetime = ''
        self.tie = False
        self.location = ''
        self.remarks = ''
    def __str__(self):
        return 'MatchData of [{0}] played by: {1}'.format(self.game,self.participants)
    def winner(self):
        # return the winner as PlayerData object:
        pass

def read_player_from_json():
    players = []
    # Load data
    j = json.load(open(JSON_DATABASE))
    # Sanity check of json file:
    pass
    #output all warnings + errors, if no error continue:
    pass
    # set player:
    for name, data in j['members'].items():
        p = PlayerData(name)
        p.elo = ELO_START_VALUE
        p.img = os.path.join(_ROOT_FILE, '..', 'docs','images',data.get('img', ''))
        players.append(p)
        logging.debug('Player found in DB: {0}'.format(p))
    return players


def read_games_from_json():
    games = []
    # Load data
    j = json.load(open(JSON_DATABASE))
    # Sanity check of json file:
    pass
    #output all warnings + errors, if no error continue:
    pass
    # set player:
    for name, data in j['games'].items():
        g = GameData(name)
        g.img = data.get('img', '')
        g.field_of_play = data.get('field_of_play', '')
        g.field_of_play_icon = data.get('field_of_play_icon', '')
        g.pointrules = data.get('pointrules', [])
        g.specific_leveling_value = data.get('specific_leveling_value', 0)
        games.append(g)
        logging.debug('Game found in DB: {0}'.format(g))
    return games


def read_matches_from_json(players, games):
    matches = []
    # Load data
    j = json.load(open(JSON_DATABASE))
    # sort matches by date:
    sorted_matchlist_db = sorted(j['matches'], key=itemgetter('time'))
    # go through all matches and iterate ELO:
    for match_db in sorted_matchlist_db:
        # search for the game played:
        game_db = match_db['game']
        g = next((x for x in games if x.name == game_db), None)
        if g is None:
            logging.warning('GameData not in database: {0}'.format(game_db))
            g = GameData(game_db)
            games.append(g)
        m = MatchData(g)
        for participant_db, points_db in match_db['result'].items():
            # search for player with same name:
            p = next((x for x in players if x.name == participant_db), None)
            if p is None:
                logging.error('Matchdata has playername not in database: {0}'.format(participant_db))
                p = PlayerData(participant_db)
                players.append(p)
            # keep same order for particpants and points lists!!!:
            m.participants.append(p)
            m.result.append(points_db)
            m.location = match_db.get('location', '')
            m.remarks = match_db.get('remarks', '')
            m.datetime = match_db.get('time', '')
        matches.append(m)
        logging.debug('Match appended: {0}'.format(m))
    return matches

def process_matches(matches):
    pass # TODO


def get_year_from_datetime_string(dt_string):
    try:
        dt = datetime.strptime(dt_string, '%Y-%m-%dT%H:%M:%S')
        return dt.year
    except ValueError:
        return None


def render_template(players, games, matches):
    templates_dir = os.path.join(_ROOT_FILE, '../templates')
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals['getYearFromDateString'] = get_year_from_datetime_string

    template = env.get_template('test.html')

    for player in players:
        filename = os.path.join(_ROOT_FILE, '..', 'build', 
            'player_{0}.html'.format(player.name))
        with open(filename, 'w') as fh:
            fh.write(template.render(
                data = {
                    'player': players[0],
                    'matches': matches
                }
            ))
            logging.info('... rendered: {0}'.format(filename))


if __name__ == '__main__':
    logging.info('RUNNING DATA EXTRACTOR')
    players = read_player_from_json()
    games = read_games_from_json()
    matches = read_matches_from_json(players, games)
    process_matches(matches)
    render_template(players, games, matches)
    logging.info('FINISHED DATA EXTRACTOR')
