from settings import theme_file
from pytils import translit
from settings import blog_folder
import os

themes = []

class Theme:
    def __init__(self, title_ru="", title_slug="", description="", summ=0, last_update=""):
        self.title_ru = title_ru
        self.title_slug = title_slug
        self.description = description
        self.summ = summ
        self.last_update = last_update
    
    def all(self):
        # return '\n%s (ru);\n%s (en);\n%s (last update);\n%s (desk);\n%s (summ);' % (self.title_ru, self.title_en, self.last_update, self.description, self.summ)
        return self.title_ru

def rebuild_theme():
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

    for i in themes:
            print(i.title_ru, ' ', i.description, ' ', i.summ, '\n')