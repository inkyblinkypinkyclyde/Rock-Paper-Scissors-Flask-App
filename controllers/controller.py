from flask import render_template, request, redirect
from app import app
from models.players import *
from models.player import *

@app.route("/rps")
def index_pvp():
    return render_template('index.html', title= 'PvP mode',)

@app.route("/rps/pve")
def index_pve():
    return render_template('pve_rps.html', title= 'PvE mode',)

@app.route("/rps/pve", methods=['post'])
def pve_play():
    outcome = play_game_pve(request.form['option'])
    return render_template('pve_rps.html', title= 'PvE mode', outcome = outcome)

@app.route('/rps/rock/scissors')
def outcome1():
    return render_template('index.html', title= 'PvP mode', outcome_string = "player 1 beat player 2")

@app.route('/rps/scissors/paper')
def outcome2():
    return render_template('index.html', title= 'PvP mode', outcome_string = "player 1 beat player 2")

@app.route('/rps/paper/rock')
def outcome3():
    return render_template('index.html', title= 'PvP mode', outcome_string = "player 1 beat player 2")

@app.route('/rps/scissors/rock')
def outcome4():
    return render_template('index.html', title= 'PvP mode', outcome_string = "player 2 beat player 1")

@app.route('/rps/paper/scissors/')
def outcome5():
    return render_template('index.html', title= 'PvP mode', outcome_string = "player 2 beat player 1")

@app.route('/rps/rock/scissors')
def outcome6():
    return render_template('index.html', title= 'PvP mode', outcome_string = "player 2 beat player 1")

