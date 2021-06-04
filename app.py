from flask import Flask, request, render_template, redirect, flash, jsonify, session
from random import choice
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"

this_game = Boggle()

@app.route('/')
def load_home_page():
    """load home page to display high score, number of games played, average score"""
    board_size = int(session.get('board_size', 5))
    highscore = int(session.get('highscore', '0'))
    average_score = int(session.get('average_score', '0'))
    game_num = int(session.get('game_num', '0'))
    # if the game_num says games have been played and either of the other numbers are zero, something is wonky, so reset and start over
    if highscore == 0 or average_score == 0:
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

    board_size = int(session.get('board_size', 5))
    highscore = int(session.get('highscore', 0))
    average_score = int(session.get('average_score', 0))
    game_num = int(request.args['game_on'])
    session['game_num'] = game_num
    correct_words = session.get('correct_words', [])
    board = this_game.make_board()
    session['board'] = board
    board_size = int(session.get('board_size', 5))
    return render_template('game.html', highscore = highscore, game_num = game_num, average_score = average_score, board = board, len_correct_words = len(correct_words), board_size = board_size)

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
    game_score = request.json['score']
    highscore = int(session.get("highscore", 0))
    games_played = int(session.get("game_num", 1))
    average_score = int(session.get("average_score", 0))
    new_average = ((average_score * (games_played - 1) + game_score) / games_played)
    session['average_score'] = new_average
    if game_score > highscore:
        msg = "That's a new high score"
        clss = "hooray"
        session['highscore'] = game_score
    elif game_score == highscore:
        msg = "You just tied the high score"
        clss = "info"
    else:
        msg = ""
        clss = "info"

    return jsonify({'message': msg, 'class': clss})

@app.route('/reset')
def reset_session_restart():
    session.clear()
    session['is_game_on'] = False
    flash('I really hope you meant that, because I did.', 'troubleshooting')
    return redirect ('/')