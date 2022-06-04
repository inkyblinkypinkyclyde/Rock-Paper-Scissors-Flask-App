from flask import render_template, request, redirect
from app import app
from models.players import *
from models.player import *

@app.route("/rps")
def home_page():
    return render_template('home.html', title='Welcome to RPS')

##### This works, don't touch this
@app.route('/rps/<player1_choice>/<player2_choice>')
def take_choices(player1_choice, player2_choice):
    player1 = Player("John", player1_choice)
    player2 = Player("Jarrod", player2_choice)
    return render_template('pvp_URL_rps.html', title= 'PvP URL entry mode', result = play_game_URL_input(player1, player2))
##### This works, don't touch this


##### This works, don't touch this
@app.route("/rps/pve")
def index_pve():
    return render_template('pve_rps.html', title= 'PvE mode',)

@app.route("/rps/pve", methods=['post'])
def pve_play():
    outcome = play_game_pve(request.form['option'])
    return render_template('pve_rps.html', title= 'PvE mode', outcome = outcome)
##### This works, don't touch this


##### This works, don't touch this
@app.route("/rps/pvp")
def pvp_play():
    return render_template('pvp_rps.html', title= 'PvP mode',)

@app.route("/rps/pvp", methods=['post'])
def pvp_play2():
    outcome = play_game_select_input(request.form['player1_choice'], request.form['player2_choice'])
    return render_template('pvp_rps.html', title= 'PvP mode', outcome = outcome)
##### This works, don't touch this


@app.route("/rps/LAN/player1")
def lan_player1():
    return "player1 area"

@app.route("/rps/LAN/player2")
def lan_player2():
    return "player2 area"



