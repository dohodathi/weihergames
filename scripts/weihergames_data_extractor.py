
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
from slugify import slugify

logging.basicConfig(level=logging.DEBUG)

_ROOT_FILE = os.path.dirname(os.path.abspath(__file__))
_IMAGE_FOLDER = os.path.join(_ROOT_FILE, '..', 'docs','images')
JSON_DATABASE = os.path.join(_ROOT_FILE, '../data2012.json')
_ALT_PLAYER_IMG = 'noun_Bear_54735.png'
_ALT_GAME_IMG = 'noun_Accessories_1485294.png'
_ALT_FIELDOFPLAY_IMG = 'noun_Lake_1479177.png'

""" ELO CALC PARAMTER """
ELO_START_VALUE = 10000.0
ELO_REGULATION_VALUE = 8 # the higher the value, the more impact has the delta between expected and made points
ELO_LEVELING_VALUE = 12 # all matches are leveld to have totalpoints of X, otherwise a game where loats of points are distrubuted may have to much impact
# can be that per game a different leveling factor must be evaluated
ELO_PARTICIPATION_VALUE = 3 # this value is added to each participation, this makes a lot of participation also positive, can be 0 if no bonus schould be given, a value higher than 0 make an inflatation

#
# template injected utils
#

def format_datetime(dt_string, date_format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if dt_string is None:
        return ""
    return datetime.strptime(dt_string, '%Y-%m-%dT%H:%M:%S').strftime(date_format)

def get_year_from_datetime_string(dt_string):
    try:
        dt = datetime.strptime(dt_string, '%Y-%m-%dT%H:%M:%S')
        return dt.year
    except ValueError:
        return None

def slugify_underscore(anyString):
    return slugify(anyString, separator="_")

#
# model utils
#

def get_relative_image_path(filename):
    return '/images/' + filename
#
# models
#

class PlayerData():
    def __init__(self, name):
        self.name = name
        self.elo = 0.0
        self.rank = 0
        self.img = None
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

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img_filename=None):
        img_path = os.path.join(_IMAGE_FOLDER, str(img_filename))
        if os.path.isfile(img_path):
            self.__img = get_relative_image_path(img_filename)
        else:
            self.__img = get_relative_image_path(_ALT_PLAYER_IMG)

class GameData():
    def __init__(self, name):
        self.name = name
        self.img = None
        self.field_of_play = ''
        self.field_of_play_icon = None
        self.pointrules = []
        self.specific_leveling_value = 0
    def __str__(self):
        return 'GameData for {0}'.format(self.name)

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img_filename):
        img_path = os.path.join(_IMAGE_FOLDER, str(img_filename))
        if os.path.isfile(img_path):
            self.__img = get_relative_image_path(img_filename)
        else:
            self.__img = get_relative_image_path(_ALT_GAME_IMG)

    @property
    def field_of_play_icon(self):
        return self.__field_of_play_icon

    @img.setter
    def field_of_play_icon(self, img_filename):
        img_path = os.path.join(_IMAGE_FOLDER, str(img_filename))
        if os.path.isfile(img_path):
            self.__field_of_play_icon = get_relative_image_path(img_filename)
        else:
            self.__field_of_play_icon = get_relative_image_path(_ALT_FIELDOFPLAY_IMG)

class MatchData():
    def __init__(self, game):
        self.game = game
        self.participants= []
        self.elos_after = [] # must have same oder as participants
        self.elos_delta = [] # must have same oder as participants
        self.result = [] # must have same oder as participants
        self.datetime = ''
        self.tie = False
        self.location = ''
        self.remarks = ''
    def __str__(self):
        return 'MatchData of [{0}] played by: {1}'.format(self.game,self.participants)

    @property
    def winner(self):
        if 'lowerwins' in self.game.pointrules:
            # LOWEST SCORE WINS:
            search_value = min(self.result)
        else:
            # HIGEHST SCORE WINS:
            search_value = max(self.result)
        # get index of result array with the highest or lowest result:
        index_of = [i for i, j in enumerate(self.result) if j == search_value]
        if len(index_of) > 1:
            self.tie = True
            return [self.participants[x] for x in index_of]
        elif len(index_of) == 1:
            return self.participants[index_of[0]]
        else:
            logging.error('NO WINNER IDENTIFIED ON: {0}'.format(self))
            return None

#
# data extraction
#

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
        p.img = data.get('img', None)
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
        g.img = data.get('img', None)
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

#
# data transformation
#

def get_matches_by_player(matches, playerName):
    playerMatches = []

    for match in matches:
        participantNames = set([p.name for p in match.participants])

        if (playerName in participantNames):
            playerMatches.append(match)

    return playerMatches

def process_matches(matches):
    """
    oldest match first,
    calculate elo of participants,
        store new elo and delta in MatchData
        store new elo in PlayerData,
    next match,
    """
    for match in matches:
        pass # TODO

#
# template rendering
#

def render_templates(players, games, matches):
    templates_dir = os.path.join(_ROOT_FILE, '../templates')
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals['getYearFromDateString'] = get_year_from_datetime_string
    env.globals['slugify'] = slugify_underscore
    env.globals['formatDateTime'] = format_datetime

    template = env.get_template('userprofile.html')

    # generate html to be embedded via iframe within the .md files
    for player in players:
        filename = os.path.join(_ROOT_FILE, '..', 'build',
            'player_{0}.html'.format(player.name.lower()))
        with open(filename, 'w') as fh:
            fh.write(template.render(
                data = {
                    'player': player,
                    'matches': get_matches_by_player(matches, player.name)
                }
            ))
            logging.info('... rendered: {0}'.format(filename))

    mdTemplate = env.get_template('test_no_embed.html')

    # generate .md files directly
    for player in players:
        filename = os.path.join(_ROOT_FILE, '..', 'docs/users/',
            'dynamic_{0}.md'.format(player.name.lower()))
        with open(filename, 'w') as fh:
            fh.write(mdTemplate.render(
                data = {
                    'player': player,
                    'matches': get_matches_by_player(matches, player.name)
                }
            ))
            logging.info('... rendered: {0}'.format(filename))


if __name__ == '__main__':
    logging.info('RUNNING DATA EXTRACTOR')
    players = read_player_from_json()
    games = read_games_from_json()
    matches = read_matches_from_json(players, games)
    process_matches(matches)
    render_templates(players, games, matches)
    logging.info('FINISHED DATA EXTRACTOR')
    logging.debug('Winner: {w}, Match {m}'.format(m=matches[-1], w=matches[-1].winner))
