from flask import Blueprint


bp = Blueprint('main', __name__) #main là thư mục hiện tại và hàm __name__ đặc biêt chứa tên của module Python hiện tại


from app.main import routes