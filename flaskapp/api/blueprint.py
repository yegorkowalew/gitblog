from flask import Blueprint, jsonify, abort
import io
from datetime import datetime
import time
from settings import status_file
from api.modules.rebuild_theme import rebuild_theme
from settings import theme_json_file
import json
import pickle

api = Blueprint('api', __name__, template_folder='templates')

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
    time.sleep(1)
    data = json.load(open(theme_json_file))
    return jsonify({'themes': data})


@api.route('/v1.0/last_rebuild', methods=['GET'])
def get_last_rebuild():
    last_rebuild = rebuild_status(status_file)
    return jsonify({'last_rebuild': last_rebuild})

@api.route('/v1.0/rebuild', methods=['GET'])
def get_rebuild():
    rebuild_theme()
    status = True
    rebuild = {
            'status': status
            }
    return jsonify({'rebuild': rebuild})