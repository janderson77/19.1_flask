from operations import *
from flask import Flask, request
app = Flask(__name__)


@app.route("/add")
def addition():
    """Adds a and b together from params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a, b)
    return str(res)


@app.route("/sub")
def subtract():
    """Performs subtraction on a and b from params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a, b)
    return str(res)


@app.route("/mult")
def multiply():
    """Performs multiplication on a and b from params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a, b)
    return str(res)


@app.route("/div")
def divide():
    """Performs division on a and b from params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a, b)
    return str(res)


ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route("/math/<formula>")
def do_math(formula):
    """Performs math on a and b from params"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = ops[formula](a, b)
    return str(res)
