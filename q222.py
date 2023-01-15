import csv
import matplotlib.pyplot as plt


def calculate(matches, deliveries):
    topplayers = set()

    for player in deliveries:
        if player['batting_team'] == 'Royal Challengers Bangalore':
            topplayers.add(player['batsman'])
    topplayers = list(topplayers)
    runsscored = [0]*len(topplayers)
    players_and_runs = dict(zip(topplayers, runsscored))
    for player in deliveries:
        if player['batsman'] in players_and_runs.keys():
            players_and_runs[player['batsman']] += int(player['batsman_runs'])
    sorted_players_and_runs = {key: value for key, value in sorted(
        players_and_runs.items(), key=lambda item: item[1])}
    print(sorted_players_and_runs)
    return sorted_players_and_runs


def plot(players, runs):
    fig, aux = plt.subplots()

    blabels = players

    aux.bar(blabels, runs, label=blabels, color='red')

    aux.set_ylabel('Total runs')
    aux.set_title('max runs scored by each team')
    # ax.legend(title='Teams')

    plt.show()


match_data = []
deliveries_data = []
with open("mock_matches2.csv", 'r') as file:
    matches = csv.DictReader(file)

    for match in matches:
        match_data.append(match)

with open("mock_deliveries2.csv", 'r') as file:
    deliveries = csv.DictReader(file)
    for delivery in deliveries:
        deliveries_data.append((delivery))

players_and_runs = calculate(match_data, deliveries_data)

players = list(players_and_runs.keys())[-10:]
runs = list(players_and_runs.values())[-10:]
plot(players, runs)
