"""
Voting Booth

"""

from pprint import pprint as pp

def vote():
    votes = dict()
    voting = True
    while voting:
        voter_input = input("Who would you like to vote for? : Enter a name here or type 'done' >>> ")

        if voter_input == 'done':
            pp(max(votes.items(), key=lambda t: t[1]))
            exit()
        try:
            votes[voter_input] += 1
        except KeyError:
            votes[voter_input] = 1

    pp(votes)

vote()
    # vote[voter_input] = vote.get(voter_input, 0) + 1 #Boolean, checks for key, then assigns new dict item, adds 1.
    # try:
    #     votes['phillip'] += 1
    # except KeyError:
    #     votes['phillip'] = 1
    #
    #     {k: v for k, v in enumerate(range(11))}
    #
    # name = input("What's the name of the person you are voting for?")
    # votes.update((name: votes.get(name, +=1)))
