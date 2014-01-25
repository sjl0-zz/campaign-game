"""
A text-input based game where users campaign to win the presidency. Computer 
randomly decides how to allocate (fairly) each state originally as a state which 
leans to the player, is a swing state, or towards the computer. Player takes 
actions to "campaign" which state "voters" respond to. Implements a basic AI that 
uses a queue to determine where to campaign. 

Instructions:
Each turn, a play will pick a state to campaign in. In each state, players take 
one of three action which effet various voting groups differently. After all turns
have been taken, undecided voters make up their minds and the canidate with
270 votes is declared the winner!

To play game, run Campaign.py and type game()

Note: Color codes only work when printed to a Mac terminal. Otherwise, the 
information will still be there, just without the helpful colors. When the 
map is printed, the percentage of vote player 1 has is listed first, followed
by the percentage of vote player 2 or the computer has.
"""

import random
import math
import collections

def game():
    print "Welcome to Campaign Game!"
    number = number_of_players()
    player = raw_input("Player 1, what is your name? ")
    if player == '':
        player = raw_input("You don't have a name? Type a name or press enter to be called 'Player'. ")
    if player == '':
        player = 'Player'
    party_name, party = get_party(player)
    party_name, player = name_correct(party_name, player)

    auto = False
    if number == '1':
        auto = True
        action_text = {'1' : " bought a campaign ad ", '2' : " held a rally ", '3' : " went door to door "}
        comp_state_tries = {}
    party_colors = {'R' : 'red', 'D' : 'blue', 'L' : 'yellow', 'G' : 'green', 'O' : 'black'}
    party_choices = ['Democratic'] * 8 + ['Republican'] * 8 + ['Libertarian', 'Green']
    if auto:
        opponent = random.choice(["Jeff", "Alejandra", "Rixner", "Compy", "Devika", "Berta", "Elly", "Fergie", "Georgie the Gorilla", "Helga", "Iggy", "Kelvin the Kangaroo", "Ludwig", "Magical Merlin", "No Nonsense Norm", "Oprah", "Percy", "Quillan", "Sammy the Owl", "The Tenacious Terrapin", "Yurtle the Turtle", "Ursula", "Vernon", "Walt Disney", "Mr. X", "Zia the Zebra"])
        opposing = party_name
        while opposing == party_name:
            opposing = random.choice(party_choices)
        print color_text("Your opponent is " + opponent + " and is from the " + opposing + " party.", party_colors[opposing[0]])
    else:
        opponent = raw_input("Player 2, what is your name? ")
        if opponent == '':
            opponent = raw_input("You don't have a name? Type a name or press enter to be called 'Player 2'. ")
        if opponent == '':
            opponent = 'Player 2'
        party_2 = party
        a = 0
        while party_2 == party:
            if a > 0:
                print "I'm sorry, the " + party_name + " party has nominated " + player + " as their canidate. Please pick a different party."
            a += 1
            opposing, party_2 = get_party(opponent)
        opposing, opponent = name_correct(opposing, opponent)

    print player + " will go first."
    enter()
    id = {opponent : opposing, player : party_name, 'swing' : 'swing'}
    data = {'Alabama': {'abbr': 'AL',
  'elec. votes': 9,
  'population': 4779736,
  'turnout': {'overall': 0.55},
  'voters': 2628855},
 'Alaska': {'abbr': 'AK',
  'elec. votes': 3,
  'population': 710231,
  'turnout': {'overall': 0.615},
  'voters': 436792},
 'Arizona': {'abbr': 'AZ',
  'elec. votes': 11,
  'population': 6392017,
  'turnout': {'overall': 0.49700000000000005},
  'voters': 3176832},
 'Arkansas': {'abbr': 'AR',
  'elec. votes': 6,
  'population': 2915918,
  'turnout': {'overall': 0.469},
  'voters': 1367566},
 'California': {'abbr': 'CA',
  'elec. votes': 55,
  'population': 37253956,
  'turnout': {'overall': 0.555},
  'voters': 20675946},
 'Colorado': {'abbr': 'CO',
  'elec. votes': 9,
  'population': 5029196,
  'turnout': {'overall': 0.635},
  'voters': 3193539},
 'Connecticut': {'abbr': 'CT',
  'elec. votes': 7,
  'population': 3574097,
  'turnout': {'overall': 0.6090000000000001},
  'voters': 2176625},
 'Delaware': {'abbr': 'DE',
  'elec. votes': 3,
  'population': 897934,
  'turnout': {'overall': 0.5940000000000001},
  'voters': 533373},
 'District of Columbia': {'abbr': 'DC',
  'elec. votes': 3,
  'population': 601723,
  'turnout': {'overall': 0.539},
  'voters': 324329},
 'Florida': {'abbr': 'FL',
  'elec. votes': 29,
  'population': 18801310,
  'turnout': {'overall': 0.61},
  'voters': 11468799},
 'Georgia': {'abbr': 'GA',
  'elec. votes': 16,
  'population': 9687653,
  'turnout': {'overall': 0.55},
  'voters': 5328209},
 'Hawaii': {'abbr': 'HI',
  'elec. votes': 4,
  'population': 1360301,
  'turnout': {'overall': 0.43700000000000006},
  'voters': 594452},
 'Idaho': {'abbr': 'ID',
  'elec. votes': 4,
  'population': 1567582,
  'turnout': {'overall': 0.5750000000000001},
  'voters': 901360},
 'Illinois': {'abbr': 'IL',
  'elec. votes': 20,
  'population': 12830632,
  'turnout': {'overall': 0.564},
  'voters': 7236476},
 'Indiana': {'abbr': 'IN',
  'elec. votes': 11,
  'population': 6483802,
  'turnout': {'overall': 0.535},
  'voters': 3468834},
 'Iowa': {'abbr': 'IA',
  'elec. votes': 6,
  'population': 3046355,
  'turnout': {'overall': 0.632},
  'voters': 1925296},
 'Kansas': {'abbr': 'KS',
  'elec. votes': 6,
  'population': 2835118,
  'turnout': {'overall': 0.561},
  'voters': 1590501},
 'Kentucky': {'abbr': 'KY',
  'elec. votes': 8,
  'population': 4339367,
  'turnout': {'overall': 0.519},
  'voters': 2252131},
 'Louisiana': {'abbr': 'LA',
  'elec. votes': 8,
  'population': 4533372,
  'turnout': {'overall': 0.557},
  'voters': 2525088},
 'Maine': {'abbr': 'ME',
  'elec. votes': 4,
  'population': 1328361,
  'turnout': {'overall': 0.657},
  'voters': 872733},
 'Maryland': {'abbr': 'MD',
  'elec. votes': 10,
  'population': 5773552,
  'turnout': {'overall': 0.612},
  'voters': 3533414},
 'Massachusetts': {'abbr': 'MA',
  'elec. votes': 11,
  'population': 6547629,
  'turnout': {'overall': 0.5970000000000001},
  'voters': 3908935},
 'Michigan': {'abbr': 'MI',
  'elec. votes': 16,
  'population': 9883640,
  'turnout': {'overall': 0.6240000000000001},
  'voters': 6167391},
 'Minnesota': {'abbr': 'MN',
  'elec. votes': 10,
  'population': 5303925,
  'turnout': {'overall': 0.715},
  'voters': 3792306},
 'Mississippi': {'abbr': 'MS',
  'elec. votes': 6,
  'population': 2967297,
  'turnout': {'overall': 0.546},
  'voters': 1620144},
 'Missouri': {'abbr': 'MO',
  'elec. votes': 10,
  'population': 5988927,
  'turnout': {'overall': 0.618},
  'voters': 3701157},
 'Montana': {'abbr': 'MT',
  'elec. votes': 3,
  'population': 989415,
  'turnout': {'overall': 0.601},
  'voters': 594638},
 'Nebraska': {'abbr': 'NE',
  'elec. votes': 5,
  'population': 1826341,
  'turnout': {'overall': 0.5650000000000001},
  'voters': 1031883},
 'Nevada': {'abbr': 'NV',
  'elec. votes': 6,
  'population': 2700551,
  'turnout': {'overall': 0.517},
  'voters': 1396185},
 'New Hampshire': {'abbr': 'NH',
  'elec. votes': 4,
  'population': 1316470,
  'turnout': {'overall': 0.652},
  'voters': 858338},
 'New Jersey': {'abbr': 'NJ',
  'elec. votes': 14,
  'population': 8791894,
  'turnout': {'overall': 0.5990000000000001},
  'voters': 5266345},
 'New Mexico': {'abbr': 'NM',
  'elec. votes': 5,
  'population': 2059179,
  'turnout': {'overall': 0.536},
  'voters': 1103720},
 'New York': {'abbr': 'NY',
  'elec. votes': 29,
  'population': 19379102,
  'turnout': {'overall': 0.512},
  'voters': 9922100},
 'North Carolina': {'abbr': 'NC',
  'elec. votes': 15,
  'population': 9525483,
  'turnout': {'overall': 0.595},
  'voters': 5667662},
 'North Dakota': {'abbr': 'ND',
  'elec. votes': 3,
  'population': 672591,
  'turnout': {'overall': 0.59},
  'voters': 396829},
 'Ohio': {'abbr': 'OH',
  'elec. votes': 18,
  'population': 11536504,
  'turnout': {'overall': 0.606},
  'voters': 6991121},
 'Oklahoma': {'abbr': 'OK',
  'elec. votes': 7,
  'population': 3751351,
  'turnout': {'overall': 0.503},
  'voters': 1886930},
 'Oregon': {'abbr': 'OR',
  'elec. votes': 7,
  'population': 3831074,
  'turnout': {'overall': 0.615},
  'voters': 2356111},
 'Pennsylvania': {'abbr': 'PA',
  'elec. votes': 20,
  'population': 12702379,
  'turnout': {'overall': 0.5790000000000001},
  'voters': 7354677},
 'Rhode Island': {'abbr': 'RI',
  'elec. votes': 4,
  'population': 1052567,
  'turnout': {'overall': 0.559},
  'voters': 588385},
 'South Carolina': {'abbr': 'SC',
  'elec. votes': 9,
  'population': 4625364,
  'turnout': {'overall': 0.518},
  'voters': 2395939},
 'South Dakota': {'abbr': 'SD',
  'elec. votes': 3,
  'population': 814180,
  'turnout': {'overall': 0.5770000000000001},
  'voters': 469782},
 'Tennessee': {'abbr': 'TN',
  'elec. votes': 11,
  'population': 9346105,
  'turnout': {'overall': 0.508},
  'voters': 4747821},
 'Texas': {'abbr': 'TX',
  'elec. votes': 38,
  'population': 25145561,
  'turnout': {'overall': 0.48200000000000004},
  'voters': 12120160},
 'Utah': {'abbr': 'UT',
  'elec. votes': 6,
  'population': 2763885,
  'turnout': {'overall': 0.473},
  'voters': 1307318},
 'Vermont': {'abbr': 'VT',
  'elec. votes': 3,
  'population': 625741,
  'turnout': {'overall': 0.601},
  'voters': 376070},
 'Virginia': {'abbr': 'VA',
  'elec. votes': 13,
  'population': 8001024,
  'turnout': {'overall': 0.612},
  'voters': 4896627},
 'Washington': {'abbr': 'WA',
  'elec. votes': 12,
  'population': 6724540,
  'turnout': {'overall': 0.6070000000000001},
  'voters': 4081796},
 'West Virginia': {'abbr': 'WV',
  'elec. votes': 5,
  'population': 1852994,
  'turnout': {'overall': 0.549},
  'voters': 1017294},
 'Wisconsin': {'abbr': 'WI',
  'elec. votes': 10,
  'population': 5686989,
  'turnout': {'overall': 0.663},
  'voters': 3770474},
 'Wyoming': {'abbr': 'WY',
  'elec. votes': 3,
  'population': 563626,
  'turnout': {'overall': 0.588},
  'voters': 331412}}
    abbr_dict = {'AK': 'Alaska',
 'AL': 'Alabama',
 'AR': 'Arkansas',
 'AZ': 'Arizona',
 'CA': 'California',
 'CO': 'Colorado',
 'CT': 'Connecticut',
 'DC': 'District of Columbia',
 'DE': 'Delaware',
 'FL': 'Florida',
 'GA': 'Georgia',
 'HI': 'Hawaii',
 'IA': 'Iowa',
 'ID': 'Idaho',
 'IL': 'Illinois',
 'IN': 'Indiana',
 'KS': 'Kansas',
 'KY': 'Kentucky',
 'LA': 'Louisiana',
 'MA': 'Massachusetts',
 'MD': 'Maryland',
 'ME': 'Maine',
 'MI': 'Michigan',
 'MN': 'Minnesota',
 'MO': 'Missouri',
 'MS': 'Mississippi',
 'MT': 'Montana',
 'NC': 'North Carolina',
 'ND': 'North Dakota',
 'NE': 'Nebraska',
 'NH': 'New Hampshire',
 'NJ': 'New Jersey',
 'NM': 'New Mexico',
 'NV': 'Nevada',
 'NY': 'New York',
 'OH': 'Ohio',
 'OK': 'Oklahoma',
 'OR': 'Oregon',
 'PA': 'Pennsylvania',
 'RI': 'Rhode Island',
 'SC': 'South Carolina',
 'SD': 'South Dakota',
 'TN': 'Tennessee',
 'TX': 'Texas',
 'UT': 'Utah',
 'VA': 'Virginia',
 'VT': 'Vermont',
 'WA': 'Washington',
 'WI': 'Wisconsin',
 'WV': 'West Virginia',
 'WY': 'Wyoming'}
    if auto:
        for state in data.keys():
            comp_state_tries[state] = 0
    pop_tot = 308745538
    human_votes, comp_votes, swing_votes = 0, 0, 0
    states_list, mutatable_states_list = [], []
    for k in data.keys(): states_list.append(k)
    for l in states_list: mutatable_states_list.append(l)
    comp_states, human_states, neutral, comp_states_power, human_states_power = [], [], [], 0, 0
    while human_states_power < 165:
        new_state = random.choice(mutatable_states_list)
        state_elec_value = data[new_state]['elec. votes']
        if human_states_power + state_elec_value < 175:
            human_states.append(new_state)
            human_states_power += state_elec_value
            mutatable_states_list.remove(new_state)
    while comp_states_power < 165:
        new_state = random.choice(mutatable_states_list)
        state_elec_value = data[new_state]['elec. votes']
        if comp_states_power + state_elec_value < 175:
            comp_states.append(new_state)
            comp_states_power += state_elec_value
            mutatable_states_list.remove(new_state)
    neutral = mutatable_states_list
    neutral_power = 538 - comp_states_power - human_states_power
    totals_dict = {'elec. votes' : {player : human_states_power, opponent : comp_states_power, 'swing' : neutral_power}, '%' : {}}
    reverse_party_colors = reverse_dict(party_colors)
    for s in range(len(human_states)): 
        # A state is considered to be possessed if there is greater than a 2% difference in the
        # vote unless the number of swing voters is 10% or greater
        state = data[human_states[s]]
        state['color'] = party_colors[party]
        state['leans'] = player
        neu_num = random.choice(range(4) * 3 + range(4, 10)) * .01
        state['pop. vote %'] = {}
        state['pop. vote %']['swing'] = neu_num
        min = math.trunc(round(((1 - neu_num) / 2 + .01) * 100, 0))
        pla_num = random.choice(range(min, 57) * 3 + range(57, 73)) * .01
        while math.fabs(1 - 2 * pla_num - neu_num) < .03:
            neu_num = random.choice(range(4) * 3 + range(4, 10)) * .01
        state['pop. vote %'][player] = pla_num
        state['pop. vote %'][opponent] = 1 - pla_num - neu_num
        if s < (len(human_states) / 3):
            state['change constant'] = '2'
        # A change constant of '1' means the people of the state are likely to change and 
        # '3' means they are unlikely to change.
        elif (len(human_states) / 3) <= s < (2 * len(human_states) / 3):
            state['change constant'] = '1'
        else:
            state['change constant'] = '3'
        state['pop. vote'] = {player : math.trunc(round(pla_num * state['voters'])), opponent : math.trunc(round(state['pop. vote %'][opponent] * state['voters'])), 'swing' : math.trunc(round(neu_num * state['voters']))}
        not_voting = state['population'] - state['voters']
        player_reg_not_voting = random.choice(range(not_voting))
        comp_reg_not_voting = random.randrange(not_voting - player_reg_not_voting)
        state['party registration'] = {player : state['pop. vote'][player] + player_reg_not_voting, opponent : state['pop. vote'][opponent] + comp_reg_not_voting, 'swing' : state['pop. vote']['swing'] + not_voting - player_reg_not_voting - comp_reg_not_voting}
        data = get_turnout(data, human_states[s], player, opponent)
        state['color code'] = color_state(human_states[s], state['color'], data, player, opponent)
    for t in range(len(comp_states)):
        state = data[comp_states[t]]
        state['color'] = party_colors[opposing[0]]
        state['leans'] = opponent
        neu_num = random.choice(range(4) * 3 + range(4, 10)) * .01
        state['pop. vote %'] = {}
        state['pop. vote %']['swing'] = neu_num
        min = math.trunc(round(((1 - neu_num) / 2 + .01) * 100, 0))
        comp_num = random.choice(range(min, 57) * 3 + range(57, 73)) * .01
        while math.fabs(1 - 2 * comp_num - neu_num) < .03:
            neu_num = random.choice(range(4) * 3 + range(4, 10)) * .01
        state['pop. vote %'][opponent] = comp_num
        state['pop. vote %'][player] = 1 - comp_num - neu_num
        if t < (len(human_states) / 3):
            state['change constant'] = '2'
        elif (len(human_states) / 3) <= t < (2 * len(human_states) / 3):
            state['change constant'] = '1'
        else:
            state['change constant'] = '3'
        state['pop. vote'] = {player : math.trunc(round(state['pop. vote %'][player] * state['voters'])), opponent : math.trunc(round(state['pop. vote %'][opponent] * state['voters'])), 'swing' : math.trunc(round(neu_num * state['voters']))}
        not_voting = state['population'] - state['voters']
        player_reg_not_voting = random.randrange(not_voting)
        comp_reg_not_voting = random.randrange(not_voting - player_reg_not_voting)
        state['party registration'] = {player : state['pop. vote'][player] + player_reg_not_voting, opponent : state['pop. vote'][opponent] + comp_reg_not_voting, 'swing' : state['pop. vote']['swing'] + not_voting - player_reg_not_voting - comp_reg_not_voting}
        data = get_turnout(data, comp_states[t], player, opponent)
        state['color code'] = color_state(comp_states[t], state['color'], data, player, opponent)
    for u in range(len(neutral)):
    # A swing state is one where the vote between the computer and the human is less than 2.1%
        state = data[neutral[u]]
        state['color'] = 'purple'
        state['leans'] = 'swing'
        players = [player, opponent]
        minority = random.choice(players)
        players.remove(minority)
        minor_num = random.randrange(44, 50) * .01
        swing = random.choice([0, .01, .02])
        major_num = minor_num + swing
        swing_num = 1 - major_num - minor_num
        state['pop. vote %'] = {}
        state['pop. vote %']['swing'] = swing_num
        state['pop. vote %'][minority] = minor_num
        state['pop. vote %'][players[0]] = major_num
        if u < (len(human_states) / 4):
            state['change constant'] = '2'
        elif (len(human_states) / 4) <= u < (3 * len(human_states) / 4):
            state['change constant'] = '3'
        else:
            state['change constant'] = '1'
        state['pop. vote'] = {minority : math.trunc(round(minor_num * state['voters'])), players[0] : math.trunc(round(major_num * state['voters'])), 'swing' : math.trunc(round(swing_num * state['voters']))}
        not_voting = state['population'] - state['voters']
        player_reg_not_voting = random.randrange(not_voting)
        comp_reg_not_voting = random.randrange(not_voting - player_reg_not_voting)
        state['party registration'] = {player : state['pop. vote'][player] + player_reg_not_voting, opponent : state['pop. vote'][opponent] + comp_reg_not_voting, 'swing' : state['pop. vote']['swing'] + not_voting - player_reg_not_voting - comp_reg_not_voting}
        data = get_turnout(data, neutral[u], player, opponent)
        state['color code'] = color_state(neutral[u], 'purple', data, player, opponent)
    totals_dict['%'][player], totals_dict['%'][opponent], totals_dict['%']['swing'] = tally_votes(pop_tot, player, opponent, data)
    print "\nHere's the current standing! \n" + state_map(data, party_colors, opponent, opposing, player, party, totals_dict)
    if auto:
        comp_axn_queue = collections.deque(get_comp_queue(neutral, human_states, data, player, opponent))
        hold = []
    turns = 0
    total_turns = random.randrange(10, 30)
    # The maximum number of tries the computer should try to change a state is 10% of its turns
    max_num = math.trunc(total_turns * .1)
    while turns < total_turns:
        before = []
        after = []
        if auto:
            before_lean = []
            after_lean = []
        enter()
        # Player takes turn
        print player + "'s turn! " + str(total_turns - turns) + " turns left!"
        campaign_state, player_action = campaign(data, player, party, opponent, opposing, totals_dict, party_colors, abbr_dict, id)
        before.append(data[campaign_state]['color code'])
        # Player 2 or Computer takes turn
        enter()
        print '\n' + opponent + "'s turn!"
        if auto:
            campaign_state_2 = comp_axn_queue.popleft()
            comp_state_tries[campaign_state_2] += 1
            player_2_action = computer_action(data, opponent, campaign_state_2)
            print opponent + action_text[player_2_action] + "in " + campaign_state_2
            enter()
        else:    
            campaign_state_2, player_2_action = campaign(data, opponent, opposing, player, party , totals_dict, party_colors, abbr_dict, id)
        before.append(data[campaign_state_2]['color code'])
        # Player's action is performed
        data = perform_action(player_action, player, opponent, data, campaign_state)
        # Computer's action is performed
        data = perform_action(player_2_action, opponent, player, data, campaign_state_2)
        # Changes are tracked
        if auto:
            before_lean.append(data[campaign_state]['leans'])
            before_lean.append(data[campaign_state_2]['leans'])
        # Data is updated for each
        data = update_data(data, campaign_state, player, opponent, party_colors, id)
        data = update_data(data, campaign_state_2, player, opponent, party_colors, id)
        totals_dict['elec. votes'], change = update_electoral_count(data, player, opponent, totals_dict['elec. votes'])
        totals_dict['%'][player], totals_dict['%'][opponent], totals_dict['%']['swing'] = tally_votes(pop_tot, player, opponent, data)
        after.append(data[campaign_state]['color code'])
        after.append(data[campaign_state_2]['color code'])
        if auto:
            if len(comp_axn_queue) == 0:
                comp_axn_queue.append(random.choice(data.keys()))
            after_lean.append(data[campaign_state]['leans'])
            after_lean.append(data[campaign_state_2]['leans'])
            if before_lean[1] == after_lean[1] or data[campaign_state_2]['leans'] == 'swing':
                if comp_state_tries[campaign_state_2] < max_num:
                    comp_axn_queue.appendleft(campaign_state_2)
            if before_lean[0] != after_lean[0]:
                if data[campaign_state]['leans'] == opponent:
                    if campaign_state in comp_axn_queue:
                        comp_axn_queue.remove(campaign_state)
                if comp_state_tries[campaign_state] < max_num:
                    hold.append(campaign_state)
            for n in hold:
                if data[n]['elec. votes'] > data[comp_axn_queue[0]]['elec. votes'] and data[n]['leans'] != opponent:
                    if n in comp_axn_queue:
                        comp_axn_queue.remove(n)
                    comp_axn_queue.appendleft(n)
                    hold.remove(n)
        report_changes(before, after, change, player, opponent, totals_dict)
        turns += 1
    enter()
    data, before, after = game_end(data, player, opponent, party_colors, id)
    totals_dict['elec. votes'], change = update_electoral_count(data, player, opponent, totals_dict['elec. votes'])
    totals_dict['%'][player], totals_dict['%'][opponent], totals_dict['%']['swing'] = tally_votes(pop_tot, player, opponent, data)
    report_changes(before, after, change, player, opponent, totals_dict)
    winner = find_winner(totals_dict, player, opponent)
    enter()
    print "Game Over!\n\n" + state_map(data, party_colors, opponent, opposing, player, party, totals_dict) + '\n' + winner

