from modules.gitwork import to_git

from modules.blogwork import to_article_base
from modules.settings import blog_folder

print(to_git())
ae = to_article_base(blog_folder)
for a in ae:
    print(a.all())