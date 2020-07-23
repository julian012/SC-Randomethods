from flask import request, render_template, url_for
import os
from app import app
from app.lib.methods import mean_square_method, linear_congruence_method, multiplicative_congruence_method, \
    uniform_distribution_method, normal_distribution_method
from app.lib.chi2 import Chi2
from app.lib.ks import KS
from app.lib.mean_test import MeanTest
from app.lib.variance_test import VarianceTest
import numpy as np

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        nums = np.array(request.json['numbers'])
        print(type(nums))
        result = {'varianza': None, 'cuadrados-medios': None, 'ks': None, 'chi-cuadrado': None}
        if request.json['varianza']:
            result['varianza'] = VarianceTest(nums, 0.05).getResult().tolist()
        if request.json['cuadrados-medios']:
            result['cuadrados-medios'] = MeanTest(nums, 0.05).getResult().tolist()
        if request.json['ks']:
            result['ks'] = KS(nums, 0.05).makeTest().tolist()
        if request.json['chi-cuadrado']:
            result['chi-cuadrado'] = Chi2(0.05, nums).makeTest().tolist()
        return result

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
