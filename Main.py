flask import Flask, flash, render_template, redirect

app = Flask(__name__)


@app.route('/')
def Homepage():
    return render_template('Menu.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key = 'Ly_YcGrphysXZpwnCCw0nnCm'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
