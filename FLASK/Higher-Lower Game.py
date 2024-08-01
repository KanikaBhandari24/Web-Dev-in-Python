from flask import Flask
import random 

rand=random.randint(0, 9)
print(rand)
app = Flask(__name__)

@app.route('/')
def fun():
    return '<h1>Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif?cid=790b7611ufvcsmleg2zlaeshef98ibwbkdnhch4j22czchnw&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>'

@app.route("/<int:guess>")
def guessno(guess):
    if guess>rand:
        return '<h1 style="color: red">Too High, try again!</h1>'\
        '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb285dnVja2F5Znp1NmM3Nmk3ZGg5dXVkMzIwNHFwbTdrbXN2ZmR2ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/gKHGnB1ml0moQdjhEJ/giphy.gif"/>'
    
    elif guess<rand:
        return "<h1 style='color: red'>Too Low, try again!</h1>"\
        "<img src='https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif?cid=790b7611oo9vuckayfzu6c76i7dh9uud3204qpm7kmsvfdvf&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"

    else:
        return "<h1 style='color: red'>You found me. Yay!</h1>"\
        "<img src='https://media.giphy.com/media/kiBcwEXegBTACmVOnE/giphy.gif?cid=790b7611oo9vuckayfzu6c76i7dh9uud3204qpm7kmsvfdvf&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"

if __name__ == '__main__':
    app.run(debug=True) 