def enter():
    print raw_input("< Press enter to continue. >")

def get_party(player):
    msg = "Select a party! (D)emocrat, (R)epublican, (G)reen, (L)ibertarian: "
    parties = {'R' : 'Republican', 'D' : 'Democratic', 'L' : 'Libertarian', 'G' : 'Green'}
    party = check_input(raw_input("Welcome " + player + "! " + msg), msg, 'u', parties.keys()) 
    return parties[party], party
    
def number_of_players():
    msg = "How many people will be playing today? '1' or '2' player(s)? "
    number = check_input(raw_input(msg), msg, '', ['1', '2'])
    return number

def check_input(a_input, message, direction, alist):
    if a_input == '':
        a_input = check_input(raw_input("Your input is invalid. " + message), message, direction, alist)
    if direction == 'u':
        a_input = a_input[0].upper()
    if direction == 'l':
        a_input = a_input[0].lower()
    if a_input not in alist:
        a_input = check_input(raw_input("Your input is invalid. " + message), message, direction, alist)
    return a_input

def name_correct(party_name, player):
    party_colors = {'R' : 'red', 'D' : 'blue', 'L' : 'yellow', 'G' : 'green', 'O' : 'black'}
    msg = "Name: " + player + "\nParty: " + color_text(party_name, party_colors[party_name[0].upper()]) + "\nIs this information correct? "
    correct = check_input(raw_input(msg), msg, 'l', ['y', 'n'])
    if correct == 'n':
        msg = "What's wrong? (N)ame or (P)arty? "
        wrong = check_input(raw_input(msg), msg, 'l', ['n', 'p'])
        if wrong == 'n':
            player = raw_input("What's your name? ")
            if player == '':
                player = raw_input("You don't have a name? Type a name or press enter to be called 'player'. ")
                if player == '':
                    player = 'player'
            party_name, player = name_correct(party_name, player)
        if wrong == 'p':
            party_name = get_party(player)
            party_name, player = name_correct(party_name, player)
    return party_name, player

