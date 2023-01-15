import csv
import matplotlib.pyplot as plt

def calculate(matches,deliveries):
        
    match_data=[]
    deliveries_data=[]
    with open(matches, 'r') as file:
            match_reader = csv.DictReader(file)

            for match in match_reader:
                    match_data.append(match)
    
    with open(deliveries, 'r') as file:
            delivery_reader = csv.DictReader(file)
            for delivery in delivery_reader:
                    deliveries_data.append((delivery))
        
    runsperteam = []
    matchids = []
    for details in match_data:
        if details['season'] == '2016':
            matchids.append(details['id'])
    print(matchids)
    teams = set()
    for details in  deliveries_data:
        if details['match_id'] in matchids:
            teams.add(details['bowling_team'])
    teams = sorted(list(teams))
    runsperteam = [0]*len(teams)
    teams_extraruns = dict(zip(teams, runsperteam))

    for details in  deliveries_data:
        if details['bowling_team'] in teams_extraruns.keys() and details['match_id'] in matchids:
            teams_extraruns[details['bowling_team']
                            ] += int(details['extra_runs'])

    return teams_extraruns


def plot(teams,runsperteam):
    fig, ax = plt.subplots()
    blabels = teams
    ax.barh(blabels, runsperteam, label=blabels, color='green')

    ax.set_ylabel('Runsperteam')
    ax.set_title('Teams')
    plt.show()

                                 
seasonsandmatches=calculate("mock_matches2.csv", "mock_deliveries2.csv")
print(seasonsandmatches)
players=list(seasonsandmatches.keys())
runs=list(seasonsandmatches.values())
plot(players,runs)