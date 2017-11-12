from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/play', methods=['GET', 'POST'])
def game():
    if request.form['name']:
        name = request.form['name']
    else:
        name = 'Sara'

    back = 'purple_back'
    pocket11 = "/static/images/{}.png".format(back)
    pocket12 = "/static/images/{}.png".format(back)
    pocket21 = "/static/images/{}.png".format(back)
    pocket22 = "/static/images/{}.png".format(back)
    flop1 = "/static/images/{}.png".format(back)
    flop2 = "/static/images/{}.png".format(back)
    flop3 = "/static/images/{}.png".format(back)
    turn = "/static/images/{}.png".format(back)
    river = "/static/images/{}.png".format(back)
    money1 = 10000
    money2 = 10000
    pot = 100
    return render_template('game.html', name=name, pocket11=pocket11, pocket12=pocket12,
        pocket21=pocket21, pocket22=pocket22, flop1=flop1, flop2=flop2, flop3=flop3,
        turn=turn, river=river, money1=money1, money2=money2, pot=pot)
#    else:
#        return redirect(url_for('main'))


def get_card():
    values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits = ['H','D','C','S']
    return ''.join([random.choice(values), random.choice(suits)])


if __name__ == "__main__":
    app.run(debug=True)
