from ast import While
import numbers
from selectors import EpollSelector
from bs4 import BeautifulSoup
import requests

url = "https://www.landofbasketball.com/championships/year_by_year.htm"
teams_url = "https://www.landofbasketball.com/nba_teams.htm"


def champions_yby():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    main_tables = soup.find_all('div', class_ = "color-alt a-center max-0")

    # extracted the nba champions year by year data ; complete
    lst = []
    for i in range(1,len(main_tables)):
        main_table = main_tables[i]
        
        tags = main_table.find_all('div', class_ ="pad-5 clearfix")
        for i in range(len(tags)):
            yearly_lst = []
            tag = tags[i]
            text = tag.find_all("a")
            for i in range(len(text)):
                yearly_lst.append(text[i].string)
            score = tag.find('div', class_ = "rd-100 margen-r5").string
            yearly_lst.insert(2,score)
            lst.append(yearly_lst)
    
    return lst  # returning list of lists comprised of [year, winner, score, loser, Finals MVP, Season MVP]


def display_champs(lst, num = 6):
    new_lst = [['Year', 'Score', 'Winner', 'Loser', 'Finals MVP', 'Season MVP']] + lst
    
    for i in range(num):
        print(new_lst[i])

def get_teams_lst():
    result = requests.get(teams_url)
    doc = BeautifulSoup(result.text, 'html.parser')
    body_doc = doc.find_all('div', class_ = "left margen-l2 negri")

    team_lst = []
    for body in body_doc:
        team_lst.append(body.string)
    return team_lst

def get_teams_dict(nba_team_lst):
    team_lst_keys = []
    for team in nba_team_lst:
        x = team.replace(" ", "_").lower()
        team_lst_keys.append(x)
    
    nba_teams_dict = dict(zip(nba_team_lst, team_lst_keys))
        
    return nba_teams_dict    
    
def get_teams_keys(nba_teams_dict, selected_team):
    
    nba_team = nba_teams_dict[selected_team]
    return nba_team

def get_retired_jerseys(team_url):
    # messy code 
    result = requests.get(team_url)
    soup1 = BeautifulSoup(result.text, 'html.parser')
    retired_jersey = soup1.find_all('div', class_ = "margen-l2 margen-r2") 
    retired_jersey = retired_jersey[0]
    datas = retired_jersey.find_all("tr")
    data_set = datas[1]
    data_set.find("p").text
    a = data_set.find("p").text
    new_a = a.replace('.','  -') 

    new_a = new_a.split('\t\n')
    new_a.pop()
    print(new_a)

def main():
    print("Hello this is a repository of NBA chamnpions year by year!")
    
    lst = champions_yby()
    display_champs(lst)
    
    while True:
        more_output = str(input("Do you want to see more NBA champions by year? Please enter Yes or No: ")).lower()
        if more_output == "yes":
            how_much_output = int(input("How many more years do you want to see? "))
            # work in progress
            num = 6 + how_much_output
            display_champs(lst, num)
        
        elif more_output == "no":
            break   
        else:
            more_output
    
    get_teams_url = str(input("Would you like to look at the retired jersey numbers of a NBA team? [Yes/No]: ")).lower()
    if get_teams_url == "yes":
        nba_team_lst = get_teams_lst()
        print(nba_team_lst)
        select_team = str(input("Please select a team [type in as shown]: "))

        teams_dict = get_teams_dict(nba_team_lst)
        selected_team = get_teams_keys(teams_dict, select_team)

        team_url = "https://www.landofbasketball.com/teams/" + selected_team + ".htm"
        retired_jerseys = get_retired_jerseys(team_url)
        
    elif get_teams_url == "no":
        pass

main()



