import sys
import json
import datetime
import plotly
import os
from pprint import pprint
from operator import itemgetter


root = os.path.dirname(os.path.abspath(__file__))

# r(x) = current ranking points before the match for the player Px
# e(x) = expected points for that player Px based on the old ranking points
#      = (totalpoints)/(1+10^((mediaOpponentELO-ownELO)/ELO_START_VALUE))
# r'(x) = new calculated ranking points for player Px
#       =r(x)+REGULATION_VALUE*(ownPoints-e(x))

ELO_DICT_KEY = 'ELO'
ELO_START_VALUE = 10000.0
REGULATION_VALUE = 8 # the higher the value, the more impact has the delta between expected and made points
LEVELING_VALUE = 12 # all matches are leveld to have totalpoints of X, otherwise a game where loats of points are distrubuted may have to much impact
# can be taht per game a different leveling factor must be evaluated
PARTICIPATION_VALUE = 3 # this value is added to each participation, this makes a lot of participation also positive, can be 0 if no bonus schould be given, a value higher than 0 make an inflatation




def check_point_rules(match, total_points, made_points):
    if "pointrule" in match:
        if "lowerwins" in match["pointrule"]:
            return total_points - made_points
            # return made_points
    return made_points

def start_calculation():
    # Load data
    j = json.load(open(os.path.join(root, '../data2012.json')))

    # pprint(j)

    # Sanity check of json file:
    pass
    
    #output all warnings + errors, if no error continue:
    pass


    # set members:
    for name, data in j["members"].items():
        data[ELO_DICT_KEY] = ELO_START_VALUE
        data['ELO_HISTORY'] = []
        data['MATCH_DATA'] = []


    # sort matches by date:
    pass
    # sorted_matchlist = j['matches']
    sorted_matchlist = sorted(j['matches'], key=itemgetter('time'))
    # pprint(sorted_matchlist)

    # go through all matches and iterate ELO:
    for match in sorted_matchlist:
        # print('\n----- MATCH: ' + match['time'])
        totalpoints = sum(match['result'].values())
        levelingfactor = LEVELING_VALUE / totalpoints
        totalparticipants = len(match['result'])
        totalelo = 0.0

        # get total elo value by adding all current ELOs:
        for participant in match['result']:
            totalelo += j["members"][participant][ELO_DICT_KEY]
        # print("\tTotal pts: {}, Player: {}, Total ELO: {}".format(totalpoints, totalparticipants, totalelo))

        for name, points in match['result'].items():
            ownELO = j["members"][name][ELO_DICT_KEY]
            mediaOpponentELO = (totalelo - ownELO) / (totalparticipants-1)
            expected_points = ((totalpoints*2/totalparticipants) / (1+10**((mediaOpponentELO-ownELO)/ELO_START_VALUE)))*levelingfactor
            # print("\tPlayer: {}, ELO: {}, Opp Med ELO: {}, e(x): {}, p(x): {}".\
            #     format(name, ownELO, mediaOpponentELO, expected_points, made_points))
            made_points = check_point_rules(match, totalpoints, points) * levelingfactor
            # new elo:
            newELO = ownELO + REGULATION_VALUE*(made_points-expected_points) + PARTICIPATION_VALUE
            #update data:
            j["members"][name][ELO_DICT_KEY] = newELO
            j["members"][name]['ELO_HISTORY'].append(j["members"][name][ELO_DICT_KEY])
            j["members"][name]['MATCH_DATA'].append("{}: {}, ELO: {}".\
                format(match['game'], match['result'],newELO))

        # not participated players have to get olds hisorty value:
        for name, data in j["members"].items():
            if not name in match['result']:
                j["members"][name]['ELO_HISTORY'].append(j["members"][name][ELO_DICT_KEY])
                j["members"][name]['MATCH_DATA'].append("not participated, ELO: {}".\
                    format(j["members"][name][ELO_DICT_KEY]))

    return j


def create_plot(procesedData):
    # CREATE A PLOT, Traces -> Data -> Plot
    plotdata = []
    for name, data in procesedData['members'].items():
        trace = plotly.graph_objs.Scatter(
            # x = procesedData['matches'],
            x = [i+1 for i in range(len(procesedData['matches']))],
            y = data['ELO_HISTORY'],
            name = name,
            text = data['MATCH_DATA'],
            hoverinfo = 'text',
            line = dict(
                width = 2,
                color = 'rgb(0, 0, 0)'
            )
        )
        plotdata.append(trace)
    layout = dict(title = 'WEIHERGAMES ELO CHART',
              xaxis = dict(title = 'Matches'),
              yaxis = dict(title = 'WG-ELO'),
              )
    plotly.offline.plot(
        {
            "data": plotdata,
            "layout": layout
        },
        auto_open=False,
        filename=os.path.join(root, 'builds/plot_elo_overall.html')
    )


#-------------------------------
if __name__ == "__main__":
    procesedData = start_calculation()
    create_plot(procesedData)
    pprint("SUCCESS")
    sys.exit(0)