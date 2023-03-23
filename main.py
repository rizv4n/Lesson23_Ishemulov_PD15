from flask import Flask, request
from service import main_func

app = Flask(__name__)


@app.route("/perform_query")
def perform_query():
    args = request.args
    res = main_func(args)
    return res


if "__main__" == __name__:
    app.run()
