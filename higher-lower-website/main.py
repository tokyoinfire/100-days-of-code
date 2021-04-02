import random
from flask import Flask
app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:number>")
def make_a_guess(number):
    if int(number) < random_number:
        return '<h1 style="color:red">Too low, try again!</h1>'\
               '<img src="https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif">'
    elif int(number) > random_number:
        return '<h1 style="color:violet">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/WTL02R1L7YCGUEunFy/giphy.gif">'
    elif int(number) == random_number:
        return '<h1 style="color:green">You found me!</h1>'\
               '<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif">'


if __name__ == "__main__":
    app.run()
