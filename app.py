from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
board = [""] * 9
current_player = "X"

def check_winner(board):
    win_combos = [
        (1,2,3), (3,4,5), (6,7,8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_combos:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route("/", methods=['GET', 'POST'])
def index():
    global board, current_player
    message = ''

    if request.method == 'POST':
        index = int(request.form['cell'])
        if board[index] == '':
            board[index] = current_player
            winner = check_winner(board)
            if winner:
                message = f"🎉 Player {winner} wins!"
            elif "" not in board:
                message = "😐 It's a draw!"
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            message = "❌ Invalid move!"
    return render_template("index.html", board=board, message=message, current=current_player)


@app.route("/reset")
def reset():
    global board, current_player
    board = [''] * 9
    current_player = "O"
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)