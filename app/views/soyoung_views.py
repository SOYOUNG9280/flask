from flask import Blueprint

soyoung = Blueprint('soyoung', __name__, url_prefix='/soyoung')

@soyoung.route('/about_me')
def about_me():
    return f'저는 {__name__} 입니다' 

@soyoung.route('/hello')
def hello():
    return f'안녕하세요' 

@soyoung.route('/bye')
def bye():
    return f'잘 가세요 ' 