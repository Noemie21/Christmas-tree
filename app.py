from flask import Flask

app = Flask(__name__)


@app.route("/sapin/<id>")
def christmas_tree(n):
    max_width = 1 + 2 * 4 * 4
    width = 1
    for i in range(1, n+1):
        for j in range(4):
            print(("*" * width).center(max_width))
            width += 2
        width -= 2 * 2
    for x in range(i):
        print(("|" *i).center(max_width))

