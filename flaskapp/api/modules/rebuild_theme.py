from settings import theme_file
from pytils import translit
from settings import blog_folder, theme_json_file
from datetime import datetime
import os
import json

class Theme:
    def __init__(self, 
                title_ru="", 
                title_slug="", 
                description="", 
                summ=0, 
                last_update=datetime.strptime('2018-01-01 00-00-00', '%Y-%m-%d %H-%M-%S'),
                img=""
                ):
        self.title_ru = title_ru
        self.title_slug = title_slug
        self.description = description
        self.summ = summ
        self.last_update = last_update
        self.img = img

def rebuild_articles():
    json_list = []
    try:
        article_id = 0
        for directory in os.listdir(blog_folder):
            spl = directory.split("=")
            json_list.append({
                'id':article_id,
                'title_ru': spl[2],
                'title_slug': translit.slugify(spl[2]),
                'description': "description", # TODO Описание. Нужно открыть файл и скопировать с него первый абзац
                'last_update': datetime.strptime(spl[0], '%Y-%m-%d %H-%M-%S'),
                'img': 'img' # TODO Открыть папку и взять картинку.
            })
            article_id +=1
        return json_list
    except:
        return False

def rebuild_theme():
    themes = []
    f = open(theme_file)
    strings = f.readlines()
    for i in strings:
        theme = Theme(
            i.split('=')[0], 
            translit.slugify(i.split('=')[0]),
            i.split('=')[1].rstrip('\n'), 
            0, 
            datetime.strptime('2018-01-01 00-00-00', '%Y-%m-%d %H-%M-%S'),
            "/static/img/header/" + translit.slugify(i.split('=')[0]) + '.jpg'
        )
        themes.append(theme)
    for directory in os.listdir(blog_folder):
        spl = directory.split("=")
        for theme in themes:
            if theme.title_ru == spl[1]:
                theme.summ +=1
                if theme.last_update<datetime.strptime(spl[0], '%Y-%m-%d %H-%M-%S'):
                    theme.last_update = datetime.strptime(spl[0], '%Y-%m-%d %H-%M-%S')

    json_list = []
    for i in themes:
        json_list.append({
            'title_ru': i.title_ru,
            'title_slug': i.title_slug,
            'description': i.description,
            'summ': i.summ,
            'last_update': i.last_update,
            'img': i.img
        })

    return json_list