def get_turnout(data, state, player, opponent):
    state_det = data[state]
    turnout_dict, reg_dict, vote_dict = state_det['turnout'], state_det['party registration'], state_det['pop. vote']
    turnout_dict[player], turnout_dict[opponent], turnout_dict['swing'] = vote_dict[player] * 1.0 / reg_dict[player], vote_dict[opponent] * 1.0 / reg_dict[opponent], vote_dict['swing'] * 1.0 / reg_dict['swing']
    return data
    
def color_state(state, color, data, player, opponent):
    string = state + ' [' + data[state]['abbr'] + '] (' + str(data[state]['elec. votes']) + ')  ' + str(round(data[state]['pop. vote %'][player] * 100, 1)) + '% vs. ' + str(round(data[state]['pop. vote %'][opponent] * 100, 1)) + '%'
    return color_text(string, color)

def color_text(string, color):
    color_dict = { 'red' : '\033[1;31m' + string + '\033[1;m' , 'blue' : '\033[1;34m' + string + '\033[1;m', 'purple' : '\033[1;35m' + string + '\033[1;m', 'green' : '\033[1;32m' + string + '\033[1;m', 'yellow' : '\033[1;33m' + string + '\033[1;m', 'black' : string}
    return color_dict[color]
    
def state_map(data, party_colors, opponent, opposing, player, party, totals_dict):
    comp_states_power = totals_dict['elec. votes'][opponent]
    human_states_power = totals_dict['elec. votes'][player]
    neutral_power = totals_dict['elec. votes']['swing']
    swing_votes = totals_dict['%']['swing']
    human_votes = totals_dict['%'][player]
    comp_votes = totals_dict['%'][opponent]
    map = color_text(opponent + ': ' + str(comp_states_power) + '   ' + str(comp_votes * 100) + '%', party_colors[opposing[0]]) + '\n' + color_text(player + ': ' + str(human_states_power) + '   ' + str(human_votes * 100) + '%', party_colors[party[0]]) + '\n' + color_text('Swing: ' + str(neutral_power) + '   ' + str(swing_votes * 100) + '%', 'purple') + '\n\n'
    for st in sorted(data.keys()):
        map = map + data[st]['color code'] + '\n'
    return map
    
