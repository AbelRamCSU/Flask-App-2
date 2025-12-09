from flask import Flask, render_template, request
import random

app = Flask(__name__)

# ===== CONFIGURABLE MESSAGES =====
WIN_MESSAGE = [
    "Okay you won who cares",
    "Bet this is the highlight of your day",
    "Want a cookie?",
    "DO it again I bet you won't",
    ]

LOSE_MESSAGE = [
    "HA YOU LOST",
    "well I expected you'd lose",
    "I would feel bad if you didn't suck",
    "Are even trying?",
    "I would cry if I had your guessing abilities",
    ]


GRID_SIZE = 3


@app.route("/", methods=["GET", 'POST'])
def index():
    result_message = None
    is_correct = None
    chosen_index = None

    correct_index = random.randint(0, GRID_SIZE * GRID_SIZE - 1)

    if request.method == "POST":
        try:
            chosen_index = int(request.form.get("choice"))
        except (TypeError, ValueError):
            chosen_index = None

        if chosen_index is None:
            is_correct = False
            result_message = "You have to actually click a box. I can't read minds. Yet."
        elif chosen_index == correct_index:
            is_correct = True
            win = random.choice(WIN_MESSAGE)
            result_message = (
                f"<center>{win}<br>"
                f"Right box was #{correct_index + 1}."
            )
        else:
            is_correct = False
            lose = random.choice(LOSE_MESSAGE)
            result_message = (
                f"<center>{lose}<br>"
                f"<center>You picked #{chosen_index + 1}<br>"
                f"<center>Right box was #{correct_index + 1}."
            )

    return render_template(
        "index.html",
        grid_size=GRID_SIZE,
        correct_index=correct_index,
        result=result_message,
        is_correct=is_correct,
        chosen_index=chosen_index,
    )

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug=True)
