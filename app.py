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
        if option == '1':
            teams_menu()
            continue
        elif option == '2':
            print("Goodbye!")
            break


def teams_menu():
    new_panthers = []
    new_bandits = []
    new_warriors = []
    print("\n--Teams Menu--\n")
    print("1.Panthers\n2.Bandits\n3.Warriors\n")
    while True:
        option = input("Please choose an option. ")
        try:
            if option != '1' and option != '2' and option != '3':
                raise ValueError("Try again!")
        except ValueError as err:
            print("That is an invalid option")
            print(err)
        if option == '1':
            print("\nPanthers\nTotal players: {}".format(len(panthers)))
            for player in panthers:
                new_panthers.append(player['name'])
            print(", ".join(new_panthers))
            back_to_main()
            break
        elif option == '2':
            print("\nBandits\nTotal players: {}".format(len(bandits)))
            for player in bandits:
                new_bandits.append(player['name'])
            print(", ".join(new_bandits))
            back_to_main()
            break
        elif option == '3':
            print("\nWarriors\nTotal players: {}".format(len(warriors)))
            for player in warriors:
                new_warriors.append(player['name'])
            print(", ".join(new_warriors))
            back_to_main()
            break


def back_to_main():
    print("\n1.Main Menu\n2.Teams Menu\n3.Quit")
    while True:
        option = input("\nWhat would you like to do? ")
        if option == '1':
            main_menu()
        elif option == '2':
            teams_menu()
        elif option == '3':
            print("Goodbye!")
            break 
            
def get_exp():
    for player in players:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False


def get_height():
    for player in players:
        player['height'] = int(player['height'].split()[0])


if __name__ == "__main__":
    get_exp()
    get_height()
    main_menu()
    
    
    
    