def tally_votes(pop_tot, player, opponent, data):
    human_votes, comp_votes, total_votes = 0, 0, 0
    for state in data.keys():
        human_votes += data[state]['pop. vote'][player]
        comp_votes += data[state]['pop. vote'][opponent]
        total_votes += data[state]['voters']
    human_perc, comp_perc = round(human_votes * 1.0 / total_votes, 3), round(comp_votes * 1.0 / total_votes, 3)
    swing_perc = round(1 - human_perc - comp_perc, 3)
    return human_perc, comp_perc, swing_perc
    
def campaign(data, turn_taker, turn_taker_party, other_player, other_player_party, totals_dict, party_colors, abbr_dict, id):
    campaign_state = get_state(state_map(data, party_colors, other_player, other_player_party, turn_taker, turn_taker_party, totals_dict), data, abbr_dict)
    msg = turn_taker + ", pick the number of the action you would like to take. 1. Campaign Ad, 2. Rally, 3. Personal Contact or type 'x' for more options. "
    action = options(check_input(raw_input('\n' + msg), msg, 'l', ['1', '2', '3', 'x', 'i', 'd', 'q']), campaign_state)
    while action in ['x', 'i', 'd', 'q']:
        if action == 'q':
            return campaign(data, turn_taker, turn_taker_party, other_player, other_player_party, totals_dict, party_colors, abbr_dict, id)
        while action in ['i', 'd']:
            state_det = data[campaign_state]
            if action == 'i':
                print "\n1. Campaign Ad: Targets undecided voters and increases the likelihood that they will vote for you.\n2. Rally: Targets voters on your side and increases the likelihood that they will turnout\n3. Personal Contact: Targets your opponent's voters and increases the likelihod that they will change their vote.\n"
                action = options(check_input(raw_input(msg), msg, 'l', ['1', '2', '3', 'x', 'i', 'd', 'q']), campaign_state)
                continue
            if action == 'd':
                player_id, comp_id = id[turn_taker], id[other_player]
                print color_text("\n" + campaign_state + "\nElectoral Votes: " + str(state_det['elec. votes']) + '\nLeans: ' + id[state_det['leans']][0].upper() + id[state_det['leans']][1:], state_det['color']) + '\n\nPercent of Vote:\n' + color_text(id[turn_taker] + ': ' + str(round(state_det['pop. vote %'][turn_taker] * 100, 1)) + '%\n', party_colors[player_id[0].upper()])  + color_text(id[other_player] + ': ' + str(round(state_det['pop. vote %'][other_player] * 100, 1)) + '%', party_colors[comp_id[0].upper()]) + color_text('\nSwing: ' + str(round(state_det['pop. vote %']['swing'] * 100, 1)) + '%\n\n','purple') + 'Turnout:\n' + color_text(id[turn_taker] + ': ' + str(round(state_det['turnout'][turn_taker] * 100, 1)) + '%\n',  party_colors[player_id[0].upper()]) + color_text(id[other_player] + ': ' + str(round(state_det['turnout'][other_player] * 100, 1)) + '%', party_colors[comp_id[0].upper()]) + color_text('\nSwing: ' + str(round(state_det['turnout']['swing'] * 100, 1)) + '%\n', 'purple')
                action = options(check_input(raw_input(msg), msg, 'l', ['1', '2', '3', 'x', 'i', 'd', 'q']), campaign_state)
    return campaign_state, action
    
