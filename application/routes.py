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

    place = request.form.get('place')
    category = request.form.get('category')

    print(f'request got in here for place ...', place)
    print(f'request got in here for category ...', category)

    res = ''

    if(place != None):
        if(place == 'NEWYORK'):
            res = 'NEWYORK'
        elif(place == 'CHICAGO'):
            res = 'CHICAGO'
        else:
            res = 'TEXAS'
    elif(category != None):
        if(category == 'food'):
            res = 'food'
        else:
            res = ''


    return render_template('dashboard.html', result=res)