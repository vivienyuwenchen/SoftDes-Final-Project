from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/play')
def game():
    return render_template('game.html')


if __name__ == "__main__":
    app.run()