def options(action, campaign_state):
    acceptable_actions = ['1', '2', '3', 'x', 'i', 'd', 'q']
    if action == 'x':
        msg = "\nOptions:\n'I'-get info about what each action does\n'D'-more details about " + campaign_state + "\n'Q'-pick a new state.\n\nSelect the action you would like to take: "
        action = options(check_input(raw_input(msg), "Select the action you would like to take: ", 'l', acceptable_actions), campaign_state)
    return action

def perform_action(action, turn_taker, other_player, data, campaign_state):
    scenarios = {'1' : ['g'] * 8 + ['n'] * 2 + ['b'] + ['r'], '2' : ['g', 'n', 'b'] * 3 + ['r'], '3' : ['g'] + ['n'] * 3 + ['b'] * 6 + ['r']}
    # A value of 'g' means there will be a good outcome, 'n' is 'neutral', 'b' is bad,
    # 'r' is really bad
    state_det = data[campaign_state]
    outcome = random.choice(scenarios[state_det['change constant']])
    pop_vote = state_det['pop. vote']
    reg_dict = state_det['party registration']
    turn_out = state_det['turnout']
    if action == '1':
        if pop_vote['swing'] == 0:
            outcome = 'b'
        if outcome == 'g':
            new_votes = math.trunc(round(state_det['voters'] * (random.randrange(15, 35) * .001), 0))
            status = 'not changed'
            if new_votes > pop_vote['swing']:
                status = 'changed'
                new_votes = math.trunc(round(pop_vote['swing'] * (random.randrange(500, 750) * .001), 0))
            pop_vote['swing'] = pop_vote['swing'] - new_votes
            pop_vote[turn_taker] = pop_vote[turn_taker] + new_votes
            reg_dict['swing'] = reg_dict['swing'] - new_votes
            reg_dict[turn_taker] = reg_dict[turn_taker] + new_votes
            if status == 'changed':
                print "\n" + turn_taker + ": Great ad, but there aren't many swing voters in this state, so only " + str(new_votes) + " more swing voters will vote for you now!"
            else:
                print "\n" + turn_taker + ": Great ad! " + str(new_votes) + " more swing voters will vote for you now!"
        if outcome == 'n':
            new_votes = math.trunc(round(state_det['voters'] * (random.randrange(5, 15) * .001), 0))
            status = 'not changed'
            if new_votes > pop_vote['swing']:
                status = 'changed'
                new_votes = math.trunc(round(pop_vote['swing'] * (random.randrange(150, 499) * .001), 0))
            pop_vote['swing'] = pop_vote['swing'] - new_votes
            pop_vote[turn_taker] = pop_vote[turn_taker] + new_votes
            reg_dict['swing'] = reg_dict['swing'] - new_votes
            reg_dict[turn_taker] = reg_dict[turn_taker] + new_votes
            if status == 'changed':
                print "\n" + turn_taker + ": Your ad had a small effect, but there aren't many swing voters in this state, so only " + str(new_votes) + " more swing voters will vote for you now!"
            else:
                print "\n" + turn_taker + ": Your ad had a small effect! " + str(new_votes) + " more swing voters will vote for you now!"
        if outcome == 'b':
            print "\n" + turn_taker + ": Your ad failed to inspire any voters. No voters changed their preference"
        if outcome == 'r':
            new_votes = math.trunc(round(state_det['voters'] * (random.randrange(10, 30) * .001), 0))
            status = 'not changed'
            if new_votes > pop_vote['swing']:
                status = 'changed'
                new_votes = math.trunc(round(pop_vote['swing'] * (random.randrange(400, 600) * .001), 0))
            pop_vote['swing'] = pop_vote['swing'] - new_votes
            pop_vote[turn_taker] = pop_vote[turn_taker] - math.trunc(round(new_votes * .5, 0))
            pop_vote[other_player] = pop_vote[other_player] + math.trunc(round(new_votes * 1.5, 0))
            reg_dict['swing'] = reg_dict['swing'] - new_votes
            reg_dict[turn_taker] = reg_dict[turn_taker] - math.trunc(round(new_votes * .5, 0))
            reg_dict[other_player] = reg_dict[other_player] + math.trunc(round(new_votes * 1.5, 0))
            if status == 'changed':
                print "\n" + turn_taker + ": Your ad backfired! Luckily, it only had a small effect because there aren't many swing voters in this state, so only " + str(new_votes) + " swing voters and " + str(math.trunc(round(new_votes * .5, 0))) + " of your voters will vote for " + other_player + " now!"
            else:
                print "\n" + turn_taker + ": Your ad backfired! " + str(new_votes) + " swing voters and " + str(math.trunc(round(new_votes * .5, 0))) + " of your voters will vote for " + other_player + " now!"
    if action == '2':
        if outcome == 'g':
            new_votes = math.trunc(round((reg_dict[turn_taker] - pop_vote[turn_taker]) * random.randrange(30, 70) * .001, 0))
            pop_vote[turn_taker] = pop_vote[turn_taker] + new_votes
            state_det['voters'] = state_det['voters'] + new_votes
            print "\n" + turn_taker + ": Great rally! " + str(new_votes) + " more people will turn out to vote for you on election day!"
        if outcome == 'n':
            new_votes = math.trunc(round((reg_dict[turn_taker] - pop_vote[turn_taker]) * random.randrange(10, 30) * .001, 0))
            pop_vote[turn_taker] = pop_vote[turn_taker] + new_votes
            state_det['voters'] = state_det['voters'] + new_votes
            print "\n" + turn_taker + ": Pretty good rally! " + str(new_votes) + " more people will turn out to vote for you on election day!"
        if outcome == 'b':
            print "\n" + turn_taker + ": Ineffective rally, no new voters have decided to turnout for election day."
        if outcome == 'r':
            new_votes = math.trunc(round((reg_dict[turn_taker] - pop_vote[turn_taker]) * random.randrange(20, 60) * .001, 0))
            pop_vote[turn_taker] = pop_vote[turn_taker] - new_votes
            state_det['voters'] = state_det['voters'] - new_votes
            print "\n" + turn_taker + ": Terrible rally! " + str(new_votes) + " more people have decided to stay home on election day!"
    if action == '3':
        if outcome == 'g':
            new_votes = math.trunc(round(state_det['voters'] * (random.randrange(7, 19) * .001), 0))
            status = 'not changed'
            if new_votes > pop_vote[other_player]:
                status = 'changed'
                new_votes = math.trunc(round(pop_vote[other_player] * (random.randrange(250, 375) * .001), 0))
            pop_vote[other_player] = pop_vote[other_player] - new_votes
            pop_vote[turn_taker] = pop_vote[turn_taker] + new_votes
            reg_dict[other_player] = reg_dict[other_player] - new_votes
            reg_dict[turn_taker] = reg_dict[turn_taker] + new_votes
            if status == 'changed':
                print "\n" + turn_taker + ": Awesome! It worked great! Unfortunately, " + other_player + " doesn't have very many voters in this state, so only " + str(new_votes) + " voters have decided to vote for you instead of " + other_player + "."
            else:
                print "\n" + turn_taker + ": Awesome! It worked great! " + str(new_votes) + " voters have decided to vote for you instead of " + other_player + "!"
        if outcome == 'n':
            new_votes = math.trunc(round(state_det['voters'] * (random.randrange(5, 15) * .001), 0))
            status = 'not changed'
            if new_votes > pop_vote[other_player]:
                status = 'changed'
                new_votes = math.trunc(round(pop_vote[other_player] * (random.randrange(150, 499) * .001), 0))
            pop_vote[other_player] = pop_vote[other_player] - new_votes
            pop_vote[turn_taker] = pop_vote[turn_taker] + new_votes
            reg_dict[other_player] = reg_dict[other_player] - new_votes
            reg_dict[turn_taker] = reg_dict[turn_taker] + new_votes
            if status == 'changed':
                print "\n" + turn_taker + ": Good job! Unfortunately, " + other_player + "doesn't have very many voters in this state, so only " + str(new_votes) + " voters have decided to vote for you instead of " + other_player + "."
            else:    
                print "\n" + turn_taker + ": Good job! " + str(new_votes) + " have decided to vote for you instead of " + other_player + "!"
        if outcome == 'b':
            print "\n" + turn_taker + ": Whoops! You failed to inpsire any new voters to vote for you."
        if outcome == 'r':
            new_votes = math.trunc(round(state_det['voters'] * (random.randrange(10, 30) * .001), 0))
            status = 'not changed'
            if new_votes > pop_vote[turn_taker]:
                status = 'changed'
                new_votes = math.trunc(round(pop_vote['swing'] * (random.randrange(400, 600) * .001), 0))
            pop_vote[other_player] = pop_vote[other_player] + new_votes
            pop_vote[turn_taker] = pop_vote[turn_taker] - new_votes
            reg_dict[other_player] = reg_dict[other_player] + new_votes
            reg_dict[turn_taker] = reg_dict[turn_taker] - new_votes
            if status == 'changed':
                print "\n" + turn_taker + ": Oh no! What did you say? Luckily, only " + str(new_votes) + " of your own voters now plan to vote for " + other_player + " because you don't have very many voters in this state."
            else:
                print "\n" + turn_taker + ": Oh no! What did you say? " + str(new_votes) + " of your own voters now plan to vote for " + other_player + "!"
    return data

