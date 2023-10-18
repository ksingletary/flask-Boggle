from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, jsonify, session

app = Flask(__name__)
app.secret_key = "giggitygoo"

boggle_game = Boggle()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/board')
def board():
    width = 5
    height = 5
    full_board = boggle_game.make_board()
    session["full_board"] = full_board
    print(full_board)

    return render_template('board.html', full_board=full_board, width=width, height=height)



