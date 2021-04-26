from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
from random import choice
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"

debug = "DebugToolbarExtension(app)"

this_game = Boggle()

@app.route('/')
def load_home_page():
    """load home page to display high score, number of games played, average score"""
    board_size = int(session.get('board_size', 5))
    highscore = int(session.get('high_score', '0'))
    average_score = int(session.get('average_score', '0'))
    game_num = int(session.get('game_num', '0'))
    # if the game_num says games have been played and either of the other numbers are zero, something is wonky, so reset and start over
    if highscore == 0 or averagescore == 0:
        flash('something odd happened in the records of games', 'error')
        flash("so we're starting over. Sorry for any inconvenience", 'info')
        session.clear()
    session['board_size'] = board_size
    session['highscore'] = highscore
    session['average_score'] = average_score
    return render_template('home.html', highscore = highscore, game_num = game_num, average_score = average_score)

@app.route('/board', methods=["GET", "POST"])
def load_board():
    """set up the board and the game-play form"""

    game_num = session.get('game_num', request.args['game_on'])
    session['game_num'] = game_num
    correct_words = session.get('correct_words', [])
    board = this_game.make_board()
    session['board'] = board
    board_size = int(session.get('board_size', 5))
    return render_template('game.html', board = board, len_correct_words = len(correct_words), board_size = board_size)

@app.route('/played-word')
def play_a_word():
    """find out if word is in our word list AND on the current board"""

    board = session["board"]
    word = request.args["word"]
    response = this_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def process_score():
    """receive score, update average_score, and update highscore if there is one."""

    this_score = request.json["score"]
    highscore = session.get("highscore", 0)
    games_played = session.get("game_num", 1)
    average_score = session.get("average_score", 0)
    new_average = (average_score * (game_num - 1) + this_score) / game_num
    session['average_score'] = average_score
    session['highscore'] = max(score, highscore)

    return jsonify(brokenRecord=score > highscore)

@app.route('/reset')
def reset_session_restart():
    session.clear()
    session['is_game_on'] = False
    flash('I really hope you meant that, because I did.', 'troubleshooting')
    return redirect ('/')