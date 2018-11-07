from flask import Blueprint, jsonify, abort
import io
from datetime import datetime
import time
from settings import status_file
from api.modules.rebuild_theme import rebuild_theme, rebuild_articles
from settings import theme_json_file
import json
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
    # data = json.load(open(theme_json_file))
    return jsonify({'themes': rebuild_theme()})

@api.route('/v1.0/articles_count/<theme>', methods=['GET'])
def get_articles_count(theme):
    articles = rebuild_articles()
    if articles != False:
        if theme == 'all':
            return jsonify({'articles_count': len(articles)})
        else:
            count = 0
            for i in articles:
                if i["theme_slug"] == theme:
                    count += 1
            if count > 0:
                return jsonify({'articles_count': count})
            else:
                return abort(404)
    else:
        return abort(404)

@api.route('/v1.0/article/<theme>/<article_id>', methods=['GET'])
def get_article(theme, article_id):
    articles = rebuild_articles()
    if articles != False:
        try:
            if theme == 'all':
                article_id = int(article_id)
                article = articles[article_id]
                article['last_update'] = article['last_update'].strftime("%Y.%m.%d %H:%M")
                return jsonify({'article': article})
            else:
                theme_articles = []
                for i in articles:
                    if i['theme_slug'] == theme:
                        theme_articles.append(i)
                article_id = int(article_id)
                article = theme_articles[article_id]
                article['last_update'] = article['last_update'].strftime("%Y.%m.%d %H:%M")
                return jsonify({'article': article})
        except (ValueError, IndexError) as identifier:
            print(identifier)
            return abort(404)
    else:
        return abort(404)

@api.route('/v1.0/articles', methods=['GET'])
def get_articles():
    articles = rebuild_articles()
    if articles != False:
        return jsonify({'articles': articles})
    else:
        return abort(404)

@api.route('/v1.0/last_rebuild', methods=['GET'])
def get_last_rebuild():
    last_rebuild = rebuild_status(status_file)
    return jsonify({'last_rebuild': last_rebuild})

@api.route('/v1.0/rebuild', methods=['GET'])
def get_rebuild():
    rebuild_theme() # TODO Сдесь нужно написать функцию которая будет делать git pull
    status = True
    rebuild = {
            'status': status
            }
    return jsonify({'rebuild': rebuild})