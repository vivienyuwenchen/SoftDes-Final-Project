from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
import random

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def hand(game):
    # if request.form['name']:
    #     name = request.form['name']
    # else:
    #     name = 'Sara'
    #pocket11_ = get_card()
    #if request.method == 'GET':
    #    if request.form['submit'] == 'Fold':
    #        pocket11_ = 'AS'
    pocket1 = game.player1.pocket
    pocket2 = game.player2.pocket
    community_cards = game.community_cards

    back = 'purple_back'
    pocket11 = "/static/images/{}.png".format(pocket1[0])
    pocket12 = "/static/images/{}.png".format(pocket2[1])
    pocket21 = "/static/images/{}.png".format(back)
    pocket22 = "/static/images/{}.png".format(back)
    try:
        i = 0
        flop1 = "/static/images/{}.png".format(community_cards[0])
        i = 1
        flop2 = "/static/images/{}.png".format(community_cards[1])
        i = 2
        flop3 = "/static/images/{}.png".format(community_cards[2])
        i = 3
        turn = "/static/images/{}.png".format(community_cards[3])
        i = 4
        river = "/static/images/{}.png".format(community_cards[4])
    except IndexError:
        if i == 0:
            flop1 = "/static/images/{}.png".format(back)
            flop2 = "/static/images/{}.png".format(back)
            flop3 = "/static/images/{}.png".format(back)
            turn = "/static/images/{}.png".format(back)
            river = "/static/images/{}.png".format(back)
        if i == 1:
            flop1 = "/static/images/{}.png".format(community_cards[0])
            flop2 = "/static/images/{}.png".format(back)
            flop3 = "/static/images/{}.png".format(back)
            turn = "/static/images/{}.png".format(back)
            river = "/static/images/{}.png".format(back)
        if i == 2:
            flop1 = "/static/images/{}.png".format(community_cards[0])
            flop2 = "/static/images/{}.png".format(community_cards[1])
            flop3 = "/static/images/{}.png".format(back)
            turn = "/static/images/{}.png".format(back)
            river = "/static/images/{}.png".format(back)
        if i == 3:
            flop1 = "/static/images/{}.png".format(community_cards[0])
            flop2 = "/static/images/{}.png".format(community_cards[1])
            flop3 = "/static/images/{}.png".format(community_cards[2])
            turn = "/static/images/{}.png".format(back)
            river = "/static/images/{}.png".format(back)
        if i == 4:
            flop1 = "/static/images/{}.png".format(community_cards[0])
            flop2 = "/static/images/{}.png".format(community_cards[1])
            flop3 = "/static/images/{}.png".format(community_cards[2])
            turn = "/static/images/{}.png".format(community_cards[3])
            river = "/static/images/{}.png".format(back)
    money1 = 1000
    money2 = 1000
    pot = 150

    if request.method == 'POST':
        return render_template('game.html', pocket11=pocket11, pocket12=pocket12,
            pocket21=pocket21, pocket22=pocket22, flop1=flop1, flop2=flop2, flop3=flop3,
            turn=turn, river=river, money1=money1, money2=money2, pot=pot)

#    else:
#        return redirect(url_for('main'))
#def get_card():
    #values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    #suits = ['H','D','C','S']
    #return ''.join([random.choice(values), random.choice(suits)])


def run_gui(game):
    # create new episode for training with every new game
    episode = []
    socketio.run(app, debug=True)
