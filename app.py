from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"


from boggle import Boggle


@app.route('/')
def load_home_page():
    if session.get('is_game_on') and session.get('board'):
        board = session['board']
        return render_template('board.html', board = board)
    return redirect('/reset')

@app.route('/board')
def load_board():
    game_on = request.args['play']
    session['is_game_on'] = game_on
    if not game_on:
        flash('something went wrong, please try again', 'info')
        return redirect('/')

    game_num = session.get('game_num', 0)
    game_num += 1
    session['game_num'] = game_num

    this_game = Boggle()
    board = this_game.make_board()
    session['board'] = board
    flash("Let's play!", "info")
    return render_template('board.html', board = board)

@app.route('/reset')
def reset_session_restart():
    session.clear()
    session['is_game_on'] = False
    return render_template ('home.html')