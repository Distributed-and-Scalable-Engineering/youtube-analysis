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

    if(place != None and category != None):
        print(f'request got in here for category and place...', category, place)
        if(place == 'NEWYORK' and category.lower() == 'food'):
            res = 'newyork'
        elif(place == 'TEXAS' and category.lower() == 'food'):
            res = 'texas'
        elif(place == 'CHICAGO' and category.lower() == 'food'):
            res = 'chicago'

    if(place != None and category == None or category == ''):
        print(f'request got in here for place ...', place)
        if(place == 'NEWYORK'):
            res = 'NEWYORK'
        elif(place == 'CHICAGO'):
            res = 'CHICAGO'
        elif(place == 'TEXAS'):
            res = 'TEXAS'
    
   

    if(res == None):
        res = 'NORESULT'
    print(f'request for res result ...', res)
    return render_template('dashboard.html', result=res)