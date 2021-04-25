from flask import Flask, request, render_template, redirect, flash, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "damn-secret"


from boggle import Boggle, this_game


@app.route('/')
def load_home_page():
    return render_template('home.html')

@app.route('/board')
def load_board():
    # game_on = request.args['play']
    # session['is_game_on'] = game_on
    # if not game_on:
    #     flash('something went wrong, please try again', 'info')
    #     return redirect('/')

    game_num = session.get('game_num', 0)
    game_num += 1
    session['game_num'] = game_num
    correct_words = session.get('correct_words', [])
    this_game = Boggle()
    board = this_game.make_board()
    session['board'] = board
    flash("Let's play!", "info")
    return render_template('board.html', board = board, len_correct_words = len(correct_words))

@app.route('/play')
def play_a_word():
    word = request.args['word']
    board = session['board']
    correct_words = session.get('correct_words', [])
    is_word_valid = this_game.check_valid_word(board, word)
    if is_word_valid == "ok":
        if correct_words.count(word) > 0:
            flash ("You already got that word.", "info")
        else:
            correct_words.append(word)
            session['correct_words'] = correct_words
            random_compliment = "good one!"
            flash (random_compliment, "thank_you")
    else:
        flash (f"Sorry, that word is {is_word_valid}.", "error")    
    return render_template('board.html', board = board, len_correct_words = len(correct_words))

@app.route('/reset')
def reset_session_restart():
    session.clear()
    session['is_game_on'] = False
    return redirect ('/')