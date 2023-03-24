from flask import Flask, request
from service import main_func

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    args = request.json
    res = main_func(args)
    return res


if "__main__" == __name__:
    app.run()