def update_data(data, state, player, opponent, party_colors, id):
    data = get_turnout(data, state, player, opponent)
    data = adjust_pop_vote_perc(data, state, player, opponent)
    data, color = check_status(data, state, player, opponent, party_colors, id)
    data[state]['color code'] = color_state(state, color, data, player, opponent)
    return data
    
def adjust_pop_vote_perc(data, state, player, opponent):    
    state_det = data[state]
    for key in state_det['pop. vote %'].keys():
        state_det['pop. vote %'][key] = round(state_det['pop. vote'][key] * 1.0 / state_det['voters'], 3)
    return data
    
def check_status(data, state, player, opponent, party_colors, id):
    """
    Checks to see if state has changed 'lean'.
    """
    state_det = data[state]
    pop_vote = state_det['pop. vote %']
    if math.fabs(pop_vote[player] - pop_vote[opponent]) <= .02:
        if state_det['leans'] != 'swing':
            state_det['leans'] = 'swing'
            state_det['color'] = 'purple'
    if state_det['leans'] == 'swing':
        if math.fabs(pop_vote[player] - pop_vote[opponent]) > .021:
            if pop_vote[player] > pop_vote[opponent]:
                state_det['leans'] = player
                state_det['color'] = party_colors[id[player][0]]
            else:
                state_det['leans'] = opponent
                state_det['color'] = party_colors[id[opponent][0]]
    return data, state_det['color']
               
