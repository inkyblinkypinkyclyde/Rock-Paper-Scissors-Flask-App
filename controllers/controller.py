from flask import render_template, request, redirect
from app import app
from models.players import *
from models.player import *


#pve routes
@app.route("/rps/pve")
def index_pve():
    return render_template('pve_rps.html', title= 'PvE mode',)

@app.route("/rps/pve", methods=['post'])
def pve_play():
    outcome = play_game_pve(request.form['option'])
    return render_template('pve_rps.html', title= 'PvE mode', outcome = outcome)

# #pvp routes  I'll fix these later
# @app.route("/rps/pvp")
# def pvp_play():
#     return render_template('pvp_rps.html', title= 'PvP mode',)

# @app.route("/rps/pvp", methods=['post'])
# def pvp_play():
#     outcome = play_game_pve(request.form['option'])
#     return render_template('pve_rps.html', title= 'PvE mode', outcome = outcome)

@app.route("/rps")
def index_pvp():
    return render_template('pvp_rps.html', title= 'PvP mode',)


@app.route('/rps/<player1_choice>/<player2_choice>')
def take_choices(player1_choice, player2_choice):
    player1 = Player("John", player1_choice)
    player2 = Player("Jarrod", player2_choice)
    return render_template('pvp_URL_rps.html', title= 'PvP URL entry mode', result = play_game_URL_input(player1, player2))

#player navigates to rps/rock/paper
#create player1 object w/name player 1 choice rock
#create player2 object w/name player 2 choice paper


