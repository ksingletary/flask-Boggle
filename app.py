from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, jsonify, session


app = Flask(__name__)
app.secret_key = "giggitygoo"
boggle_game = Boggle()

word_list = []

@app.route('/')
def home_page():
    global word_list
    word_list = []
    if not session.get('high_score'):
        session['high_score'] = 0
    if not session.get('games'):
        session['games'] = 0
    session['board'] = boggle_game.make_board()
    return render_template('home.html', board=session['board'], high_score=session['high_score'], games=session['games'])

@app.route('/board')
def board():
    width = 5
    height = 5
    full_board = boggle_game.make_board()
    session["full_board"] = full_board

    return render_template('board.html', full_board=full_board, width=width, height=height)

@app.route('/guess')
def guess():
    """Check a guess against the current board."""
    word_guess = request.args.get("word_guess")
    if word_guess not in word_list:
        board = session['board']
        result = boggle_game.check_valid_word(board, word_guess)

        if result == "ok":
            word_list.append(word_guess)
            print(word_list)
        return result
    
    else:
        return "not-on-board"    

@app.route('/score')
def score():
    """Takes the final score for the current game, compares it to the high
    score, and displays the new high score. Iterates the current number of games
    in the session.
    """
    final_score = int(request.args.get("final_score"))
    if final_score > session.get('high_score'):
        session['high_score'] = final_score
    session['games'] += 1
    info = {"games": session.get('games'), "high_score": session.get('high_score')}
    info = jsonify(info)
    return info



