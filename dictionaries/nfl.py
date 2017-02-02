"""
Prompt the user for either an NFL conference and division or the name of an NFL team.
Based on the response, return either a list of teams in that division or the name of the team's division.

>>> NFL_TEAMS = {'foo': {'bar': ['baz']}}

>>> get_teams_by_conference_and_division(NFL_TEAMS, 'foo', 'bar')
['baz']

>>> get_conference_and_division_by_team_name(NFL_TEAMS, 'baz')
('foo', 'bar')
"""


def get_teams_by_conference_and_division(league, conference, division):
    print(league[conference][division])
    return league[conference][division]


def get_conference_and_division_by_team_name(league, team_name):
    for conf, divisions in league.items():
        for div, teams in divisions.items():
            for team in teams:
                if team_name in team:
                    print(conf, div)
                    return conf, div


def main():
    """Prompt for user input, get a result from the data, print a nicely formatted answer"""
    user_input = input("Enter the name of either a conference (AFC or NFC) or team. >>  ")
    return user_input


def run_program(league):
    user_input = main()

    if user_input in ('AFC', 'NFC'):
        division = input("In which division? >>  ")
        get_teams_by_conference_and_division(league, user_input, division)

    else:
        get_conference_and_division_by_team_name(league, user_input)


if __name__ == '__main__':
    NFL_TEAMS = {
        'AFC': {
            'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
            'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
            'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
            'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
        },
        'NFC': {
            'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
            'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
            'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
            'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
        }
    }

    run_program(NFL_TEAMS)