def update_electoral_count(data, player, opponent, previous):
    elec_votes_dict = {player : 0, opponent : 0, 'swing' : 0}
    for state in data:
        state_det = data[state]
        lean = state_det['leans']
        votes = state_det['elec. votes']
        if lean == 'swing':
            elec_votes_dict['swing'] += votes
        elif lean == player:
            elec_votes_dict[player] += votes
        else:
            elec_votes_dict[opponent] += votes
    change = {}
    for key in elec_votes_dict.keys():
        difference = elec_votes_dict[key] - previous[key]
        if difference > 0:
            change[key] = '+' + str(difference)
        else:
            change[key] = str(difference)
    return elec_votes_dict, change
        
def get_state(map, data, abbr_dict):
    campaign_state = raw_input("\nSelect the state you would like to campaign in by typing its name or two letter abbreviation. Type 'M' to see the map. ")
    while campaign_state == '':
        campaign_state = raw_input("Your input is not valid. Please select the state you would like to campaign in by typing its name or two letter abbreviation: ")
    if campaign_state.lower() in ['m', 'map']:
        print map
        campaign_state = raw_input("Select the state you would like to campaign in by typing its name or two letter abbreviation: ")
    campaign_state = check_state(campaign_state, abbr_dict)
    print '\n' + data[campaign_state]['color code']
    return campaign_state

