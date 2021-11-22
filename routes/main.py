from app import app
from flask import render_template


@app.route('/', methods=["GET"])
def main_page():
    return render_template('main.html')
