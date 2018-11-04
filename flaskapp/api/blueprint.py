from flask import Blueprint, jsonify, abort

api = Blueprint('api', __name__, template_folder='templates')

last_rebuild = {
        'last_rebuild': '2018-10-23 13:30:23',
        'status': True
    }

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

@api.route('/<page>')
def show(page):
    return abort(404)

@api.route('/v1.0/themes', methods=['GET'])
def get_themes():
    return jsonify({'themes': tasks})


import io
from datetime import datetime
@api.route('/v1.0/last_rebuild', methods=['GET'])
def get_last_rebuild():
    f = open('api/data/last_rebuild.txt')
    strings = f.readlines()
    last_datetime = datetime.strptime(strings[0], '%Y-%m-%d %H:%M')
    now_datetime = datetime.now()
    print(now_datetime - last_datetime)
    return jsonify({'last_rebuild': last_rebuild})