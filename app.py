from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    computer_choice = ""
    player_choice = ""

    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = get_winner(player_choice, computer_choice)

    return render_template("index.html",
                           result=result,
                           computer_choice=computer_choice,
                           player_choice=player_choice)

if __name__ == "__main__":
    app.run(debug=True)
