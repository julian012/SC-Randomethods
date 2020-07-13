from flask import request, render_template, flash, url_for
import os
from app import app
from app.lib.methods import mean_square_method, linear_congruence_method, multiplicative_congruence_method, \
    uniform_distribution_method, normal_distribution_method

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mean_square', methods=['POST'])
def mean_square():
    if request.method == 'POST':
        numList = mean_square_method(int(request.form['seed']), int(request.form['k']), int(request.form['limit']))
        return render_template('index.html', nums=numList)

@app.route('/linear_congruence', methods=['POST'])
def linear_congruence():
    if request.method == 'POST':
        numList = linear_congruence_method(int(request.form['x0']), int(request.form['k']), int(request.form['c']),
                                           int(request.form['g']), int(request.form['limit']))
        return render_template('index.html', nums=numList)

@app.route('/multiplicative_congruence', methods=['POST'])
def multiplicative_congruence():
    if request.method == 'POST':
        numList = multiplicative_congruence_method(int(request.form['x0']), int(request.form['t']),
                                                   int(request.form['d']), int(request.form['limit']))
        return render_template('index.html', nums=numList)

@app.route('/uniform_distribution', methods=['POST'])
def uniform_distribution():
    if request.method == 'POST':
        numList = uniform_distribution_method(int(request.form['max']), int(request.form['min']),
                                              int(request.form['limit']))
        return render_template('index.html', nums=numList)

@app.route('/normal_distribution', methods=['POST'])
def normal_distribution():
    if request.method == 'POST':
        numList = normal_distribution_method(int(request.form['mu']), int(request.form['sigma']),
                                              int(request.form['limit']))
        return render_template('index.html', nums=numList)
