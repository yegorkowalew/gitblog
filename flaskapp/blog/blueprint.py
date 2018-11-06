from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, template_folder='templates')

# @blog.route('/', methods=['GET'])
# def get_blog():
#     rebuild = {
#             'status': True
#             }
#     return jsonify({'rebuild': rebuild})
@blog.route('/', methods=['GET'])
def index():
    return render_template('clear.html')