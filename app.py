import constants
import copy

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
panthers = players[:6]
bandits = players[6:12]
warriors = players[12:]
# deepcopy method is needed for compound objects.https://docs.python.org/3/library/copy.html

def main_menu():
    print("***Basketball Team Stats Tool***\n\n")
    print(".....Main Menu.....\n\n")
    print("1. Display Teams\n2. Quit\n")
    while True:
        option = input("Please choose 1 or 2. ")
        try:
            if option != '1' and option != '2':
                raise ValueError("Try again!")
        
        except ValueError as err:
            print("That is an invalid option")
            print(err)
        
        else:
            break
    
    return option


def teams_menu():
    print("\n--Teams Menu--\n")
    print("1.Panthers\n2.Bandits\n3.Warriors\nEnter \"b\" to go back")
    while True:
        option = input("Please choose an option. ")
        try:
            if option != '1' and option != '2' and option != '3' and option != 'b':
                raise ValueError("Try again!")
        
        except ValueError as err:
            print("That is an invalid option")
            print(err)
        
        if option == '1':
            print_team_stats("Panthers", panthers)
            
        elif option == '2':
            print_team_stats("Bandits", bandits)
            
        elif option == '3':
            print_team_stats("Warriors", warriors)
        
        elif option == 'b':
            break

    return option
     

def get_exp():
    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False


def get_height():
    for player in players:
        player['height'] = int(player['height'].split()[0])

def print_team_stats(team_name, team):
    player_names = []
    print("\n{}\nTotal players: {}".format(team_name, len(bandits)))
    for player in team:
        player_names.append(player['name'])
    print(", ".join(player_names))


if __name__ == "__main__":
    get_exp()
    get_height()
    user_option = main_menu()
    while user_option != '2':
        team_option = None
        while team_option != 'b':
            team_option = teams_menu()
        user_option = main_menu()
    
    

    
    
    
    