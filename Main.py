#!/usr/bin/python 2.7
#This is a very basic web application displaying all of my exercises
#from Codewars.com. It is built with Flask, and it has nothing special
#besides loading new pages.
from flask import Flask, render_template


app = Flask(__name__)

#Menu for all the exercises.
@app.route('/')
def menu():
    return render_template('Menu.html')

#New Member exercise page.
@app.route('/newmember')
def new_member_checker_exercise():
    return render_template('newMember.html')

#Narcissistic Number exercise page.
@app.route('/narcissisticnumber')
def narcissistic_number_exercise():
    return render_template('narcissisticnumber.html')

#IQ Test Exercise Page
@app.route('/iqtest')
def iq_test():
    return render_template('iqtest.html')

#IQ Test Exercise Page
@app.route('/camelcase')
def camel_case_exercise():
    return render_template('camelcase.html')

#404 Page in case I make a mistake and delete a page.
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key = 'Ly_YcGrphysXZpwnCCw0nnCm'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