def check_state(campaign_state, abbr_dict):
    if len(campaign_state) == 2:
        campaign_state = campaign_state.upper()
    elif len(campaign_state) == 0:
        pass
    else: 
        campaign_state = campaign_state[0].upper() + campaign_state[1:].lower()
    while campaign_state not in abbr_dict.keys() and campaign_state not in abbr_dict.values() or campaign_state == '':
        campaign_state = raw_input("Your input is not valid. Please select the state you would like to campaign in by typing its name or two letter abbreviation: ")
        if len(campaign_state) == 2:
            campaign_state = campaign_state.upper()
        elif len(campaign_state) == 0:
            pass
        else: 
            campaign_state = campaign_state[0].upper() + campaign_state[1:].lower()
    if len(campaign_state) == 2:
        campaign_state = abbr_dict[campaign_state]
    go_on = raw_input("You chose " + campaign_state + ". Is that correct? (Y)es or (N)o? ")
    while go_on.lower() not in ['y', 'n', 'yes', 'no']:
        go_on = raw_input("Your input is not valid. You chose " + campaign_state + ". Is that correct? (Y)es or (N)o? ")
    if go_on.lower() in ['no', 'n']:
        campaign_state = check_state(raw_input("Select the state you would like to campaign in by typing its name or two letter abbreviation: "), abbr_dict)
    return campaign_state
    
def report_changes(before, after, change, player, opponent, totals_dict):
    msg = "\nStates campaigned in this round:\n"
    for i in range(len(before)):
        msg += before[i] + " --> " + after[i] + '\n'
    msg += "\nElectoral Count:\n" + opponent + ': ' + change[opponent] + ' --> ' + str(totals_dict['elec. votes'][opponent]) + '\n' + player + ': ' + change[player] + ' --> ' + str(totals_dict['elec. votes'][player]) + '\nSwing: ' + change['swing'] + ' --> ' + str(totals_dict['elec. votes']['swing']) + '\n'
    print  msg
    
def game_end(data, player, opponent, party_colors, id):
    before, after = [], []
    for state in data.keys():
        pop_vote = data[state]['pop. vote']
        if data[state]['leans'] == 'swing':
            before.append(data[state]['color code'])
            if pop_vote['swing'] > 1:
                new_votes = random.randrange(pop_vote['swing'])
                pop_vote['swing'] -= new_votes
                pop_vote[player] += new_votes
                pop_vote[opponent] += pop_vote['swing']
                pop_vote['swing'] = 0
            data = get_turnout(data, state, player, opponent)
            data = adjust_pop_vote_perc(data, state, player, opponent)
            if pop_vote[player] == pop_vote[opponent]:
                rand = random.choice['a', 'b']
                if rand == 'a':
                    pop_vote[player] += 1
                    pop_vote[opponent] -= 1
                else:
                    pop_vote[player] -= 1
                    pop_vote[opponent] += 1
            if pop_vote[player] > pop_vote[opponent]:
                color = party_colors[id[player][0]]
                data[state]['leans'] = player
            else:
                color = party_colors[id[opponent][0]]
                data[state]['leans'] = opponent
            data[state]['color code'] = color_state(state, color, data, player, opponent)
            after.append(data[state]['color code'])
    return data, before, after
    
def find_winner(totals_dict, player, opponent):
    votes = totals_dict['elec. votes']
    if votes[player] >= 270:
        winner = player + " wins with " + str(votes[player]) + " votes!"
    elif votes[opponent] >= 270:
        winner = opponent + " wins with " + str(votes[opponent]) + " votes!"
    else:
        winner = "Nobody recieved 270 electoral votes! The House of Representatives will decide who becomes president!"
    return winner

def reverse_dict(adict):
    reversal = {}
    for key, value in adict.items():
        reversal[value] = key
    return reversal

def get_comp_queue(neutral, human_states, data, player, opponent):
    possible = neutral
    for state in human_states:
        if (data[state]['pop. vote %'][player] - data[state]['pop. vote %'][opponent]) < .07:
            possible.append(state)
    return mergesort(possible, data, "elec. votes")

def computer_action(data, opponent, campaign_state):
    if data[campaign_state]['pop. vote %']['swing'] >= .06:
        return '1'
    elif data[campaign_state]['turnout'][opponent] <= .55:
        return '2'
    else:
        return '3'

def mergesort(l, adict, val):
    """
    Sorts keys of a dictionary into a list based on a specific value.

    Arguments: 
    l     -- the keys of the dictionary to be sorted
    adict -- a dictionary whose keys are to be sorted by its value
    val   -- the value to sort by

    Returns:
    l     -- a list sorted in-place in ascending order
    """
    n = len(l)
    if n > 1:
        a = l[0 : (n / 2)]
        b = l[(n / 2) : n]
        mergesort(a, adict, val)
        mergesort(b, adict, val)
        merge(a, b, l, adict, val)
    return l

def merge(a, b, l, adict, val):
    i, j, k = 0, 0, 0
    p = len(a)
    q = len(b)
    while i < p and j < q:
        if adict[a[i]][val] >= adict[b[j]][val]:
            l[k] = a[i]
            i += 1
        else:
            l[k] = b[j]
            j += 1
        k += 1
    if i == p:
        l[k : (p + q)] = b[j : q]
    else:
        l[k : (p + q)] = a[i : p]
    return l

    

    
    