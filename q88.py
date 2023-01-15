import csv
import matplotlib.pyplot as plt


def calculate(matches, deliveries):
    '''For calculating'''
    match_data = []
    deliveries_data = []
    with open(matches, 'r') as file:
        matchreader = csv.DictReader(file)

        for match in matchreader:
            match_data.append(match)

    with open(deliveries, 'r') as file:
        delivery_reader = csv.DictReader(file)
        for delivery in delivery_reader:
            deliveries_data.append((delivery))
    matchids = []
    for match in match_data:
        if match['season'] == '2015':
            matchids.append(match['id'])

    bowlerslist = set()
    for delivery in deliveries_data:

        if delivery['match_id'] in matchids:
            bowlerslist.add(delivery['bowler'])
    bowlerslist = sorted(list(bowlerslist))
    runsgiven = [0]*len(bowlerslist)
    bowler_runs = dict(zip(bowlerslist, runsgiven))


    for delivery in deliveries_data:
        if delivery['bowler'] in bowler_runs.keys() and delivery['match_id'] in matchids:
            bowler_runs[delivery['bowler']] += int(delivery['total_runs'])
  

    sorted_bowler_runs = {key: value for key, value in sorted(
        bowler_runs.items(), key=lambda item: item[1])}

    return sorted_bowler_runs

    # worstbowlers=(list(sorted_dict.values()))
    # totalruns=(list(sorted_dict.keys()))
    # print( worstbowlers.reverse() , totalruns.reverse())


def plot(players, runsgiven):
    fig, ax = plt.subplots()

    blabels = players[-10:]

    ax.bar(blabels,    runsgiven[-10:], label=blabels, color='red')

    ax.set_ylabel('Total runs')
    ax.set_title('Top 10 economical bowlers in the year 2015')
    # ax.legend(title='Teams')
    plt.show()


sorted_bowler_runs = calculate("mock_matches2.csv", "mock_deliveries2.csv")
print(sorted_bowler_runs)
players = list(sorted_bowler_runs.keys())
runs = list(sorted_bowler_runs.values())
plot(players, runs)
