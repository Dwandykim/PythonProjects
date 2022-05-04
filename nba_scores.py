from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"
#TO DO: look up other data (all-time data) 

printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()  # think of json as a python dictionary
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']
    

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        # Visualization component, instaed of console interface 
        print("--------------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")


get_scoreboard()