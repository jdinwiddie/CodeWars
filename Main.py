#!/usr/bin/python 2.7
from flask import Flask, flash, render_template, redirect

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('Menu.html')


@app.route('/newmember')
def new_member_checker_exercise():
    return render_template('newMember.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key = 'Ly_YcGrphysXZpwnCCw0nnCm'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
