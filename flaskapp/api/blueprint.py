from flask import Blueprint, jsonify, abort
import io
from datetime import datetime
import time
from settings import status_file
api = Blueprint('api', __name__, template_folder='templates')

tasks = [
    {
        'name_ru': u'Программирование',
        'name_slug': u'programming',
        'summ': 2, 
        'description': u'Программирование на Python, JavaScript.',
        'head_img': '/static/img/themes/programming.jpg'
    },
        {
        'name_ru': u'Домашнее',
        'name_slug': u'home',
        'summ': 2, 
        'description': u'Все что связано с домом.',
        'head_img': '/static/img/themes/home.jpg'
    },
]

def rebuild_status(status_file):
    last_rebuild = {}
    f = open(status_file)
    strings = f.readlines()
    last_datetime = datetime.strptime(strings[0], '%Y-%m-%d %H:%M')
    now_datetime = datetime.now()
    delta = (now_datetime - last_datetime).seconds // 3600
    if delta >= 1:
        status = False
    else:
        status = True
    last_rebuild = {
            'last_rebuild': last_datetime,
            'status': status
            }
    return last_rebuild

@api.route('/<page>')
def show(page):
    return abort(404)

@api.route('/v1.0/themes', methods=['GET'])
def get_themes():
    return jsonify({'themes': tasks})

@api.route('/v1.0/last_rebuild', methods=['GET'])
def get_last_rebuild():
    last_rebuild = rebuild_status(status_file)
    return jsonify({'last_rebuild': last_rebuild})

@api.route('/v1.0/rebuild', methods=['GET'])
def get_rebuild():
    status = True
    rebuild = {
            'status': status
            }
    return jsonify({'rebuild': rebuild})

