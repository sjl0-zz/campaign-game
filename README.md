Campaign Game

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