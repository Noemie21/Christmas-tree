from flask import Flask

app = Flask(__name__)


@app.route("/sapin/<id>")
def christmas_tree(n):
    max_width = 1 + 2 * 5 * 4
    width = 1
    for _ in range(n):
        for _ in range(5):
            print(("*" * width).center(max_width))
            width += 2
        width -= 2 * 2
