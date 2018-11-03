import os
from pytils import translit

from modules.settings import blog_folder

article_base = []

class Article:
    def __init__(self, title_ru="", title_en="", date="", tags=[]):
        self.title_ru = title_ru
        self.title_en = translit.slugify(title_ru)
        self.date = date
        self.tags = tags
    
    def all(self):
        return '\n%s (ru);\n%s (en);\n%s (date);\n%s (tags)' % (self.title_ru, self.title_en, self.date, self.tags)

def to_article_base(directory):
    for directory in os.listdir(directory):
        spl = directory.split("=")
        art = Article(spl[2], "", spl[0], spl[1])
        article_base.append(art)
    return article_base

if __name__ == '__main__':
    ae = to_article_base(blog_folder)
    for a in ae:
        print(a.all())