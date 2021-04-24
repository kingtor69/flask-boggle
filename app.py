from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"


from boggle import Boggle


@app.route('/')
def load_home_page():
    if session.get('is_game_on'):
        return redirect('board')
    game_num = session.get('game_num', 0)
    game_num += 1
    session['game_num'] = game_num
    return render_template('home.html')

@app.route('/board')
def load_board():
    game_on = session.get('is_game_on', False)
    if game_on:
        flash('write some game_on logic', 'troubleshooting')
    else:
        flash('write some new_game logic', 'troubleshooting')
    (rows, columns) = board_size(session['board'])

    return render_tamplate('board.html', )
