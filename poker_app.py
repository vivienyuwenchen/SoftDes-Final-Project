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
    pocket1 = "/static/images/{}.png".format(get_card())
    pocket2 = "/static/images/{}.png".format(get_card())
    return render_template('game.html', name=name, pocket1=pocket1,
                            pocket2=pocket2)
#    else:
#        return redirect(url_for('main'))


def get_card():
    values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits = ['H','D','C','S']
    return ''.join([random.choice(values), random.choice(suits)])


if __name__ == "__main__":
    app.run(debug=True)
