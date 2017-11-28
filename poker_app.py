from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
import random

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/play', methods=['GET', 'POST'])
def game():
    # if request.form['name']:
    #     name = request.form['name']
    # else:
    #     name = 'Sara'
    pocket11_ = get_card()
    if request.method == 'GET':
        if request.form['submit'] == 'Fold':
            pocket11_ = 'AS'

    back = 'purple_back'
    pocket11 = "/static/images/{}.png".format(pocket11_)
    pocket12 = "/static/images/{}.png".format(get_card())
    pocket21 = "/static/images/{}.png".format(back)
    pocket22 = "/static/images/{}.png".format(back)
    flop1 = "/static/images/{}.png".format(get_card())
    flop2 = "/static/images/{}.png".format(get_card())
    flop3 = "/static/images/{}.png".format(get_card())
    turn = "/static/images/{}.png".format(get_card())
    river = "/static/images/{}.png".format(get_card())
    money1 = 10000
    money2 = 10000
    pot = 100

    if request.method == 'POST':
        return render_template('game.html', pocket11=pocket11, pocket12=pocket12,
            pocket21=pocket21, pocket22=pocket22, flop1=flop1, flop2=flop2, flop3=flop3,
            turn=turn, river=river, money1=money1, money2=money2, pot=pot)

#    else:
#        return redirect(url_for('main'))


def get_card():
    values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits = ['H','D','C','S']
    return ''.join([random.choice(values), random.choice(suits)])


if __name__ == "__main__":
    socketio.run(app, debug=True)
