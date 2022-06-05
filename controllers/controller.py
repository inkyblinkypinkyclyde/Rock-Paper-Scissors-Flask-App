from operator import truediv
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
    player1 = Player("John", player1_choice, True)
    player2 = Player("Jarrod", player2_choice, True)
    return render_template('pvp_URL_rps.html', title= 'PvP URL entry mode', result = play_game_URL_input(player1, player2))
##### This works, don't touch this


##### This works, don't touch this
@app.route("/rps/pve")
def index_pve():
    return render_template('pve_rps.html', title= 'PvE mode',)

@app.route("/rps/pve", methods=['post'])
def pve_play():
    outcome = play_game_pve(request.form['option'])
    results_list.append(outcome)
    return render_template('pve_rps.html', title= 'PvE mode', outcome = outcome, results_list = results_list)

@app.route("/rps/pve/clear")
def clear_results_list():
    results_list.clear()
    return redirect('/rps/pve')
##### This works, don't touch this_number


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
    return render_template('pvp_LAN.html', title= "player1 - LAN", player = "player1")

@app.route('/rps/LAN/player1', methods=['post'])
def play_LAN1():
    player1LAN.choice = request.form['player1_choice']
    if player2LAN.has_played == True:
        outcome = play_game_URL_input(player1LAN, player2LAN)
        return render_template('pvp_LAN.html', title= "player1 - LAN", player = "player1", outcome = outcome)
    else:
        return render_template('pvp_LAN.html', title= "player1 - LAN", player = "player1", outcome = "error!!")

@app.route("/rps/LAN/player2")
def lan_player2():
    return render_template('pvp_LAN.html', title= "player2 - LAN", player = "player2")

@app.route('/rps/LAN/player2', methods=['post'])
def play_LAN2():
    player1LAN.choice = request.form['player2_choice']
    if player1LAN.choice != "":
        outcome = play_game_URL_input(player1LAN, player2LAN)
        return render_template('pvp_LAN.html', title= "player2 - LAN", player = "player2", outcome = outcome)
    else:
        return render_template('pvp_LAN.html', title= "player2 - LAN", player = "player2", outcome = "error!!")

 
 
 