from flask import Flask, g
from flask_login import current_user, LoginManager




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'new_password'
    
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
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app

