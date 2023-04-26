from flask import Blueprint, render_template, request, json, jsonify
import requests

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/dashboard')
def dahboard():
    return render_template('dashboard.html')

@routes.route('/result', methods=['GET', 'POST'])
def getImageResult():

    place = None
    category = None
    place = request.form.get('place')
    category = request.form.get('category')


    res = None

    if(place != None):
        print(f'request got in here for place ...', place)
        if(place == 'NEWYORK'):
            res = 'NEWYORK'
        elif(place == 'CHICAGO'):
            res = 'CHICAGO'
        elif(place == 'TEXAS'):
            res = 'TEXAS'
    
    if(category != None):
        print(f'request got in here for category ...', category)
        if(category.lower() == 'Newyork'.lower()):
            res = 'newyork'
        elif(category.lower() == 'Texas'.lower()):
            res = 'texas'
        elif(category.lower() == 'Chicago'.lower()):
            res = 'chicago'

    if(res == None):
        res = 'NORESULT'
    print(f'request for res result ...', res)
    return render_template('dashboard.html', result=res)