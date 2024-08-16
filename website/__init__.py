from flask import Flask, g
from flask_login import current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_FLASK1 = "database.db"




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'new_password'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FLASK1}'
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    
    
    from .views import views
    from .models import User
    from .routes import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
        
    
    def inject_user():
        return dict(user=current_user)
    
    app.context_processor(inject_user)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    
    from . import models
    
    create_db(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    
    return app

def create_db(app):
    if not path.exists('website/'+ DB_FLASK1):
        with app.app_context():
            db.create_all()
        print('Database created!')
    

