from settings import theme_file
from pytils import translit
from settings import blog_folder, theme_json_file
import os
import json

# themes = []

class Theme:
    def __init__(self, title_ru="", title_slug="", description="", summ=0, last_update=""):
        self.title_ru = title_ru
        self.title_slug = title_slug
        self.description = description
        self.summ = summ
        self.last_update = last_update
    
def rebuild_theme():
    themes = []
    f = open(theme_file)
    strings = f.readlines()
    for i in strings:
        theme = Theme(i.split('=')[0], translit.slugify(i.split('=')[0]), i.split('=')[1].rstrip('\n'))
        themes.append(theme)
    for directory in os.listdir(blog_folder):
        spl = directory.split("=")
        for theme in themes:
            if theme.title_ru == spl[1]:
                theme.summ +=1

    json_list = []
    for i in themes:
        json_list.append({
            'title_ru': i.title_ru,
            'title_slug': i.title_slug,
            'description': i.description,
            'summ': i.summ,
            'last_update': i.last_update
        })
    with open(theme_json_file, 'w') as file:
        json.dump(json_list, file, indent=2, ensure_ascii=False)